---
title: Tooltip PDF menggunakan C#
linktitle: PDF Tooltip
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/pdf-tooltip/
description: Pelajari cara menambahkan tooltip ke fragmen teks dalam PDF menggunakan C# dan Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using C#",
    "alternativeHeadline": "Add Interactive Tooltips to PDF Text in C#",
    "abstract": "Tingkatkan dokumen PDF Anda dengan fitur Tooltip PDF baru menggunakan C#. Fungsionalitas ini memungkinkan Anda untuk dengan mudah menambahkan tooltip ke fragmen teks dalam file PDF, memberikan pengguna informasi tambahan saat mengarahkan kursor mouse. Manfaatkan tombol tak terlihat dan blok teks tersembunyi untuk menciptakan pengalaman membaca yang dinamis dan interaktif dengan Aspose.PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1072",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2024-11-26",
    "description": "Pelajari cara menambahkan tooltip ke fragmen teks dalam PDF menggunakan C# dan Aspose.PDF"
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

## Tambahkan Tooltip ke Teks yang Dicari dengan Menambahkan Tombol Tak Terlihat

Sering kali diperlukan untuk menambahkan beberapa detail untuk frasa atau kata tertentu sebagai tooltip dalam dokumen PDF sehingga dapat muncul saat pengguna mengarahkan kursor mouse ke teks. Aspose.PDF for .NET menyediakan fitur ini untuk membuat tooltip dengan menambahkan tombol tak terlihat di atas teks yang dicari. Potongan kode berikut akan menunjukkan cara mencapai fungsionalitas ini:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToSearchedText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a tooltip"));
        document.Pages[1].Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a very long tooltip"));
        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Tooltip_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a tooltip");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the extracted text fragments
        var textFragments = absorber.TextFragments;

        // Loop through the fragments
        foreach (var fragment in textFragments)
        {
            // Create invisible button on text fragment position
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // AlternateName value will be displayed as tooltip by a viewer application
            field.AlternateName = "Tooltip for text.";
            // Add button field to the document
            document.Form.Add(field);
        }

        absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.Pages.Accept(absorber);
        textFragments = absorber.TextFragments;

        foreach (var fragment in textFragments)
        {
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // Set very long text
            field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.";
            document.Form.Add(field);
        }

        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }
}
```

{{% alert color="primary" %}}

Mengenai panjang tooltip, teks tooltip terkandung dalam dokumen PDF sebagai tipe string PDF, di luar aliran konten. Tidak ada batasan efektif pada string semacam itu dalam file PDF (Lihat Referensi PDF Lampiran C.). Namun, pembaca yang sesuai (misalnya Adobe Acrobat) yang berjalan di prosesor tertentu dan dalam lingkungan operasi tertentu memang memiliki batasan semacam itu. Silakan merujuk ke dokumentasi aplikasi pembaca PDF Anda.

{{% /alert %}}

## Buat Blok Teks Tersembunyi dan Tampilkan Saat Mouse Melintas

Dalam Aspose.PDF, fitur untuk menyembunyikan aksi diimplementasikan di mana dimungkinkan untuk menampilkan/menghapus blok teks (atau jenis anotasi lainnya) saat mouse masuk/keluar di atas beberapa tombol tak terlihat. Untuk tujuan ini, Kelas Aspose.Pdf.Annotations.HideAction digunakan untuk menetapkan aksi sembunyi/tampilkan ke blok teks. Silakan gunakan potongan kode berikut untuk Menampilkan/Menyembunyikan Blok Teks saat Mouse Masuk/Keluar.

Silakan juga perhatikan bahwa aksi PDF dalam dokumen berfungsi dengan baik di pembaca yang sesuai (misalnya Adobe Reader) tetapi tidak ada jaminan untuk pembaca PDF lainnya (misalnya plugin browser web). Kami telah melakukan penyelidikan singkat dan menemukan:

- Semua implementasi aksi sembunyi dalam dokumen PDF berfungsi dengan baik di Internet Explorer v.11.0.
- Semua implementasi aksi sembunyi juga berfungsi di Opera v.12.14, tetapi kami menemukan beberapa keterlambatan respons saat pertama kali membuka dokumen.
- Hanya implementasi yang menggunakan konstruktor HideAction yang menerima nama bidang yang berfungsi jika Google Chrome v.61.0 menjelajahi dokumen; Silakan gunakan konstruktor yang sesuai jika menjelajahi di Google Chrome signifikan:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHiddenTextBlock()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add paragraph with text
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display floating text"));
        // Save PDF document
        document.Save(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display floating text");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the first extracted text fragment
        var textFragments = absorber.TextFragments;
        var fragment = textFragments[1];

        // Create hidden text field for floating text in the specified rectangle of the page
        var floatingField = new Aspose.Pdf.Forms.TextBoxField(fragment.Page, new Aspose.Pdf.Rectangle(100, 700, 220, 740));
        // Set text to be displayed as field value
        floatingField.Value = "This is the \"floating text field\".";
        // We recommend to make field 'readonly' for this scenario
        floatingField.ReadOnly = true;
        // Set 'hidden' flag to make field invisible on document opening
        floatingField.Flags |= Aspose.Pdf.Annotations.AnnotationFlags.Hidden;

        // Setting a unique field name isn't necessary but allowed
        floatingField.PartialName = "FloatingField_1";

        // Setting characteristics of field appearance isn't necessary but makes it better
        floatingField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
        floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
        floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
        floatingField.Border = new Aspose.Pdf.Annotations.Border(floatingField);
        floatingField.Border.Width = 1;
        floatingField.Multiline = true;

        // Add text field to the document
        document.Form.Add(floatingField);

        // Create invisible button on text fragment position
        var buttonField = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
        // Create new hide action for specified field (annotation) and invisibility flag
        // (You also may reffer floating field by the name if you specified it above)
        // Add actions on mouse enter/exit at the invisible button field
        buttonField.Actions.OnEnter = new Aspose.Pdf.Annotations.HideAction(floatingField, false);
        buttonField.Actions.OnExit = new Aspose.Pdf.Annotations.HideAction(floatingField);

        // Add button field to the document
        document.Form.Add(buttonField);

        // Save PDF document
        document.Save(dataDir + "CreateHiddenTextBlock_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>