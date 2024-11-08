---
title: Hapus Metadata dari PDF di Python
type: docs
weight: 70
url: /id/python-java/remove-metadata-from-pdf-in-python/
---

<ins>Untuk menghapus Metadata dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **RemoveMetadata**.

**Kode Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# simpan dokumen yang diperbarui dengan informasi baru
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Metadata berhasil dihapus, silakan periksa file output."
```


**Unduh Kode Berjalan**

Unduh **Hapus Metadata (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)