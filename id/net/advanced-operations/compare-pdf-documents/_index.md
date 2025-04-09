---
title: Bandingkan dokumen PDF
linktitle: Bandingkan PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /id/net/compare-pdf-documents/
description: Sejak rilis 24.7, kini dimungkinkan untuk membandingkan konten dokumen PDF dengan tanda anotasi dan output berdampingan
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "Fitur perbandingan PDF baru di Aspose.PDF for .NET memungkinkan pengguna untuk dengan efisien mengidentifikasi perbedaan antara dua dokumen PDF, baik berdasarkan halaman tertentu atau seluruh konten. Dengan output berdampingan dan opsi yang dapat disesuaikan seperti penanda perubahan tambahan dan berbagai mode perbandingan, alat yang kuat ini meningkatkan kolaborasi dengan membuat revisi mudah dilacak dan ditinjau",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1165",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Harap dicatat bahwa semua alat perbandingan tersedia di [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/) library.

## Cara membandingkan Dokumen PDF

Saat bekerja dengan dokumen PDF, terkadang Anda perlu membandingkan konten dari dua dokumen untuk mengidentifikasi perbedaan. Library Aspose.PDF for .NET menyediakan seperangkat alat yang kuat untuk tujuan ini. Dalam artikel ini, kita akan menjelajahi cara membandingkan dokumen PDF menggunakan beberapa potongan kode sederhana.

Fungsi perbandingan di Aspose.PDF memungkinkan Anda untuk membandingkan dua dokumen PDF halaman demi halaman. Anda dapat memilih untuk membandingkan halaman tertentu atau seluruh dokumen. Dokumen perbandingan yang dihasilkan menyoroti perbedaan, sehingga lebih mudah untuk mengidentifikasi perubahan antara kedua file.

Berikut adalah daftar cara yang mungkin untuk membandingkan dokumen PDF menggunakan Aspose.PDF untuk .NET library:

1. **Membandingkan Halaman Tertentu** - Bandingkan halaman pertama dari dua dokumen PDF.

1. **Membandingkan Seluruh Dokumen** - Bandingkan seluruh konten dari dua dokumen PDF.

1. **Bandingkan dokumen PDF secara grafis**:

- Bandingkan PDF dengan metode GetDifference - gambar individu di mana perubahan ditandai.

- Bandingkan PDF dengan metode CompareDocumentsToPdf - dokumen PDF dengan gambar di mana perubahan ditandai.

## Membandingkan Halaman Tertentu

Potongan kode pertama menunjukkan cara membandingkan halaman pertama dari dua dokumen PDF.

1. Inisialisasi Dokumen.
Kode dimulai dengan menginisialisasi dua dokumen PDF menggunakan jalur file masing-masing (documentPath1 dan documentPath2). Jalur tersebut ditentukan sebagai string kosong untuk saat ini, tetapi dalam praktiknya, Anda akan menggantinya dengan jalur file yang sebenarnya.

2. Proses Perbandingan.

- Pemilihan Halaman - perbandingan dibatasi pada halaman pertama dari setiap dokumen ('Pages[1]').
- Opsi Perbandingan:

'AdditionalChangeMarks = true' - opsi ini memastikan bahwa penanda perubahan tambahan ditampilkan. Penanda ini menyoroti perbedaan yang mungkin ada di halaman lain, bahkan jika mereka tidak ada di halaman saat ini yang dibandingkan.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - mode ini memberi tahu pembanding untuk mengabaikan spasi dalam teks, hanya fokus pada perubahan dalam kata.

3. Dokumen perbandingan yang dihasilkan, yang menyoroti perbedaan antara kedua halaman, disimpan ke jalur file yang ditentukan dalam 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## Membandingkan Seluruh Dokumen

Potongan kode kedua memperluas cakupan untuk membandingkan seluruh konten dari dua dokumen PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Hasil perbandingan yang dihasilkan oleh potongan kode ini adalah dokumen PDF yang dapat Anda buka di penampil seperti Adobe Acrobat. Jika Anda menggunakan tampilan Dua halaman di Adobe Acrobat, Anda akan melihat perubahan berdampingan:

- Penghapusan - ini dicatat di halaman kiri.
- Penyisipan - ini dicatat di halaman kanan.

Dengan mengatur 'AdditionalChangeMarks' ke 'true', Anda juga dapat melihat penanda untuk perubahan yang mungkin terjadi di halaman lain, bahkan jika perubahan tersebut tidak ada di halaman saat ini yang sedang dilihat.

**Aspose.PDF for .NET** menyediakan alat yang kuat untuk membandingkan dokumen PDF, baik Anda perlu membandingkan halaman tertentu atau seluruh dokumen. Dengan menggunakan opsi seperti 'AdditionalChangeMarks' dan pengaturan 'ComparisonMode' yang berbeda, Anda dapat menyesuaikan proses perbandingan sesuai dengan kebutuhan spesifik Anda. Dokumen yang dihasilkan memberikan tampilan yang jelas, berdampingan dari perubahan, sehingga lebih mudah untuk melacak revisi dan memastikan akurasi dokumen.

## Bandingkan dokumen PDF menggunakan GraphicalPdfComparer

Saat berkolaborasi pada dokumen, terutama di lingkungan profesional, Anda sering kali berakhir dengan beberapa versi dari file yang sama.

Anda dapat menggunakan kelas [GraphicalPdfComparer](https://reference.aspose.com/pdf/id/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) untuk membandingkan dokumen dan halaman PDF. Kelas ini cocok untuk membandingkan perubahan dalam konten grafis halaman.

Dengan Aspose.PDF for .NET, dimungkinkan untuk membandingkan dokumen dan halaman serta mengeluarkan hasil perbandingan ke dokumen PDF atau file gambar.

Anda dapat mengatur properti kelas berikut:

- Resolusi - resolusi dalam satuan DPI untuk gambar output, serta untuk gambar yang dihasilkan selama perbandingan.
- Warna - warna penanda perubahan.
- Ambang - ambang perubahan dalam persen. Nilai default adalah nol. Mengatur nilai selain nol memungkinkan Anda untuk mengabaikan perubahan grafis yang tidak signifikan bagi Anda.

Kelas ini memiliki metode yang memungkinkan Anda untuk mendapatkan perbedaan gambar halaman dalam bentuk yang cocok untuk pemrosesan lebih lanjut: **ImagesDifference GetDifference(Page page1, Page page2)**.

Metode ini mengembalikan objek dari kelas [ImagesDifference](https://reference.aspose.com/pdf/id/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) yang berisi gambar dari halaman pertama yang dibandingkan dan array perbedaan. Array perbedaan dan gambar asli memiliki format piksel **RGB24bpp**.

ImagesDifference memungkinkan Anda untuk menghasilkan gambar yang berbeda dan mendapatkan gambar dari halaman kedua yang dibandingkan dengan menambahkan array perbedaan ke gambar asli. Untuk melakukan ini, gunakan metode **ImagesDifference.GetDestinationImage dan ImagesDifference.DifferenceToImage**.

### Bandingkan PDF dengan metode GetDifference

Kode yang disediakan mendefinisikan metode [GetDifference](https://reference.aspose.com/pdf/id/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) yang membandingkan dua dokumen PDF dan menghasilkan representasi visual dari perbedaan antara keduanya.

Metode ini membandingkan halaman pertama dari dua file PDF dan menghasilkan dua gambar PNG:

- Satu gambar (diffPngFilePath) menyoroti perbedaan antara halaman dalam warna merah.
- Gambar lainnya (destPngFilePath) adalah representasi visual dari halaman PDF tujuan (kedua).

Proses ini dapat berguna untuk membandingkan secara visual perubahan atau perbedaan antara dua versi dokumen.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### Bandingkan PDF dengan metode CompareDocumentsToPdf

Potongan kode yang disediakan menggunakan metode [CompareDocumentsToPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) yang membandingkan dua dokumen dan menghasilkan laporan PDF dari hasil perbandingan.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```