---
title: Добавление JavaScript в Python
type: docs
weight: 10
url: ru/python-java/adding-javascript-in-python/
---

Чтобы добавить JavaScript с использованием Aspose.PDF Java в Python, просто вызовите метод AddJavascript() класса Document.

**Python Код**

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

# Сохранение PDF документа
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript успешно добавлен, пожалуйста, проверьте выходной файл."

```

**Скачать Исполняемый Код**

Скачайте **Add Javascript (Aspose.PDF)** из любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)