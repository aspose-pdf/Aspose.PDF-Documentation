---
title: Définir l'expiration du PDF en Python
linktitle: Définir l'expiration du PDF en Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
description: Découvrez comment définir une date d'expiration pour un fichier PDF en Python à l'aide d'Aspose.PDF pour un accès aux documents urgent.
lastmod: "2026-06-09"
---

Pour définir l'expiration d'un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **SetExpiration**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```


**Télécharger le code d'exécution**

Téléchargez** Définir l'expiration du PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
