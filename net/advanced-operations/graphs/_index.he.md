---
title: עבודה עם גרפים בקובץ PDF
linktitle: עבודה עם גרפים
type: docs
weight: 70
url: /net/graphs/
description: מאמר זה מסביר מהו גרף, איך ליצור אובייקט מלבן מלא ופונקציות נוספות
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-graphs/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם גרפים בקובץ PDF",
    "alternativeHeadline": "איך ליצור גרפים ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, גרפים ב-pdf",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מסביר מהו גרף, איך ליצור אובייקט מלבן מלא ופונקציות נוספות"
}
</script>
## מהו גרף

הוספת גרפים למסמכי PDF היא משימה נפוצה מאוד עבור מפתחים בעת עבודה עם Adobe Acrobat Writer או אפליקציות אחרות לעיבוד PDF. ישנם סוגים רבים של גרפים שניתן להשתמש בהם באפליקציות PDF.
[Aspose.PDF for .NET](/pdf/net/) תומך גם בהוספת גרפים למסמכי PDF. לשם כך, מסופקת המחלקה Graph. Graph הוא אלמנט ברמת פסקה וניתן להוסיף אותו לאוסף הפסקאות במופע של עמוד. מופע של Graph מכיל אוסף של צורות.

הסוגים הבאים של צורות נתמכים על ידי מחלקת [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/net/add-arc/) - לפעמים גם נקרא דגל הוא זוג צמוד של קודקודים סמוכים, אך לעיתים גם נקרא קו מוכוון.
- [Circle](/pdf/net/add-circle/) - מציג נתונים באמצעות מעגל המחולק למגזרים. אנו משתמשים בגרף מעגל (הנקרא גם תרשים עוגה) כדי להראות כיצד נתונים מייצגים חלקים של שלם אחד או קבוצה אחת.
- [Curve](/pdf/net/add-curve/) - הוא איחוד מחובר של קווים פרויקטיביים, כל קו נפגש עם שלושה אחרים בנקודות כפולות רגילות.
- [Curve](/pdf/net/add-curve/) - היא איחוד מחובר של קווים פרויקטיביים, כל קו נפגש עם שלושה קווים אחרים בנקודות כפולות רגילות.
- [Line](/pdf/net/add-line) - גרפים של קווים משמשים להצגת נתונים רציפים ויכולים להיות שימושיים בחיזוי אירועים עתידיים כאשר הם מציגים מגמות לאורך זמן.
- [Rectangle](/pdf/net/add-rectangle/) - הוא אחד מהצורות הבסיסיות הרבות שתראה בגרפים, יכול להיות מאוד שימושי בעזרה לך לפתור בעיה.
- [Ellipse](/pdf/net/add-ellipse/) - הוא קבוצת נקודות על מישור, יוצרת צורה עגולה, מעוקלת.

הפרטים הנ"ל מוצגים גם בדמויות שלהלן:

![Figures in Graphs](graphs.png)

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

