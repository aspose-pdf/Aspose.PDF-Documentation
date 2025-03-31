---
title: Memperbarui Tautan di PDF
linktitle: Memperbarui Tautan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/update-links/
description: Memperbarui tautan di PDF secara programatik. Panduan ini menjelaskan cara memperbarui tautan di PDF dalam bahasa C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update Links in PDF",
    "alternativeHeadline": "Programmatically Modify PDF Links Using C#",
    "abstract": "Fitur baru Memperbarui Tautan di PDF memungkinkan pengguna untuk memodifikasi hyperlink dalam dokumen PDF secara programatik menggunakan C#. Fungsionalitas ini memungkinkan pengguna untuk mengarahkan tautan ke halaman tertentu, alamat web eksternal, atau bahkan file PDF lainnya, meningkatkan interaktivitas dan kegunaan dokumen digital. Dengan menyederhanakan proses manajemen tautan, fitur ini sangat ideal bagi pengembang yang ingin mengoptimalkan aplikasi PDF mereka.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Update links in PDF, C#, LinkAnnotation, GoToAction, XYZExplicitDestination, GoToURIAction, update hyperlink, PDF manipulation",
    "wordcount": "797",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2024-11-25",
    "description": "Memperbarui tautan di PDF secara programatik. Panduan ini menjelaskan cara memperbarui tautan di PDF dalam bahasa C#."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) pustaka.

## Memperbarui Tautan di File PDF

Seperti yang dibahas dalam Menambahkan Hyperlink di File PDF, kelas [LinkAnnotation](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/linkannotation) memungkinkan untuk menambahkan tautan di file PDF. Ada juga kelas serupa yang digunakan untuk mendapatkan tautan yang ada dari dalam file PDF. Gunakan ini jika Anda perlu memperbarui tautan yang ada. Untuk memperbarui tautan yang ada:

1. Muat file PDF.
1. Pergi ke halaman tertentu di file PDF.
1. Tentukan tujuan tautan menggunakan properti Destination dari objek [GoToAction](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/gotoaction).
1. Halaman tujuan ditentukan menggunakan konstruktor [XYZExplicitDestination](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/xyzexplicitdestination).

### Atur Target Tautan ke Halaman di Dokumen yang Sama

Potongan kode berikut menunjukkan cara memperbarui tautan di file PDF dan mengatur targetnya ke halaman kedua dokumen.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link destination
        var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

        // Specify the destination for link object
        // The first parameter is document object, second is destination page number.
        // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
        goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

        // Save PDF document
        document.Save(dataDir + "UpdateLinks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link destination
    var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

    // Specify the destination for link object
    // The first parameter is document object, second is destination page number.
    // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
    goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

    // Save PDF document
    document.Save(dataDir + "UpdateLinks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Atur Tujuan Tautan ke Alamat Web

Untuk memperbarui hyperlink sehingga mengarah ke alamat web, buat objek [GoToURIAction](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/gotouriaction) dan berikan ke properti Action dari LinkAnnotation. Potongan kode berikut menunjukkan cara memperbarui tautan di file PDF dan mengatur targetnya ke alamat web.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link action and set target as web address
        linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

        // Save PDF document
        document.Save(dataDir + "SetDestinationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link action and set target as web address
    linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

    // Save PDF document
    document.Save(dataDir + "SetDestinationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Atur Target Tautan ke File PDF Lain

Potongan kode berikut menunjukkan cara memperbarui tautan di file PDF dan mengatur targetnya ke file PDF lain.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
        var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

        // Next line update destination, do not update file
        goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

        // Next line update file
        goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

        // Save PDF document
        document.Save(dataDir + "SetTargetLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
    var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

    // Next line update destination, do not update file
    goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

    // Next line update file
    goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

    // Save PDF document
    document.Save(dataDir + "SetTargetLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Perbarui Warna Teks LinkAnnotation

Anotasi tautan tidak mengandung teks. Sebaliknya, teks ditempatkan di konten halaman di bawah anotasi. Oleh karena itu, untuk mengubah warna teks, ganti warna teks halaman alih-alih mencoba mengubah warna anotasi. Potongan kode berikut menunjukkan cara memperbarui warna anotasi tautan di file PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        foreach (var annotation in document.Pages[1].Annotations)
        {
            if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
            {
                // Search the text under the annotation
                var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
                var rect = annotation.Rect;
                rect.LLX -= 10;
                rect.LLY -= 10;
                rect.URX += 10;
                rect.URY += 10;
                ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
                ta.Visit(document.Pages[1]);

                // Change color of the text.
                foreach (var textFragment in ta.TextFragments)
                {
                    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    foreach (var annotation in document.Pages[1].Annotations)
    {
        if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Search the text under the annotation
            var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
            var rect = annotation.Rect;
            rect.LLX -= 10;
            rect.LLY -= 10;
            rect.URX += 10;
            rect.URY += 10;
            ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
            ta.Visit(document.Pages[1]);

            // Change color of the text.
            foreach (var textFragment in ta.TextFragments)
            {
                textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
            }
        }
    }

    // Save PDF document
    document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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