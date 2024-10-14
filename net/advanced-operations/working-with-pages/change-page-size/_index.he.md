---
title: שינוי גודל דף PDF ב-C#
linktitle: שינוי גודל דף PDF
type: docs
weight: 40
url: /net/change-page-size/
description: שינוי גודל דף מתוך מסמך PDF באמצעות ספריית Aspose.PDF ל-.NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "שינוי גודל דף PDF ב-C#",
    "alternativeHeadline": "שינוי גודל דף PDF ב-.NET",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, שינוי גודל pdf, שינוי גודל pdf",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "שינוי גודל דף מתוך מסמך PDF באמצעות ספריית Aspose.PDF ל-.NET"
}
</script>

## שינוי גודל עמוד PDF

Aspose.PDF עבור .NET מאפשר לך לשנות את גודל עמוד PDF באמצעות קוד פשוט ביישומי .NET שלך. נושא זה מסביר כיצד לעדכן/לשנות את ממדי העמוד (גודל) של קובץ PDF קיים.

הקטע קוד הבא פועל גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

המחלקה [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) מכילה את המתודה SetPageSize(...) המאפשרת לך לקבוע את גודל העמוד. הקטע קוד להלן מעדכן את ממדי העמוד בכמה שלבים פשוטים:

1. טען את קובץ ה-PDF המקורי.
1. השג את העמודים לתוך אובייקט [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. קבל עמוד נתון.
1. קרא למתודת SetPageSize(..) כדי לעדכן את ממדיו.
1. קרא למתודת Save(..) של מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) כדי ליצור קובץ PDF עם ממדי עמוד מעודכנים.

{{% alert color="primary" %}}

שים לב שתכונות הגובה והרוחב משתמשות בנקודות כיחידת בסיס, שבה 1 אינץ' = 72 נקודות ו-1 ס"מ = 1/2.54 אינץ' = 0.3937 אינץ' = 28.3 נקודות.
שימו לב שתכונות הגובה והרוחב משתמשות בנקודות כיחידת בסיס, שם 1 אינץ' = 72 נקודות ו-1 ס"מ = 1/2.54 אינץ' = 0.3937 אינץ' = 28.3 נקודות.

{{% /alert %}}

הקטע הבא מראה איך לשנות את ממדי דף ה-PDF לגודל A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## קבלת גודל דף PDF

ניתן לקרוא את גודל דף של קובץ PDF קיים באמצעות Aspose.PDF עבור .NET. הדוגמה הבאה מראה איך לקרוא את ממדי דף ה-PDF באמצעות C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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

