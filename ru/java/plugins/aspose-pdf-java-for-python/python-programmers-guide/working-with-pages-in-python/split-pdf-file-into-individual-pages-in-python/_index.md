---
title: Разделение PDF файла на отдельные страницы на Python
type: docs
weight: 80
url: ru/java/split-pdf-file-into-individual-pages-in-python/
lastmod: "2021-06-05"
---

Чтобы разделить PDF документ на отдельные страницы с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# перебрать все страницы
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# создать новый объект Document
new_document = self.Document();

# получить страницу по определенному индексу из коллекции страниц
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# сохранить вновь сгенерированный PDF файл
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Процесс разделения успешно завершен!";
```

**Скачать работающий код**

Скачайте **Разделение страниц (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)