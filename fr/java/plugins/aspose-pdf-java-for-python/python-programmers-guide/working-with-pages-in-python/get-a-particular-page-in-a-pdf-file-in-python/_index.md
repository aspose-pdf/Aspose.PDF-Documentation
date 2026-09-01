---
title: Obtenir une page particulière dans un fichier PDF en Python
linktitle: Obtenir une page particulière dans un fichier PDF en Python
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
description: Découvrez comment extraire une page particulière d'un fichier PDF en Python à l'aide d'Aspose.PDF pour une gestion détaillée des documents.
lastmod: "2026-06-09"
---

Pour obtenir une page particulière dans un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **GetPage**.


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

 
**Télécharger le code d'exécution**

Téléchargez **Obtenir la page (Aspose.PDF)**À partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
