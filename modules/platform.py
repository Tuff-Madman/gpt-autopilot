import sys

def join_cmd(cmd_list):
    joiner = " & " if sys.platform.startswith('win') else "; "
    return joiner.join(cmd_list)
