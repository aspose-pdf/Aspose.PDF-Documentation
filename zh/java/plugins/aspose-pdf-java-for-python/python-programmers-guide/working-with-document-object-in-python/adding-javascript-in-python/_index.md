---
title: 在Python中添加JavaScript
linktitle: 在Python中添加JavaScript
type: docs
weight: 10
url: /zh/java/adding-javascript-in-python/
description: 了解如何使用Python和Aspose.PDF在PDF文档中嵌入JavaScript代码，以增强交互性。
lastmod: "2026-10-06"
---
要在Python中使用Aspose.PDF Java添加JavaScript，只需调用Document类的AddJavascript()方法。

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

下载 **Add Javascript (Aspose.PDF)**，请从以下任意社交编码站点获取：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
