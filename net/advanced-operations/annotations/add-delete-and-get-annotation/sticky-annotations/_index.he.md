---
title: סימוניות דביקות ב-PDF באמצעות C#
linktitle: סימונית דביקה
type: docs
weight: 50
url: /net/sticky-annotations/
description: נושא זה עוסק בסימוניות דביקות, כדוגמה אנו מציגים את סימונית הווטרמרק בטקסט.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "סימוניות דביקות ב-PDF באמצעות C#",
    "alternativeHeadline": "כיצד להוסיף סימוניות דביקות ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, סימוניות דביקות, סימונית ווטרמרק",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "נושא זה עוסק בסימוניות דביקות, כדוגמה אנו מציגים את סימונית הווטרמרק בטקסט."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת סימן מים

סימן מים ישמש לייצוג גרפיקה שתודפס בגודל ובמיקום קבועים בדף, ללא תלות בממדי הדף המודפס.

ניתן להוסיף טקסט סימן מים באמצעות [WatermarkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) במיקום מסוים של דף PDF. ניתן גם לשלוט על שקיפותו של סימן המים באמצעות מאפיין השקיפות.

אנא בדוק את קטע הקוד הבא להוספת WatermarkAnnotation.

```csharp
// טעינת מסמך
Aspose.PDF.Document doc = new Aspose.PDF.Document("source.pdf");

// טעינת אובייקט עמוד להוספת הערה
Page page = doc.Pages[1];

// יצירת הערה
WatermarkAnnotation wa = new WatermarkAnnotation(page, new Aspose.PDF.Rectangle(100, 500, 400, 600));

// הוספת הערה לאוסף הערות של העמוד
page.Annotations.Add(wa);

// יצירת TextState להגדרות גופן
Aspose.PDF.Text.TextState ts = new Aspose.PDF.Text.TextState();

ts.ForegroundColor = Aspose.PDF.Color.Blue;
ts.Font = FontRepository.FindFont("Times New Roman");

ts.FontSize = 32;

// הגדרת רמת שקיפות של טקסט ההערה
wa.Opacity = 0.5;
// הוספת טקסט בהערה
wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

// שמירת המסמך
doc.Save("Output.pdf");
```
## הוסף התייחסות לתמונה בודדת מספר פעמים במסמך PDF

לעיתים קרובות יש לנו דרישה להשתמש באותה תמונה כמה פעמים במסמך PDF. הוספת מופע חדש מגדילה את המסמך המתקבל. הוספנו שיטה חדשה XImageCollection.Add(XImage) ב-Aspose.PDF עבור .NET 17.1.0. שיטה זו מאפשרת להוסיף התייחסות לאותו אובייקט PDF כמו התמונה המקורית שממטבת את גודל מסמך ה-PDF.

```csharp
 Aspose.PDF.Rectangle imageRectangle = new Aspose.PDF.Rectangle(0, 0, 30, 15);

using (Aspose.PDF.Document document = new Aspose.PDF.Document("input.pdf"))
{
    using (var imageStream = File.Open("icon.png", FileMode.Open))
    {
        XImage image = null;
        foreach (Page page in document.Pages)
        {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.Rect);
            XForm form = annotation.Appearance["N"];
            form.BBox = page.Rect;
            string name;
            if (image == null)
            {
                name = form.Resources.Images.Add(imageStream);
                image = form.Resources.Images[name];
            }
            else
            {
                name = form.Resources.Images.Add(image);
            }
            form.Contents.Add(new Operator.GSave());
            form.Contents.Add(new Operator.ConcatenateMatrix(new Aspose.PDF.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
            form.Contents.Add(new Operator.Do(name));
            form.Contents.Add(new Operator.GRestore());
            page.Annotations.Add(annotation, false);
            imageRectangle = new Aspose.PDF.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
        }
    }
    document.Save("output.pdf");
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
Sure, I can help with that. However, you need to provide the document or text that you want to translate into Hebrew. Please paste the content here, and I'll translate it for you while preserving the markdown formatting.
