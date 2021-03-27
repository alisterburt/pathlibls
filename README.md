# pathlibls

Love Python's [pathlib](https://docs.python.org/3/library/pathlib.html)?  Think listing the contents of a directory should be easier? You've come to the right place!

Say no to this...
```python
from pathlib import Path

contents = [item for item in Path('/my/favourite/folder').iterdir()]
contents = list(Path('/my/favourite/folder').glob('*'))
```


Say yes to `pathlibls`!
```python
from pathlibls import Path

contents = Path('/my/favourite/folder').ls()
```
