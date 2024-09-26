---
title: הדפס PDF באפליקציה של WPF
linktitle: הדפס מסמך PDF באפליקציה של WPF
type: docs
weight: 50
url: /net/print-pdf-document-in-wpf-application/
description: הדפסת מסמכי PDF מאפליקציה של WPF באמצעות C#. דוגמת קוד זו מדגימה איך להדפיס מסמכי PDF מאפליקציה של WPF באמצעות C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הדפס PDF באפליקציה של WPF",
    "alternativeHeadline": "איך להדפיס PDF באפליקציה של WPF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, pdf באפליקציה של WPF",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכי Aspose.PDF",
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
    "description": "הדפסת מסמכי PDF מאפליקציה של WPF באמצעות C#. דוגמת קוד זו מדגימה איך להדפיס מסמכי PDF מאפליקציה של WPF באמצעות C#."
}
</script>
הקטע הבא בקוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הדפסה ישירה

ספריית Aspose.PDF יכולה להמיר קבצי PDF ל-XPS. אנו יכולים להשתמש בתכונה זו לארגן הדפסת מסמכים.
בואו נבחן את הדוגמה להדפסה ישירה:

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
במקרה זה, נעקוב אחר השלבים הבאים:

1. פתיחת קובץ PDF באמצעות OpenFileDialog
1. המרת PDF ל-XPS ואחסון באובייקט MemoryStream
1. הקשרת אובייקט MemoryStream עם חבילת Xps
1. הוספת החבילה לחנות החבילות
1. יצירת מסמך XpsDocument מתוך חבילה
1. קבלת מופע של FixedDocumentSequence
1. שליחת סדרה זו למדפסת באמצעות PrintDialog

## צפייה והדפסת מסמך

במקרים רבים, משתמשים רוצים לראות את המסמך לפני ההדפסה. ליישום תצוגה, ניתן להשתמש במחלקת DocViewer.
רוב השלבים ליישום גישה זו דומים לדוגמה הקודמת.

```csharp
private void OpenFile_OnClick(object sender, RoutedEventArgs e)
{
    var openFileDialog = new OpenFileDialog
    {
        Filter = "מסמכי PDF|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        var document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        var package = Package.Open(memoryStream);

        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //הוספת חבילה לחנות החבילות
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
    "name": "ספריית Aspose.PDF עבור .NET",
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
                "contactType": "מכירות",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
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
    "applicationCategory": "ספריית עיבוד PDF עבור .NET",
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
```

