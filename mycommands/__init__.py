"""Command module.
Useful commands for myshell to manage the presentation of information in the terminal, and to find information on programs and classes to which myshell has access."""

from mycommands.core import MyCommand

from .command.clearterminal import ClearTerminal
from .command.pagebreak import PageBreak
from .command.listall import ListAll