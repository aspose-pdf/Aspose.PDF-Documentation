---
title: Добавление JavaScript в Python
type: docs
weight: 10
url: /ru/java/adding-javascript-in-python/
lastmod: "2021-06-05"
---

Чтобы добавить JavaScript с использованием Aspose.PDF Java в Python, просто вызовите метод AddJavascript() класса Document.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Добавление JavaScript на уровне страницы
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Сохранить PDF документ
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript успешно добавлен, пожалуйста, проверьте выходной файл."

```

**Скачать запущенный код**

Скачать **Add Javascript (Aspose.PDF)** с любого из нижеупомянутых сайтов для социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)