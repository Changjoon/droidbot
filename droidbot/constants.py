import os


class Const:
    LOCAL_SCREENSHOT_DIR = "screenshot{}".format(os.path.sep)
    REMOTE_SCREENSHOT_DIR = "{0}sdcard{0}droidbot{0}screenshot{0}".format(os.path.sep)
