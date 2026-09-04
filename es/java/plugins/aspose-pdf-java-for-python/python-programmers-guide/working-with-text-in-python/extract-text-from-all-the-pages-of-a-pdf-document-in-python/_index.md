---
title: Extraer Texto de Todas las Páginas de un Documento PDF en Python
type: docs
weight: 30
url: /es/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
description: Explica cómo extraer texto de las páginas de un PDF en Python usando la API del formato de archivo PDF.
---

## Extraer Texto del PDF usando Python

Para extraer texto de todas las páginas de un documento Pdf usando **Aspose.PDF Java para Python**, simplemente invoca el módulo **ExtractTextFromAllPages**.

```python

# Abrir el documento objetivo
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Texto extraído con éxito. Verifica el archivo de salida."

```

**Descargar Código en Ejecución**

Descarga **Extraer Texto de Todas las Páginas (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)