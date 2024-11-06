---
title: Удаление Конкретной Страницы из PDF Файла на Python
type: docs
weight: 20
url: ru/python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

Для удаления конкретной страницы из PDF документа с использованием **Aspose.PDF Java для Python**, просто вызовите класс **DeletePage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# удалить конкретную страницу
pdf.getPages().delete(2)

# сохранить вновь созданный PDF файл
doc.save(self.dataDir + "output.pdf")

print "Страница успешно удалена!"

```

**Скачать Исполняемый Код**

Скачайте **Delete Page (Aspose.PDF)** с любого из указанных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)