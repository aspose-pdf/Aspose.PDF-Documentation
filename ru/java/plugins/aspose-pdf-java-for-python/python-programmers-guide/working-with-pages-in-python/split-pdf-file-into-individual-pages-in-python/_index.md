---
title: Разделить PDF-файл на отдельные страницы в Python
linktitle: Разделить PDF-файл на отдельные страницы в Python
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
description: Узнайте, как разделить PDF-файл на отдельные страницы в Python с помощью Aspose.PDF, что позволяет легко извлекать страницы и управлять ими.
lastmod: "2026-06-09"
---
Чтобы разделить PDF-документ на отдельные страницы с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```

**Загрузить рабочий код**

Загрузите **Split Pages (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
