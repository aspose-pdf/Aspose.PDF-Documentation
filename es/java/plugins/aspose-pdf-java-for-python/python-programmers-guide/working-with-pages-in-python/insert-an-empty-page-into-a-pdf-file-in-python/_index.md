---
title: Insertar una página en blanco en un archivo PDF en Python
linktitle: Insertar una página en blanco en un archivo PDF en Python
type: docs
weight: 70
url: /es/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Aprenda cómo insertar una página en blanco en cualquier posición dentro de un archivo PDF usando Python y Aspose.PDF para una estructuración flexible de documentos.
lastmod: "2026-09-29"
---
Para insertar una página en blanco en un documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Descargar código en ejecución**

Descargar **Insertar una página en blanco (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
