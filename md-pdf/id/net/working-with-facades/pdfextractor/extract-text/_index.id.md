---
title: Extract Text from PDF File
type: docs
weight: 30
url: /net/extract-text/
description: Bagian ini menjelaskan cara mengekstrak teks dari pdf menggunakan kelas PdfExtractor.
lastmod: "2021-06-05"
---

Dalam artikel ini, kita akan melihat detail tentang cara mengekstrak teks dari file PDF. Semua fitur ekstraksi ini disediakan di satu tempat, dalam kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Kita akan melihat bagaimana menggunakan fitur-fitur ini dalam kode kita.

Kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) menyediakan tiga jenis kemampuan ekstraksi. Ketiga kategori ini adalah Teks, Gambar, dan Lampiran. Untuk melakukan ekstraksi di bawah masing-masing dari ketiga kategori ini, PdfExtractor menyediakan berbagai metode yang bekerja sama untuk memberikan output akhir kepada Anda.

Sebagai contoh, untuk mengekstrak teks Anda dapat menggunakan tiga metode yaitu. 
[ExtractText, GetText, HasNextPageText dan GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index).
``` Sekarang, untuk mulai mengekstrak teks, pertama-tama Anda perlu memanggil metode [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); ini akan mengekstrak teks dari file PDF dan akan menyimpannya ke dalam memori. Setelah itu, metode [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) akan mengambil teks yang diekstrak ini dan menyimpannya ke disk di lokasi yang ditentukan dalam sebuah file. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) membantu Anda melakukan iterasi melalui setiap halaman dan memeriksa apakah halaman berikutnya memiliki teks atau tidak. Jika berisi beberapa teks maka [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) akan membantu Anda menyimpan teks dari halaman individu ke dalam file.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Membuat objek dari kelas PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Mengikat PDF input
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtractText
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Mengekstrak teks ke dalam file terpisah
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
Untuk Mengekstrak Mode Ekstraksi Teks gunakan kode berikut:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // Buat objek dari kelas PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Mengikat PDF input
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // EkstraksiTeks
    // pdfExtractor.ExtractTextMode = 0; //mode murni
    pdfExtractor.ExtractTextMode = 1; //mode mentah
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Mengekstrak teks ke dalam file terpisah
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```