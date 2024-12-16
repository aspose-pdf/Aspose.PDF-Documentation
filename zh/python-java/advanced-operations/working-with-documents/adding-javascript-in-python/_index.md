---
title: 在 Python 中添加 JavaScript
type: docs
weight: 10
url: /zh/python-java/adding-javascript-in-python/
---

要在 Python 中使用 Aspose.PDF Java 添加 JavaScript，只需调用 Document 类的 AddJavascript() 方法。

**Python 代码**

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# 在页面级别添加 JavaScript
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# 保存 PDF 文档
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```

**下载运行代码**

从以下任一社交编程网站下载 **添加 JavaScript (Aspose.PDF)**:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)