---
title: Eliminar una página particular del archivo PDF en Python
linktitle: Eliminar una página particular del archivo PDF en Python
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Aprenda cómo eliminar una página específica de un documento PDF en Python usando Aspose.PDF, proporcionando una edición de documentos eficiente.
lastmod: "2026-06-09"
---

Para eliminar una página particular del documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **DeletePage**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```


**Descargar código de ejecución**

Descargue **Eliminar página (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
