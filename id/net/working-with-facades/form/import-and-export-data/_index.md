---
title: Impor dan Ekspor Data
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /id/net/import-and-export-data/
description: Bagian ini menjelaskan cara mengimpor dan mengekspor data dengan Aspose.PDF Facades menggunakan Kelas Form.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "Fitur Impor dan Ekspor Data di Aspose.PDF for .NET memungkinkan integrasi manajemen data dokumen yang mulus dengan memungkinkan pengguna untuk mengimpor dan mengekspor data formulir PDF menggunakan format XML, FDF, XFDF, dan JSON. Fungsionalitas ini meningkatkan kemampuan penanganan data, membuatnya lebih mudah untuk mengotomatiskan alur kerja dan mempertahankan catatan yang akurat langsung dari dokumen PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) memungkinkan Anda untuk mengimpor data dari file XML ke file PDF menggunakan metode [ImportXml](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.form/importxml/methods/1). Untuk mengimpor data dari XML, Anda perlu membuat objek dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) dan kemudian memanggil metode [ImportXml](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/importxml/index) menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/save) dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form). Potongan kode berikut menunjukkan cara mengimpor data dari file XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## Ekspor Data ke XML dari File PDF

[Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) memungkinkan Anda untuk mengekspor data ke file XML dari file PDF menggunakan metode [ExportXml](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/exportxml). Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) dan kemudian memanggil metode [ExportXml](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/exportxml) menggunakan objek FileStream. Akhirnya, Anda dapat menutup objek FileStream dan membuang objek Form. Potongan kode berikut menunjukkan cara mengekspor data ke file XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## Impor Data dari FDF ke File PDF

[Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) memungkinkan Anda untuk mengimpor data dari file FDF ke file PDF menggunakan metode [ImportFdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/importfdf). Untuk mengimpor data dari FDF, Anda perlu membuat objek dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) dan kemudian memanggil metode [ImportFdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/importfdf) menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/save) dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form). Potongan kode berikut menunjukkan cara mengimpor data dari file FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## Ekspor Data ke FDF dari File PDF

[Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) memungkinkan Anda untuk mengekspor data ke file FDF dari file PDF menggunakan metode [ExportFdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/exportfdf). Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) dan kemudian memanggil metode [ExportFdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/exportfdf) menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/save) dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form). Potongan kode berikut menunjukkan cara mengekspor data ke file FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## Impor Data dari XFDF ke File PDF

[Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) memungkinkan Anda untuk mengimpor data dari file XFDF ke file PDF menggunakan metode [ImportXfdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/importxfdf). Untuk mengimpor data dari XFDF, Anda perlu membuat objek dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) dan kemudian memanggil metode [ImportXfdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/importxfdf) menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/save) dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form). Potongan kode berikut menunjukkan cara mengimpor data dari file XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## Ekspor Data ke XFDF dari File PDF

[Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) memungkinkan Anda untuk mengekspor data ke file XFDF dari file PDF menggunakan metode [ExportXfdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/exportxfdf). Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form) dan kemudian memanggil metode [ExportXfdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/exportxfdf) menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/save) dari kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/form). Potongan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## Ekspor nilai dari bidang ke file JSON

Aspose.Pdf.Facades menyediakan API alternatif untuk bekerja dengan bidang formulir. Potongan kode ini menunjukkan cara mengekspor dan mengimpor nilai bidang menggunakan API ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## Impor nilai ke bidang dari file JSON

Potongan kode ini menunjukkan cara mengimpor nilai ke dalam bidang formulir dari dokumen PDF dari file JSON menggunakan API Aspose.Pdf.Facades. FileStream digunakan untuk menangani file JSON.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```