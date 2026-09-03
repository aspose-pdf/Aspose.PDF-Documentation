---
title: Insertar una página en blanco al final de un archivo PDF en Python
linktitle: Insertar una página en blanco al final de un archivo PDF en Python
type: docs
weight: 60
url: /es/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Descubra cómo insertar una página en blanco al final de un documento PDF en Python con Aspose.PDF para una fácil expansión de documentos.
lastmod: "2026-09-03"
---
Para insertar una página en blanco al final de un documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Descargar código en ejecución**

Descargar **Insertar una página vacía al final del archivo PDF (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
