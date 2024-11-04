---
title: Удаление метаданных из PDF на Python
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
lastmod: "2021-06-05"
---

Чтобы удалить метаданные из документа PDF, используя **Aspose.PDF Java for Python**, просто вызовите класс **RemoveMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# сохранить обновленный документ с новой информацией
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Метаданные успешно удалены, пожалуйста, проверьте выходной файл."

```

**Скачать Исполняемый Код**

Скачайте **Удаление метаданных (Aspose.PDF)** с любого из перечисленных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)