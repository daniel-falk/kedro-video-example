from kedro.pipeline import Pipeline, node

from .to_frames import video_to_frames
from .to_video import video_to_video, video_to_edge_video


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=video_to_frames,
                inputs="virat_tiny",
                outputs="frames_virat_tiny",
                name="unpack_video_to_images",
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
                outputs="edge_video",
                name="run_edge_detector_on_video",
            ),
        ]
    )
