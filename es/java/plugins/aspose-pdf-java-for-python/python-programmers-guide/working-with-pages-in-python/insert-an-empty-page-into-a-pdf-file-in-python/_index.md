---
title: Insertar una página vacía en un archivo PDF en Python
linktitle: Insertar una página vacía en un archivo PDF en Python
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Aprenda a insertar una página vacía en cualquier posición dentro de un archivo PDF usando Python y Aspose.PDF para una estructuración flexible de documentos.
lastmod: "2026-06-09"
---

Para insertar una página vacía en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **InsertEmptyPage**.


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


**Descargar código de ejecución**

Descargue **Inserte una página vacía (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
