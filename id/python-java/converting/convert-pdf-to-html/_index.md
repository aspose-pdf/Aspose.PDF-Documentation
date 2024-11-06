---
title: Mengonversi PDF ke HTML dalam Python 
linktitle: Mengonversi PDF ke format HTML
type: docs
weight: 50
url: id/python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Topik ini menunjukkan cara mengonversi file PDF ke format HTML dengan pustaka Aspose.PDF untuk Python Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Ikhtisar

Artikel ini menjelaskan cara **mengonversi PDF ke HTML menggunakan Python**. Ini mencakup topik-topik berikut.

_Format_: **HTML**
- [Python PDF ke HTML](#python-pdf-to-html)
- [Python Mengonversi PDF ke HTML](#python-pdf-to-html)
- [Python Cara mengonversi file PDF ke HTML](#python-pdf-to-html)


## Mengonversi PDF ke HTML

**Aspose.PDF untuk Python via .NET** menyediakan banyak fitur untuk mengonversi berbagai format file ke dalam dokumen PDF dan mengonversi file PDF ke berbagai format keluaran.
 Artikel ini membahas cara mengonversi file PDF menjadi <abbr title="HyperText Markup Language">HTML</abbr>. Anda dapat menggunakan beberapa baris kode Python untuk mengonversi PDF ke HTML. Anda mungkin perlu mengonversi PDF ke HTML jika Anda ingin membuat situs web atau menambahkan konten ke forum online. Salah satu cara untuk mengonversi PDF ke HTML adalah dengan menggunakan Python secara programatis.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke HTML secara online**

Aspose.PDF untuk Python menyajikan aplikasi gratis online ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Langkah-langkah: Konversi PDF ke HTML dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/) dengan memanggil metode [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# Buka dokumen PDF
document = Api.Document(documentName)

# simpan dokumen dalam format HTML
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **HTML**
- [Python PDF ke Kode HTML](#python-pdf-to-html)
- [Python PDF ke API HTML](#python-pdf-to-html)
- [Python PDF ke HTML secara Programatik](#python-pdf-to-html)
- [Python PDF ke Perpustakaan HTML](#python-pdf-to-html)
- [Python Simpan PDF sebagai HTML](#python-pdf-to-html)
- [Python Hasilkan HTML dari PDF](#python-pdf-to-html)
- [Python Buat HTML dari PDF](#python-pdf-to-html)

- [Python PDF ke Konverter HTML](#python-pdf-to-html)