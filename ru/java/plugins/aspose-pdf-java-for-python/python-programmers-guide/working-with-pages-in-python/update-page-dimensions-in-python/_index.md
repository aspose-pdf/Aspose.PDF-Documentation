---
title: Обновление размеров страницы в Python
linktitle: Обновление размеров страницы в Python
type: docs
weight: 90
url: /ru/java/update-page-dimensions-in-python/
description: Поймите, как обновить размеры страницы в PDF‑документе на Python с использованием Aspose.PDF для лучшего контроля макета документа.
lastmod: "2026-08-19"
---
Чтобы обновить размеры страницы, используя **Aspose.PDF Java for Python**, просто вызовите класс **UpdatePageDimensions**.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

**Скачать работающий код**

Скачать **Update Page Dimensions (Aspose.PDF)** из любого из перечисленных ниже сайтов совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)

