import sublime
import sublime_plugin


# Required PowerCursor extension
class ExpandCursorDown(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command("power_cursor_add")
    self.view.run_command("move", {"by": "lines", "forward": True})
    self.view.run_command("power_cursor_activate")
