import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def create_wavelet_video(input_audio_path, output_video_path, fps=30):
    # Load the audio file
    y, sr = librosa.load(input_audio_path)
    
    # Calculate the duration of the audio
    duration = len(y) / sr
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    # Set up the plot
    line, = ax.plot([], [], linewidth=1)
    ax.set_xlim(0, len(y))
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    # Function to update the plot for each frame
    def update(frame):
        # Calculate the window size for this frame
        window_size = int(sr / fps)
        start = frame * window_size
        end = start + window_size
        
        # Get the audio data for this window
        if end > len(y):
            end = len(y)
        data = y[start:end]
        
        # Calculate color based on amplitude
        amplitude = np.abs(data).mean()
        color = plt.cm.viridis(amplitude)
        
        # Update the line data and color
        line.set_data(range(len(data)), data)
        line.set_color(color)
        
        # Add a subtle background effect
        ax.set_facecolor(plt.cm.viridis(amplitude * 0.5))
        
        return line,
    
    # Create the animation
    frames = int(duration * fps)
    anim = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
    
    # Save the animation as a video
    temp_video = "temp_video.mp4"
    anim.save(temp_video, writer='ffmpeg', fps=fps)
    plt.close()
    
    # Add audio to the video
    video = VideoFileClip(temp_video)
    audio = AudioFileClip(input_audio_path)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
    
    # Clean up temporary file
    video.close()
    audio.close()
    final_video.close()
    os.remove(temp_video)

def main():
    # Get the input audio file path
    # input_audio = input("Enter the path to your WAV file: ")
    input_audio = "Paper 01 -  Attention is all you need.wav"
    if not os.path.exists(input_audio):
        print("Error: File not found!")
        return
    
    # Generate output video path
    output_video = os.path.splitext(input_audio)[0] + "_wavelet.mp4"
    
    print("Creating wavelet video...")
    create_wavelet_video(input_audio, output_video)
    print(f"Video created successfully: {output_video}")

if __name__ == "__main__":
    main() 