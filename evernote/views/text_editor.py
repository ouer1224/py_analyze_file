import wx
#from .noname import note
class TextEditor(wx.Panel):#Panel表示不是一个单独的窗口,如果修改为Frame,就变为了2个独立的窗口
    def __init__(self, parent):
        super().__init__(parent)
        #wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
        #                  size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.tc_title = wx.TextCtrl(self, wx.ID_ANY, u"请输入标题", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer1.Add(self.tc_title, 0, wx.ALL | wx.EXPAND, 5)

        self.tc_detail = wx.TextCtrl(self, wx.ID_ANY, u"请输入内容", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer1.Add(self.tc_detail, 1, wx.ALL | wx.EXPAND, 5)

        self.bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_save = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer2.Add(self.btn_save, 0, wx.ALL, 5)

        self.bSizer1.Add(self.bSizer2, 0, wx.EXPAND, 5)

        self.SetSizer(self.bSizer1)
        #self.Layout()

        #self.Centre(wx.BOTH)