---
title: 在 Python 中添加 JavaScript
linktitle: 在 Python 中添加 JavaScript
type: docs
weight: 10
url: /java/adding-javascript-in-python/
description: 了解如何使用 Python 和 Aspose.PDF 在 PDF 文档中嵌入 JavaScript 代码以增强交互性。
lastmod: "2026-06-09"
---
要在 Python 中使用 Aspose.PDF Java 附加 Add Javascript，只需调用 Document 类的 AddJavascript() 方法即可。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Adding JavaScript at Page Level
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Save PDF Document
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```

**下载运行代码**

从以下任何一个社交编码网站下载 **Add Javascript (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
