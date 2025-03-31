---
title: Bekerja dengan Item Daftar
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/working-with-list-item/
description: Bagian ini menjelaskan cara bekerja dengan Item Daftar menggunakan Aspose.PDF Facades dengan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Tingkatkan formulir PDF Anda dengan fitur Item Daftar di Aspose.PDF for .NET. Dengan mudah menambahkan atau menghapus item dari bidang ListBox menggunakan kelas FormEditor, memungkinkan input pengguna yang dinamis dan dapat disesuaikan. Fungsionalitas ini menyederhanakan manajemen formulir, membuatnya lebih mudah untuk menyesuaikan konten sesuai kebutuhan Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Tambahkan Item Daftar di File PDF yang Ada

[AddListItem](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/addlistitem) metode memungkinkan Anda untuk menambahkan item di bidang [ListBox](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/listboxfield). Argumen pertama adalah nama bidang dan argumen kedua adalah item bidang. Anda dapat melewatkan satu item bidang atau Anda dapat melewatkan array string yang berisi daftar item. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor). Cuplikan kode berikut menunjukkan cara menambahkan item daftar di file PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Hapus Item Daftar dari File PDF yang Ada

[DelListItem](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/dellistitem) metode memungkinkan Anda untuk menghapus item tertentu dari [ListBox](https://reference.aspose.com/pdf/id/net/aspose.pdf.forms/listboxfield). Parameter pertama adalah nama bidang sementara parameter kedua adalah item yang ingin Anda hapus dari daftar. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor). Cuplikan kode berikut menunjukkan cara menghapus item daftar dari file PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```