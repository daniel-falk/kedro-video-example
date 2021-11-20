# Kedro video dataset example pipeline

This repository aims to implement a video dataset for the Kedro project (take a look at the [Kedro documentation](https://kedro.readthedocs.io)).

Currently the video dataset is implemented in `src/test2/extras/datasets/video_dataset.py`.

There is a simple pipeline implemented in `src/test2/pipelines/data_preprocessing` that reads a video using the `VideoDataSet` and saves each frame using the `PartitionedDataset` for `ImageDataSet`.

## Installation

```bash
cd src && pip install -e . && cd ..
```

## Running

The pipeline expects a video with exactly 30 frames (crop with e.g. `ffmpeg -to 00:00:01 -i VIRAT_S_050000_01_000207_000361.mp4 -c:v copy short_video.mp4`) and independent frames extracted with e.g. ffmpeg (`ffmpeg -i short_video.mp4 %6d.png`) as these are used to validate the indexing in the implemented `VideoDataSet`. These should all be located in the `data/01_raw/virat_tiny` folder as specified in the `conf/base/catalog.yml` file.

The pipeline can be run with
```bash
kedro run
```
which will create output frames in `data/02_intermediate/virat_tiny/`. The interframe difference against the `ffmpeg` generated frames can be inspected with the Jupyter Notebook implemented in `notebooks/check_decoder_indexing.ipynb`. Start the Jupyter server with
```bash
kedro jupyter notebook
```
