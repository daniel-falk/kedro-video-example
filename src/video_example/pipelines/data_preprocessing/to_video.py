from skimage import filters
import numpy as np
import PIL.Image

from ...extras.datasets.video_dataset import IterableVideo


def video_to_video(video):
    """Returns the same video to write it with no modifications"""
    return video


def video_to_edge_video(video):
    """Do edge detection on a video"""
    width, height = video.size
    np_frames = [
        filters.sobel(np.array(frame.convert("L"), dtype=np.float32)).astype(np.uint8)
        for frame in video
    ]
    frames = [PIL.Image.fromarray(frame).convert("RGB") for frame in np_frames]
    return IterableVideo(frames, fps=video.fps, fourcc=video.fourcc)
