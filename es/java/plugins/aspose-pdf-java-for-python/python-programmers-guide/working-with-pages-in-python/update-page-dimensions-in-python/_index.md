---
title: Actualizar dimensiones de página en Python
linktitle: Actualizar dimensiones de página en Python
type: docs
weight: 90
url: /es/java/update-page-dimensions-in-python/
description: Comprenda cómo actualizar las dimensiones de página dentro de un documento PDF en Python usando Aspose.PDF para un mejor control del diseño del documento.
lastmod: "2026-09-03"
---
Para actualizar las dimensiones de página usando **Aspose.PDF Java for Python**, simplemente invoque la clase **UpdatePageDimensions**.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

**Descargar código en ejecución**

DescargarВ **Actualizar dimensiones de página (Aspose.PDF)**В desdeВ cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
