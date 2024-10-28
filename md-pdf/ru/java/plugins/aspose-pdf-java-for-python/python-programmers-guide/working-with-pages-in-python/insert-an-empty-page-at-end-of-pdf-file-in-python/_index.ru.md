---
title: Вставить пустую страницу в конец PDF файла на Python
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

Чтобы вставить пустую страницу в конец PDF документа, используя **Aspose.PDF Java для Python**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# вставить пустую страницу в PDF
pdf_document.getPages().add();

# Сохранить объединенный выходной файл (целевой документ)
pdf_document.save(self.dataDir + "output.pdf")

print "Пустая страница успешно добавлена!"

```

**Скачать работающий код**

Скачайте **Вставить пустую страницу в конец PDF файла (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)