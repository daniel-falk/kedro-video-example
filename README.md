# Kedro video dataset example pipeline

This repository aims to implement a video dataset for the Kedro project (take a look at the [Kedro documentation](https://kedro.readthedocs.io)).

Currently the video dataset is implemented in `src/video_example/extras/datasets/video_dataset.py`.

There is a simple pipeline implemented in `src/video_example/pipelines/data_preprocessing` that reads a video using the `VideoDataSet` and saves each frame using the `PartitionedDataset` for `ImageDataSet`.

## Installation

Install the project. This will install dependencies such as Kedro and DVC. Installation can preferably be done inside a python virtual envrionment.
```bash
python -mvenv venv
source venv/bin/activate
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
which will read the video file and create output frames in `data/02_intermediate/virat_tiny/`.

Since the `dvc repro` command also generated raw frames using ffmpeg we can now compare the output of our pipeline using the `VideoDataSet` reader to the ones generated using ffmpeg. This can be done using the Jupyter Notebook implemented in `notebooks/check_decoder_indexing.ipynb`. Start the Jupyter server with the following command and open the notebook.
```bash
kedro jupyter notebook
```

In the notebook result it can be seen that there are some small differences in the pixel values as decoded by OpenCV (`VideoDataSet`) and ffmpeg, but there is no offset or index errors in the addressing since the diagonal of the distance comparizon is the smallest.
