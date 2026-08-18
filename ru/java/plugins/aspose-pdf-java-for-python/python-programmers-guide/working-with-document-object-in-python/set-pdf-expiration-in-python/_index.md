---
title: Установить срок действия PDF в Python
linktitle: Установить срок действия PDF в Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
description: Узнайте, как установить дату истечения срока действия PDF-файла в Python с помощью Aspose.PDF для доступа к документам, чувствительным ко времени.
lastmod: "2026-06-09"
---
Чтобы установить срок действия PDF-документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```

**Загрузить рабочий код**

Загрузите **Установите срок действия PDF (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
