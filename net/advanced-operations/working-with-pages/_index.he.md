---
title: עבודה עם דפים ב-PDF ב-C#
linktitle: עבודה עם דפים
type: docs
weight: 20
url: /net/working-with-pages/
description: כיצד להוסיף דפים, להוסיף כותרות עליונות ותחתונות, להוסיף סימני מים תוכלו לדעת בחלק זה. Aspose.PDF עבור .NET מסבירה לכם את כל הפרטים בנושא זה.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם דפים ב-PDF ב-C#",
    "alternativeHeadline": "כיצד לעבוד עם דפי PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, דף pdf, הוספת דף pdf, הוספת מספר דף, סיבוב דף, מחיקת דף",
    "wordcount": "302",
    "proficiencyLevel":"מתחילים",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "כיצד להוסיף דפים, להוסיף כותרות עליונות ותחתונות, להוסיף סימני מים תוכלו לדעת בחלק זה. Aspose.PDF עבור .NET מסבירה לכם את כל הפרטים בנושא זה."
}
</script>
**Aspose.PDF for .NET** מאפשר לך להוסיף דף למסמך PDF בכל מיקום בקובץ כמו גם להוסיף דפים לסוף קובץ PDF. סעיף זה מראה כיצד להוסיף דפים ל-PDF ללא Acrobat Reader.
תוכל להוסיף טקסט או תמונות בכותרות עליונות ותחתונות של קובץ ה-PDF שלך, ולבחור כותרות שונות במסמך שלך עם ספריית C# מבית Aspose.
כמו כן, נסה לחתוך דפים במסמך PDF באופן תכנותי באמצעות C#.

סעיף זה ילמד אותך כיצד להוסיף סימני מים בקובץ ה-PDF שלך באמצעות מחלקת Artifact. תבדוק את דוגמת התכנות למשימה זו.
הוסף מספר עמוד באמצעות מחלקת PageNumberStamp. להוספת חותמת במסמך שלך השתמש במחלקות ImageStamp ו-TextStamp. השתמש בהוספת סימן מים ליצירת תמונות רקע בקובץ ה-PDF שלך עם **Aspose.PDF for .NET**.

אתה מסוגל לבצע את הפעולות הבאות:

- [הוספת דפים](/pdf/net/add-pages/) - הוסף דפים במיקום הרצוי או לסוף קובץ PDF ומחק דף מהמסמך שלך.
- [העברת דפים](/pdf/net/move-pages/) - העבר דפים ממסמך אחד למשנהו.
- [העברת דפים](/pdf/net/move-pages/) - העברת דפים ממסמך אחד למסמך אחר.
- [מחיקת דפים](/pdf/net/delete-pages/) - מחיקת דף מקובץ PDF שלך באמצעות אוסף PageCollection.
- [שינוי גודל דף](/pdf/net/change-page-size/) - ניתן לשנות את גודל דף PDF באמצעות קטע קוד בשימוש בספריית Aspose.PDF.
- [סיבוב דפים](/pdf/net/rotate-pages/) - ניתן לשנות את כיוון הדפים בקובץ PDF קיים.
- [פיצול דפים](/pdf/net/split-document/) - ניתן לפצל קבצי PDF לקובץ אחד או יותר.
- [הוספת כותרות עליונות ו/או תחתונות](/pdf/net/add-headers-and-footers-of-pdf-file/) - הוספת טקסט או תמונות בכותרות העליונות והתחתונות של קובץ PDF שלך.
- [חיתוך דפים](/pdf/net/crop-pages/) - ניתן לחתוך דפים במסמך PDF באופן תכנותי עם מאפייני דף שונים.
- [הוספת סימני מים](/pdf/net/add-watermarks/) - הוספת סימני מים בקובץ PDF שלך באמצעות מחלקת Artifact.
- [הוספת מספור דפים בקובץ PDF](/pdf/net/add-page-number/) - מחלקת PageNumberStamp תעזור לך להוסיף מספר דף בקובץ PDF שלך.
- [הוספת מספור עמודים בקובץ PDF](/pdf/net/add-page-number/) - מחלקת PageNumberStamp תעזור לך להוסיף מספר עמוד בקובץ PDF שלך.
- [הוספת רקעים](/pdf/net/add-backgrounds/) - ניתן להשתמש בתמונות רקע כדי להוסיף סימן מים.
- [חותמות](/pdf/net/stamping/) - תוכל להשתמש במחלקת ImageStamp כדי להוסיף חותמת תמונה לקובץ PDF ובמחלקת TextStamp להוספת טקסט.

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


