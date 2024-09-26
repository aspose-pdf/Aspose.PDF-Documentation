---
title: הוספת סימן מים ל-PDF באמצעות C#
linktitle: הוספת סימן מים
type: docs
weight: 90
url: /net/add-watermarks/
description: המאמר מסביר את התכונות של עבודה עם ארטיפקטים וקבלת סימני מים ב-PDF באמצעות תוכנות C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת סימן מים ל-PDF באמצעות C#",
    "alternativeHeadline": "כיצד להוסיף סימן מים ל-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הוספת סימן מים",
    "wordcount": "302",
    "proficiencyLevel":"מתחילים",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "המאמר מסביר את התכונות של עבודה עם ארטיפקטים וקבלת סימני מים ב-PDF באמצעות תוכנות C#."
}
</script>
**Aspose.PDF for .NET** מאפשר להוסיף סימני מים למסמך PDF שלך באמצעות ארטיפקטים. אנא בדוק את המאמר הזה כדי לפתור את המשימה שלך.

הקטע קוד הבא פועל גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

סימן מים שנוצר עם Adobe Acrobat נקרא ארטיפקט (כפי שמתואר ב-14.8.2.2 תוכן אמיתי וארטיפקטים של מפרט ה-PDF). כדי לעבוד עם ארטיפקטים, ל-Aspose.PDF יש שתי מחלקות: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) ו-[ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

כדי לקבל את כל הארטיפקטים בעמוד מסוים, למחלקת [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) יש את התכונה Artifacts. נושא זה מסביר כיצד לעבוד עם ארטיפקט בקבצי PDF.

## עבודה עם ארטיפקטים

המחלקה [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) מכילה את התכונות הבאות:

**Artifact.Type** – מקבל את סוג הארטיפקט (תומך בערכים של האנומרציה Artifact.ArtifactType שכוללת ערכים כמו רקע, פריסה, עמוד, עימוד ולא מוגדר).
**Artifact.Type** – מקבל את סוג הארטיפקט (תומך בערכים של המנייה Artifact.ArtifactType שכוללת את הערכים Background, Layout, Page, Pagination ו-Uncategorized).

**Artifact.Subtype** – מקבל את תת-הסוג של הארטיפקט (תומך בערכים של המנייה Artifact.ArtifactSubtype שכוללת את הערכים Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

שים לב שסימני מים שנוצרים עם Adobe Acrobat יש להם את הסוג Pagination ואת התת-סוג Watermark.

{{% /alert %}}

**Artifact.Contents** – מקבל אוסף של אופרטורים פנימיים של ארטיפקט. סוגו התומך הוא System.Collections.ICollection.
**Artifact.Form** – מקבל את XForm של ארטיפקט (אם XForm משמש). ארטיפקטים של סימן מים, כותרת עליונה ותחתונה מכילים XForm המציג את כל תוכן הארטיפקט.
**Artifact.Image** – מקבל את תמונת הארטיפקט (אם יש תמונה, אחרת null).
**Artifact.Text** – מקבל את טקסט הארטיפקט.
**Artifact.Rectangle** – מקבל את מיקום הארטיפקט בעמוד.
**Artifact.Rotation** – מקבל את סיבוב הארטיפקט (במעלות, ערך חיובי מציין סיבוב נגד כיוון השעון).
**Artifact.Rotation** – מקבל את סיבוב הארטיפקט (במעלות, ערך חיובי מציין סיבוב נגד כיוון השעון).
**Artifact.Opacity** – מקבל את אטימות הארטיפקט. הערכים האפשריים נעים בין 0 ל-1, כאשר 1 הוא לחלוטין אטום.

## דוגמאות תכנות: איך להוסיף סימן מים על קבצי PDF

הקטע הבא מראה איך להוסיף כל סימן מים בדף הראשון של קובץ PDF באמצעות C#.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF ל-.NET",
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

