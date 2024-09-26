---
title: קבל את הרזולוציה והמידות של תמונות
linktitle: קבל את הרזולוציה והמידות
type: docs
weight: 40
url: /net/get-resolution-and-dimensions-of-embedded-images/
description: פרק זה מציג פרטים בקבלת רזולוציה ומידות של תמונות מוטבעות
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "קבל את הרזולוציה והמידות של תמונות",
    "alternativeHeadline": "איך לקבל רזולוציה ומידות של תמונות מוטבעות",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, קבל רזולוציה, קבל מידות",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מציג פרטים בקבלת רזולוציה ומידות של תמונות מוטבעות"
}
</script>
הקטע הבא בקוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

נושא זה מסביר כיצד להשתמש במחלקות האופרטור במרחב השמות Aspose.PDF שמספקות את היכולת לקבל מידע על רזולוציה ומידות של תמונות מבלי להוציא אותן.

ישנן דרכים שונות להשיג זאת. מאמר זה מסביר כיצד להשתמש ב-`arraylist` וב[מחלקות הצבת תמונה](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. ראשית, טען את קובץ ה-PDF המקורי (עם תמונות).
1. לאחר מכן צור אובייקט ArrayList לאחסון שמות התמונות במסמך.
1. קבל את התמונות באמצעות התכונה Page.Resources.Images.
1. צור אובייקט מחסנית כדי לאחסן את מצב הגרפיקה של התמונה והשתמש בו כדי לעקוב אחר מצבי תמונה שונים.
1.
1. מכיוון שאנו יכולים לשנות את המטריצה באמצעות ConcatenateMatrix, ייתכן שנצטרך גם לחזור למצב התמונה המקורי. השתמש באופרטורים GSave ו-GRestore. אופרטורים אלה מזוגגים ולכן יש לקרוא להם יחד. לדוגמה, אם אתה עושה עבודה גרפית עם המרות מורכבות ולבסוף מחזיר את ההמרות חזרה למצב ההתחלתי, הגישה תהיה כזו:

```csharp
// צייר קצת טקסט
GSave

ConcatenateMatrix  // סובב תוכן לאחר האופרטור

// עבודה גרפית מסוימת

ConcatenateMatrix // הגדל (עם סיבוב קודם) תוכן לאחר האופרטור

// עבודה גרפית נוספת

GRestore

// צייר קצת טקסט
```

כתוצאה מכך, הטקסט נצייר בצורה רגילה אך כמה המרות מתבצעות בין אופרטורי הטקסט. כדי להציג את התמונה או לצייר פורמות אובייקטים ותמונות, אנו צריכים להשתמש באופרטור Do.

יש לנו גם מחלקה בשם XImage שמספקת שתי תכונות, רוחב וגובה, שניתן להשתמש בהן כדי לקבל ממדי תמונה.

1.
1.
1. הצג את המידע בחלון הפקודה יחד עם שם התמונה.

הקטע הבא מראה איך לקבל את ממדי התמונה ורזולוציה ללא הוצאת התמונה מהמסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// טען את קובץ ה-PDF המקורי
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// הגדר את הרזולוציה המוגדרת כברירת מחדל לתמונה
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// הגדר אובייקט מסוג רשימה שיכיל שמות תמונות
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// הוסף אובייקט למחסנית
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// קבל את כל האופרטורים בעמוד הראשון של המסמך
foreach (Operator op in doc.Pages[1].Contents)
{
    // השתמש באופרטורים GSave/GRestore כדי להחזיר את השינויים למצב שהוגדר קודם
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // צור אובייקט ConcatenateMatrix שמגדיר את מטריצת ההמרה הנוכחית.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // צור אופרטור Do שמצייר אובייקטים מהמשאבים. הוא מצייר אובייקטים של טופס ואובייקטים של תמונה
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // שמור את המצב הקודם והוסף את המצב הנוכחי לראש המחסנית
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // זרוק את המצב הנוכחי ושחזר את הקודם
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // כפול את מטריצת המצב הנוכחית עם מטריצת המצב
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // במקרה וזהו אופרטור ציור של תמונה
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // צור אובייקט XImage לאחזקת תמונות של עמוד PDF ראשון
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // קבל ממדי תמונה
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // קבל מידע על גובה ורוחב התמונה המקורית
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // חשב רזולוציה על סמך המידע לעיל
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // הצג מידע על ממד ורזולוציה של כל תמונה
            Console.Out.WriteLine(
                    string.Format(dataDir + "תמונה {0} ({1:.##}:{2:.##}): רזולוציה {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
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

