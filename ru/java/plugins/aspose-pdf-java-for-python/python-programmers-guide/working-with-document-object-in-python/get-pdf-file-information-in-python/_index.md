---
title: Получение информации о PDF файле на Python
type: docs
weight: 40
url: ru/java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Чтобы получить информацию о файле PDF документа, используя **Aspose.PDF Java для Python**, просто вызовите класс **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Получить информацию о документе
doc_info = doc.getInfo();

# Показать информацию о документе
print "Автор:-" + str(doc_info.getAuthor())
print "Дата создания:-" + str(doc_info.getCreationDate())
print "Ключевые слова:-" + str(doc_info.getKeywords())
print "Дата изменения:-" + str(doc_info.getModDate())
print "Тема:-" + str(doc_info.getSubject())
print "Название:-" + str(doc_info.getTitle())
```

**Скачать исполняемый код**

Скачайте **Получение информации о PDF файле (Aspose.PDF)** с одного из нижеуказанных сайтов социального программирования:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)