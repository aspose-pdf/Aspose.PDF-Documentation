---
title: Ekstrak Teks Dari Semua Halaman Dokumen PDF di Python
linktitle: Ekstrak Teks Dari Semua Halaman Dokumen PDF di Python
type: docs
weight: 30
url: /id/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-09-29"
description: Menjelaskan cara mengekstrak teks dari halaman PDF di Python menggunakan API format file PDF.
---
## Ekstrak Teks dari PDF menggunakan Python

Untuk mengekstrak TextrFrom Semua Halaman dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil modul **ExtractTextFromAllPages**.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**Unduh Kode yang Berjalan**

DownloadВ **Ekstrak Teks Dari Semua Halaman (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
