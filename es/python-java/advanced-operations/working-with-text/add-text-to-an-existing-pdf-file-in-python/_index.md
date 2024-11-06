---
title: Agregar texto a un archivo PDF existente en Python
type: docs
weight: 20
url: es/python-java/add-text-to-an-existing-pdf-file-in-python/
---

Para agregar una cadena de texto en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca el módulo **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("texto principal")
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

**Descargar código ejecutable**

Descarga **Agregar Texto (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)