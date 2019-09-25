class SemanticVersion():
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def patch_version_up(self):
        return SemanticVersion(self.major, self.minor, self.patch + 1)

    def minor_version_up(self):
        return SemanticVersion(self.major, self.minor + 1, self.patch)

    def major_version_up

def main():
    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)  # True


if __name__ == '__main__':
    main()
