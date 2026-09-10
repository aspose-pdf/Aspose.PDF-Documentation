---
title: Définir les informations du fichier PDF en Python
linktitle: Définir les informations du fichier PDF en Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
description: Découvrez comment définir les informations d'un fichier PDF telles que l'auteur, le titre, etc. en Python à l'aide d'Aspose.PDF pour organiser les documents.
lastmod: "2026-06-09"
---

Pour mettre à jour les informations du document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **SetPdfFileInfo**.


```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```


**Télécharger le code d'exécution**

Téléchargez** Définir les informations du fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
