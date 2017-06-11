# Temporary Directory

A context manager to get a path to a temporary directory that's deleted when the context is exited.

```python
import os

from temporarydirectory import TemporaryDirectory

with TemporaryDirectory() as tempdir:
    # Create subdirectory...
    d = os.path.join(tempdir, 'dir')
    os.mkdir(d)
    # Create file...
    f = os.path.join(tempdir, 'file.txt')
    with open(f, 'w') as writer:
        writer.write('Hello, world!')

# And that's it.
assert not os.path.exists(tempdir)
```
