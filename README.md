[![QuickPYTHON - Educational Interactive Coding Environment](https://raw.githubusercontent.com/timothycrosley/quickpython/master/art/logo_large.png)](https://timothycrosley.github.io/quickpython/)
_________________

[![PyPI version](https://badge.fury.io/py/quickpython.svg)](http://badge.fury.io/py/quickpython)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/quickpython/)
[![Downloads](https://pepy.tech/badge/quickpython)](https://pepy.tech/project/quickpython)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)
_________________

[Read Latest Documentation](https://timothycrosley.github.io/quickpython/) - [Browse GitHub Code Repository](https://github.com/timothycrosley/quickpython/)
_________________

![Example Usage](https://raw.githubusercontent.com/timothycrosley/quickpython/master/art/example.gif)

**QuickPYTHON** A retro-futuristic educational interactive coding environment. Powered by Python and nostalgia.

Key features

- Mouse support
- Futuristic blue color scheme
- Auto-formatting
- Integrated Debugging Support
- Quick shortcuts for creating new dataclasses, static methods, etc
- Built-in help
- Games!

## Quick Start Instructions

```bash
pip install quickpython
```

then start with

```bash
qpython
```

or

```bash
quickpython
```
_________________

# What is different to the original version?

In this branch is a version of `quickpython` that contains a visual debugger: 
![Example Usage](art/debug_example.gif)

To debug your programs, you can use the following keys:

  * `ctrl+d` ... start/stop the debugger
  * `ctrl+b` ... set a breakpoint on the line under the cursor
  * `ctrl+n` ... execute the `n`ext line
  * `ctrl+i` ... step into execution of a function/method
  * `ctrl+c` ... continue execution until the next breakpoint is hit or the program ends


Technically, this visual debugger is done by wrapping `pdb` via `pexpect`.

Things that I think should be there but are not implemented yet:

  * The frames to the right `Locals`, `Globals`, `Output` should be of fixed height, scrollable in both directions, and they should only appear when the debugger is active.
  * Some of the output from PDB has to be removed from the displayed output, e.g., `--Return--`


*Disclaimer*: This project is provided as-is, for fun, with no guarantee of long-term support or maintenance.
