import re
import ast
import platform
from pexpect.replwrap import REPLWrapper


# For Windows, see https://github.com/raczben/wexpect
PDB_COMMAND = "python -m pdb {}"
PDB_PROMPT_STR = "(Pdb) "
GET_LOCALS_CMD = "{k: str(v) for k, v in locals().items() if k != '__builtins__'}"
GET_GLOBALS_CMD = "{k: str(v) for k, v in globals().items() if k != '__builtins__'}"
NEXT_CMD = "n"
STEP_CMD = "s"
CONTINUE_CMD = "c"
SET_BREAKPOINT_CMD = "b {}:{}"  # First is filename, second is line number


class Debugger:
    """Debugger"""

    def __init__(self, python_module: str, breakpoints: list[int]):
        self.python_module = python_module
        self.current_line = None
        self.current_locals = None
        self.current_globals = None

        self.pdb_command = PDB_COMMAND.format(python_module)
        # TODO: Change prompt to something more unique, via last arg
        os_str = platform.system()
        if os_str == "Windows":
            raise NotImplmentedError
            # TODO: Implement me
        elif os_str == "Linux" or os_str == "Darwin":
            try:
                self.pdb = REPLWrapper(self.pdb_command, PDB_PROMPT_STR, None)
            except Exception as e:
                raise e
        else:
            # What here??? Is there anything else where it should/could work?
            raise NotImplmentedError

        # Set all the breakpoints from the file
        self.set_breakpoints(self.python_module, breakpoints)

    def update_locals(self):
        response = self.pdb.run_command(GET_LOCALS_CMD)
        locals_dict = ast.literal_eval(response)
        self.current_locals = locals_dict

    def update_globals(self):
        response = self.pdb.run_command(GET_GLOBALS_CMD)
        globals_dict = ast.literal_eval(response)
        self.current_globals = globals_dict

    def _parse_lineno(self, response):
        if response.startswith("The program finished and will be restarted"):
            # The debugger would otherwise continue forever.
            return None

        try:
            # Parse the currently active line out of the pdb output
            # '> /path/to/python/module.py(3)<module>()\r\n-> b = 1.2\r\n'
            reg_exp = f"{self.python_module}\((?P<lineno>\d+)\)"
            match = re.search(reg_exp, response, flags=0)
            active_line = None
            if match.groupdict():
                active_line = int(match.groupdict()["lineno"])

            self.update_locals()
            self.update_globals()
        except Exception:
            # The second last response coming from pdb does not contain a line
            # number either... It looks like:
            # --Return--\r\n> <string>(1)<module>()->None\r\n
            # Likely this case is also good for all other potential parsing
            # issues?
            return None
        return active_line

    def next_line(self):
        response = self.pdb.run_command(NEXT_CMD)
        return self._parse_lineno(response)

    def step(self):
        response = self.pdb.run_command(STEP_CMD)
        return self._parse_lineno(response)

    def continue_debug(self):
        response = self.pdb.run_command(CONTINUE_CMD)
        return self._parse_lineno(response)

    def set_breakpoint(self, fname, lineno):
        bp_cmd = SET_BREAKPOINT_CMD.format(fname, lineno)
        self.pdb.run_command(bp_cmd)
        # I do not think I need to parse responses since they could look like:
        # 'Breakpoint 1 at /Users/ropf/Documents/workspace/Python/qpython/quickpython/examples/fibonacci.py:10\r\n'
        # or like:
        # '*** Blank or comment\r\n'

    def set_breakpoints(self, fname, linenos):
        for brkpoint in linenos:
            self.set_breakpoint(self.python_module, brkpoint)

    def kill_debugger(self):
        self.pdb.child.terminate(force=True)
