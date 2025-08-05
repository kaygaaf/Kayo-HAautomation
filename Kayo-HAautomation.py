import yaml
import re
from datetime import datetime

def validate_entity(entity):
    """Ensure entity ID follows Home Assistant format (e.g., light.kitchen)."""
    return bool(re.match(r"^[a-z]+\.[a-z0-9_]+$", entity))

def validate_time(time_str):
    """Ensure time is in HH:MM:SS format."""
    try:
        datetime.strptime(time_str, "%H:%M:%S")
        return True
    except ValueError:
        return False

def get_trigger():
    trigger_type = input("Trigger type (state/time): ").lower()
    trigger = {}
    if trigger_type == "state":
        entity = input("Trigger entity (e.g., sensor.kitchen_motion): ")
        if not validate_entity(entity):
            print("Invalid entity ID! Use format: domain.entity_name")
            return None
        trigger_to = input("Trigger to state: ")
        trigger = {"platform": "state", "entity_id": entity, "to": trigger_to}
    elif trigger_type == "time":
        at_time = input("Trigger at time (HH:MM:SS): ")
        if not validate_time(at_time):
            print("Invalid time format! Use HH:MM:SS")
            return None
        trigger = {"platform": "time", "at": at_time}
    else:
        print("Unsupported trigger type!")
        return None
    return trigger

def get_condition():
    add_condition = input("Add condition? (y/n): ").lower()
    if add_condition != "y":
        return []
    condition_type = input("Condition type (time/state): ").lower()
    condition = {}
    if condition_type == "time":
        after = input("Time after (HH:MM:SS): ")
        before = input("Time before (HH:MM:SS): ")
        if not (validate_time(after) and validate_time(before)):
            print("Invalid time format! Use HH:MM:SS")
            return []
        condition = {"condition": "time", "after": after, "before": before}
    elif condition_type == "state":
        entity = input("Condition entity (e.g., binary_sensor.window): ")
        if not validate_entity(entity):
            print("Invalid entity ID!")
            return []
        state = input("Condition state: ")
        condition = {"condition": "state", "entity_id": entity, "state": state}
    else:
        print("Unsupported condition type!")
        return []
    return [condition]

def get_action():
    service = input("Action service (e.g., light.turn_on): ")
    if not re.match(r"^[a-z]+\.[a-z_]+$", service):
        print("Invalid service format! Use domain.service_name")
        return None
    entity = input("Action entity (e.g., light.kitchen): ")
    if not validate_entity(entity):
        print("Invalid entity ID!")
        return None
    return [{"service": service, "entity_id": entity}]

def main():
    print("Welcome to Home Assistant Automation Generator!")
    alias = input("Automation name: ")
    trigger = get_trigger()
    if not trigger:
        print("Failed to create automation due to invalid trigger.")
        return
    conditions = get_condition()
    action = get_action()
    if not action:
        print("Failed to create automation due to invalid action.")
        return

    automation = [
        {
            "id": alias.lower().replace(" ", "_"),
            "alias": alias,
            "trigger": [trigger],
            "condition": conditions,
            "action": action
        }
    ]

    with open("automation.yaml", "w") as f:
        yaml.dump(automation, f, default_flow_style=False, sort_keys=False)
    print("Automation saved to automation.yaml!")

if __name__ == "__main__":
    main()
