---
title: Mengubah PDF ke HTML dalam Python 
linktitle: Mengubah PDF ke format HTML
type: docs
weight: 50
url: /python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Topik ini menunjukkan cara mengubah file PDF ke format HTML dengan pustaka Aspose.PDF untuk Python .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Ikhtisar

Artikel ini menjelaskan bagaimana **mengubah PDF ke HTML menggunakan Python**. Ini mencakup topik-topik berikut.

_Format_: **HTML**
- [Python PDF ke HTML](#python-pdf-to-html)
- [Python Mengubah PDF ke HTML](#python-pdf-to-html)
- [Python Cara mengubah file PDF ke HTML](#python-pdf-to-html)


## Mengubah PDF ke HTML

**Aspose.PDF untuk Python via .NET** menyediakan banyak fitur untuk mengonversi berbagai format file ke dalam dokumen PDF dan mengonversi file PDF ke berbagai format keluaran.
 Artikel ini membahas bagaimana mengonversi file PDF menjadi <abbr title="HyperText Markup Language">HTML</abbr>. Anda dapat menggunakan beberapa baris kode Python untuk mengonversi PDF ke HTML. Anda mungkin perlu mengonversi PDF ke HTML jika ingin membuat situs web atau menambahkan konten ke forum online. Salah satu cara untuk mengonversi PDF ke HTML adalah dengan menggunakan Python secara programatis.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke HTML secara online**

Aspose.PDF untuk Python menyajikan aplikasi gratis online ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Langkah-langkah: Mengonversi PDF ke HTML dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # simpan dokumen dalam format HTML
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **HTML**
- [Kode Python PDF ke HTML](#python-pdf-to-html)
- [API Python PDF ke HTML](#python-pdf-to-html)
- [Python PDF ke HTML Secara Programatis](#python-pdf-to-html)
- [Pustaka Python PDF ke HTML](#python-pdf-to-html)
- [Python Menyimpan PDF sebagai HTML](#python-pdf-to-html)
- [Python Menghasilkan HTML dari PDF](#python-pdf-to-html)
- [Python Membuat HTML dari PDF](#python-pdf-to-html)

- [Konverter Python PDF ke HTML](#python-pdf-to-html)