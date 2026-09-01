---
title: Insérer une page vide à la fin du fichier PDF en Python
linktitle: Insérer une page vide à la fin du fichier PDF en Python
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Découvrez comment insérer une page vide à la fin d'un document PDF en Python avec Aspose.PDF pour une extension facile du document.
lastmod: "2026-06-09"
---

Pour insérer une page vide à la fin d'un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **InsertEmptyPageAtEndOfFile**.


```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```


**Télécharger le code d'exécution**

Téléchargez ** Insérer une page vide à la fin du fichier PDF (Aspose.PDF) ** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
