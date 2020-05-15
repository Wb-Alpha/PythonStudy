import wx

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wxPython')#创建窗口
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()#创建App类的实例
    app.MainLoop()#调用App类的MainLoop()主循环方法