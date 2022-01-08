def video_to_frames(video):
    if len(video) != 30:
        raise ValueError("Node expects video with exactly 30 frames")

    # Test forward stepping in video
    imgs = {"%08d" % i: video[i] for i in range(5)}
    # Test backward stepping
    imgs.update({"%08d" % i: video[i] for i in reversed(range(5, 10))})
    # Test individual indexes
    for i in [12,14,11,13,10]:
        imgs["%08d" % i] = video[i]
    # Test slices:
    for offset, img in enumerate(video[15:20]):
        imgs["%08d" % (15 + offset)] = img
    # Test slices of slices and negative slices
    for offset, img in enumerate(video[-10:-5]):
        imgs["%08d" % (20 + offset)] = img
    # Test slices
    for offset, img in enumerate(video[-5:-1]):
        imgs["%08d" % (25 + offset)] = img
    # Test negative indexing
    imgs["00000030"] = video[-1]
    return imgs
