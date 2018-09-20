## About

[![Join the chat at https://gitter.im/Shougo/defx.nvim](https://badges.gitter.im/Shougo/defx.nvim.svg)](https://gitter.im/Shougo/defx.nvim?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Defx is a dark powered plugin for Neovim/Vim to browse files.
It can replace deprecated vimfiler plugin.


## Concept

* Not depends on denite.nvim

* Vim8/neovim compatible(nvim-yarp is needed for Vim8)

* Implemented by Python3

* No double filer feature

* Column feature

* Source feature like denite.nvim

* Options

* Highlight is defined by column

* Few commands (:Defx command only?)

* Extended rename

* Mark

* Windows supporters are needed

* Maximum features dislike other file managers


## Installation

**Note:** defx requires Neovim 0.3.0+ or Vim8.1+ with Python3.6.1+.  See
[requirements](#requirements) if you aren't sure whether you have this.

For vim-plug

```viml
if has('nvim')
  Plug 'Shougo/defx.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/defx.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
```

For dein.vim

```viml
call dein#add('Shougo/defx.nvim')
if !has('nvim')
  call dein#add('roxma/nvim-yarp')
  call dein#add('roxma/vim-hug-neovim-rpc')
endif
```

For manual installation(not recommended)

1. Extract the files and put them in your Neovim or .vim directory
   (usually `$XDG_CONFIG_HOME/nvim/`).


## Requirements

defx requires Python3.6.1+ and Neovim(0.3.0+) or Vim8.1+ with if\_python3.  If
`:echo has("python3")` returns `1`, then you have python 3 support; otherwise,
see below.

You can enable Python3 interface with pip:

    pip3 install neovim

Please install nvim-yarp plugin for Vim8.
https://github.com/roxma/nvim-yarp

Please install vim-hug-neovim-rpc plugin for Vim8.
https://github.com/roxma/vim-hug-neovim-rpc


## Note: Python3 must be enabled before updating remote plugins
If Defx was installed prior to Python support being added to Neovim,
`:UpdateRemotePlugins` should be executed manually.


## Configuration Examples

```vim
" Todo
```



## Screenshots

![multi root feature](https://user-images.githubusercontent.com/41495/45696476-ac9d0a80-bb9e-11e8-9ee2-120ac7d0f045.png)
![Defx -split=vertical](https://user-images.githubusercontent.com/2835826/45823772-7190f900-bcbc-11e8-9727-3dda3ce4c07c.png)
