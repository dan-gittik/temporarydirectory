import contextlib
import tempfile
import shutil


@contextlib.contextmanager
def TemporaryDirectory():
    temporary_directory_path = tempfile.mkdtemp()
    try:
        yield temporary_directory_path
    finally:
        shutil.rmtree(temporary_directory_path)
