---
title: חיפוש ואיחזור תמונות ב-PDF
linktitle: חיפוש ואיחזור תמונות
type: docs
weight: 60
url: /net/search-and-get-images-from-pdf-document/
description: פרק זה מסביר איך לחפש ולאחזר תמונות ממסמך PDF באמצעות ספריית Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "חיפוש ואיחזור תמונות ב-PDF",
    "alternativeHeadline": "איך לחפש ולאחזר תמונות בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, .net, get image, search image",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות Aspose.PDF Doc",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מסביר איך לחפש ולאחזר תמונות ממסמך PDF באמצעות ספריית Aspose.PDF."
}
</script>
ImagePlacementAbsorber מאפשר לך לחפש בין תמונות בכל הדפים במסמך PDF.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

לחיפוש תמונות במסמך שלם:

1. קרא לשיטת Accept של אוסף הדפים. שיטת ה-Accept לוקחת אובייקט מסוג ImagePlacementAbsorber כפרמטר. זה מחזיר אוסף של אובייקטים מסוג ImagePlacement.
1. עבור על אובייקטי ה-ImagePlacement וקבל את התכונות שלהם (תמונה, ממדים, רזולוציה וכו').

הקטע קוד הבא מראה כיצד לחפש במסמך את כל התמונות שלו.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// פתח מסמך
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// צור אובייקט ImagePlacementAbsorber כדי לבצע חיפוש אחזור תמונה
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// קבל את ה-absorber עבור כל הדפים
doc.Pages.Accept(abs);

// עבור על כל ה-ImagePlacements, קבל תמונה ותכונות ImagePlacement
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // קבל את התמונה באמצעות אובייקט ImagePlacement
    XImage image = imagePlacement.Image;

    // הצג תכונות אחזור תמונה עבור כל ההשמות
    Console.Out.WriteLine("רוחב תמונה:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("גובה תמונה:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("תמונה LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("תמונה LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("רזולוציה אופקית של תמונה:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("רזולוציה אנכית של תמונה:" + imagePlacement.Resolution.Y);
}
```
כדי לקבל תמונה מדף נפרד, השתמש בקוד הבא:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
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
    "applicationCategory": "ספריית עיבוד PDF ל-.NET",
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


