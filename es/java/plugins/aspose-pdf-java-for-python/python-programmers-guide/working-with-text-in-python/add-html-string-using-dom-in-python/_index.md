---
title: Agregar cadena HTML usando DOM en Python
linktitle: Add HTML String using DOM in Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: Explica cómo agregar una cadena HTML en DOM usando Python con la biblioteca de formato de archivo PDF
---
## Add HTML string in PDF DOM using Python

To add HTML string in Pdf document using **Aspose.PDF Java for Python**, simply invoke **AddHtml** module.

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

**Download Running Code**

DownloadВ **Add HTML (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
