---
title: Obtener una página concreta en un archivo PDF en Python
linktitle: Obtener una página concreta en un archivo PDF en Python
type: docs
weight: 30
url: /es/java/get-a-particular-page-in-a-pdf-file-in-python/
description: Explore cómo extraer una página concreta de un archivo PDF en Python usando Aspose.PDF para un manejo detallado de documentos.
lastmod: "2026-09-03"
---
Para obtener una página concreta en un documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 **Descargar código en ejecución**

Descargar **Get Page (Aspose.PDF)**В desdeВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
