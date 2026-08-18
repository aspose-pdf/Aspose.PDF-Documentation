---
title: Добавьте строку HTML, используя DOM в Python
linktitle: Добавьте строку HTML, используя DOM в Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: Объясняет, как добавить строку HTML в DOM с помощью Python с библиотекой форматов файлов PDF.
---
## Добавьте строку HTML в PDF DOM с помощью Python

Чтобы добавить строку HTML в документ PDF с помощью **Aspose.PDF Java for Python**, просто вызовите модуль **AddHtml**.

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**Загрузить рабочий код**

Загрузите **Добавьте HTML (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
