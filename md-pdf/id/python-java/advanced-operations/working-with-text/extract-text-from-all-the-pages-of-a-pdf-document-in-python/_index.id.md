---
title: Ekstrak Teks Dari Semua Halaman Dokumen PDF di Python
type: docs
weight: 30
url: /python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

Untuk mengekstrak teks dari semua halaman dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil modul **ExtractTextFromAllPages**.

```python
# Buka dokumen target
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Teks diekstraksi dengan sukses. Periksa file keluaran."

```

**Unduh Kode yang Berjalan**

Unduh **Ekstrak Teks Dari Semua Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)