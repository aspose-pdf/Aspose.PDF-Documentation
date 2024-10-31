---
title: Mengonversi HTML ke PDF dalam Python
linktitle: Mengonversi file HTML ke PDF
type: docs
weight: 40
url: /python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: Topik ini menunjukkan kepada Anda cara mengonversi HTML ke PDF dan MHTML ke PDF menggunakan Aspose.PDF. untuk Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Ikhtisar 

Aspose.PDF untuk Python via .NET adalah solusi profesional yang memungkinkan Anda membuat file PDF dari halaman web dan kode HTML mentah dalam aplikasi Anda.

Artikel ini menjelaskan cara **mengonversi HTML ke PDF menggunakan Python**. Ini mencakup topik-topik berikut.

_Format_: **HTML**
- [Python HTML ke PDF](#python-html-to-pdf)
- [Python Mengonversi HTML ke PDF](#python-html-to-pdf)
- [Python Cara mengonversi HTML ke PDF](#python-html-to-pdf)

## Konversi HTML ke PDF dalam Python

**Aspose.PDF untuk Python** adalah API manipulasi PDF yang memungkinkan Anda mengonversi dokumen HTML yang ada ke PDF dengan mulus. Proses mengonversi HTML ke PDF dapat disesuaikan dengan fleksibel.

## Mengonversi HTML ke PDF

Contoh kode Python berikut menunjukkan cara mengonversi dokumen HTML ke PDF.

1. Buat instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Simpan dokumen PDF keluaran dengan memanggil metode **Document.Save()**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**Coba konversi HTML ke PDF secara online**

Aspose menyajikan aplikasi gratis online ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi HTML ke PDF menggunakan Aplikasi Gratis](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}