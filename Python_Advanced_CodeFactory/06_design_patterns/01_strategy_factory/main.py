from typing import Protocol


class Exporter(Protocol):
    def export(self, rows: list[dict[str, str]]) -> str: ...


class DebugExporter:
    def export(self, rows: list[dict[str, str]]) -> str:
        return repr(rows)


class SimpleTextExporter:
    def export(self, rows: list[dict[str, str]]) -> str:
        return "\n".join(" | ".join(row.values()) for row in rows)


def create_exporter(kind: str) -> Exporter:
    factories: dict[str, type] = {
        "debug": DebugExporter,
        "text": SimpleTextExporter,
    }
    try:
        return factories[kind]()
    except KeyError as error:
        raise ValueError(f"Unsupported format: {kind}") from error


if __name__ == "__main__":
    records = [{"name": "Ali", "status": "active"}]
    print(create_exporter("text").export(records))
