---
title: Print PDF in WPF application
linktitle: Print PDF document in WPF application
type: docs
weight: 50
url: /net/print-pdf-document-in-wpf-application/
description: C# Print PDF documents from a WPF application. This code sample shows how to print PDF documents from a WPF application using C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Print PDF in WPF application",
    "alternativeHeadline": "How to print PDF in WPF application",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, pdf in WPF application",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/print-pdf-document-in-wpf-application/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-pdf-document-in-wpf-application/"
    },
    "dateModified": "2022-02-04",
    "description": "C# Print PDF documents from a WPF application. This code sample shows how to print PDF documents from a WPF application using C#."
}
</script>

## Direct print

The Aspose.PDF library has the ability to convert PDF files to XPS. We can use this function to organize the printing of documents.
Let's consider the example for direct printing:

```csharp
    private void Print_OnClick(object sender, RoutedEventArgs e)
    {
        var openFileDialog = new OpenFileDialog
        {
            Filter = "PDF Documents|*.pdf"
        };
        openFileDialog.ShowDialog();

        Aspose.Pdf.Document document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);
        var package = Package.Open(memoryStream);

        //Create URI for Xps Package
        //Any Uri will actually be fine here. It acts as a place holder for the
        //Uri of the package inside of the PackageStore
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();

        var printDialog = new PrintDialog();
        if (printDialog.ShowDialog() == true)
        {
            if (fixedDocumentSequence != null)
                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator, "A fixed document");
            else
                throw new NullReferenceException();
        }
        PackageStore.RemovePackage(packageUri);
        xpsDoc.Close();

    }
```

In this case, we will follow these steps:

1. Open PDF file using OpenFileDialog
1. Convert PDF to XPS and store it in MemoryStream object
1. Associate MemoryStream object with Xps Package
1. Add the package to the Package Store
1. Create an XpsDocument based on package
1. Get an instance of the FixedDocumentSequence
1. Send this sequence to the printer using PrintDialog

## View and print document

In many cases, users want to see the document before printing. To implement a view, we can use a DocViewer class.
Most of the steps for implementing this approach are similar to the previous example.

```csharp
private void OpenFile_OnClick(object sender, RoutedEventArgs e)
{
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        var document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        var package = Package.Open(memoryStream);

        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        DocViewer.Document = xpsDoc.GetFixedDocumentSequence();
        xpsDoc.Close();
    };
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
