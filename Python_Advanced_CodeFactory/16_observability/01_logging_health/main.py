import logging
from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceStatus:
    name: str
    ready: bool
    detail: str


def check_configuration(configured: bool) -> ServiceStatus:
    if configured:
        return ServiceStatus("demo-service", True, "Required configuration present")
    return ServiceStatus("demo-service", False, "Required configuration missing")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    status = check_configuration(configured=True)
    logging.info("service=%s ready=%s detail=%s", status.name, status.ready, status.detail)
    print("Ready:", status.ready)
