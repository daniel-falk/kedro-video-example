def video_to_frames(video):
    if len(video) != 24:
        raise ValueError("Node expects video with exactly 24 frames")

    # Test forward stepping in video
    imgs = {"%08d" % i: video[i] for i in range(4)}
    # Test backward stepping
    imgs.update({"%08d" % i: video[i] for i in reversed(range(4, 8))})
    # Test individual indexes
    for i in [10, 11, 9, 8]:
        imgs["%08d" % i] = video[i]
    # Test slices:
    for offset, img in enumerate(video[12:16]):
        imgs["%08d" % (12 + offset)] = img
    # Test slices of slices and negative slices
    for offset, img in enumerate(video[-8:-4]):
        imgs["%08d" % (16 + offset)] = img
    # Test slices
    for offset, img in enumerate(video[-4:-1]):
        imgs["%08d" % (20 + offset)] = img
    # Test negative indexing
    imgs["00000024"] = video[-1]
    return imgs
