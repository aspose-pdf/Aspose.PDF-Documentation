---
title: HTML Formatting
type: docs
weight: 20
url: /id/reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Kadang-kadang Anda mungkin ingin mengekspor teks dalam kotak teks dengan pemformatan. Sayangnya, Reporting Services tidak mendukung ini. Namun, Anda masih bisa menerapkannya menggunakan Aspose.PDF untuk Reporting Services. Cukup aktifkan mode khusus di mana semua teks dalam kotak teks diperlakukan sebagai HTML dan masukkan tag HTML yang diperlukan untuk memformat teks dalam dokumen keluaran. Misalnya, untuk memiliki teks normal, tebal, dan miring dalam kotak teks yang sama, masukkan nilai kotak teks berikut:

Beberapa dari teks ini adalah ```<b>tebal</b>``` dan teks lainnya adalah ```<i>miring</i>```.

Ketika diekspor, teks akan terlihat seperti beberapa dari teks ini adalah **tebal** dan teks lainnya adalah *miring*.

Harap diperhatikan bahwa pendekatan ini memiliki beberapa keterbatasan

{{% /alert %}}

{{% alert color="primary" %}}

- Pemformatan tidak terlihat pada saat desain (di Report Builder, portal web Reporting Services, dll.). Instead, you will see the HTML text in form of plain text with tags.  
- Aspose.PDF untuk Reporting Services rendering extension mengenali dan memformat kode HTML dengan benar dalam kotak teks. Renderer PDF default dari Reporting Services akan mengekspor markup ini sebagai teks biasa.

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

Saat ini Aspose.Pdf untuk Reporting Services mendukung sebagian dari semua tag HTML. Anda dapat menemukan informasi lebih lanjut di [Dokumentasi](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}