---
title: Mengonversi PDF ke Excel di .NET
linktitle: Mengonversi PDF ke Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Aspose.PDF for .NET library memungkinkan Anda untuk mengonversi PDF ke format Excel menggunakan C#. Format ini mencakup XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "Temukan kemampuan kuat dari Aspose.PDF for .NET untuk dengan mudah mengonversi dokumen PDF menjadi berbagai format Excel, termasuk XLS, XLSX, CSV, dan ODS, menggunakan C#. Fitur ini tidak hanya memungkinkan transformasi halaman PDF individu menjadi lembar kerja Excel terpisah tetapi juga menawarkan opsi untuk lembar gabungan, memberikan fleksibilitas bagi pengguna untuk mengelola data PDF mereka dengan efisien",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1445",
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
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ikhtisar

Artikel ini menjelaskan bagaimana **mengonversi PDF ke format Excel menggunakan C#**. Ini mencakup topik-topik berikut.

Potongan kode berikut juga bekerja dengan library [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

- [Mengonversi PDF ke XLS](#csharp-pdf-to-xls)
- [Mengonversi PDF ke XLSX](#csharp-pdf-to-xlsx)
- [Mengonversi PDF ke Excel](#csharp-pdf-to-xlsx)
- [Mengonversi PDF ke XLS dengan Lembar Kerja Tunggal](#csharp-pdf-to-excel-single)
- [Mengonversi PDF ke XLSX dengan Lembar Kerja Tunggal](#csharp-pdf-to-excel-single)
- [Mengonversi PDF ke XML Excel](#csharp-pdf-to-excel-xml-2003)
- [Mengonversi PDF ke CSV](#csharp-pdf-to-csv)
- [Mengonversi PDF ke ODS](#csharp-pdf-to-ods)
- [Mengonversi PDF ke XLSM](#csharp-pdf-to-xlsm)

## Konversi PDF ke Excel C#

**Aspose.PDF for .NET** mendukung fitur mengonversi file PDF ke format Excel 2007, CSV, dan SpeadsheetML.

Aspose.PDF for .NET adalah komponen manipulasi PDF, kami telah memperkenalkan fitur yang merender file PDF ke workbook Excel (file XLSX). Selama konversi ini, halaman-halaman individu dari file PDF dikonversi menjadi lembar kerja Excel.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke Excel secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Untuk mengonversi file PDF ke format <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/excelsaveoptions). Sebuah objek dari kelas ExcelSaveOptions diteruskan sebagai argumen kedua ke konstruktor Document.Save(..).

Potongan kode berikut menunjukkan proses untuk mengonversi file PDF menjadi format XLS atau XLSX dengan Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>Mengonversi PDF ke XLS</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions**.
3. Simpan ke format **XLS** dengan menentukan **.xls extension** dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>Mengonversi PDF ke XLSX</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions**.
3. Simpan ke format **XLSX** dengan menentukan **.xlsx extension** dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## Mengonversi PDF ke XLS dengan Kontrol Kolom

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file output sebagai kolom pertama. Opsi InsertBlankColumnAtFirst dari kelas ExcelSaveOptions digunakan untuk mengontrol kolom ini. Nilai default adalah `false`, yang berarti kolom kosong tidak akan disisipkan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Mengonversi PDF ke Lembar Kerja Excel Tunggal

Saat mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar yang berbeda dalam file Excel. Ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar tunggal dalam file Excel output, atur properti MinimizeTheNumberOfWorksheets ke true.

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>Mengonversi PDF ke XLS atau XLSX Lembar Kerja Tunggal</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions** dengan **MinimizeTheNumberOfWorksheets = true**.
3. Simpan ke format **XLS** atau **XLSX** dengan memiliki lembar kerja tunggal dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Mengonversi ke format spreadsheet lainnya

### Mengonversi ke format XML Spreadsheet 2003

Sejak versi 20.8 Aspose.PDF menggunakan format file Microsoft Excel Open XML Spreadsheet 2007 sebagai default untuk menyimpan data. Untuk mengonversi file PDF ke format XML Spreadsheet 2003, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/excelsaveoptions) dengan [Format](https://reference.aspose.com/pdf/id/net/aspose.pdf/excelsaveoptions/properties/format). Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/excelsaveoptions) diteruskan sebagai argumen kedua ke metode [Document.Save(..)](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save/index).

Potongan kode berikut menunjukkan proses untuk mengonversi file PDF menjadi format XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>Mengonversi PDF ke Format Excel 2003 XML</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions** dengan **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**.
3. Simpan ke format **XLS - Format Excel 2003 XML** dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### Mengonversi ke CSV

Konversi ke format CSV dilakukan dengan cara yang sama seperti di atas. Semua yang Anda butuhkan - atur format yang sesuai.

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>Mengonversi PDF ke CSV</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions** dengan **Format = ExcelSaveOptions.ExcelFormat.CSV**.
3. Simpan ke format **CSV** dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### Mengonversi ke ODS

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>Mengonversi PDF ke ODS</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions** dengan **Format = ExcelSaveOptions.ExcelFormat.ODS**.
3. Simpan ke format **ODS** dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.


Konversi ke format ODS dilakukan dengan cara yang sama seperti semua format lainnya.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

### Mengonversi ke XLSM

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>Mengonversi PDF ke XLSM</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instance dari **ExcelSaveOptions** dengan **Format = ExcelSaveOptions.ExcelFormat.XLSM**.
3. Simpan ke format **XLSM** dengan memanggil metode **Document.Save()** dan meneruskan **ExcelSaveOptions**.

Konversi ke format XLSM dilakukan dengan cara yang sama seperti semua format lainnya.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in XLSM format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```