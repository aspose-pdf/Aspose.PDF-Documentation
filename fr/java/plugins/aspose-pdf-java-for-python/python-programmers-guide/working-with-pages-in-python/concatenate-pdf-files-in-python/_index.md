---
title: Concaténer des fichiers PDF en Python
linktitle: Concaténer des fichiers PDF en Python
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
description: Apprenez à concaténer plusieurs fichiers PDF en un seul document PDF en Python à l'aide d'Aspose.PDF, simplifiant ainsi la gestion des documents.
lastmod: "2026-06-09"
---

Pour concaténer des fichiers PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **ConcatenatePdfFiles**.


```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```


**Télécharger le code d'exécution**

Téléchargez** Concaténer des fichiers PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
