# Plugin Manager

Small plugin manager that dynamically loads Python modules from the `plugins` directory and reports available plugins.

## Overview

This project demonstrates a simple plugin loader that:
- Adds the `plugins` directory to `sys.path`.
- Imports all `.py` files (excluding `__init__.py`/dunder files) as modules.
- Keeps imported modules in `manager.plugins` and exposes helper functions to list and inspect them.

## Requirements

- Python 3.7+ (tested with Python 3.14)

## Structure

- `main.py` - Plugin manager and example runner.
- `plugins/` - Directory containing plugin modules, e.g. `email_plugin.py`, `logger_plugin.py`, `sms_plugin.py`.

A plugin is simply a Python module. Recommended optional functions in a plugin:
- `get_info()` — return a short description string.
- `send(message)` — example action for sending messages.
- `log(message)` — example logging action.

## Usage

Run the manager from the `plugin-manager` folder:

```bash
python main.py
```

Expected behaviour:
- The script will import each `.py` file in `plugins/` (skipping dunder files) and append the module to `manager.plugins`.
- `show_plugins()` and `show_plugins_()` print information about discovered plugins.

## Adding a plugin

1. Create a new file `plugins/my_plugin.py`.
2. Optionally implement `get_info()` and other functions such as `send()` or `log()`.
3. Run `python main.py` to see the plugin listed.

Example minimal plugin (`plugins/example_plugin.py`):

```python
# plugins/example_plugin.py

def get_info():
    return "Example plugin"

def send(msg):
    print(f"Sending: {msg}")
```

## Notes and suggestions

- The manager currently imports modules by filename. If you prefer module names only, strip the `.py` extension when listing files.
- The listing in `main.py` filters files using `os.listdir()` and checks `endswith('.py')` and `not startswith('__')`.
- If plugins require package-level imports, consider adding an `__init__.py` in `plugins/` and using package import semantics.

## License

MIT-style: use and modify as you like.
