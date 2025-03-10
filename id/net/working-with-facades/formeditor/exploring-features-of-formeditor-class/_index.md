---
title: Menjelajahi fitur kelas FormEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/exploring-features-of-formeditor-class/
description: Anda dapat mempelajari rincian menjelajahi fitur kelas FormEditor dengan Aspose. PDF untuk .NET library
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "Temukan kemampuan yang ditingkatkan dari kelas FormEditor dalam pustaka Aspose.PDF for .NET, yang dirancang untuk manipulasi formulir PDF interaktif dengan mudah. Fitur ini memberdayakan pengembang untuk dengan mudah menambahkan, mengedit, dan mengonfigurasi bidang formulir, dengan metode yang ramah pengguna untuk memperlancar proses modifikasi. Optimalkan penanganan formulir PDF Anda dengan memanfaatkan fungsionalitas komprehensif dari FormEditor untuk meningkatkan alur kerja dokumen Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Dokumen PDF terkadang mengandung formulir interaktif, yang dikenal sebagai AcroForm. Ini mirip dengan formulir yang digunakan di halaman web. Formulir ini mengandung berbagai jenis kontrol yaitu. Kotak Teks, Kotak Centang, dan Tombol, dll. Seorang pengembang yang bekerja dengan file PDF mungkin terkadang harus mengedit formulir ini. Dalam artikel ini, kita akan melihat rincian bagaimana [ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) memungkinkan kita untuk melakukan itu.

{{% /alert %}}

## Rincian implementasi

Pengembang dapat menggunakan [ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) tidak hanya untuk menambahkan formulir baru dan bidang formulir dalam dokumen PDF, tetapi juga memungkinkan Anda untuk mengedit bidang yang ada. Ruang lingkup artikel ini terbatas pada fitur-fitur dari [Aspose.PDF for .NET](/pdf/net/) yang berhubungan dengan pengeditan formulir.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) adalah kelas yang berisi sebagian besar metode dan properti yang memungkinkan pengembang untuk mengedit bidang formulir. Anda tidak hanya dapat menambahkan bidang baru, tetapi juga menghapus bidang yang ada, memindahkan satu bidang ke posisi lain, mengubah nama bidang, atau atribut, dll. Daftar fitur yang disediakan oleh kelas ini cukup komprehensif, dan sangat mudah untuk bekerja dengan bidang formulir menggunakan kelas ini.

Metode-metode ini dapat dibagi menjadi dua kategori utama, salah satunya digunakan untuk memanipulasi bidang, dan yang lainnya digunakan untuk mengatur atribut baru dari bidang-bidang ini. Metode yang dapat kita kelompokkan di bawah kategori pertama termasuk AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, dan RenameField, dll. Dalam kategori kedua dari metode SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript dapat dimasukkan. Potongan kode berikut menunjukkan beberapa metode dari kelas FormEditor dalam bekerja:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```