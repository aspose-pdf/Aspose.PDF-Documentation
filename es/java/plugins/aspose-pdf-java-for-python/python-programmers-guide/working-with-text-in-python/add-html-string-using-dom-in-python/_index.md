---
title: Agregar cadena HTML usando DOM en Python
linktitle: Agregar cadena HTML usando DOM en Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: Explica cómo agregar una cadena HTML en DOM usando Python con la biblioteca de formato de archivo PDF
---
## 
Agregue una cadena HTML en PDF DOM usando Python



Para agregar una cadena HTML en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque el módulo **AddHtml**.

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

**Descargar código de ejecución**



Descargue **Agregue HTML (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
