---
title: Ekstrak Halaman PDF
type: docs
weight: 40
url: /net/extract-pdf-pages/
description: Bagian ini menjelaskan cara mengekstrak halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Ekstrak Halaman PDF antara Dua Angka Menggunakan Jalur File

Metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk mengekstrak rentang halaman tertentu dari file PDF. Overload ini memungkinkan Anda untuk mengekstrak halaman sambil memanipulasi file PDF dari disk. Overload ini memerlukan parameter berikut: jalur file input, halaman awal, halaman akhir, dan jalur file output. Halaman dari halaman awal hingga halaman akhir akan diekstrak dan output akan disimpan di disk. Cuplikan kode berikut menunjukkan cara mengekstrak halaman PDF antara dua angka menggunakan jalur file.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // Buat objek PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Ekstrak halaman
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Ekstrak Array dari Halaman PDF Menggunakan Jalur File

Jika Anda tidak ingin mengekstrak rentang halaman, melainkan satu set halaman tertentu, metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) memungkinkan Anda untuk melakukannya juga. Anda pertama-tama perlu membuat array integer dengan semua nomor halaman yang perlu diekstrak. Overload metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) ini mengambil parameter berikut: file PDF input, array integer dari halaman yang akan diekstrak, dan file PDF output. Cuplikan kode berikut menunjukkan cara mengekstrak halaman PDF menggunakan jalur file.

```csharp
public static void Extract_PDFPages_Streams()
{
    // Buat objek PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Buat stream
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // Ekstrak halaman
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## Ekstrak Halaman PDF antara Dua Angka Menggunakan Streams

Metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda mengekstrak rentang halaman menggunakan streams. Anda perlu memberikan parameter berikut ke overload ini: input stream, halaman awal, halaman akhir, dan output stream. Halaman yang ditentukan oleh rentang antara halaman awal dan halaman akhir akan diekstrak dari input stream dan disimpan ke output stream. Cuplikan kode berikut menunjukkan cara mengekstrak halaman PDF antara dua angka menggunakan streams.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // Buat objek PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Ekstrak halaman
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Ekstrak Array Halaman PDF Menggunakan Streams

Sebuah array dari halaman dapat diekstrak dari aliran PDF dan disimpan dalam aliran keluaran menggunakan overload yang sesuai dari metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Jika Anda tidak ingin mengekstrak rentang halaman, melainkan satu set halaman tertentu, metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) memungkinkan Anda untuk melakukan itu juga. Anda pertama-tama perlu membuat array integer dengan semua nomor halaman yang perlu diekstrak. Overload dari metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) ini mengambil parameter berikut: aliran input, array integer dari halaman yang akan diekstrak dan aliran keluaran. 
Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengekstrak halaman PDF menggunakan aliran.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // Buat objek PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Buat aliran
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // Ekstrak halaman
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```