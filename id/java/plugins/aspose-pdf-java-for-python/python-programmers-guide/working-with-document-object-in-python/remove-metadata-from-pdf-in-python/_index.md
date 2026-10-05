---
title: "Menghapus metadata dari PDF di Python"
linktitle: "Menghapus metadata dari PDF di Python"
type: docs
weight: 70
url: /id/java/remove-metadata-from-pdf-in-python/
description: Ketahui cara menghapus metadata dari dokumen PDF di Python menggunakan Aspose.PDF, memastikan privasi dan keamanan data.
lastmod: "2026-09-30"
---
Untuk menghapus Metadata dari dokumen Pdf menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **RemoveMetadata**.

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

**Mengunduh kode yang dapat dijalankan**

Unduh **Remove Metadata (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
