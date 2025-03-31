---
title: Tambahkan Bidang Formulir PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/add-form-fields/
description: Topik ini menjelaskan cara bekerja dengan Bidang Formulir menggunakan Aspose.PDF Facades dengan kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "Tingkatkan dokumen PDF Anda dengan interaktivitas dinamis dengan menambahkan bidang formulir menggunakan kelas FormEditor di Aspose.PDF for .NET. Fitur ini memungkinkan Anda untuk dengan mudah menggabungkan bidang teks, tombol kirim dengan URL, dan fungsionalitas JavaScript untuk tombol dorong, menyederhanakan input pengguna dan pengiriman data dalam PDF Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Tambahkan Bidang Formulir di File PDF yang Ada

Untuk menambahkan bidang formulir di file PDF yang ada, Anda perlu menggunakan metode [AddField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/addfield/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor). Metode ini mengharuskan Anda untuk menentukan jenis bidang yang ingin Anda tambahkan bersama dengan nama dan lokasi bidang tersebut. Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor), menggunakan metode [AddField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/addfield/index) untuk menambahkan bidang baru di PDF, Selain itu, Anda dapat menentukan batasan jumlah karakter di bidang Anda dengan [SetFieldLimit](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) dan akhirnya menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/save/index) untuk menyimpan file PDF yang diperbarui. Potongan kode berikut menunjukkan kepada Anda cara menambahkan bidang formulir di file PDF yang ada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## Tambahkan URL Tombol Kirim di File PDF yang Ada

Metode [AddSubmitBtn](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) memungkinkan Anda untuk mengatur URL tombol kirim di file PDF. Ini adalah URL tempat data diposting ketika tombol kirim diklik. Dalam kode contoh kami, kami menentukan URL, nama bidang kami, nomor halaman tempat kami ingin menambahkan, dan koordinat penempatan tombol. Metode [AddSubmitBtn](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) memerlukan nama bidang tombol kirim dan URL. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Potongan kode berikut menunjukkan kepada Anda cara mengatur URL tombol kirim.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Tambahkan JavaScript untuk Tombol Dorong

Metode [AddFieldScript](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/addfieldscript) memungkinkan Anda untuk menambahkan JavaScript ke tombol dorong di file PDF. Metode ini memerlukan nama tombol dorong dan JavaScript. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Potongan kode berikut menunjukkan kepada Anda cara mengatur JavaScript ke tombol dorong.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```