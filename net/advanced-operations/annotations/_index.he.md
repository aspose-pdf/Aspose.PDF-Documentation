---
title: עבודה עם הערות 
linktitle: הערות ב-PDF
type: docs
weight: 100
url: /net/annotations/
description: סעיף זה מציג כיצד להשתמש בכל סוגי ההערות לקובץ PDF שלך באמצעות ספריית Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-annotations/
    - /net/annotation/
    - /net/working-with-annotations-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הערות PDF",
    "alternativeHeadline": "עבודה עם הערות ב-PDFs",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "ייצור מסמכי PDF",
    "keywords": "pdf, c#, annotations",
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
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "סעיף זה מציג כיצד להשתמש בכל סוגי ההערות לקובץ PDF שלך באמצעות ספריית Aspose.PDF."
}
</script>
תוכן שבתוך דף PDF קשה לעריכה, אך מפרט ה-PDF מגדיר קבוצה מלאה של אובייקטים שניתן להוסיף לדפי PDF ללא שינוי תוכן הדף.

אובייקטים אלו נקראים הערות, ומטרתם נעה מסימון תוכן דף ועד ליישום תכונות אינטראקטיביות כמו טפסים.

תוכנות צפייה ב-PDF בדרך כלל מאפשרות יצירה ועריכה של סוגים שונים של הערות, לדוגמה הדגשת טקסטים, הערות, קווים או צורות. ללא תלות בסוגי ההערות שניתן ליצור, תוכנות צפייה התואמות למפרט ה-PDF צריכות גם לתמוך בעיבוד של כל סוגי ההערות.

הערה היא חלק חשוב בקובץ PDF. באמצעות Aspose.PDF עבור .NET ניתן להוסיף הערה חדשה, לערוך הערה קיימת ולמחוק הערות וכדומה. בפרק זה מכוסה הנושא הבא:

אתה יכול לבצע את הפעולות הבאות:

- [סקירה כללית של הערות](/pdf/net/overview-of-annotations/) - למד אילו סוגים של הערות מוגדרות על ידי מפרט ה-PDF, ומה Aspose.PDF תומך.
- [הוספה, מחיקה וקבלת הערה](/pdf/net/add-delete-and-get-annotation/) - בפרק זה מוסבר כיצד לעבוד עם כל סוגי ההערות המותרים.
- [הוספה, מחיקה וקבלת אנוטציה](/pdf/net/add-delete-and-get-annotation/) - פרק זה מסביר כיצד לעבוד עם כל סוגי האנוטציות המותרות.
- [יבוא ויצוא של אנוטציה בפורמט XFDF](/pdf/net/import-export-xfdf/) - ספריית Aspose.PDF מספקת שיטות ליבוא ויצוא נתוני אנוטציות לקבצי XFDF.

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


