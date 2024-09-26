---
title: Working with Image Placement
linktitle: Working with Image Placement
type: docs
weight: 50
url: /net/working-with-image-placement/
description: פרק זה מתאר את התכונות של עבודה עם מיקום תמונה בקובץ PDF באמצעות ספריית C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Image Placement",
    "alternativeHeadline": "How to get the position of an Image in PDF File",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, image placement in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/working-with-image-placement/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-image-placement/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מתאר את התכונות של עבודה עם מיקום תמונה בקובץ PDF באמצעות ספריית C#."
}
</script>
עם השקת Aspose.PDF עבור .NET 7.0.0, הצגנו מחלקות בשם [ImagePlacement](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber) ו-[ImagePlacementCollection](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection) שמספקות יכולות דומות כמו המחלקות שתוארו למעלה כדי לקבל את רזולוציית התמונה והמיקום שלה במסמך PDF.

- ImagePlacementAbsorber מבצע חיפוש שימוש בתמונה כאוסף אובייקטים של ImagePlacement.
- ImagePlacement מספק את המשתנים Resolution ו-Rectangle שמחזירים את ערכי המיקום האמיתיים של התמונה.

הקטע קוד הבא עובד גם עם ממשק גרפי חדש של [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// טעינת מסמך PDF המקורי
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "ImagePlacement.pdf");
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// טעינת תוכן העמוד הראשון
doc.Pages[1].Accept(abs);
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // קבלת מאפייני התמונה
    Console.Out.WriteLine("רוחב תמונה:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("גובה תמונה:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("רזולוציה אופקית של תמונה:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("רזולוציה אנכית של תמונה:" + imagePlacement.Resolution.Y);

    // אחזור תמונה עם ממדים נראים
    Bitmap scaledImage;
    using (MemoryStream imageStream = new MemoryStream())
    {
        // אחזור תמונה ממשאבים
        imagePlacement.Image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Png);
        Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
        // יצירת תמונת bitmap עם הממדים האמיתיים
        scaledImage = new Bitmap(resourceImage, (int)imagePlacement.Rectangle.Width, (int)imagePlacement.Rectangle.Height);
    }
}
```

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
                "areaServed": "ארה\"ב",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
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
```

