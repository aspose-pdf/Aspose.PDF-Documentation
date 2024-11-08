---
title: Tambahkan String HTML menggunakan DOM di Python
type: docs
weight: 10
url: /id/python-java/add-html-string-using-dom-in-python/
---

Untuk menambahkan string HTML dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil modul **AddHtml**.

```python

# Membuat objek Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Mengatur informasi margin
title.setMargin(margin)

# Menambahkan Fragmen HTML ke koleksi paragraf halaman
page.getParagraphs().add(title)

# Menyimpan file PDF
doc.save(self.dataDir + 'html.output.pdf')

print "HTML berhasil ditambahkan"
```

**Unduh Kode Berjalan**

Unduh **Tambahkan HTML (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)