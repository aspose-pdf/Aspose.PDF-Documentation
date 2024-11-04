---
title: Вставка Пустой Страницы в PDF Файл на Python
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

Чтобы вставить пустую страницу в документ PDF с использованием **Aspose.PDF Java для Python**, просто вызовите класс **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# вставить пустую страницу в PDF
pdf_document.getPages().insert(1)

# Сохранить объединенный выходной файл (целевой документ)
pdf_document.save(self.dataDir + "output.pdf")

print "Пустая страница успешно добавлена!"

```

**Скачать Запускаемый Код**

Скачайте **Вставка Пустой Страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)