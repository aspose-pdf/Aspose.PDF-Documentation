---
title: Obtenez des métadonnées XMP à partir d'un fichier PDF en Python
linktitle: Obtenez des métadonnées XMP à partir d'un fichier PDF en Python
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
description: Découvrez comment récupérer les métadonnées XMP d'un fichier PDF en Python à l'aide d'Aspose.PDF, permettant une analyse détaillée du contenu.
lastmod: "2026-06-09"
---

Pour obtenir les métadonnées XMP d'un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la classe **GetXMPMetadata**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```


**Télécharger le code d'exécution**

Téléchargez** Obtenez des métadonnées XMP (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
