#pip install moviepy
# import moviepy.editor
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# replace the parameter with the location of video.
# video = moviepy.editor.VideoFileClip(r"SEO.mp4")
video = VideoFileClip(r"SEO.mp4")

audio_data = video.audio
# replace the parameter with the location
#along with filename
audio_data.write_audiofile("VID_20160512_213116.mp3")