---
title: Hias Bidang Form di PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/decorate-form-field/
description: Jelajahi cara menghias bidang formulir dalam dokumen PDF, menambahkan peningkatan visual seperti batas, di .NET dengan Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "Memperkenalkan fitur kuat yang meningkatkan manajemen formulir PDF: kemampuan untuk menghias bidang formulir individu atau semua bidang formulir menggunakan Kelas FormEditor. Fungsionalitas ini memungkinkan pengguna untuk menyesuaikan atribut bidang seperti gaya font, ukuran, warna batas, dan perataan, menyederhanakan proses pembuatan formulir PDF yang menarik secara visual dan terstruktur dengan baik. Tingkatkan alur kerja PDF Anda dengan metode dekorasi intuitif ini untuk presentasi dokumen yang lebih halus.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "609",
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
    "url": "/net/decorate-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decorate-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Hias Bidang Form Tertentu dalam File PDF yang Ada

[DecorateField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/decoratefield) metode yang ada dalam kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor) memungkinkan Anda untuk menghias bidang formulir tertentu dalam file PDF. Jika Anda ingin menghias bidang tertentu maka Anda perlu mengirimkan nama bidang ke metode ini. Namun, sebelum memanggil metode ini, Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor) dan [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade). Anda juga perlu menetapkan objek [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade) ke properti [Facade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/facade/properties/index) dari objek [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Setelah itu, Anda dapat mengatur atribut apa pun yang disediakan oleh objek [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade). Setelah Anda mengatur atribut, Anda dapat memanggil metode [DecorateField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/decoratefield) dan akhirnya menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/save/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor). 
Potongan kode berikut menunjukkan kepada Anda cara menghias bidang formulir tertentu.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define decoration properties for the field
        var cityDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set the font style to Courier
            Font = Aspose.Pdf.Facades.FontStyle.Courier,
            // Set the font size to 12
            FontSize = 12,
            // Set the border color to black
            BorderColor = System.Drawing.Color.Black,
            // Set the border width to 2
            BorderWidth = 2
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = cityDecoration;

        // Apply the decoration to the field named "City"
        editor.DecorateField("City");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-02.pdf");
    }
}
```

## Hias Semua Bidang Tipe Tertentu dalam File PDF yang Ada

Metode [DecorateField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) memungkinkan Anda untuk menghias semua bidang formulir dari tipe tertentu dalam file PDF sekaligus. Jika Anda ingin menghias semua bidang dari tipe tertentu maka Anda perlu mengirimkan tipe bidang ke metode ini. Namun, sebelum memanggil metode ini, Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor) dan [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade). Anda juga perlu menetapkan objek [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade) ke properti [Facade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/facade/properties/index) dari objek [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Setelah itu, Anda dapat mengatur atribut apa pun yang disediakan oleh objek [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade). Setelah Anda mengatur atribut, Anda dapat memanggil metode [DecorateField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) dan akhirnya menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/save/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor). Potongan kode berikut menunjukkan kepada Anda cara menghias semua bidang dari tipe tertentu.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define alignment properties for text fields
        var textFieldDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set text alignment to center
            Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignCenter
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = textFieldDecoration;

        // Apply the alignment decoration to all text fields in the PDF
        editor.DecorateField(Aspose.Pdf.Facades.FieldType.Text);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-align-text.pdf");
    }
}
```