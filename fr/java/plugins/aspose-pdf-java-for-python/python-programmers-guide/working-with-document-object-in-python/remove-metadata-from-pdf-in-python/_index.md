---
title: Supprimer les métadonnées du PDF en Python
linktitle: Supprimer les métadonnées du PDF en Python
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
description: Découvrez comment supprimer les métadonnées des documents PDF en Python à l'aide d'Aspose.PDF, garantissant ainsi la confidentialité et la sécurité des données.
lastmod: "2026-06-09"
---

Pour supprimer les métadonnées d'un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **RemoveMetadata**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```


**Télécharger le code d'exécution**

Téléchargez** Supprimer les métadonnées (Aspose.PDF)** de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
