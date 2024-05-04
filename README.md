# OneTabPy

> [!NOTE]
> Python Library for Managing the Browser Extension OneTab.

## Installation

```bash
pip install onetabpy
```

## Usage

Instantiate the OneTab class and use the methods to get the tabs in different formats.

```bash
from onetabpy import OneTab

# Create an instance of OneTab
onetab = OneTab()
```

### Get All Tabs

```python

# Get all tabs
onetab.get_tabs()

# Get all tabs in a dictionary format
onetab.get_tabs_dict()

# Get all tabs in a list format
onetab.get_tabs_list()

# Get all tabs in a JSON format
onetab.get_tabs_json()

# Get all tabs in a CSV format
onetab.get_tabs_csv()

# Get all tabs in a HTML format
onetab.get_tabs_html()

# Get all tabs in a Markdown format
onetab.get_tabs_md()

# Get all tabs in a YAML format
onetab.get_tabs_yaml()
```

### Backup Tabs

```python
# Backup all tabs - direct
backup_onetabs()

# Backup all tabs - using onetab's method
onetab.backup_tabs()
```

### Restore Tabs

```python
# Restore all tabs - direct
restore_onetabs()

# Restore all tabs - using onetab's method
onetab.restore_tabs()
```
