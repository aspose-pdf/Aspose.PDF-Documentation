---
title: עבודה עם AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /net/acroforms/
description: עם Aspose.PDF עבור .NET תוכל ליצור טופס מאפס, למלא שדה טופס במסמך PDF, לחלץ נתונים מהטופס וכו'.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם AcroForms",
    "alternativeHeadline": "אפשרויות לעבודה עם AcroForms ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, acroforms in pdf",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "עם Aspose.PDF עבור .NET תוכל ליצור טופס מאפס, למלא שדה טופס במסמך PDF, לחלץ נתונים מהטופס וכו'."
}
</script>
## עקרונות בסיסיים של AcroForms

**AcroForms** הם טכנולוגיית הטפסים המקורית של PDF. AcroForms הם טופס מבוסס דפים. הם הוצגו לראשונה ב-1998. הם מקבלים קלט בפורמט נתוני טופס או FDF ופורמט נתוני טופס XML או xFDF. ספקים צד שלישי תומכים ב-AcroForms. כאשר Adobe הציגה את ה-AcroForms, הם כינו אותם "טופס PDF שנוצר עם Adobe Acrobat Pro/Standard ואינו סוג מיוחד של טופס XFA סטטי או דינמי. Acroforms הם ניידים והם עובדים בכל הפלטפורמות.

ניתן להשתמש ב-AcroForms כדי להוסיף דפים נוספים למסמך טופס PDF. בזכות המושג של תבניות, ניתן להשתמש ב-AcroForms לתמיכה במילוי הטופס עם מספר רשומות מסד נתונים.

PDF 1.7 תומך בשני שיטות שונות לשילוב נתונים וטפסי PDF.

*AcroForms (ידועים גם כטפסי Acrobat)*, הוצגו וכלולים במפרט התצורה של PDF 1.2.

*Adobe XML Forms Architecture (XFA) forms*, הוצגו במפרט התצורה של PDF 1.5 כתכונה אופציונלית (מפרט ה-XFA אינו כלול במפרט ה-PDF, הוא רק מתייחס).
*Adobe XML Forms Architecture (XFA) forms*, הוצגו במפרט פורמט PDF 1.5 כתכונה אופציונלית (מפרט ה-XFA אינו כלול במפרט ה-PDF, הוא רק מתואר בו.

כדי להבין את **Acroforms** לעומת **XFA** עלינו להבין קודם את היסודות. לשם כך, שניהם הם טפסי PDF שניתן להשתמש בהם. Acroforms הוא הישן יותר, שנוצר ב-1998, ועדיין מתייחסים אליו כאל טופס PDF קלאסי. טפסי XFA הם דפי אינטרנט שניתן לשמור כ-PDF, והופיעו ב-2003. לקח זמן מה לפני ש-PDF התחיל לקבל טפסי XFA.

ל-AcroForms יש יכולות שלא נמצאות ב-XFA ולהפך, ל-XFA יש כמה יכולות שלא נמצאות ב-AcroForms. לדוגמה:

- AcroForms תומך במושג של "תבניות", המאפשר הוספת דפים נוספים למסמך טופס PDF כדי לתמוך במילוי הטופס עם מספר רשומות ממסד נתונים.
- XFA תומך במושג של זרימת מסמך מחדש המאפשר לשדה להתאים את גודלו במידת הצורך כדי להכיל נתונים.

למידע מפורט יותר על יכולות של ספריית ה-Java, ראה את המאמרים הבאים:
למידה מפורטת יותר על היכולות של ספריית ה-Java, ראה את המאמרים הבאים:

- [יצירת AcroForm](/pdf/net/create-form) - יצירת טופס מאפס באמצעות C#.
- [מילוי AcroForm](/pdf/net/fill-form) - מילוי שדה טופס במסמך PDF שלך.
- [חילוץ AcroForm](/pdf/net/extract-form) - קבלת ערך מכל שדה או משדה יחיד במסמך PDF.
- [שינוי AcroForm](/pdf/net/modifing-form) - קבלה או הגדרה של FieldLimit, הגדרת גופן שדה הטופס וכו'.
- [שליחת נתוני AcroForm](/pdf/net/posting-acroform-data/) - ייבוא ויצוא נתוני טופס לקובץ XML וממנו.
- [יבוא ויצוא נתונים](/pdf/net/import-and-export-data/) - יבוא ויצוא נתונים באמצעות מחלקת הטופס.

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

