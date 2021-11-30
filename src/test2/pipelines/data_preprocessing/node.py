def video_to_frames(video):
    return {"%08d" % i: video[i] for i in range(min(20, len(video)))}
