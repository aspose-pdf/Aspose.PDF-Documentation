---
title: "Menambahkan string HTML menggunakan DOM di Python"
linktitle: "Menambahkan string HTML menggunakan DOM di Python"
type: docs
weight: 10
url: /id/java/add-html-string-using-dom-in-python/
lastmod: "2026-09-30"
description: "Menjelaskan cara menambahkan String HTML dalam DOM menggunakan Python dengan pustaka format file PDF"
---
## Menambahkan string HTML dalam PDF DOM menggunakan Python

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

**Mengunduh kode yang dapat dijalankan**

Download **Tambahkan HTML (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
