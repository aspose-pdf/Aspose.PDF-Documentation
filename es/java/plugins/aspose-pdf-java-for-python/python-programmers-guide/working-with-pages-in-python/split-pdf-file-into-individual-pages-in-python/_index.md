---
title: Dividir un archivo PDF en páginas individuales en Python
linktitle: Dividir un archivo PDF en páginas individuales en Python
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
description: Explore cómo dividir un PDF en páginas individuales en Python usando Aspose.PDF, lo que permite una fácil extracción y administración de páginas.
lastmod: "2026-06-09"
---

Para dividir un documento PDF en páginas individuales usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **SplitAllPages**.


```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```


**Descargar código de ejecución**

Descargue **Split Pages (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
