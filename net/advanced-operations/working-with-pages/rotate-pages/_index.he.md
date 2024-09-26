---
title: סיבוב דפי PDF באמצעות C#
linktitle: סיבוב דפי PDF
type: docs
weight: 50
url: /net/rotate-pages/
description: נושא זה מתאר איך לסובב את כיוון הדף בקובץ PDF קיים באופן תכנותי ב-C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "סיבוב דפי PDF באמצעות C#",
    "alternativeHeadline": "איך לסובב דפי PDF עם .NET",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, סיבוב דף pdf",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכים של Aspose.PDF",
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
    "url": "/net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "נושא זה מתאר איך לסובב את כיוון הדף בקובץ PDF קיים באופן תכנותי ב-C#."
}
</script>
נושא זה מתאר כיצד לעדכן או לשנות את כיוון הדף של דפים בקובץ PDF קיים באופן תכנותי ב-C#.

הקטע קוד שלהלן עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## שינוי כיוון הדף

משחרור Aspose.PDF עבור .NET 9.6.0, הוספנו תכונות חדשות נהדרות כמו שינוי כיוון הדף מנוף לדיוקן ולהפך. לשינוי כיוון הדף, הגדר את תיבת המדיה של הדף באמצעות הקטע קוד הבא. ניתן גם לשנות את כיוון הדף על ידי הגדרת זווית סיבוב באמצעות שיטת Rotate().

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-ChangeOrientation-ChangeOrientation.cs" >}}

## התאמת תוכן הדף לכיוון הדף החדש

שים לב שכאשר משתמשים בקטע הקוד שלעיל, חלק מתוכן המסמך עשוי להיחתך מכיוון שגובה הדף מופחת. כדי למנוע זאת, הגדל את הרוחב באופן פרופורציונלי והשאר את הגובה ללא שינוי. דוגמה לחישובים:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-FitPageContents-FitPageContents.cs" >}}
{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-FitPageContents-FitPageContents.cs" >}}

בנוסף לגישה שלעיל, שקול להשתמש בממשק ה-PdfPageEditor שיכול להחיל זום על תוכן הדף.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-ZoomToPageContents-ZoomToPageContents.cs" >}}

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

