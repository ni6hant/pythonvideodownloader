import os
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Read video URLs from the text file
with open("video_urls.txt", "r") as file:
    video_urls = [line.strip() for line in file.readlines()]

# Create base directory to save the downloaded videos
base_download_directory = "downloaded_videos"
os.makedirs(base_download_directory, exist_ok=True)

# Variable to keep track of completed downloads and skipped downloads
completed_downloads = 0
skipped_downloads = 0

# Function to download a video from a given URL and save it in a folder based on URL structure
def download_video(url):
    global completed_downloads, skipped_downloads
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        url_path = urlparse(url).path
        file_name = os.path.basename(url_path)
        folder_path = os.path.dirname(url_path)
        folder_path = folder_path.lstrip('/').replace('/', os.path.sep)
        full_folder_path = os.path.join(base_download_directory, folder_path)
        os.makedirs(full_folder_path, exist_ok=True)
        file_path = os.path.join(full_folder_path, file_name)
        
        if os.path.exists(file_path):
            print(f"Skipped (Already Downloaded): {file_name} -> {folder_path}")
            skipped_downloads += 1
        else:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            
            print(f"Downloaded: {file_name} -> {folder_path}")
            completed_downloads += 1
    else:
        print(f"Failed to download: {url}")

# Download videos from the list of URLs using ThreadPoolExecutor
total_files = len(video_urls)
with ThreadPoolExecutor(max_workers=5) as executor:  # You can adjust max_workers based on your system's capabilities
    for url in video_urls:
        executor.submit(download_video, url)

while completed_downloads + skipped_downloads < total_files:
    print(f"{completed_downloads} downloaded, {skipped_downloads} skipped out of {total_files} files.", end="\r")

print("\nAll videos have been downloaded.")
print(f"Number of unique video URLs: {len(set(video_urls))}")
