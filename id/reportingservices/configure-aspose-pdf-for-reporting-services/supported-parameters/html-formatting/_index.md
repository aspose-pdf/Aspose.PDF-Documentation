---
title: Pemformatan HTML
linktitle: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Aktifkan pemformatan HTML dalam laporan PDF menggunakan Aspose.PDF untuk Layanan Pelaporan. Tambahkan gaya dan struktur dengan mudah.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Terkadang Anda mungkin ingin mengekspor teks dalam kotak teks dengan pemformatan. Sayangnya, Layanan Pelaporan tidak mendukung hal ini. Namun, Anda masih bisa menerapkannya menggunakan Aspose.PDF untuk Layanan Pelaporan. Cukup aktifkan mode khusus di mana semua teks di kotak teks diperlakukan sebagai HTML dan masukkan tag HTML yang diperlukan untuk memformat teks dalam dokumen keluaran. Misalnya, untuk memiliki teks normal, tebal, dan miring dalam kotak teks yang sama, masukkan nilai kotak teks berikut:

Beberapa teks ini adalah `<b>bold</b>` dan teks lainnya adalah `<i>italic</i>`.

Saat diekspor, teks akan terlihat seperti beberapa teks ini **tebal** dan teks lainnya *miring*.

Harap dicatat bahwa pendekatan ini memiliki beberapa keterbatasan

{{% /alert %}}

{{% alert color="primary" %}}

- Pemformatan tidak terlihat pada waktu desain (di Pembuat Laporan, portal web Layanan Pelaporan, dll.). Sebaliknya, Anda akan melihat teks HTML dalam bentuk teks biasa dengan tag.
- Ekstensi rendering Aspose.PDF untuk Layanan Pelaporan mengenali dan memformat kode HTML dengan benar di kotak teks. Perender PDF default Layanan Pelaporan akan mengekspor markup ini sebagai teks biasa.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## Contoh

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

Jika Anda ingin menambahkan parameter ini di Perancang Laporan, gunakan tipe data `Boolean`.

Saat ini Aspose.Pdf untuk Layanan Pelaporan mendukung subset dari semua tag HTML. Anda dapat menemukan informasi lebih lanjut di Aspose.PDF [Dokumentasi](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}
