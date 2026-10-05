---
title: Insertar una página vacía al final del archivo PDF en Python
linktitle: Insertar una página vacía al final del archivo PDF en Python
type: docs
weight: 60
url: /es/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Descubra cómo insertar una página vacía al final de un documento PDF en Python con Aspose.PDF para una fácil expansión del documento.
lastmod: "2026-09-29"
---
Para insertar una página vacía al final del documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **InsertEmptyPageAtEndOfFile**.

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

Descargar **Insert an Empty Page at End of PDF File (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
