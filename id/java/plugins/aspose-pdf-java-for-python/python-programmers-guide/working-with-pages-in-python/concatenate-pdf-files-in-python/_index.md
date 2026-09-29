---
title: Menggabungkan File PDF di Python
linktitle: Menggabungkan File PDF di Python
type: docs
weight: 10
url: /id/java/concatenate-pdf-files-in-python/
description: Pelajari cara menggabungkan beberapa file PDF menjadi satu dokumen PDF di Python menggunakan Aspose.PDF, menyederhanakan manajemen dokumen.
lastmod: "2026-09-29"
---
Untuk menggabungkan file PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```

**Unduh Kode yang Berjalan**

Unduh **Concatenate PDF Files (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
