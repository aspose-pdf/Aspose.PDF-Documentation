---
title: 获取 Python 中的文档窗口和页面显示属性
type: docs
weight: 30
url: /python-java/get-document-window-and-page-display-properties-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 获取 PDF 文档的窗口和页面显示属性，只需调用 **GetDocumentWindow** 类。

**Python 代码**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取不同的文档属性
# 文档窗口的位置 - 默认: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# 主要的阅读顺序；确定页面并排显示时的位置 - 默认: L2R
print "Direction :- " + str(doc.getDirection())

# 窗口的标题栏是否应显示文档标题。
# 如果为 false，标题栏显示 PDF 文件名 - 默认: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# 是否调整文档窗口的大小以适应
# 第一个显示页面的大小 - 默认: false

print "FitWindow :- " + str(doc.getFitWindow())

# 是否隐藏查看器应用程序的菜单栏 - 默认值: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# 是否隐藏查看器应用程序的工具栏 - 默认值: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# 是否隐藏UI元素如滚动条
# 并仅显示页面内容 - 默认值: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# 文档的页面模式。退出全屏模式时如何显示文档。
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# 页面布局，即单页，一列
print "PageLayout :-" + str(doc.getPageLayout())

# 打开文档时的显示方式。
print "pageMode :-" + str(doc.getPageMode())
```


**下载运行代码**

从以下任一社交编码网站下载 **获取文档窗口和页面显示属性 (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)