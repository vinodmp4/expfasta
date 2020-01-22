import wx

class addseqwindow(wx.Dialog):
    def __init__(self,parent=None,title="Add New Sequence"):
        super(addseqwindow,self).__init__(parent=parent,title=title)
        self.draw()
        

    def draw(self):
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        #----- RADIO BUTTON REGION ----------
        radiobox = wx.BoxSizer(wx.HORIZONTAL)
        customseq = wx.RadioButton(panel,label="Enter custom sequence")
        onlineseq = wx.RadioButton(panel,label="Load from database")
        radiobox.Add(customseq)
        radiobox.Add(onlineseq,border=10,flag=wx.LEFT)
        #------------------------------------
        #------ CUSTOM BUTTON REGION --------
        custombox = wx.BoxSizer(wx.VERTICAL)
        self.customdesc = wx.TextCtrl(panel)
        self.customseqn = wx.TextCtrl(panel,style=wx.TE_MULTILINE)
        custombox.Add(wx.StaticText(panel,label="Enter description here:"))
        custombox.Add(self.customdesc,flag=wx.EXPAND)
        custombox.Add(wx.StaticText(panel,label="Enter sequence here:"))
        custombox.Add(self.customseqn,proportion=2,flag=wx.EXPAND)
        #------------------------------------
        #------ USER BUTTON REGION ----------
        self.addbutton = wx.Button(panel,label='Add Sequence')
        self.cancelbutton = wx.Button(panel,wx.ID_CANCEL,label='Cancel')
        hbox.Add(self.cancelbutton)
        hbox.Add(self.addbutton,border=10,flag=wx.LEFT)
        #-------------------------------------
        vbox.Add(radiobox,proportion=1,flag=wx.ALIGN_CENTER)
        vbox.Add(custombox,proportion=5,flag=wx.EXPAND)
        vbox.Add(hbox,proportion=1,flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM,border=10)
        panel.SetSizer(vbox)
        self.addbutton.Bind(wx.EVT_BUTTON,self.OnClose)

    def OnClose(self,event):
        self.Destroy()
