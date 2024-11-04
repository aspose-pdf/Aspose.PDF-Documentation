---
title: 获取文档窗口和页面显示属性在 Python 中
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

要获取 PDF 文档的窗口和页面显示属性，使用 **Aspose.PDF Java for Python**，只需调用 **GetDocumentWindow** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取不同的文档属性
# 文档窗口的位置 - 默认: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# 主要的阅读顺序；确定页面的位置
# 当并排显示时 - 默认: L2R
print "Direction :- " + str(doc.getDirection())

# 窗口的标题栏是否应显示文档标题。
# 如果为 false，标题栏显示 PDF 文件名 - 默认: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# 是否调整文档窗口的大小以适应
# 第一个显示的页面的大小 - 默认: false
print "FitWindow :- " + str(doc.getFitWindow())

# 是否隐藏查看器应用程序的菜单栏 - 默认: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# 是否隐藏查看器应用程序的工具栏 - 默认: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# 是否隐藏 UI 元素如滚动条
# 仅显示页面内容 - 默认: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# 文档的页面模式。退出全屏模式时如何显示文档。
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# 页面布局，即单页、单列
print "PageLayout :-" + str(doc.getPageLayout())

# 文档打开时应如何显示。
print "pageMode :-" + str(doc.getPageMode())
```


**下载运行代码**

从以下任一社交编程网站下载**获取文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)