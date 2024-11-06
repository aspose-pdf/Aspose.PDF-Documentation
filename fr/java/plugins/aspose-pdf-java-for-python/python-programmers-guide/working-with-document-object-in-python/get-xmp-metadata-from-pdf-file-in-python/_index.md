---
title: Obtenir les métadonnées XMP d'un fichier PDF en Python
type: docs
weight: 50
url: fr/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

Pour obtenir les métadonnées XMP d'un document Pdf en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtenir les propriétés
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Télécharger le code en cours d'exécution**

Téléchargez **Obtenir les métadonnées XMP (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)