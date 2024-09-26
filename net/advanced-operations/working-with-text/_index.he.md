---
title: עבודה עם טקסט ב-PDF באמצעות C#
linktitle: עבודה עם טקסט
type: docs
weight: 30
url: /net/working-with-text/
description: פרק זה מסביר שיטות שונות של טיפול בטקסט. למד כיצד להוסיף, להחליף, לסובב, ולחפש טקסט באמצעות Aspose.PDF ו-C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם טקסט ב-PDF באמצעות C#",
    "alternativeHeadline": "הוספה, סיבוב, חיפוש ומחיקת טקסט בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "ייצור מסמכי PDF",
    "keywords": "pdf, c#, הוספת טקסט, חיפוש טקסט, מחיקת טקסט, ניהול טקסט ב-pdf",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מסביר שיטות שונות של טיפול בטקסט. למד כיצד להוסיף, להחליף, לסובב, ולחפש טקסט באמצעות Aspose.PDF ו-C#."
}
</script>

כולנו לפעמים צריכים להוסיף טקסט לקובץ PDF. לדוגמה, כאשר אתה רוצה להוסיף תרגום מתחת לטקסט הראשי, למקם כיתוב ליד תמונה, או פשוט למלא טופס בקשה. זה גם מועיל אם ניתן לעצב את כל אלמנטי הטקסט בסגנון הרצוי שלך. השימושים הפופולריים ביותר בניהול טקסט בקובץ PDF שלך הם: הוספת טקסט ל-PDF, עיצוב טקסט בתוך קובץ PDF, החלפה וסיבוב טקסט במסמך שלך. **Aspose.PDF for .NET** הוא הפתרון הטוב ביותר שיש לו הכל כדי להתמודד עם תוכן PDF.

אתה יכול לבצע את הפעולות הבאות:

- [הוספת טקסט לקובץ PDF](/pdf/net/add-text-to-pdf-file/) - הוסף טקסט ל-PDF שלך, השתמש בגופנים מזרם וקבצים, הוסף מחרוזת HTML, הוסף קישור כלשהו, ועוד.
- [טיפ ל-PDF](/pdf/net/pdf-tooltip/) - תוכל להוסיף טיפ לטקסט שחיפשת על ידי הוספת כפתור בלתי נראה באמצעות C#.
- [עיצוב טקסט בתוך PDF](/pdf/net/text-formatting-inside-pdf/) - תכונות רבות שתוכל להוסיף למסמך שלך בעת עיצוב הטקסט בתוכו.
- [עיצוב טקסט בתוך PDF](/pdf/net/text-formatting-inside-pdf/) - מגוון תכונות שתוכל להוסיף למסמך שלך בעת עיצוב הטקסט בתוכו.
- [החלפת טקסט ב-PDF](/pdf/net/replace-text-in-pdf/) - להחליף טקסט בכל הדפים של מסמך PDF. תחילה עליך להשתמש ב-TextFragmentAbsorber.
- [סיבוב טקסט בתוך PDF](/pdf/net/rotate-text-inside-pdf/) - סובב טקסט בתוך PDF באמצעות תכונת הסיבוב של מחלקת TextFragment.
- [חיפוש וקבלת טקסט מדפי מסמך PDF](/pdf/net/search-and-get-text-from-pdf/) - תוכל להשתמש במחלקת TextFragmentAbsorber לחיפוש וקבלת טקסט מדפים.
- [קביעת שבירת שורה](/pdf/net/determine-line-break/) - הנושא מסביר כיצד לעקוב אחר שבירת שורות של קטעי טקסט מרובי שורות.

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

