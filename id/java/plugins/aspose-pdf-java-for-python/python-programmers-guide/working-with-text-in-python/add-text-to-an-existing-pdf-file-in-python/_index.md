---
title: Tambahkan Teks ke PDF yang Ada Menggunakan Python
type: docs
weight: 20
url: /id/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
description: Contoh kode bagaimana menambahkan atau menulis teks dalam dokumen Pdf menggunakan Python dengan pustaka PDF.
---

## Menulis atau Menambahkan Teks dalam PDF menggunakan Python

Untuk menambahkan string Teks dalam dokumen Pdf menggunakan **Aspose.PDF Java for Python**, cukup panggil modul **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("teks utama")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Simpan file PDF
doc.save(self.dataDir + "Text_Added.pdf")
print "Teks berhasil ditambahkan"
```


**Unduh Kode yang Sedang Berjalan**

Unduh **Tambahkan Teks (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)