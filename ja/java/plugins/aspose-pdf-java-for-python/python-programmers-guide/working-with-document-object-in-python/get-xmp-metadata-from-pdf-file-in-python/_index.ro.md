---
title: Obțineți Metadate XMP din Fișier PDF în Python
type: docs
weight: 50
url: ja/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

Pentru a obține Metadate XMP dintr-un document Pdf folosind **Aspose.PDF Java pentru Python**, pur și simplu invocați clasa **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obțineți proprietățile
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Descărcați Codul Funcțional**

Descărcați **Obțineți Metadate XMP (Aspose.PDF)** de la oricare dintre site-urile sociale de codare menționate mai jos:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)