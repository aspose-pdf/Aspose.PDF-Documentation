---
title: Установить срок действия PDF в Python
type: docs
weight: 80
url: /ru/python-java/set-pdf-expiration-in-python/
---

<ins>Чтобы установить срок действия PDF документа с использованием **Aspose.PDF Java for Python**, просто вызовите класс **SetExpiration**.

**Код на Python**
```

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# сохранить обновленный документ с новой информацией
doc.save(self.dataDir + "set_expiration.pdf");

print "Обновите информацию о документе, пожалуйста, проверьте выходной файл."
```

**Скачать выполняемый код**

Скачайте **Set PDF Expiration (Aspose.PDF)** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)