---
title: Получить информацию о PDF-файле на Python
type: docs
weight: 40
url: /python-java/get-pdf-file-information-in-python/
---

<ins>Чтобы получить информацию о файле PDF-документа с использованием **Aspose.PDF Java for Python**, просто вызовите класс **GetPdfFileInfo**.

**Код на Python**
```

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
print "Заголовок:-" + str(doc_info.getTitle())
```

**Скачать работающий код**

Скачайте **Получить информацию о PDF-файле (Aspose.PDF)** с любого из нижеуказанных социальных кодирующих сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)