---
title: יצירת קישורים בקובץ PDF עם C#
linktitle: יצירת קישורים
type: docs
weight: 10
url: /net/create-links/
description: סעיף זה מסביר כיצד ליצור קישורים במסמך PDF שלך עם C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "יצירת קישורים בקובץ PDF עם C#",
    "alternativeHeadline": "כיצד ליצור קישורים ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, יצירת קישור ב-pdf",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "סעיף זה מסביר כיצד ליצור קישורים במסמך PDF שלך עם C#."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## יצירת קישורים

על ידי הוספת קישור ליישום במסמך, ניתן לקשר ליישומים מתוך מסמך. זה שימושי כאשר ברצונך שקוראים יבצעו פעולה מסוימת בנקודה מסוימת במדריך, לדוגמה, או ליצור מסמך עשיר בתכונות. כדי ליצור קישור ליישום:

1. [יצירת אובייקט מסמך](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. קבל את ה[דף](https://reference.aspose.com/pdf/net/aspose.pdf/page) שבו אתה רוצה להוסיף קישור.
1. צור אובייקט [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) באמצעות הדף ואובייקטים [מלבן](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. הגדר את תכונות הקישור באמצעות אובייקט [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. בעת יצירת אובייקט [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction), ציין את היישום שברצונך להפעיל.
1. הוסף את הקישור לתכונת [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) של אובייקט הדף.
1. לבסוף, שמור את ה-PDF עם השינויים באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) של אובייקט המסמך.

הקטע הבא מראה איך ליצור קישור ליישום בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// פתח מסמך
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// צור קישור
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// שמור מסמך מעודכן
document.Save(dataDir);
```
### יצירת קישור למסמך PDF בקובץ PDF

Aspose.PDF עבור .NET מאפשר לך להוסיף קישור לקובץ PDF חיצוני כך שתוכל לקשר מסמכים מספר יחד. כדי ליצור קישור למסמך PDF:

1. תחילה, צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. לאחר מכן, קבל את ה[עמוד](https://reference.aspose.com/pdf/net/aspose.pdf/page) שבו אתה רוצה להוסיף את הקישור.
1. צור אובייקט [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) באמצעות אובייקטי העמוד ו[מלבן](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. הגדר את תכונות הקישור באמצעות אובייקט [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. הגדר את תכונת ה-Action לאובייקט [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1. הוסף את הקישור לאוסף ההערות של אובייקט הדף.
1. שמור את ה-PDF המעודכן באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) של אובייקט המסמך.

הקטע הבא מראה כיצד ליצור קישור למסמך PDF בקובץ PDF.

 ```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// פתח מסמך
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// צור קישור
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// שמור מסמך מעודכן
document.Save(dataDir);
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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "אנגלית"
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

