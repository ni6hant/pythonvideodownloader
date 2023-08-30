
# Project Setup and Execution Guide

Welcome to the video downloader project! This guide will help you set up and run the project on a Windows machine. Even if you're new to programming, don't worry—we'll guide you through the steps.

## Prerequisites
- **Windows Machine**: Anyone using Linux can easily figure out how to run this project. This setup assumes you have a Windows Machine.

- **Python Installation**: Make sure you have Python installed on your machine. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).

- **Text Editor**: You'll need a text editor to modify the provided code. You should use Visual Studio Code as it will be less of a hassle while running the virtual environment commands.

## Step 1: Clone the Repository

1. **Download the Code**: Click the "Code" button at the top of this repository and select "Download ZIP". Extract the downloaded ZIP file to a location on your computer.

## Step 2: Prepare the Environment

1. **Open a Command Prompt**: Press `Win + R`, type `cmd`, and press Enter. This will open the Command Prompt. 

2. **Navigate to the Project Directory**: Use the `cd` command to navigate to the directory where you extracted the downloaded ZIP file. For example:
   ```sh
   cd path\to\downloaded\folder
   ```

If however, you are using Visual Studio Code, you can open terminal right inside it and navigate to the directory.

## Setting Up the Environment and Installing Dependencies:
To keep your project dependencies isolated, it's a good idea to use a virtual environment. Run these commands:

## Create and Activate a Virtual Environment:
 ```sh
python -m venv venv
venv\Scripts\activate
```
## Step 3: Install Dependencies

1.  **Install Required Libraries**: In the activated virtual environment, run the following command to install the required libraries:
    
    shCopy code
    
    `pip install -r requirements.txt` 
    

## Step 4: Add Video URLs

1.  **Prepare Video URLs**: Open the `video_urls.txt` file in the project directory using your text editor. Add one video URL per line. Save the file. Example:
    
	   ```sh
	   https://www.example.com/video1
	   https://www.example.com/video2
## Step 5: Run the Script

1.  **Run the Script**: In the Command Prompt with the virtual environment active, run the script using the following command:
    
     `python download.py` 
   
2.  **Monitor Progress**: The script will start downloading videos from the URLs you provided. You'll see progress messages in the Command Prompt.
    
3.  **Downloaded Videos**: The downloaded videos will be saved in the `downloaded_videos` directory.
    
4.  **Completion**: Once all videos are downloaded, you'll see a completion message.
    

## Congratulations!

You've successfully set up and run the video downloader project on your Windows machine. If you encounter any issues or have questions, don't hesitate to seek help.
