import wx

class TextEditorToolbar(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.editor = parent
        self._init_ui()
        self._init_event()

    def _init_ui(self):
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.tool_font_name = wx.Choice(self, choices=['Helvetica','Arial','sans-serif'])
        self.tool_font_size = wx.Choice(self, choices=['12','13','14','16','18','24','36','48','72'])

        self.main_sizer.AddSpacer(2)
        self.main_sizer.Add(self.tool_font_name, flag=wx.RIGHT, border=5)
        self.main_sizer.Add(self.tool_font_size, flag=wx.RIGHT, border=5)

        self.SetSizer(self.main_sizer)

    def _init_event(self):
        self.tool_font_name.Bind(wx.EVT_CHOICE, self._on_font_name_selected)
        self.tool_font_size.Bind(wx.EVT_CHOICE, self._on_font_size_selected)

    def _on_font_name_selected(self, e):
        pass

    def _on_font_size_selected(self, e):
        pass