---
title: Concatenar archivos PDF en Python
linktitle: Concatenar archivos PDF en Python
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
description: Aprenda a concatenar varios archivos PDF en un solo documento PDF en Python usando Aspose.PDF, simplificando la administración de documentos.
lastmod: "2026-06-09"
---

Para concatenar archivos PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **ConcatenatePdfFiles**.


```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```


**Descargar código de ejecución**

Descargue **Concatenar archivos PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
