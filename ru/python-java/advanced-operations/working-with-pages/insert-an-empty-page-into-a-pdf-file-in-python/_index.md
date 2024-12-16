---
title: Вставка пустой страницы в PDF файл на Python
type: docs
weight: 70
url: /ru/python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>Чтобы вставить пустую страницу в PDF документ с использованием **Aspose.PDF Java for Python**, просто вызовите класс **InsertEmptyPage**.

**Python Код**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# вставить пустую страницу в PDF
pdf_document.getPages().insert(1)

# Сохраните объединенный выходной файл (целевой документ)
pdf_document.save(self.dataDir + "output.pdf")

print "Пустая страница успешно добавлена!"

```

**Скачать работающий код**

Скачайте **Вставка пустой страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)