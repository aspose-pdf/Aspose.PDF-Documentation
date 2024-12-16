---
title: Tambahkan String HTML menggunakan DOM di Python
type: docs
weight: 10
url: /id/java/add-html-string-using-dom-in-python/
lastmod: "2021-06-05"
description: Menjelaskan cara menambahkan string HTML di DOM menggunakan Python dengan pustaka format file PDF
---

## Tambahkan string HTML di PDF DOM menggunakan Python
Untuk menambahkan string HTML dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil modul **AddHtml**.

```python

# Instansiasi objek Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Tetapkan informasi margin
title.setMargin(margin)

# Tambahkan Fragmen HTML ke koleksi paragraf halaman
page.getParagraphs().add(title)

# Simpan file PDF
doc.save(self.dataDir + 'html.output.pdf')

print "HTML berhasil ditambahkan"
```

**Unduh Kode Berjalan**

Unduh **Tambahkan HTML (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)