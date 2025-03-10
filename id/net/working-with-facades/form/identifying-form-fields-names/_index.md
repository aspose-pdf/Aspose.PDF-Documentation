---
title: Mengidentifikasi nama bidang formulir
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades memungkinkan Anda mengidentifikasi nama bidang formulir menggunakan Kelas Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "Fungsionalitas dalam Aspose.PDF for .NET menyederhanakan proses identifikasi nama bidang formulir dalam dokumen PDF. Dengan memanfaatkan kelas Form dan atributnya, pengguna dapat dengan mudah mengambil dan menampilkan nama bidang bersama dengan bidang yang sesuai, memperlancar pengisian dan pengeditan formulir PDF. Fitur ini meningkatkan pengalaman pengguna dengan memastikan manipulasi bidang yang akurat, terutama saat bekerja dengan formulir yang dibuat di alat eksternal seperti Adobe Designer",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[Aspose.PDF for .NET](/pdf/net/) menyediakan kemampuan untuk membuat, mengedit, dan mengisi formulir Pdf yang sudah dibuat. [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace berisi kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), yang memiliki fungsi bernama [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) dan mengambil dua argumen yaitu nama bidang dan nilai bidang. Jadi, untuk mengisi bidang formulir, Anda harus mengetahui nama bidang formulir yang tepat.

## Detail implementasi

Kami sering menemui skenario di mana kami perlu mengisi formulir yang dibuat di beberapa alat yaitu Adobe Designer, dan kami tidak yakin tentang nama bidang formulir. Jadi, untuk mengisi bidang formulir, pertama-tama kami perlu membaca nama semua bidang formulir Pdf. Kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) menyediakan properti bernama [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) yang mengembalikan semua nama bidang dan mengembalikan null jika PDF tidak mengandung bidang apa pun. Namun, saat menggunakan properti ini, kami mendapatkan nama semua bidang dalam formulir PDF dan kami mungkin tidak yakin nama mana yang sesuai dengan bidang mana di formulir.

Sebagai solusi untuk masalah ini, kami akan menggunakan atribut penampilan dari setiap bidang. Kelas Form memiliki fungsi bernama [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) yang mengembalikan atribut, termasuk lokasi, warna, gaya batas, font, item daftar, dan sebagainya. Untuk menyimpan nilai-nilai ini, kami perlu menggunakan kelas [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), yang digunakan untuk mencatat atribut visual dari bidang. Setelah kami memiliki atribut ini, kami dapat menambahkan bidang teks di bawah setiap bidang yang akan menampilkan nama bidang.

{{% alert color="primary" %}}
Pada titik ini, muncul pertanyaan "bagaimana kami akan menentukan lokasi di mana menambahkan bidang teks?"
{{% /alert %}}

{{% alert color="primary" %}}
Solusi untuk masalah ini adalah properti Box dalam kelas [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), yang menyimpan lokasi bidang. Kami perlu menyimpan nilai-nilai ini ke dalam array tipe persegi panjang dan menggunakan nilai-nilai ini untuk mengidentifikasi posisi di mana menambahkan bidang teks baru.

{{% /alert %}}

Dalam namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) kami memiliki kelas bernama [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) yang menyediakan kemampuan untuk memanipulasi formulir PDF. Buka formulir pdf; tambahkan bidang teks di bawah setiap bidang formulir yang ada dan simpan formulir Pdf dengan nama baru.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```