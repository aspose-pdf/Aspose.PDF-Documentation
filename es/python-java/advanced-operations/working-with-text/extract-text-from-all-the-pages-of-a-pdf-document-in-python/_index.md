---
title: Extraer Texto De Todas las Páginas de un Documento PDF en Python
type: docs
weight: 30
url: /es/python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

Para extraer texto de todas las páginas de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca el módulo **ExtractTextFromAllPages**.

```python
# Abre el documento objetivo
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Texto extraído exitosamente. Revisa el archivo de salida."

```

**Descargar Código en Ejecución**

Descarga **Extraer Texto De Todas las Páginas (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)