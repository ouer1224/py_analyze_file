import wx
#from .noname import note
from .text_editor_toolbar import TextEditorToolbar


class TextEditor(wx.Panel):#Panel表示不是一个单独的窗口,如果修改为Frame,就变为了2个独立的窗口
    def __init__(self, parent):
        super().__init__(parent)
        self._init_ui()
    def _init_ui(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.bSizer1 = wx.BoxSizer(wx.VERTICAL)
        self._init_title()
        self._init_toolbar()
        self._init_edit()
        self.SetSizer(self.bSizer1)
    def _init_title(self):
        self.tc_title = wx.TextCtrl(self, wx.ID_ANY, u"请输入标题", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer1.Add(self.tc_title, 0, wx.ALL | wx.EXPAND, 5)
    def _init_edit(self):
        self.tc_detail = wx.TextCtrl(self, wx.ID_ANY, u"请输入内容", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer1.Add(self.tc_detail, 1, wx.ALL | wx.EXPAND, 5)
    def _init_toolbar(self):
        self.toolbar = TextEditorToolbar(self);
        self.bSizer1.Add(self.toolbar, flag=wx.EXPAND | wx.LEFT, border=15)
        line = wx.StaticLine(self, size=(-1, 1))
        line.SetBackgroundColour("#e5e5e5")
        self.bSizer1.Add(line, flag=wx.EXPAND | wx.TOP, border=25);





