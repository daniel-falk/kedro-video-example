from kedro.pipeline import Pipeline, node

from .to_frames import video_to_frames
from .to_video import video_to_video


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
        ]
    )
