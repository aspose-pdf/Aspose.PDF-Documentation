---
title: Mengonversi XML ke format FDF
type: docs
weight: 20
url: /id/net/converting-an-xml-to-fdf-format/
description: Bagian ini menjelaskan bagaimana Anda dapat mengonversi XML ke format FDF dengan FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dalam [Aspose.PDF for .NET](/pdf/id/net/) mendukung AcroForms dengan sangat baik. Ini juga mendukung pengimporan dan pengeksporan data formulir ke berbagai format file seperti FDF, XFDF, dan XML. Namun, kadang-kadang seorang pengembang perlu mengonversi satu format ke format lain. Dalam artikel ini, kita akan melihat fitur yang memungkinkan kita mengonversi format FDF menjadi XML.

{{% /alert %}}

## Rincian

FDF adalah singkatan dari Forms Data Format, dan file FDF berisi nilai-nilai formulir dalam pasangan kunci/nilai. Kami juga tahu bahwa file XML mengandung nilai-nilai sebagai tag. Di mana, sebagian besar kunci diwakili sebagai nama tag dan nilai diwakili sebagai nilai di dalam tag tersebut. Sekarang, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) menyediakan fleksibilitas untuk mengonversi format file XML ke format FDF.

Gunakan kelas [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) untuk tujuan ini. Kelas ini menyediakan berbagai metode untuk mengonversi satu format data ke format lainnya. Artikel ini menunjukkan cara menggunakan satu metode, ConvertXmlToFdf(..), yang mengambil file FDF sebagai input atau aliran sumber dan menyimpannya ke dalam format XML. Cuplikan kode berikut menunjukkan cara mengonversi file FDF ke file XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-XMLToPdf-XMLToPdf.cs" >}}