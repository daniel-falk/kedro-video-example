"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline


from .to_frames import video_to_frames
from .to_video import video_to_video, video_to_edge_video, frames_to_edge_video, video_to_edge_video_generator


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=video_to_frames,
                inputs="virat_tiny",
                outputs="frames_virat_tiny",
                name="unpack_video_to_images",
            ),
            node(
                func=frames_to_edge_video,
                inputs="frames_virat_tiny",
                outputs="edge_video_frames",
                name="run_edge_detector_on_intermediate_frames",
            ),
            node(
                func=frames_to_edge_video,
                inputs="ffmpeg_frames_virat_tiny",
                outputs="edge_video_ffmpeg_frames",
                name="run_edge_detector_on_ffmpeg_frames",
            ),
            node(
                func=video_to_video,
                inputs="virat_tiny",
                outputs="same_video",
                name="copy_video_with_video_writer",
            ),
            node(
                func=video_to_edge_video,
                inputs="virat_tiny",
                outputs="edge_video_from_video",
                name="run_edge_detector_on_video",
            ),
            node(
                func=video_to_edge_video_generator,
                inputs="virat_tiny",
                outputs="edge_video_generator",
                name="run_edge_detector_on_video_as_generator",
            ),
        ]
    )
