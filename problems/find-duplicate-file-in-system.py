import os
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths)]: # O(N * M)

        groups = defaultdict(list)

        for path in paths: # O(N)
            folder = path.split(" ")[0]
            for file in path.split(" ")[1:]: # O(M)
                filename, content = file.split("(")
                content = content.strip(")")
                groups[content].append(os.path.join(folder, filename))

        return [i for i in groups.values() if len(i) > 1]
