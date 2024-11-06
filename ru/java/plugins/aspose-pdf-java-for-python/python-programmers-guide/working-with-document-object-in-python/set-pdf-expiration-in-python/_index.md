---
title: Установить срок действия PDF в Python
type: docs
weight: 80
url: ru/java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

Чтобы установить срок действия PDF-документа с использованием **Aspose.PDF Java для Python**, просто вызовите класс **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('Файл просрочен. Вам нужен новый.');");

doc.setOpenAction(javascript);

# сохранить обновленный документ с новой информацией
doc.save(self.dataDir + "set_expiration.pdf");

print "Обновите информацию документа, пожалуйста, проверьте выходной файл."
```

**Загрузить работающий код**

Загрузите **Установить срок действия PDF (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)