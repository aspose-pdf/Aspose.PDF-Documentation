---
title: Obtenir des informations sur un fichier PDF en Python
linktitle: Obtenir des informations sur un fichier PDF en Python
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: Découvrez comment récupérer des informations détaillées sur un fichier PDF telles que les métadonnées et les propriétés en Python à l'aide d'Aspose.PDF pour la gestion des documents.
lastmod: "2026-06-09"
---

Pour obtenir les informations sur le fichier d'un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **GetPdfFileInfo**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```


**Télécharger le code d'exécution**

Téléchargez** Obtenez des informations sur le fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
