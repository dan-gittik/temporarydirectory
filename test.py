import os

import temporarydirectory


def test_temporarydirectory():
    with temporarydirectory.TemporaryDirectory() as tempdir:
        assert os.path.isdir(tempdir)
    assert not os.path.exists(tempdir)
