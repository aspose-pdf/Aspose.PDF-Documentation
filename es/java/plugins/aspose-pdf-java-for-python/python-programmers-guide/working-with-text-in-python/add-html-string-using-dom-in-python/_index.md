---
title: Agregar cadena HTML usando DOM en Python
type: docs
weight: 10
url: /es/java/add-html-string-using-dom-in-python/
lastmod: "2021-06-05"
keywords: html dom python, python html dom library
description: Explica cómo agregar una cadena HTML en DOM usando Python con biblioteca de formato de archivo PDF
---

## Agregar cadena HTML en PDF DOM usando Python
Para agregar una cadena HTML en un documento Pdf usando **Aspose.PDF Java for Python**, simplemente invoque el módulo **AddHtml**.

```python

# Instanciar objeto Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Tabla</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Establecer información de margen
title.setMargin(margin)

# Agregar fragmento HTML a la colección de párrafos de la página
page.getParagraphs().add(title)

# Guardar archivo PDF
doc.save(self.dataDir + 'html.output.pdf')

print "HTML agregado exitosamente"
```

**Descargar Código en Ejecución**

Descargar **Add HTML (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)