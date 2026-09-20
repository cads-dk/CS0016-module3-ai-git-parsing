# AI Usage and Validation Log

Student name: Deanna Juliana K. de la Cruz
Section: TS31
AI tool used: ChatGPT/Codex

# Expected Values


## Entry 1 - XML parsing

Prompt: 
I am completing an authorized classroom Python lab.
Review this function stub and the supplied fictional [XML/JSON/YAML] structure.
Recommend an implementation that returns exactly the keys described in the docstring.
Explain namespace handling, data types, error risks, and each library function used.
Do not invent files, credentials, network calls, or expected test results.
I will validate your recommendation using unit tests and Git diffs.

Function stub:
def parse_xml(path: str | Path) -> dict:
   """Return default_operation and test_option from the NETCONF-style XML."""
   # TODO: parse the XML, handle its default namespace, and return two strings.
   raise NotImplementedError("Complete parse_xml")

Relevant fictional data: 
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <edit-config>
   <target>
     <candidate />
   </target>
   <default-operation>merge</default-operation>
   <test-option>test-then-set</test-option>
   <config>
     <interface xmlns="urn:example:network">
       <name>GigabitEthernet1</name>
       <enabled>true</enabled>
     </interface>
   </config>
 </edit-config>
</rpc>


AI recommendation summary:

Recommended a parse_xml() implementation that:

Parses the XML file using Python’s xml.etree.ElementTree.
Handles the NETCONF default namespace using the prefix nc.
Extracts <default-operation> and <test-option>.
Returns exactly two dictionary keys: default_operation and test_option.
Removes surrounding whitespace from both string values.
Raises ValueError if either required element is missing.
Explains the expected data types, namespace behavior, library functions, and possible parsing or file-related errors.


Decision: Accepted

Validation evidence: 

test_xml_default_operation (__main__.ParserTests.test_xml_default_operation) ... ok
test_xml_test_option (__main__.ParserTests.test_xml_test_option) ... ok


## Entry 2 - JSON parsing

Prompt:

I am completing an authorized classroom Python lab.
Review this function stub and the supplied fictional [XML/JSON/YAML] structure.
Recommend an implementation that returns exactly the keys described in the docstring.
Explain namespace handling, data types, error risks, and each library function used.
Do not invent files, credentials, network calls, or expected test results.
I will validate your recommendation using unit tests and Git diffs.

Function stub:

def parse_json(path: str | Path) -> dict:
   """Return site, device_count, enabled_devices, and roles from the JSON."""
   # TODO: use json.load and derive the requested summary values.
   raise NotImplementedError("Complete parse_json")

Relevant fictional data: 
{
 "site": "FEU-Tech-Lab",
 "devices": [
   {
     "hostname": "R1",
     "management_ip": "192.0.2.10",
     "role": "router",
     "enabled": true
   },
   {
     "hostname": "SW1",
     "management_ip": "192.0.2.20",
     "role": "switch",
     "enabled": true
   },
   {
     "hostname": "AP1",
     "management_ip": "192.0.2.30",
     "role": "wireless-ap",
     "enabled": false


AI recommendation summary:
Recommended using `json.load()` to read the JSON file, then:

* Retrieve the site name and device list.
* Count all devices with `len()`.
* Collect the hostnames of enabled devices.
* Collect each device’s role.
* Return exactly `site`, `device_count`, `enabled_devices`, and `roles`.


Decision: Accepted

Validation evidence:

test_json_device_count (__main__.ParserTests.test_json_device_count) ... ok
test_json_enabled_devices (__main__.ParserTests.test_json_enabled_devices) ... ok
test_json_roles (__main__.ParserTests.test_json_roles) ... ok
test_xml_default_operation (__main__.ParserTests.test_xml_default_operation) ... ok
test_xml_test_option (__main__.ParserTests.test_xml_test_option) ... ok

## Entry 3 - YAML parsing and integration

Prompt:
I am completing an authorized classroom Python lab.
Review this function stub and the supplied fictional [XML/JSON/YAML] structure.
Recommend an implementation that returns exactly the keys described in the docstring.
Explain namespace handling, data types, error risks, and each library function used.
Do not invent files, credentials, network calls, or expected test results.
I will validate your recommendation using unit tests and Git diffs.

Function stub:
def parse_yaml(path: str | Path) -> dict:
   """Return name, approved, duration_minutes, devices, and action from YAML."""
   # TODO: use yaml.safe_load and return the normalized maintenance summary.
   raise NotImplementedError("Complete parse_yaml")


Relevant fictional data:
window:
 name: Saturday-Lab
 approved: true
 duration_minutes: 90
devices:
 - R1
 - SW1
action: validate-configuration


AI recommendation summary:
Recommended using yaml.safe_load() to safely read the YAML file, then:

Extract name, approved, and duration_minutes from the nested window section.
Extract devices and action from the top level.
Return exactly those five keys in one dictionary.

YAML has no XML-style namespaces. Its values become standard Python types: strings, a Boolean, an integer, a list, and dictionaries. Possible issues include missing or unreadable files, malformed YAML, absent keys, unexpected structures, or PyYAML not being installed.

Decision: Accepted

Validation evidence:
test_json_device_count (__main__.ParserTests.test_json_device_count) ... ok
test_json_enabled_devices (__main__.ParserTests.test_json_enabled_devices) ... ok
test_json_roles (__main__.ParserTests.test_json_roles) ... ok
test_xml_default_operation (__main__.ParserTests.test_xml_default_operation) ... ok
test_xml_test_option (__main__.ParserTests.test_xml_test_option) ... ok
test_yaml_window (__main__.ParserTests.test_yaml_window) ... ok

## Controlled merge-conflict line

Validation status: PENDING

## Final reflection

Describe one AI suggestion that you changed or rejected and explain the evidence that guided your decision.
