---
title: Insertar una página vacía en un archivo PDF con Python
linktitle: Insertar una página vacía en un archivo PDF con Python
type: docs
weight: 70
url: /es/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Aprenda cómo insertar una página vacía en cualquier posición dentro de un archivo PDF usando Python y Aspose.PDF para una estructuración flexible de documentos.
lastmod: "2026-09-03"
---
Para insertar una página vacía en un documento Pdf usando **Aspose.PDF Java for Python**, simplemente invoque la clase **InsertEmptyPage**.

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

DescargarВ **Insertar una página vacía (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
