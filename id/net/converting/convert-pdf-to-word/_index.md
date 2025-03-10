---
title: Mengonversi PDF ke Dokumen Microsoft Word di .NET
linktitle: Mengonversi PDF ke Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Pelajari cara menulis kode C# untuk konversi format PDF ke Microsoft Word dengan Aspose.PDF for .NET. dan menyesuaikan konversi PDF ke DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur yang kuat untuk mengonversi file PDF ke format Microsoft Word (DOC dan DOCX) menggunakan C#. Fungsionalitas ini tidak hanya meningkatkan pengeditan dokumen tetapi juga menyediakan opsi fleksibel untuk pengenalan teks dan pemformatan, memastikan kesetiaan tinggi antara PDF sumber dan dokumen Word yang dihasilkan.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1495",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF tidak hanya dapat melakukan tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ikhtisar

Artikel ini menjelaskan cara **mengonversi PDF ke Dokumen Microsoft Word menggunakan C#**. Ini mencakup topik-topik berikut.

_Format_: **DOC**

- [C# PDF ke DOC](#csharp-pdf-to-doc)
- [C# Mengonversi PDF ke DOC](#csharp-pdf-to-doc)
- [C# Cara mengonversi file PDF ke DOC](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# PDF ke DOCX](#csharp-pdf-to-docx)
- [C# Mengonversi PDF ke DOCX](#csharp-pdf-to-docx)
- [C# Cara mengonversi file PDF ke DOCX](#csharp-pdf-to-docx)

_Format_: **Word**

- [C# PDF ke Word](#csharp-pdf-to-docx)
- [C# Mengonversi PDF ke Word](#csharp-pdf-to-doc)
- [C# Cara mengonversi file PDF ke Word](#csharp-pdf-to-docx)

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Konversi PDF ke DOC dan DOCX

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang membuat manajemen konten menjadi lebih mudah. **Aspose.PDF for .NET** memungkinkan Anda untuk mengonversi file PDF ke format DOC dan DOCX dengan cepat dan efisien.

## Mengonversi PDF ke file DOC (Microsoft Word 97-2003)

Mengonversi file PDF ke format DOC dengan mudah dan kontrol penuh. Aspose.PDF for .NET fleksibel dan mendukung berbagai konversi. Mengonversi halaman dari dokumen PDF ke gambar, misalnya, adalah fitur yang sangat populer.

Banyak pelanggan kami telah meminta konversi dari PDF ke DOC: mengonversi file PDF ke dokumen Microsoft Word. Pelanggan menginginkan ini karena file PDF tidak dapat diedit dengan mudah, sedangkan dokumen Word dapat. Beberapa perusahaan ingin pengguna mereka dapat memanipulasi teks, tabel, dan gambar dalam file yang berasal dari PDF.

Dengan mempertahankan tradisi membuat hal-hal sederhana dan dapat dipahami, Aspose.PDF for .NET memungkinkan Anda untuk mengubah file PDF sumber menjadi file DOC dengan dua baris kode. Untuk mencapai fitur ini, kami telah memperkenalkan enumerasi bernama SaveFormat dan nilainya .Doc memungkinkan Anda menyimpan file sumber ke format Microsoft Word.

Potongan kode C# berikut menunjukkan cara mengonversi file PDF menjadi format DOC.

<a name="csharp-pdf-to-doc"><strong>Langkah: Mengonversi PDF ke DOC di C#</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat.Doc** dengan memanggil metode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### Menggunakan Kelas DocSaveOptions

Kelas [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) menyediakan banyak properti yang meningkatkan konversi file PDF ke format DOC. Di antara properti ini, Mode memungkinkan Anda untuk menentukan mode pengenalan untuk konten PDF. Anda dapat memilih nilai apa pun dari enumerasi RecognitionMode untuk properti ini. Setiap nilai ini memiliki manfaat dan batasan tertentu:

- Mode [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) cepat dan baik untuk mempertahankan tampilan asli file PDF, tetapi kemampuan edit dokumen yang dihasilkan bisa terbatas. Setiap blok teks yang dikelompokkan secara visual dalam PDF asli diubah menjadi kotak teks dalam dokumen keluaran. Ini mencapai kemiripan maksimal dengan yang asli, sehingga dokumen keluaran terlihat baik, tetapi sepenuhnya terdiri dari kotak teks, yang dapat diedit di Microsoft Word, yang cukup menantang.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) adalah mode pengenalan penuh, di mana mesin melakukan pengelompokan dan analisis multi-level untuk mengembalikan dokumen asli sesuai dengan niat penulis sambil menghasilkan dokumen yang mudah diedit. Batasannya adalah dokumen keluaran mungkin terlihat berbeda dari yang asli.

Properti [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) dapat digunakan untuk mengontrol kedekatan relatif antara elemen teks. Ini berarti bahwa jarak dinormalkan berdasarkan ukuran font. Font yang lebih besar mungkin memiliki ruang yang lebih besar antara suku kata dan masih dianggap sebagai satu kesatuan. Ini ditentukan sebagai persentase dari ukuran font; misalnya, 1 = 100%. Ini berarti bahwa dua karakter 12pt yang ditempatkan 12 pt terpisah adalah proximal.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) digunakan untuk mengaktifkan pengenalan bullet selama konversi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke DOC secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF ke DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Mengonversi PDF ke DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Mengonversi PDF ke file DOCX (Microsoft Word 2007-2024)

API Aspose.PDF for .NET memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX menggunakan C# dan bahasa .NET lainnya. DOCX adalah format yang dikenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner biasa menjadi kombinasi file XML dan biner. File Docx dapat dibuka dengan Word 2007 dan versi yang lebih baru tetapi tidak dengan versi MS Word yang lebih lama, yang mendukung ekstensi file DOC.

Potongan kode C# berikut menunjukkan cara mengonversi file PDF menjadi format DOCX.

<a name="csharp-pdf-to-docx"><strong>Langkah: Mengonversi PDF ke DOCX di C#</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat.DocX** dengan memanggil metode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### Mengonversi PDF ke DOCX dalam Mode Ditingkatkan

Untuk mendapatkan hasil yang lebih baik dari konversi PDF ke DOCX, Anda dapat menggunakan mode `EnhancedFlow`.
Perbedaan utama antara Flow dan Enhanced Flow adalah bahwa tabel (baik dengan maupun tanpa batas) dikenali sebagai tabel nyata, bukan sebagai teks dengan gambar di latar belakang.
Ada juga pengenalan daftar bernomor dan banyak hal kecil lainnya.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**Cobalah untuk mengonversi PDF ke DOCX secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aplikasi Gratis Konversi PDF ke Word Aspose.PDF](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Lihat Juga

Artikel ini juga mencakup topik-topik berikut. Kode-kode sama seperti di atas.

_Format_: **Word**

- [C# Kode PDF ke Word](#csharp-pdf-to-docx)
- [C# API PDF ke Word](#csharp-pdf-to-docx)
- [C# PDF ke Word Secara Programatik](#csharp-pdf-to-docx)
- [C# Perpustakaan PDF ke Word](#csharp-pdf-to-docx)
- [C# Simpan PDF sebagai Word](#csharp-pdf-to-docx)
- [C# Hasilkan Word dari PDF](#csharp-pdf-to-docx)
- [C# Buat Word dari PDF](#csharp-pdf-to-docx)
- [C# Konverter PDF ke Word](#csharp-pdf-to-docx)

_Format_: **DOC**

- [C# Kode PDF ke DOC](#csharp-pdf-to-doc)
- [C# API PDF ke DOC](#csharp-pdf-to-doc)
- [C# PDF ke DOC Secara Programatik](#csharp-pdf-to-doc)
- [C# Perpustakaan PDF ke DOC](#csharp-pdf-to-doc)
- [C# Simpan PDF sebagai DOC](#csharp-pdf-to-doc)
- [C# Hasilkan DOC dari PDF](#csharp-pdf-to-doc)
- [C# Buat DOC dari PDF](#csharp-pdf-to-doc)
- [C# Konverter PDF ke DOC](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# Kode PDF ke DOCX](#csharp-pdf-to-docx)
- [C# API PDF ke DOCX](#csharp-pdf-to-docx)
- [C# PDF ke DOCX Secara Programatik](#csharp-pdf-to-docx)
- [C# Perpustakaan PDF ke DOCX](#csharp-pdf-to-docx)
- [C# Simpan PDF sebagai DOCX](#csharp-pdf-to-docx)
- [C# Hasilkan DOCX dari PDF](#csharp-pdf-to-docx)
- [C# Buat DOCX dari PDF](#csharp-pdf-to-docx)
- [C# Konverter PDF ke DOCX](#csharp-pdf-to-docx)