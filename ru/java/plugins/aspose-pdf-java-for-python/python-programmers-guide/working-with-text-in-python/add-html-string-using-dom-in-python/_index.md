---
title: Добавление HTML‑строки с использованием DOM в Python
linktitle: Добавление HTML‑строки с использованием DOM в Python
type: docs
weight: 10
url: /ru/java/add-html-string-using-dom-in-python/
lastmod: "2026-09-17"
description: Объясняет, как добавить HTML‑строку в DOM с помощью Python и библиотеки формата файлов PDF
---
## Добавление HTML‑строки в PDF‑DOM с помощью Python

Чтобы добавить HTML‑строку в документ Pdf с использованием **Aspose.PDF Java for Python**, просто вызовите модуль **AddHtml**.

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

**Скачать исполняемый код**

Скачайте **Add HTML (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)


