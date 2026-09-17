---
title: Diviser un fichier PDF en pages individuelles en Python
linktitle: Diviser un fichier PDF en pages individuelles en Python
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
description: Découvrez comment diviser un PDF en pages individuelles en Python à l'aide d'Aspose.PDF, permettant une extraction et une gestion faciles des pages.
lastmod: "2026-06-09"
---

Pour diviser un document PDF en pages individuelles à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **SplitAllPages**.


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


**Télécharger le code d'exécution**

Téléchargez **Split Pages (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
