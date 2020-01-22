import wx
from exp_seq import fastafile
from exp_dialogs import addseqwindow

class GUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None)
        self.SetTitle("ExpFasta 0.1 beta")
        self.myfasta = fastafile("")
        self.draw()
        self.Show()
        
    def draw(self):
        panel = wx.Panel(self)
        self.toolbarui()
        self.listbox = wx.ListCtrl(panel,style=wx.LC_REPORT)
        self.listbox.InsertColumn(0,'Index',wx.LIST_FORMAT_CENTER,width=100)
        self.listbox.InsertColumn(1,'Length',wx.LIST_FORMAT_CENTER,width=100)
        self.listbox.InsertColumn(2,'Description',wx.LIST_FORMAT_LEFT,width=400)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED,self.showseq,self.listbox)
        self.textbox = wx.TextCtrl(panel,style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.status = self.CreateStatusBar(1)
        self.status.SetStatusText("Ready")
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.listbox,2,wx.EXPAND)
        box.Add(self.textbox,1,wx.EXPAND)
        panel.SetSizer(box)
        self.SetMinSize(wx.Size(600,400))

    def toolbarui(self):
        self.toolbar=wx.ToolBar(self,-1)
        self.toolbar.AddTool(101,'OPEN',wx.Bitmap("Images/open.png"),shortHelp="Open Fasta File")
        self.toolbar.AddTool(102,'CLOSE',wx.Bitmap("Images/close.png"),shortHelp="Close Fasta File")
        self.toolbar.AddSeparator()
        self.toolbar.AddTool(103,'ADD',wx.Bitmap("Images/add.png"),shortHelp="Add new Sequence")
        self.toolbar.AddTool(104,'FILTER',wx.Bitmap("Images/filter.png"),shortHelp="Filter Data")
        self.toolbar.AddTool(105,'SAVE',wx.Bitmap("Images/save.png"),shortHelp="Save As")
        self.toolbar.Bind(wx.EVT_TOOL,self.catchtoolevent)
        self.ToolBar = self.toolbar

    def catchtoolevent(self,event):
        m_id = event.GetId()
        if m_id == 101:
            formats = "Fasta File (*.fasta)|*.fasta|Fasta File(*.fa)|*.fa"
            dialog = wx.FileDialog(self,"Choose Fasta File","~","",formats,wx.FD_OPEN)
            if dialog.ShowModal() == wx.ID_OK:
                self.myfasta = fastafile(dialog.GetPath())
                try:
                    self.myfasta.read()
                    self.loadlistbox()
                except:
                    wx.MessageBox("Error Loading File","Error")
        if m_id == 102:
            self.myfasta = fastafile('')
            self.listbox.DeleteAllItems()
            self.textbox.SetValue('')
            self.status.SetStatusText("Ready")
        if m_id == 103:
            addnwseq = addseqwindow()
            addnwseq.ShowModal()

    def loadlistbox(self):
        self.listbox.DeleteAllItems()
        d_arr = list(self.myfasta.data.keys())
        for i in range(0,len(self.myfasta.data)):
            self.listbox.InsertItem(i,"")
            self.listbox.SetItem(i,0,str(i+1))
            self.listbox.SetItem(i,1,str(len(self.myfasta.data[d_arr[i]])))
            self.listbox.SetItem(i,2,str(d_arr[i]))
        d_arr = []
        self.textbox.SetValue('')
        self.status.SetStatusText("Total: "+str(len(self.myfasta.data))+" sequences.")

    def showseq(self,event):
        self.textbox.SetValue(self.myfasta.data[self.listbox.GetItem(event.GetIndex(),2).GetText()])
