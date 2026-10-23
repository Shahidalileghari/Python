from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int = 0

    def __post_init__(self) -> None:
        if min(self.major, self.minor, self.patch) < 0:
            raise ValueError("Version parts cannot be negative")

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


class Playlist:
    def __init__(self, tracks: list[str]) -> None:
        self._tracks = tuple(track.strip() for track in tracks if track.strip())

    def __len__(self) -> int:
        return len(self._tracks)

    def __iter__(self):
        return iter(self._tracks)

    def __repr__(self) -> str:
        return f"Playlist(tracks={self._tracks!r})"


if __name__ == "__main__":
    playlist = Playlist(["Track A", " ", "Track B"])
    print(Version(2, 4), repr(playlist), len(playlist), list(playlist))
