---
title: Agregar Texto a un PDF existente usando Python
type: docs
weight: 20
url: /es/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
description: Ejemplo de código sobre cómo agregar o escribir texto en un documento Pdf usando Python con la biblioteca PDF.
---

## Escribir o Agregar Texto en PDF usando Python

Para agregar una cadena de texto en un documento Pdf usando **Aspose.PDF Java para Python**, simplemente invoque el módulo **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Guardar archivo PDF
doc.save(self.dataDir + "Text_Added.pdf")
print "Texto agregado exitosamente"
```


**Descargar Código en Ejecución**

Descargue **Agregar Texto (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)