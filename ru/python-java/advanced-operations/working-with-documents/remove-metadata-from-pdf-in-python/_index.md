---
title: Удаление метаданных из PDF на Python
type: docs
weight: 70
url: ru/python-java/remove-metadata-from-pdf-in-python/
---

<ins>Чтобы удалить метаданные из PDF-документа с использованием **Aspose.PDF Java для Python**, просто вызовите класс **RemoveMetadata**.

**Код на Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# сохраните обновленный документ с новой информацией
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Метаданные успешно удалены, пожалуйста, проверьте выходной файл."
```


**Скачать исполняемый код**

Скачайте **Удаление метаданных (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)