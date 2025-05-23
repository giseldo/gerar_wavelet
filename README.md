# Audio to Wavelet Video Converter

This application converts WAV audio files into videos that visualize the audio waveform. The visualization shows the audio waves moving across the screen in real-time.

## Requirements

- Python 3.7 or higher
- FFmpeg (required for video creation)

## Installation

1. Install the required Python packages:
```bash
pip install -r requirements.txt
```

2. Make sure you have FFmpeg installed on your system:
   - Windows: Download from https://ffmpeg.org/download.html
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

## Usage

1. Run the script:
```bash
python audio_to_wavelet_video.py
```

2. When prompted, enter the path to your WAV file.

3. The script will create a new video file in the same directory as your input file, with "_wavelet.mp4" appended to the original filename.

## Features

- Real-time audio waveform visualization
- Black background with cyan waves for better visibility
- Smooth animation at 30 FPS
- Maintains audio quality and synchronization

## Notes

- The input file must be in WAV format
- The output video will be in MP4 format
- The visualization uses a black background with cyan waves for optimal visibility 