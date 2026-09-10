---
title: Insérer une page vide dans un fichier PDF en Python
linktitle: Insérer une page vide dans un fichier PDF en Python
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Découvrez comment insérer une page vide à n'importe quel endroit dans un fichier PDF à l'aide de Python et Aspose.PDF pour une structuration flexible des documents.
lastmod: "2026-06-09"
---

Pour insérer une page vide dans un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **InsertEmptyPage**.


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


**Télécharger le code d'exécution**

Téléchargez** Insérer une page vide (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
