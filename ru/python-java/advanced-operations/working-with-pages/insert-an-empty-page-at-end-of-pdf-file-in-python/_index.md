---
title: Вставка пустой страницы в конец PDF файла на Python
type: docs
weight: 60
url: /ru/python-java/insert-an-empty-page-at-end-of-pdf-file-in-python/
---

<ins>Чтобы вставить пустую страницу в конец PDF документа с использованием **Aspose.PDF Java for Python**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

**Код на Python**
```

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# вставить пустую страницу в PDF
pdf_document.getPages().add();

# Сохранить объединенный выходной файл (целевой документ)
pdf_document.save(self.dataDir + "output.pdf")

print "Пустая страница успешно добавлена!"

```

**Загрузить выполняемый код**

Скачайте **Вставка пустой страницы в конец PDF файла (Aspose.PDF)** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)