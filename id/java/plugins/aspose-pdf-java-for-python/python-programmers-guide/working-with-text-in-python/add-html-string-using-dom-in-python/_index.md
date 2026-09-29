---
title: Tambahkan String HTML menggunakan DOM di Python
linktitle: Tambahkan String HTML menggunakan DOM di Python
type: docs
weight: 10
url: /id/java/add-html-string-using-dom-in-python/
lastmod: "2026-09-29"
description: Menjelaskan cara menambahkan String HTML dalam DOM menggunakan Python dengan perpustakaan format file PDF
---
## Tambahkan String HTML dalam PDF DOM menggunakan Python

Untuk menambahkan string HTML dalam dokumen Pdf menggunakan **Aspose.PDF Java for Python**, cukup panggil modul **AddHtml**.

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**Unduh Kode yang Berjalan**

Download\u0412\u00A0**Tambahkan HTML (Aspose.PDF)**\u0412\u00A0dari\u0412\u00A0salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
