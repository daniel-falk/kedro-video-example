from skimage import filters
import numpy as np
import PIL.Image

from kedro.extras.datasets.video.video_dataset import SequenceVideo, GeneratorVideo


def video_to_video(video):
    """Returns the same video to write it with no modifications"""
    return video


def _frame_to_edge(frame):
    gray = np.array(frame.convert("L"), dtype=np.float32)
    edge = filters.sobel(gray).astype(np.uint8)
    return PIL.Image.fromarray(edge).convert("RGB")


def video_to_edge_video(video):
    """Do edge detection on a video"""
    frames = [_frame_to_edge(frame) for frame in video]
    return SequenceVideo(frames, fps=video.fps, fourcc=video.fourcc)


def frames_to_edge_video(frames):
    """Do edge detection on a video"""
    frames = [_frame_to_edge(load_frame()) for load_frame in frames.values()]
    return SequenceVideo(frames, fps=10)


def video_to_edge_video_generator(video):
    """Do edge detection on a video"""
    generator = (_frame_to_edge(frame) for frame in video)
    return GeneratorVideo(generator, None, fps=video.fps, fourcc=video.fourcc)
