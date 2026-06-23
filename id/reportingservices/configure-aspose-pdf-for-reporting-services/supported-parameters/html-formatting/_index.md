---
title: Pemformatan HTML
linktitle: Pemformatan HTML
type: docs
weight: 20
url: /id/reportingservices/html-formatting/
description: Aktifkan pemformatan HTML dalam laporan PDF menggunakan Aspose.PDF for Reporting Services. Tambahkan gaya dan struktur dengan mudah.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Kadang-kadang Anda mungkin ingin mengekspor teks dalam kotak teks dengan pemformatan. Sayangnya, Reporting Services tidak mendukung hal ini. Namun, Anda masih dapat melakukannya menggunakan Aspose.PDF for Reporting Services. Cukup aktifkan mode khusus di mana semua teks dalam kotak teks diperlakukan sebagai HTML dan masukkan tag HTML yang diperlukan untuk memformat teks dalam dokumen keluaran. Misalnya, untuk memiliki teks normal, tebal, dan miring dalam kotak teks yang sama, masukkan nilai kotak teks berikut:

Sebagian teks ini adalah ```<b>bold</b>``` dan teks lainnya adalah ```<i>italic</i>```.

Saat diekspor, teks akan terlihat seperti sebagian dari teks ini **bold** dan teks lainnya *italic*.

Harap perhatikan bahwa pendekatan ini memiliki beberapa keterbatasan

{{% /alert %}}

{{% alert color="primary" %}}

- Pemformatan tidak terlihat pada waktu desain (di Report Builder, portal web Reporting Services, dll.). Sebaliknya, Anda akan melihat teks HTML dalam bentuk teks biasa dengan tag.
- Ekstensi render Aspose.PDF untuk Reporting Services mengenali dan memformat kode HTML dengan benar di kotak teks. Renderer PDF default dari Reporting Services akan mengekspor markup ini sebagai teks biasa.

**Nama Parameter**: IsHtmlTagSupported  
**Tipe Data**: Boolean  
**Nilai yang didukung**: True, False (default)   

**Contoh**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Jika Anda ingin menambahkan parameter ini di Report Designer, gunakan tipe data 'Boolean'.

 
Saat ini Aspose.Pdf for Reporting Services mendukung sebagian subset dari semua tag HTML. Anda dapat menemukan informasi lebih lanjut di Aspose.PDF [Dokumentasi](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

