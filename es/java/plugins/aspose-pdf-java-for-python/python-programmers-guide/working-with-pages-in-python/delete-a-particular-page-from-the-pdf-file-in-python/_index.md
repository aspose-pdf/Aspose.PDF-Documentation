---
title: Eliminar una página específica del archivo PDF en Python
linktitle: Eliminar una página específica del archivo PDF en Python
type: docs
weight: 20
url: /es/java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Aprenda cómo eliminar una página específica de un documento PDF en Python usando Aspose.PDF, proporcionando una edición de documentos eficiente.
lastmod: "2026-09-03"
---
Para eliminar una página específica del documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **DeletePage**.

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

**Descargar código en ejecución**

Descargar **Delete Page (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
