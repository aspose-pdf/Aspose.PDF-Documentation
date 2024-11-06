---
title: Menambahkan watermark multi baris
type: docs
weight: 10
url: id/net/adding-multi-line-watermark-to-existing-pdf/
description: Bagian ini menjelaskan cara menambahkan watermark multi baris ke PDF yang sudah ada menggunakan Kelas FormattedText.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Banyak pengguna ingin memberi stempel pada dokumen PDF mereka dengan teks multi-baris. Mereka biasanya mencoba menggunakan `\n` dan `<br>` tetapi jenis karakter ini tidak didukung oleh namespace Aspose.Pdf.Facades. Jadi, untuk memungkinkannya, kami telah menambahkan metode lain bernama [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) dalam kelas [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) dari namespace Aspose.Pdf.Facades.

{{% /alert %}}

## Implementasi

Silakan merujuk ke potongan kode berikut untuk menambahkan watermark multi-baris dalam PDF yang sudah ada.

```csharp

// Memulai objek stamp
Stamp logoStamp = new Stamp();

// Memulai objek dari kelas FormattedText
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// Menambahkan baris lain untuk Stamp
formatText.AddNewLineText("Good Luck");
// BindLogo ke PDF
logoStamp.BindLogo(formatText);
```