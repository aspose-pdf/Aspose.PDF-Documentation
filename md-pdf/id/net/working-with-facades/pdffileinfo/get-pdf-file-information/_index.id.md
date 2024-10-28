---
title: Dapatkan informasi file PDF
type: docs
weight: 50
url: /net/get-pdf-file-information/
description: Bagian ini menjelaskan cara mendapatkan Informasi File PDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Untuk mendapatkan informasi spesifik file dari file PDF, Anda perlu membuat objek dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Setelah itu, Anda dapat mendapatkan nilai dari properti individu seperti Subjek, Judul, Kata Kunci, dan Pembuat dll.

Cuplikan kode berikut menunjukkan kepada Anda cara mendapatkan informasi file PDF.

```csharp
 public static void GetPdfInfo()
        {
            // Buka dokumen
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // Dapatkan informasi PDF
            Console.WriteLine("Subjek: {0}", fileInfo.Subject);
            Console.WriteLine("Judul: {0}", fileInfo.Title);
            Console.WriteLine("Kata Kunci: {0}", fileInfo.Keywords);
            Console.WriteLine("Pembuat: {0}", fileInfo.Creator);
            Console.WriteLine("Tanggal Pembuatan: {0}", fileInfo.CreationDate);
            Console.WriteLine("Tanggal Modifikasi: {0}", fileInfo.ModDate);
            // Temukan apakah ini PDF yang valid dan juga terenkripsi
            Console.WriteLine("Apakah PDF Valid: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Apakah Terenkripsi: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Lebar halaman:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Tinggi halaman:{0}", fileInfo.GetPageHeight(1));
        }
```

## Dapatkan Info Meta

Untuk mendapatkan informasi, kami menggunakan properti [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). Dengan 'Hashtable' kita mendapatkan semua nilai yang mungkin.

```csharp
public static void GetMetaInfo()
        {
            // Buat instance objek PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // Mengambil semua atribut kustom yang ada
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // Mengambil satu atribut kustom
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```