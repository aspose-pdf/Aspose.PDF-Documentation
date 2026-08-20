---
title: Extraiga texto de todas las páginas de un documento PDF en Python
linktitle: Extraiga texto de todas las páginas de un documento PDF en Python
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: Explica cómo extraer texto de páginas PDF en Python usando la API de formato de archivo PDF.
---
## 
Extraer texto de PDF usando Python



Para extraer el documento PDF TextrFrom All the Pages usando **Aspose.PDF Java para Python**, simplemente invoque el módulo **ExtractTextFromAllPages**.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**Descargar código de ejecución**



Descargue **Extraiga texto de todas las páginas (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
