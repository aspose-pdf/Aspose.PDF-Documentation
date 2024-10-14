---
title: החלפת תמונה בקובץ PDF קיים
linktitle: החלפת תמונה
type: docs
weight: 70
url: /net/replace-image-in-existing-pdf-file/
description: פרק זה מתאר את החלפת תמונה בקובץ PDF קיים באמצעות ספריית C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "החלפת תמונה בקובץ PDF קיים",
    "alternativeHeadline": "כיצד להחליף תמונה ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, dotnet, החלפת תמונה ב-pdf",
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
    "url": "/net/replace-image-in-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-image-in-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מתאר את החלפת תמונה בקובץ PDF קיים באמצעות ספריית C#."
}
</script>
הקטע הבא של קוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

שיטת [Replace](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection/methods/replace/index) של אוסף התמונות מאפשרת לך להחליף תמונה בקובץ PDF קיים.

ניתן למצוא את אוסף התמונות באוסף המשאבים של דף. כדי להחליף תמונה:

1. פתח את קובץ ה-PDF באמצעות האובייקט Document.
2. החלף תמונה מסוימת, שמור את קובץ ה-PDF המעודכן באמצעות שיטת Save של האובייקט Document.

הקטע הבא של קוד מראה לך כיצד להחליף תמונה בקובץ PDF.

```csharp
// פתח מסמך
Document pdfDocument = new Document("input.pdf");
// החלף תמונה מסוימת
pdfDocument.Pages[1].Resources.Images.Replace(1, new FileStream("lovely.jpg", FileMode.Open));
// שמור את קובץ ה-PDF המעודכן
pdfDocument.Save("output.pdf");
```

