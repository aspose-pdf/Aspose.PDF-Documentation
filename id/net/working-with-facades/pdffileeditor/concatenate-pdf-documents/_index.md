---
title: Menggabungkan dokumen PDF di C#
linktitle: Menggabungkan dokumen PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/concatenate-pdf-documents/
description: Bagian ini menjelaskan cara menggabungkan dokumen PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "Fungsi dalam Aspose.PDF for .NET memungkinkan pengembang untuk menggabungkan beberapa dokumen PDF secara efisien menggunakan kelas PdfFileEditor di C#. Fitur ini mendukung penggabungan file melalui jalur file dan MemoryStreams, membuat nama field yang unik dalam formulir PDF, dan bahkan menghasilkan Daftar Isi dalam dokumen akhir, memberikan solusi yang efisien untuk manajemen dan integrasi dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
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
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## **Ikhtisar**

Artikel ini menjelaskan cara menggabungkan, mengkombinasikan, atau menggabungkan berbagai file PDF menjadi satu PDF menggunakan C#. Ini mencakup topik seperti

- [C# Menggabungkan File PDF](#concatenate-pdf-files-using-file-paths)
- [C# Menggabungkan File PDF](#concatenate-pdf-files-using-file-paths)
- [C# Menggabungkan Beberapa file PDF menjadi satu PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Menggabungkan Beberapa file PDF menjadi satu PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Menggabungkan semua file PDF dalam folder](#concatenating-all-pdf-files-in-particular-folder)
- [C# Menggabungkan semua file PDF dalam folder](#concatenating-all-pdf-files-in-particular-folder)
- [C# Menggabungkan file PDF menggunakan jalur file](#concatenate-pdf-files-using-file-paths)
- [C# Menggabungkan file PDF menggunakan stream](#concatenate-array-of-pdf-files-using-streams)
- [C# Menggabungkan semua file PDF dalam folder](#concatenate-pdf-files-in-folder)

## Menggabungkan file PDF menggunakan jalur file

[PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) adalah kelas dalam [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) yang memungkinkan Anda untuk menggabungkan beberapa file PDF. Anda tidak hanya dapat menggabungkan file menggunakan FileStreams tetapi juga menggunakan MemoryStreams. Dalam artikel ini, proses penggabungan file menggunakan MemoryStreams akan dijelaskan dan kemudian ditunjukkan menggunakan cuplikan kode.

Metode [Concatenate](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) dapat digunakan untuk menggabungkan dua file PDF. Metode [Concatenate](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) memungkinkan Anda untuk melewatkan tiga parameter: PDF input pertama, PDF input kedua, dan PDF output. PDF output akhir berisi kedua file PDF input.

Cuplikan kode C# berikut menunjukkan cara menggabungkan file PDF menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

Dalam beberapa kasus, ketika ada banyak outline, pengguna dapat menonaktifkannya dengan mengatur CopyOutlines ke false dan meningkatkan kinerja penggabungan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf", dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## Menggabungkan beberapa file PDF menggunakan MemoryStreams

Metode [Concatenate](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) mengambil file PDF sumber dan file PDF tujuan sebagai parameter. Parameter ini bisa berupa jalur ke file PDF di disk atau bisa juga berupa MemoryStreams. Sekarang, untuk contoh ini, kita akan terlebih dahulu membuat dua file stream untuk membaca file PDF dari disk. Kemudian kita akan mengonversi file-file ini menjadi array byte. Array byte dari file PDF ini akan dikonversi menjadi MemoryStreams. Setelah kita mendapatkan MemoryStreams dari file PDF, kita akan dapat meneruskannya ke metode concatenate dan menggabungkannya menjadi satu file output.

Cuplikan kode C# berikut menunjukkan cara menggabungkan beberapa file PDF menggunakan MemoryStreams:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    string document1Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf";
    string document2Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        using (var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write))
                        {
                            // Write byte array contents in the output file stream
                            output.Write(data, 0, data.Length);
                        }
                    }
                }
            }
        }
    }
}
```

## Menggabungkan Array File PDF Menggunakan Jalur File

Jika Anda ingin menggabungkan beberapa file PDF, Anda dapat menggunakan overload dari metode [Concatenate](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) yang memungkinkan Anda untuk melewatkan array file PDF. Output akhir disimpan sebagai file gabungan yang dibuat dari semua file dalam array. Cuplikan kode C# berikut menunjukkan cara menggabungkan array file PDF menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "Concatenate1.pdf";
    filesArray[1] = dataDir + "Concatenate2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## Menggabungkan Array File PDF Menggunakan Stream

Menggabungkan array file PDF tidak terbatas hanya pada file yang berada di disk. Anda juga dapat menggabungkan array file PDF dari stream. Jika Anda ingin menggabungkan beberapa file PDF, Anda dapat menggunakan overload yang sesuai dari metode [Concatenate](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Pertama, Anda perlu membuat array stream input dan satu stream untuk PDF output dan kemudian memanggil metode [Concatenate](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Output akan disimpan dalam stream output. Cuplikan kode C# berikut menunjukkan cara menggabungkan array file PDF menggunakan stream.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    var document1Path = dataDir + "Concatenate1.pdf";
    var document2Path = dataDir + "Concatenate2.pdf";
    var resultPdfPath = dataDir + "ConcatenateArrayOfPdfUsingStreams_out.pdf";

    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Output stream
    using (var outputStream = new FileStream(resultPdfPath, FileMode.Create))
    {
        using (var stream1 = new FileStream(document1Path, FileMode.Open))
        {
            using (var stream2 = new FileStream(document2Path, FileMode.Open))
            {
                // Array of streams
                var inputStreams = new Stream[2];
                inputStreams[0] = stream1;
                inputStreams[1] = stream2;
                // Concatenate file
                pdfEditor.Concatenate(inputStreams, outputStream);
            }   
        }
    }
}
```

## Menggabungkan semua file PDF dalam folder tertentu

Anda bahkan dapat membaca semua file PDF dalam folder tertentu saat runtime dan menggabungkannya, tanpa bahkan mengetahui nama file. Cukup berikan jalur direktori yang berisi dokumen PDF yang ingin Anda gabungkan.

Silakan coba menggunakan cuplikan kode C# berikut untuk mencapai fungsionalitas ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatingAllPdfFilesInParticularFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    var fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    var resultPdfPath = dataDir + "ConcatenatingAllPdfFilesInParticularFolder_out.pdf";
    // Instantiate PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, resultPdfPath);
}
```

## Menggabungkan Formulir PDF dan menjaga nama field tetap unik

Kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) dalam [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) menawarkan kemampuan untuk menggabungkan file PDF. Sekarang, jika file PDF yang akan digabungkan memiliki field formulir dengan nama field yang sama, Aspose.PDF menyediakan fitur untuk menjaga field dalam file PDF hasil sebagai unik dan Anda juga dapat menentukan sufiks untuk membuat nama field unik. Properti [KeepFieldsUnique](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) dari [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) sebagai true akan membuat nama field unik ketika formulir PDF digabungkan. Juga, properti [UniqueSuffix](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) dari PdfFileEditor dapat digunakan untuk menentukan format sufiks yang ditentukan pengguna yang ditambahkan ke nama field untuk membuatnya unik ketika formulir digabungkan. String ini harus mengandung substring `%NUM%` yang akan diganti dengan angka dalam file hasil.

Silakan lihat cuplikan kode sederhana berikut untuk mencapai fungsionalitas ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFormsAndKeepFieldsUnique()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf";
    var inputFile2 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf";
    var outFile = dataDir + "ConcatenatePDFForms_out.pdf";
    // Open PDF documents
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // To keep unique field Id for all the fields 
    fileEditor.KeepFieldsUnique = true;
    // Format of the suffix which is added to field name to make it unique when forms are concatenated.
    fileEditor.UniqueSuffix = "_%NUM%";
    // Concatenate the files into a resultant Pdf file
    fileEditor.Concatenate(inputFile1, inputFile2, outFile);
}
```

## Menggabungkan file PDF dan membuat Daftar Isi

## Menggabungkan file PDF

Silakan lihat cuplikan kode berikut untuk informasi tentang cara menggabungkan file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenateInput1.pdf";
    var inputFile2 = dataDir + "ConcatenateInput2.pdf";
    var outFile = dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf";
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    // Open PDF documents
    using (var outputStream = new FileStream(outFile, FileMode.Create))
    {
        using (var stream1 = new FileStream(inputFile1, FileMode.Open))
        {
            using (var stream2 = new FileStream(inputFile2, FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(stream1, stream2, outputStream);
            }
        }
    }
}
```

### Menyisipkan halaman kosong

Setelah file PDF digabungkan, kita dapat menyisipkan halaman kosong di awal dokumen di mana kita dapat membuat Daftar Isi. Untuk memenuhi persyaratan ini, kita dapat memuat file gabungan ke dalam objek **Document** dan kita perlu memanggil metode Page.Insert(...) untuk menyisipkan halaman kosong.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertBlankPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Insert a blank page at the beginning of concatenated file to display Table of Contents
    using (var document = new Aspose.Pdf.Document(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"))
    {
        // Insert a blank page in a PDF
        document.Pages.Insert(1);
    }
}
```

### Menambahkan Stempel Teks

Untuk membuat Daftar Isi, kita perlu menambahkan stempel teks di halaman pertama menggunakan [PdfFileStamp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilestamp) dan objek [Stamp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/stamp). Kelas Stamp menyediakan metode `BindLogo(...)` untuk menambahkan [FormattedText](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formattedtext) dan kita juga dapat menentukan lokasi untuk menambahkan stempel teks ini menggunakan metode `SetOrigin(..)`. Dalam artikel ini, kita menggabungkan dua file PDF, jadi kita perlu membuat dua objek stempel teks yang mengarah ke dokumen individu ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampForTableOfContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    var inputPdfFile = Path.Combine(dataDir, "ConcatenateInput1.pdf");
    // Set Text Stamp to display string Table Of Contents
    var stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent, Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(inputPdfFile).GetPageWidth(1) / 3, 700);
    // Set particular pages
    stamp.Pages = new[] { 1 };
}
```

### Membuat tautan lokal

Sekarang kita perlu menambahkan tautan ke halaman di dalam file yang digabungkan. Untuk memenuhi persyaratan ini, kita dapat menggunakan metode `CreateLocalLink(..)` dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor). Dalam cuplikan kode berikut, kita telah melewatkan Transparent sebagai argumen ke-4 sehingga persegi panjang di sekitar tautan tidak terlihat.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLocalLinks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Now we need to add Heading for Table Of Contents and links for documents
    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
    // Bind PDF document
    contentEditor.BindPdf(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf");
    // Create link for first document
    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
}
```

### Kode lengkap

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CompleteCode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create a MemoryStream object to hold the resultant PDf file
    using (var concatenatedStream = new MemoryStream())
    {
        using (var fs1 = new FileStream(dataDir + "ConcatenateInput1.pdf", FileMode.Open))
        {
            using (var fs2 = new FileStream(dataDir + "ConcatenateInput2.pdf", FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(fs1, fs2, concatenatedStream);
            }
        }

        using (var concatenatedPdfDocument = new Aspose.Pdf.Document(concatenatedStream))
        {
            // Insert a blank page at the beginning of concatenated file to display Table of Contents
            concatenatedPdfDocument.Pages.Insert(1);

            // Hold the result file with empty page added
            using (var documentWithBlankPage = new MemoryStream())
            {
                // Save PDF document
                concatenatedPdfDocument.Save(documentWithBlankPage);

                using (var documentWithTocHeading = new MemoryStream())
                {
                    // Add Table Of Contents logo as stamp to PDF file
                    var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp();
                    // Bind PDF document
                    fileStamp.BindPdf(documentWithBlankPage);

                    // Set Text Stamp to display string Table Of Contents
                    var stamp = new Aspose.Pdf.Facades.Stamp();
                    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(documentWithBlankPage).GetPageWidth(1) / 3, 700);
                    // Set particular pages
                    stamp.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(stamp);

                    // Create stamp text for first item in Table Of Contents
                    var document1Link = new Aspose.Pdf.Facades.Stamp();
                    document1Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("1 - Link to Document 1", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document1Link.SetOrigin(150, 650);
                    // Set particular pages on which stamp should be displayed
                    document1Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document1Link);

                    // Create stamp text for second item in Table Of Contents
                    var document2Link = new Aspose.Pdf.Facades.Stamp();
                    document2Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("2 - Link to Document 2", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document2Link.SetOrigin(150, 620);
                    // Set particular pages on which stamp should be displayed
                    document2Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document2Link);

                    // Save PDF document
                    fileStamp.Save(documentWithTocHeading);
                    fileStamp.Close();

                    // Now we need to add Heading for Table Of Contents and links for documents
                    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
                    // Bind PDF document
                    contentEditor.BindPdf(documentWithTocHeading);
                    // Create link for first document
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
                    // Create link for Second document
                    // We have used   new PdfFileInfo("d:/pdftest/Input1.pdf").NumberOfPages + 2   as PdfFileInfo.NumberOfPages(..) returns the page count for first document
                    // And 2 is because, second document will start at Input1+1 and 1 for the page containing Table Of Contents.
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 620, 100, 20),
                        new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "ConcatenateInput1.pdf").NumberOfPages + 2, 1, System.Drawing.Color.Transparent);
                    // Save PDF document
                    contentEditor.Save(dataDir + "Concatenated_Table_Of_Contents_out.pdf");
                }
            }
        }
    }
}
```

## Menggabungkan file PDF dalam folder

Kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) dalam namespace Aspose.Pdf.Facades menawarkan Anda kemampuan untuk menggabungkan file PDF. Anda bahkan dapat membaca semua file PDF dalam folder tertentu saat runtime dan menggabungkannya, tanpa bahkan mengetahui nama file. Cukup berikan jalur direktori yang berisi dokumen PDF yang ingin Anda gabungkan.

Silakan coba menggunakan cuplikan kode C# berikut untuk mencapai fungsionalitas ini dari Aspose.PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "ConcatenatePdfFilesInFolder_out.pdf");
}
```