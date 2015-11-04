CodeCells is a simple package for Sublime Text 2/3 that facilitates copying and pasting chunks of python code from a script into a REPL like IPython. This allows you the easy of working with cells of code that you might get from an IPython Notebook, but with the work flow of having separate panels for your code and it's output. 

The use of cells is taken from the Spyder IDE `#%%`, which in turn took it from Matlab `%%`. It could be extended to other languages by changing the cell marker, but I thought it might be useful to others in it's current form.

Code cells can be copied to the clipboard (for pasting into your favorite REPL) and traversed up and down quickly. There is also a command for quickly creating cell markers which is helpful for code as well. 

## Usage 
I find it easy to add the following quick bindings lines to my user keymap.

```json
{ "keys": ["shift+enter"], "command": "execute_cell" }, # Copy cell and move to bottom of cell
{ "keys": ["alt+down"], "command": "move_down_cell" }, # Incrementally adds cells to clipboard
{ "keys": ["alt+up"], "command": "move_up_cell" }, # Clear Clipboard
{ "keys": ["super+shift+/"], "command": "insert_cell_divider" } # Also works with text selected 
```
