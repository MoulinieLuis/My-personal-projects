import os

with open("path_brackdow.txt", "w") as f:
        f.write("\n".join(os.environ.get("PATH", "").split(";")))