---
title: Ekstrak Data dari AcroForm menggunakan C#
linktitle: Ekstrak Data dari AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/extract-data-from-acroform/
description: Aspose.PDF memudahkan untuk mengekstrak data field formulir dari file PDF. Pelajari cara mengekstrak data dari AcroForms dan menyimpannya dalam format JSON, XML, atau FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "Temukan fungsionalitas baru di Aspose.PDF for .NET yang menyederhanakan ekstraksi data field formulir dari AcroForms dalam dokumen PDF. Dengan kemampuan untuk mengekspor data ke format JSON, XML, FDF, dan XFDF, pengguna dapat mengelola data formulir dengan efisien sambil memanfaatkan contoh kode yang ringkas untuk integrasi yang mulus ke dalam aplikasi",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ekstrak field formulir dari dokumen PDF

Selain memungkinkan Anda untuk menghasilkan field formulir dan mengisi field formulir, Aspose.PDF for .NET memudahkan untuk mengekstrak data field formulir atau informasi tentang field formulir dari file PDF.

Dalam contoh kode di bawah ini, kami menunjukkan cara untuk mengiterasi melalui setiap halaman dalam PDF untuk mengekstrak informasi tentang semua AcroForm dalam PDF serta nilai field formulir. Contoh kode ini mengasumsikan bahwa Anda tidak mengetahui nama field formulir sebelumnya.

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

Jika Anda mengetahui nama field formulir yang ingin Anda ekstrak nilainya, maka Anda dapat menggunakan indexer dalam koleksi Documents.Form untuk dengan cepat mengambil data ini. Lihat di bagian bawah artikel ini untuk contoh kode tentang cara menggunakan fungsi tersebut.

## Ambil nilai field formulir berdasarkan judul

Properti Value dari field formulir memungkinkan Anda untuk mendapatkan nilai dari field tertentu. Untuk mendapatkan nilai, ambil field formulir dari koleksi Form objek Document. Contoh ini memilih TextBoxField dan mengambil nilainya menggunakan properti Value.

## Ekstrak field formulir dari dokumen PDF ke JSON

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## Ekstrak Data ke XML dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXml menggunakan objek FileStream. Akhirnya, Anda dapat menutup objek FileStream dan membuang objek Form. Potongan kode berikut menunjukkan cara mengekspor data ke file XML.

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## Ekspor Data ke FDF dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file FDF dari file PDF menggunakan metode ExportFdf. Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportFdf menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode Save dari kelas Form. Potongan kode berikut menunjukkan cara mengekspor data ke file FDF.

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## Ekspor Data ke XFDF dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file XFDF dari file PDF menggunakan metode ExportXfdf. Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXfdf menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode Save dari kelas Form. Potongan kode berikut menunjukkan cara mengekspor data ke file XFDF.

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```