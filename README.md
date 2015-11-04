A simple plugin for Sublime Text 2/3 that allows you to define code cells with a specifier (set by default to #%% inspired by the Spyder IDE for python, which also takes the idea from matlab`%%`).

Code cells can be copied to the clipboard (for pasting into your favorite REPL) and travsersed up and down quickly. I alos have a command for quickly creating cell demarkers which is helpful for code as well. 

## Usage 
I find it easy to add the following quick bindings lines to my user keymap.

```json
{ "keys": ["shift+enter"], "command": "execute_cell" },
{ "keys": ["alt+down"], "command": "move_down_cell" },
{ "keys": ["alt+up"], "command": "move_up_cell" },
{ "keys": ["super+shift+/"], "command": "insert_cell_divider" }
```
