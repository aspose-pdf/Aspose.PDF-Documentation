---
title: Agregar cadena HTML usando DOM en Python
type: docs
weight: 10
url: es/python-java/add-html-string-using-dom-in-python/
---

Para agregar una cadena HTML en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca el módulo **AddHtml**.

```python

# Instanciar objeto Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Tabla</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Configurar la información de márgenes
title.setMargin(margin)

# Agregar Fragmento HTML a la colección de párrafos de la página
page.getParagraphs().add(title)

# Guardar archivo PDF
doc.save(self.dataDir + 'html.output.pdf')

print "HTML agregado con éxito"
```

**Descargar Código en Ejecución**

Descargar **Agregar HTML (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)