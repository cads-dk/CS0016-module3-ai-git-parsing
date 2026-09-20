"""Module 3 combined lab starter.

Complete each function with help from an approved AI tool, then verify every
claim and code change using the supplied unit tests. The files contain only
fictional classroom data.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

from pathlib import Path
import xml.etree.ElementTree as ET


def parse_xml(path: str | Path) -> dict:
    """Return default_operation and test_option from the NETCONF-style XML."""
    root = ET.parse(path).getroot()

    namespace = {"nc": "urn:ietf:params:xml:ns:netconf:base:1.0"}

    default_operation = root.findtext(
        "nc:edit-config/nc:default-operation",
        namespaces=namespace,
    )
    test_option = root.findtext(
        "nc:edit-config/nc:test-option",
        namespaces=namespace,
    )

    if default_operation is None or test_option is None:
        raise ValueError(
            "XML must contain default-operation and test-option "
            "in the NETCONF base namespace"
        )

    return {
        "default_operation": default_operation.strip(),
        "test_option": test_option.strip(),
    }

# def parse_xml(path: str | Path) -> dict:
#     """Return default_operation and test_option from the NETCONF-style XML."""
#     # TODO: parse the XML, handle its default namespace, and return two strings.
    
#     raise NotImplementedError("Complete parse_xml")



def parse_json(path: str | Path) -> dict:
    """Return site, device_count, enabled_devices, and roles from the JSON."""
    with Path(path).open("r", encoding="utf-8") as file:
        data = json.load(file)

    site = data["site"]
    devices = data["devices"]

    enabled_devices = [
        device["hostname"]
        for device in devices
        if device["enabled"] is True
    ]

    roles = [device["role"] for device in devices]

    return {
        "site": site,
        "device_count": len(devices),
        "enabled_devices": enabled_devices,
        "roles": roles,
    }

# def parse_json(path: str | Path) -> dict:
#     """Return site, device_count, enabled_devices, and roles from the JSON."""
#     # TODO: use json.load and derive the requested summary values.
#     raise NotImplementedError("Complete parse_json")

from pathlib import Path

import yaml


def parse_yaml(path: str | Path) -> dict:
    """Return name, approved, duration_minutes, devices, and action from YAML."""
    with Path(path).open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    window = data["window"]

    return {
        "name": window["name"],
        "approved": window["approved"],
        "duration_minutes": window["duration_minutes"],
        "devices": data["devices"],
        "action": data["action"],
    }

# def parse_yaml(path: str | Path) -> dict:
#     """Return name, approved, duration_minutes, devices, and action from YAML."""
#     # TODO: use yaml.safe_load and return the normalized maintenance summary.
#     raise NotImplementedError("Complete parse_yaml")


def build_summary(xml_path: str | Path, json_path: str | Path, yaml_path: str | Path) -> dict:
    """Combine the three parser results into one dictionary."""
    return {
        "xml": parse_xml(xml_path),
        "json": parse_json(json_path),
        "yaml": parse_yaml(yaml_path),
    }


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    summary = build_summary(
        base / "network_config.xml",
        base / "devices.json",
        base / "maintenance.yaml",
    )
    print(json.dumps(summary, indent=2))
