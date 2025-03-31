---
title: Penampilan dan atribut field
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/changing-field-appearance-and-attributes/
description: Bagian ini menjelaskan bagaimana Anda dapat mengubah penampilan dan atribut field dengan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "Fitur yang diperkenalkan dalam kelas FormEditor dari namespace Aspose.Pdf.Facades memungkinkan pengguna untuk menyesuaikan baik penampilan maupun atribut field form dalam PDF. Dengan memanfaatkan metode seperti SetFieldAppearance dan SetFieldAttributes, pengembang dapat dengan mudah memodifikasi elemen visual dan perilaku, termasuk batas field, untuk meningkatkan interaksi pengguna dan efisiensi input data. Fungsionalitas ini menawarkan fleksibilitas yang lebih besar dalam merancang field form yang disesuaikan dengan kebutuhan aplikasi tertentu.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

[Kelas FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/FormEditor) dari [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) memungkinkan Anda untuk tidak hanya mengubah tampilan dan nuansa field form, tetapi juga perilaku field tersebut. Dalam artikel ini, kita akan melihat bagaimana kita dapat menggunakan kelas FormEditor untuk mengubah penampilan field, atribut field, dan batas field juga.

{{% /alert %}}

## Detail implementasi

Metode [SetFieldAppearance](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) digunakan untuk mengubah penampilan field form. Ini mengambil AnnotationFlag sebagai parameter. AnnotationFlag adalah enumerasi yang memiliki anggota berbeda seperti Hidden atau NoRotate, dll.

Metode [SetFieldAttributes](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) digunakan untuk mengubah atribut field form. Parameter yang diteruskan ke metode ini adalah enumerasi PropertyFlag yang berisi anggota seperti ReadOnly atau Required, dll.

Kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/FormEditor) juga menyediakan metode untuk mengatur batas field. Ini memberi tahu field berapa banyak karakter yang dapat diisi. Potongan kode di bawah ini menunjukkan bagaimana semua metode ini dapat digunakan.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```