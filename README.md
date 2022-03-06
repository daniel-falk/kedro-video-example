# Kedro video dataset example pipeline

This repository aims to implement a video dataset for the Kedro project (take a look at the [Kedro documentation](https://kedro.readthedocs.io)).

Currently the video dataset is implemented on a fork of Kedro (to be merged with main branch...) at:
https://github.com/daniel-falk/kedro
in the file: `kedro/extras/datasets/video/video_dataset.py`

There is a sample pipeline implemented in `src/video_example/pipelines/data_preprocessing` that:
1) reads a video using the `VideoDataSet` and saves each frame using the `PartitionedDataset` for `ImageDataSet`.
2) Reads all frames of the video, performs edge detection on them, and saves them to a new video file
3) Same as 2 but by using an generator so that only one frame is in memory at a time.

## Installation

Install the modified version of Kedro with the `VideoDataSet` added:
```bash
pip install git+https://github.com/daniel-falk/kedro
```

Install the project. This will install dependencies such as DVC and OpenCV.
```bash
pip install -r src/requirements.txt
```

After the installation finishes, standing in the repo root, download and reproduce the input data using dvc (which is installed from the requirements file above). This step requires the ffmpeg command which can be installed using `apt install ffmpeg` on ubuntu/debian or `brew install ffmpeg` on macOS.
```bash
dvc repro
```

This command will download an example movie, cut it to the correct length and extract the frames from it. The data is found in `data/01_raw`.

## Running

The kedro pipeline can be run with
```bash
kedro run
```
which will read the video file and create output frames in `data/02_intermediate/virat_tiny/`, it will also create a video in `data/03_primary/` named `edge.mp4` and `edge_generator.mp4`. These videos can be viewed with e.g. `ffplay data/03_primary/edge.mp4`.

Since the `dvc repro` command also generated raw frames using ffmpeg we can now compare the output of our pipeline using the `VideoDataSet` reader to the ones generated using ffmpeg. This can be done using the Jupyter Notebook implemented in `notebooks/check_decoder_indexing.ipynb`. Start the Jupyter server with the following command and open the notebook.
```bash
kedro jupyter notebook
```

In the notebook result it can be seen that there are some small differences in the pixel values as decoded by OpenCV (`VideoDataSet`) and ffmpeg, but there is no offset or index errors in the addressing since the diagonal of the distance comparizon is the smallest.

The kedro pipeline should also have created two edge detection videos in the `03_primary` folder. These can be played with a regular movie player, e.g. `ffplay data/03_primary/edge.mp4`.
