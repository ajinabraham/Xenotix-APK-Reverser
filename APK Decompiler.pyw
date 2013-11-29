'''
Xenotix APK Decompiler
Ajin Abraham
www.opensecurity.in
APK Decompiler is an OpenSource Android Application Package (APK) decompiler powered by dex2jar and JAD
Released under Apache License
'''
import wx #Download: http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.12.1-py27.exe
import os
apk=""
class maingui(wx.Frame):
 def __init__(self,parent,title):
  wx.Frame.__init__(self,None,-1,title=title,pos=wx.DefaultPosition, style=wx.DEFAULT_FRAME_STYLE,size=(320,200))
  self.Fit()
  self.CenterOnScreen()
  self.application=parent
  filemenu = wx.Menu()
  self.CreateStatusBar()
  openapk=filemenu.Append(wx.ID_ANY, "&Open","Open an APK")
  self.Bind(wx.EVT_MENU,self.OpenAPK,openapk)
  decomp=filemenu.Append(wx.ID_ANY,"&Decompile","Decompile the APK")
  self.Bind(wx.EVT_MENU,self.Decompile,decomp)
  about=filemenu.Append(wx.ID_ABOUT,"&About","About Xenotix APK Decompiler")
  filemenu.AppendSeparator()
  self.Bind(wx.EVT_MENU,self.About,about)
  x=filemenu.Append(wx.ID_EXIT,"E&xit","Exit the APK Decompiler")
  self.Bind(wx.EVT_MENU,self.Exit,x)
  menu=wx.MenuBar()
  menu.Append(filemenu,"&File")
  self.SetMenuBar(menu)
  self.Show(True)
 def OpenAPK(self,e):
   global apk
   self.dirname=""
   dlg= wx.FileDialog(self,"Choose an APK file",self.dirname,"","*.apk",wx.OPEN)
   if dlg.ShowModal()== wx.ID_OK:
     self.filename=dlg.GetFilename()
     self.dirname=dlg.GetDirectory()
     y=open(os.path.join(self.dirname,self.filename),'rb')
     self.contents=y.read()
     y.close()
     x=open("temp.apk","wb")
     x.write(self.contents)
     x.close()
     apk=self.filename
     dlgx=wx.MessageDialog(self,"Opened APK: "+self.filename,"APK Decompiler",wx.OK)
     dlgx.ShowModal()
     dlgx.Destroy()
   dlg.Destroy()
 def Decompile(self,e):
     global apk
     if os.path.isfile('temp.apk'):
          os.system("rmdir /Q /S src")
          os.system("rmdir /Q /S classes")
          os.system("mkdir classes")
          os.system("mkdir src")
          dlgx=wx.MessageDialog(self,"Please Wait. This process takes time.","APK Decompiler",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
          os.system("d2j-dex2jar.bat temp.apk")
          os.system("del temp.apk")
          os.system("ren temp-dex2jar.jar temp_dex2jar.zip")
          os.system("unzip -qq temp_dex2jar.zip -d classes")
          os.system("del temp_dex2jar.zip")
          os.system("jad.exe  -o -r -sjava -dsrc classes/**/*.class")
          dlgx=wx.MessageDialog(self,"Decompiled Sucessfully. Check the src directory","APK Decompiler",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
     else:
          dlgx=wx.MessageDialog(self,"Select an APK to Decompile","APK Decompiler",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
 def About(self,e):
   dlgx= wx.MessageDialog(self,"Xenotix APK Decompiler is an OpenSource Android Application Package (APK) decompiler powered by dex2jar and JAD. ","About",wx.OK)
   dlgx.ShowModal()
   dlgx.Destroy()
 def Exit(self,e):
   self.Close(True)
app=wx.App(False)
f=maingui(None,"Xenotix APK Decompiler")
f.SetIcon(wx.Icon("lib/ico.ico", wx.BITMAP_TYPE_ICO))
app.MainLoop()
