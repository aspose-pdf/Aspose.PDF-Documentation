---
title: Mettre à jour les dimensions de la page en Python
linktitle: Mettre à jour les dimensions de la page en Python
type: docs
weight: 90
url: /java/update-page-dimensions-in-python/
description: Comprenez comment mettre à jour les dimensions d'une page dans un document PDF en Python à l'aide d'Aspose.PDF pour un meilleur contrôle de la mise en page du document.
lastmod: "2026-06-09"
---

Pour mettre à jour les dimensions de la page à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **UpdatePageDimensions**.


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


**Télécharger le code d'exécution**

Téléchargez** Mettre à jour les dimensions de la page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
