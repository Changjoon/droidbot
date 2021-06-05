import os
import wrapt
import datetime


BENCHMARK_ENABLED = False
REPORT_DIR = os.path.expanduser("~/time_watch/")
REPORT_FILE = "report.csv"


def write_time(class_name, method_name, sec, msec):
    os.makedirs(REPORT_DIR, exist_ok=True)

    _file = os.path.join(REPORT_DIR, REPORT_FILE)
    with open(_file, "w") as f:
        f.write("{} {} {} {}\n".format(class_name, method_name, sec, msec))


@wrapt.decorator(enabled=BENCHMARK_ENABLED)
def measure_time(wrapped, instance, args, kwargs):
    before = datetime.datetime.now()
    ret = wrapped(*args, **kwargs)
    after = datetime.datetime.now()

    class_name = instance.__class__.__name__ if instance else "None"
    method_name = wrapped.__name__
    diff = after - before

    write_time(class_name, method_name, diff.seconds, diff.microseconds)
    return ret
