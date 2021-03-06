# ============================================================================
# FILE: time.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from defx.base.column import Base
from defx.context import Context
from defx.util import Nvim, readable

import time


class Column(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'time'
        self._length = 0
        self.vars = {
            'format': '%y.%m.%d %H:%M',
        }

    def on_init(self, context: Context) -> None:
        self._length = self.vim.call('strwidth',
                                     time.strftime(self.vars['format']))

    def get(self, context: Context, candidate: dict) -> str:
        path = candidate['action__path']
        if not readable(path) or path.is_dir():
            return str(' ' * self._length)
        return time.strftime(self.vars['format'],
                             time.localtime(path.stat().st_mtime))

    def length(self, context: Context) -> int:
        return self._length

    def highlight(self) -> None:
        self.vim.command(
            f'highlight default link {self.syntax_name} Identifier')
