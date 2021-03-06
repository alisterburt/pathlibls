from pathlib import Path as BasePath


class Path(type(BasePath())):
    def ls(self):
        """When the path points to a directory, return a list of path objects
        of the directory contents
        """
        return [item for item in self.iterdir()]