---
title: Mengatur Informasi File PDF
type: docs
weight: 40
url: /id/net/set-pdf-file-information/
description: Bagian ini menjelaskan cara mengatur Informasi File PDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Kelas [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) memungkinkan Anda untuk mengatur informasi spesifik file dari sebuah file PDF. Anda perlu membuat objek dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) dan kemudian mengatur berbagai properti spesifik file seperti Author, Title, Keyword, dan Creator dll. Akhirnya, simpan file PDF yang telah diperbarui menggunakan metode [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) dari objek [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengatur informasi file PDF.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Set PDF information
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Save updated file
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## Set Meta Info

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) metode memungkinkan Anda untuk menambahkan informasi apapun. Dalam contoh kami, kami menambahkan sebuah field. Periksa potongan kode berikut:

```csharp
 public static void SetMetaInfo()
        {
            // Buat instance objek PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // Tetapkan atribut pelanggan baru sebagai meta info
            fInfo.SetMetaInfo("Reviewer", "Pengguna Aspose.PDF");

            // Simpan file yang diperbarui
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```