---
title: Удаление определенной страницы из PDF-файла на Python
type: docs
weight: 20
url: ru/java/delete-a-particular-page-from-the-pdf-file-in-python/
lastmod: "2021-06-05"
---

Чтобы удалить определенную страницу из PDF-документа с помощью **Aspose.PDF Java для Python**, просто вызовите класс **DeletePage**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# удалить определенную страницу
pdf.getPages().delete(2)

# сохранить вновь созданный PDF-файл
doc.save(self.dataDir + "output.pdf")

print "Страница успешно удалена!"

```

**Скачать выполняемый код**

Скачайте **Удаление страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)