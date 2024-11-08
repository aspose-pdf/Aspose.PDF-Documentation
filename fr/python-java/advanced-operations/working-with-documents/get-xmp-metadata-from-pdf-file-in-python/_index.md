---
title: Obtenir les Métadonnées XMP du Fichier PDF en Python
type: docs
weight: 50
url: /fr/python-java/get-xmp-metadata-from-pdf-file-in-python/
---

<ins>Pour obtenir les métadonnées XMP d'un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **GetXMPMetadata**.

**Code Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtenir les propriétés
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Télécharger le Code Exécuté**

Téléchargez **Obtenir les Métadonnées XMP (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)