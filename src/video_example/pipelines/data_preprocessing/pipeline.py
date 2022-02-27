from kedro.pipeline import Pipeline, node

from .node import video_to_frames


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=video_to_frames,
                inputs="virat_tiny",
                outputs="frames_virat_tiny",
                name="unpack_video_to_images",
            )
        ]
    )
