---
title: Justify Text in a Textbox Field
type: docs
weight: 20
url: id/net/justify-text-in-a-textbox-field/
description: Artikel ini menunjukkan cara untuk Meratakan Teks dalam Field Kotak Teks menggunakan Form Class.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Dalam artikel ini, kami akan menunjukkan cara untuk meratakan teks dalam field kotak teks dalam file PDF.

{{% /alert %}}

## Rincian implementasi

Kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) dalam [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) menawarkan kemampuan untuk mendekorasi field formulir PDF. Sekarang, jika kebutuhan Anda adalah untuk meratakan teks dalam bidang kotak teks, Anda dapat dengan mudah mencapainya menggunakan nilai [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) dari enumerasi [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) dan memanggil metode [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). Dalam contoh di bawah ini, pertama kita akan mengisi Bidang Kotak Teks menggunakan metode [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) dari kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). Setelah itu kita akan menggunakan kelas FormEditor untuk meratakan teks dalam Bidang Kotak Teks. Cuplikan kode berikut menunjukkan kepada Anda bagaimana meratakan teks dalam Bidang Kotak Teks.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
Silakan perhatikan bahwa perataan rata kanan-kiri tidak didukung oleh PDF, itulah sebabnya teks akan diratakan ke kiri ketika Anda memasukkan teks di Field Kotak Teks. Tetapi ketika field tidak aktif, teks diratakan rata kanan-kiri.