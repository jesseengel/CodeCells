import sublime, sublime_plugin

def find_cell_bounds(self):
    # Find all cells
    cells = self.view.find_all('#\s*\%\%')
    prior_begin, cell_begin, tmp = 0, 0, 0
    post_begin = self.view.size()
    position = self.view.sel()[0].begin()

    for region in cells:
        if region.begin() <= position:
            prior_begin = tmp
            tmp = region.begin()
            cell_begin = tmp + len(self.view.full_line(region))

        if region.begin() > position:
            post_begin = region.begin()
            break

    return prior_begin, cell_begin, post_begin




class ExecuteCellCommand(sublime_plugin.TextCommand):
   def run(self, edit):
        # Find all cells
        prior_cell_begin, cell_begin, cell_end = find_cell_bounds(self)

        # Copy cell
        cell_region = sublime.Region(cell_begin, cell_end)                
        cell_txt = self.view.substr(cell_region)
        sublime.set_clipboard(cell_txt + '\n')

        # Move to next cell
        self.view.sel().clear()
        self.view.sel().add( sublime.Region(cell_end, cell_end) )
        self.view.show(cell_end)


class MoveDownCellCommand(sublime_plugin.TextCommand):
   def run(self, edit):
        # Find all cells
        prior_cell_begin, cell_begin, cell_end = find_cell_bounds(self)

        # Copy cell
        cell_region = sublime.Region(cell_begin, cell_end)                
        cell_txt = self.view.substr(cell_region)
        sublime.set_clipboard( sublime.get_clipboard() + '\n' + cell_txt + '\n')

        # Move to next cell
        self.view.sel().clear()
        self.view.sel().add( sublime.Region(cell_end, cell_end) )
        self.view.show(cell_end)


class MoveUpCellCommand(sublime_plugin.TextCommand):
   def run(self, edit):
        # Find all cells
        prior_cell_begin, cell_begin, cell_end = find_cell_bounds(self)

        # Clear clipboard
        sublime.set_clipboard('')

        # Move to previous cell
        self.view.sel().clear()
        self.view.sel().add( sublime.Region(prior_cell_begin, prior_cell_begin) )
        self.view.show(prior_cell_begin)






def up_a_line(self, line):
    return self.view.line( sublime.Region(line.begin()-1, line.begin()-1) )

def down_a_line(self, line):
    return self.view.line( sublime.Region(line.end()+1, line.end()+1) )


class InsertCellDivider(sublime_plugin.TextCommand):
    def run(self, edit):
        cell_divider = '\
#==============================================================================\n\
# %%%% %s\n\
#==============================================================================\n'

        for region in self.view.sel():
            line = self.view.line(region)
            if line.empty():
                self.view.insert(edit, line.begin(), cell_divider % '')
                # Move cursor to text enter area
                line = down_a_line(self, line)
                line = down_a_line(self, line)
                self.view.sel().clear()
                self.view.sel().add( sublime.Region(line.end(), line.end()) )
            else:
                line = self.view.line(region)

                # Remove cell markers
                cell_markers = self.view.find_all('#\s*\%\%\s*')
                for cell_marker in cell_markers:
                    if line.contains(cell_marker):
                        self.view.erase(edit, cell_marker)
                        line = self.view.line(region)
                    if cell_marker.begin() > line.end():
                        break

                line_contents = self.view.substr(line)
                self.view.erase(edit, line)
                self.view.insert(edit, line.begin(), cell_divider % line_contents)

