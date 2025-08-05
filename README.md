Kayo HAautomation 🏠
A Python tool to generate Home Assistant automation YAML files from user inputs. Create smart home automations (e.g., turn on lights when motion is detected) without manually writing YAML!
Features

Interactive CLI to input triggers, conditions, and actions.
Generates valid Home Assistant automation YAML files.
Supports common triggers (e.g., state, time) and actions (e.g., turn on/off devices).
Validates inputs to avoid YAML errors.
Saves output to automation.yaml for easy integration.

Python 🐍
Libraries: pyyaml

Installation

Clone the repo:git clone https://github.com/kaygaaf/Kayo-HAautomation


Navigate to the directory:cd Kayo-HAautomation


Install dependencies:pip install pyyaml



Usage
Run the script:
python Kayo-HAautomation.py

Follow the prompts to input:

Automation name
Trigger (e.g., motion sensor state change)
Condition (optional, e.g., time of day)
Action (e.g., turn on a light)

Example output (automation.yaml):
- id: 'motion_light_kitchen'
  alias: Kitchen Motion Light
  trigger:
    - platform: state
      entity_id: sensor.kitchen_motion
      to: 'on'
  condition:
    - condition: time
      after: '18:00:00'
      before: '23:00:00'
  action:
    - service: light.turn_on
      entity_id: light.kitchen

How It Works

The script prompts for automation details via a CLI.
It validates inputs (e.g., checks for valid entity IDs).
Generates a YAML file compatible with Home Assistant's automation format.
Saves the output to automation.yaml.


Example prompts


Welcome to Kayo HAautomation!

Automation name: Kitchen Motion Light

Trigger type (state/time): state

Trigger entity (e.g., sensor.kitchen_motion): sensor.kitchen_motion

Trigger to state: on

Add condition? (y/n): y

Condition type (time/state): time

Time after (HH:MM:SS): 18:00:00

Time before (HH:MM:SS): 23:00:00

Action service (e.g., light.turn_on): light.turn_on

Action entity (e.g., light.kitchen): light.kitchen

Automation saved to automation.yaml!
