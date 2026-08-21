---
title: Supprimer une page particulière du fichier PDF en Python
linktitle: Supprimer une page particulière du fichier PDF en Python
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Découvrez comment supprimer une page spécifique d'un document PDF en Python à l'aide d'Aspose.PDF, permettant une édition efficace du document.
lastmod: "2026-06-09"
---

Pour supprimer une page particulière du document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **DeletePage**.


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


**Télécharger le code d'exécution**

Téléchargez ** Supprimer la page (Aspose.PDF) ** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
