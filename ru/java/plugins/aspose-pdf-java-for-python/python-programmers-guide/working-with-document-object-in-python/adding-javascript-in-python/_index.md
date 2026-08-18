---
title: Добавление JavaScript в Python
linktitle: Добавление JavaScript в Python
type: docs
weight: 10
url: /java/adding-javascript-in-python/
description: Узнайте, как встроить код JavaScript в документ PDF с помощью Python и Aspose.PDF для повышения интерактивности.
lastmod: "2026-06-09"
---
Чтобы добавить «Добавить Javascript» с помощью Aspose.PDF Java в Python, просто вызовите метод AddJavascript() класса Document.

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

**Загрузить рабочий код**

Загрузите **Добавить Javascript (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
