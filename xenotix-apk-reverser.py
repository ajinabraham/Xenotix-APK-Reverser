'''
Xenotix APK Reverser
Ajin Abraham
www.opensecurity.in
Xenotix APK Reverser is an OpenSource Android Application Package (APK) decompiler and disassembler powered by dex2jar, baksmali and jd-core
Released under Apache License

Requirements
============
Java
Download WxPython
Windows: http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.12.1-py27.exe
Ubuntu: sudo apt-get install python-wxgtk2.8
'''

import os,platform,wx,shutil,subprocess
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
  decomp=filemenu.Append(wx.ID_ANY,"&Decompile","Decompile APK to java")
  self.Bind(wx.EVT_MENU,self.Decompile,decomp)
  diss=filemenu.Append(wx.ID_ANY,"&Disassemble","Disassemble APK to smali")
  self.Bind(wx.EVT_MENU,self.Disassemble,diss)
  about=filemenu.Append(wx.ID_ABOUT,"&About","About Xenotix APK Reverser")
  filemenu.AppendSeparator()
  self.Bind(wx.EVT_MENU,self.About,about)
  x=filemenu.Append(wx.ID_EXIT,"E&xit","Exit the APK Reverser")
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
     self.path=dlg.GetPath()
     self.filename=dlg.GetFilename()
     y=open(self.path,'rb')
     self.contents=y.read()
     y.close()
     x=open("temp.apk","wb")
     x.write(self.contents)
     x.close()
     apk=self.filename
     dlgx=wx.MessageDialog(self,"Opened APK: "+self.filename,"APK Reverser",wx.OK)
     dlgx.ShowModal()
     dlgx.Destroy()
   dlg.Destroy()
 def Decompile(self,e):
     global apk
     if os.path.isfile('temp.apk'):
	  dlgx=wx.MessageDialog(self,"Please Wait. This process takes time.","APK Reverser",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
	  try:
          	shutil.rmtree("src")
          	os.mkdir("src")
		if platform.system()=="Windows":
			os.system("d2j-dex2jar.bat temp.apk")
		else:
			os.system("./d2j-dex2jar.sh temp.apk")
          	os.system("java -jar jd-core.jar temp-dex2jar.jar src")
		os.remove("temp-dex2jar.jar")
	  except Exception,err:
	  	print Exception,err
          dlgx=wx.MessageDialog(self,"Decompiled Sucessfully. Check the src directory","APK Reverser",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
	  if platform.system()=="Windows":
		  path=os.path.dirname(os.path.abspath(__file__)) +'\src'
		  os.system('explorer '+path )
	  else:
		  os.system('xdg-open "%s"' % "src")
	  

     else:
          dlgx=wx.MessageDialog(self,"Select an APK to Decompile","APK Reverser",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
 def Disassemble(self,e):
     global apk
     if os.path.isfile('temp.apk'):
	  dlgx=wx.MessageDialog(self,"Please Wait. This process takes time.","APK Reverser",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
	  try:
          	shutil.rmtree("smali")
          	os.mkdir("smali")
		os.system("java -jar baksmali.jar temp.apk -o smali")
	  except Exception,err:
	  	print Exception,err
          dlgx=wx.MessageDialog(self,"Disassembled Sucessfully. Check the smali directory","APK Reverser",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
	  if platform.system()=="Windows":
		  path=os.path.dirname(os.path.abspath(__file__)) +'\smali'
		  os.system('explorer '+path )
	  else:
		  os.system('xdg-open "%s"' % "src")
     else:
          dlgx=wx.MessageDialog(self,"Select an APK to Decompile","APK Reverser",wx.OK)
          dlgx.ShowModal()
          dlgx.Destroy()
 def About(self,e):
   dlgx= wx.MessageDialog(self,"Xenotix APK Reverser is an OpenSource Android Application Package (APK) decompiler and disassembler powered by dex2jar, baksmali and jd-core\nDeveloped by Ajin Abraham | http://opensecurity.in. ","About",wx.OK)
   dlgx.ShowModal()
   dlgx.Destroy()
 def Exit(self,e):
   self.Close(True)
app=wx.App(False)
f=maingui(None,"Xenotix APK Reverser")
f.SetIcon(wx.Icon("lib/ico.ico", wx.BITMAP_TYPE_ICO))
app.MainLoop()
