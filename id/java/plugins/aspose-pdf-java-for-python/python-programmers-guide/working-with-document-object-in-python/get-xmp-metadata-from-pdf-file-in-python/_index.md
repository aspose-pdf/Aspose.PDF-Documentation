---
title: Dapatkan Metadata XMP dari File PDF di Python
type: docs
weight: 50
url: /id/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

Untuk mendapatkan Metadata XMP dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Dapatkan properti
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Unduh Kode yang Berjalan**

Unduh **Get XMP Metadata (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)