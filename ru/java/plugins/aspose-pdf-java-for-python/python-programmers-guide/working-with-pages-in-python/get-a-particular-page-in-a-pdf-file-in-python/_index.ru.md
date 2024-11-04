---
title: Получить Конкретную Страницу в PDF Файле на Python
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

Чтобы получить конкретную страницу в PDF документе, используя **Aspose.PDF Java для Python**, просто вызовите класс **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# получить страницу по определенному индексу из коллекции страниц
pdf_page = pdf.getPages().get_Item(1)

# создать новый объект Document
new_document = self.Document()

# добавить страницу в коллекцию страниц нового объекта документа
new_document.getPages().add(pdf_page)

# сохранить вновь созданный PDF файл
new_document.save(self.dataDir + "output.pdf")

print "Процесс успешно завершен!"

```

 **Скачать Исполняемый Код**

Скачайте **Get Page (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)