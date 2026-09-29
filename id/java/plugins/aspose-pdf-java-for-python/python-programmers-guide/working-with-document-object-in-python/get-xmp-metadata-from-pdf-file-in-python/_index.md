---
title: Dapatkan Metadata XMP dari File PDF dalam Python
linktitle: Dapatkan Metadata XMP dari File PDF dalam Python
type: docs
weight: 50
url: /id/java/get-xmp-metadata-from-pdf-file-in-python/
description: Temukan cara mengambil metadata XMP dari file PDF dalam Python menggunakan Aspose.PDF, memungkinkan analisis konten yang detail.
lastmod: "2026-09-29"
---
Untuk mendapatkan Metadata XMP dari dokumen Pdf menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Unduh Kode yang Berjalan**

UnduhВ **Get XMP Metadata (Aspose.PDF)**В dariВ semua situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
