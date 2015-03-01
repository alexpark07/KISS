from __future__ import with_statement
import gdb

class SaveBreakpointsCommand(gdb.Command):
    def __init__(self):
        super(SaveBreakpointsCommand, self).__init__("save breakpoints", gdb.COMMAND_SUPPORT, gdb.COMPLETE_FILENAME)

    def invoke(self, args, from_tty):
        with open(args, 'w') as f:
            for bp in gdb.get_breakpoints():
                print >> f, "break", bp.get_location(),
                if bp.get_thread() is not None:
                    print >> f, " thread", bp.get_thread

                if bp.get_condition() is not None:
                    print >> f, " if", bp.get_condition(),

                print >> f

                if not bp.is_enabled():
                    print >> f, "disable $bpnum"

                commands = bp.get_commands()
                if commands is not None:
                    print >> f, "commands"

                    print >> f, commands,
                    print >> f, "end"
                print >> f

SaveBreakpointsCommand()

