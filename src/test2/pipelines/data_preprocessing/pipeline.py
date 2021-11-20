from kedro.pipeline import Pipeline, node

from .node import preprocess_videos


def create_pipeline(**kwargs):
    return Pipeline([node(func=preprocess_videos, inputs="traffic", outputs="raw_images", name="preprocess_traffic_videos")])
