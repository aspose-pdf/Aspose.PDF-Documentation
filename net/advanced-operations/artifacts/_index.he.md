---
title: עבודה עם ארטיפקטים ב-.NET
linktitle: עבודה עם ארטיפקטים
type: docs
weight: 110
url: /net/artifacts/
description: Aspose.PDF עבור .NET מאפשר לך להוסיף תמונת רקע לדפי PDF, ולקבל כל סימן מים באמצעות מחלקת Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם ארטיפקטים ב-.NET",
    "alternativeHeadline": "ארטיפקטים במסמך PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, ארטיפקטים ב-pdf",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך להוסיף תמונת רקע לדפי PDF, ולקבל כל סימן מים באמצעות מחלקת Artifact."
}
</script>
ארטיפקטים ב-PDF הם עצמים גרפיים או אלמנטים אחרים שאינם חלק מהתוכן הממשי של המסמך. הם משמשים לרוב לקישוט, עיצוב או מטרות רקע. דוגמאות לארטיפקטים כוללות כותרות עמוד, כותרות תחתונות, מפרידים או תמונות שאינן מעבירות משמעות כלשהי.

המטרה של ארטיפקטים ב-PDF היא לאפשר הבחנה בין אלמנטים שהם תוכן לבין אלו שאינם. זה חשוב לנגישות, שכן קוראי מסך וטכנולוגיות עזר אחרות יכולות להתעלם מארטיפקטים ולהתמקד בתוכן הרלוונטי. ארטיפקטים יכולים גם לשפר את ביצועי המסמך ואת איכותו, שכן ניתן להשמיט אותם מהדפסה, חיפוש או העתקה.

כדי ליצור אלמנט כארטיפקט ב-PDF, עליך להשתמש במחלקת [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
היא כוללת את התכונות השימושיות הבאות:

- **Artifact.Type** – מקבל את סוג הארטיפקט (תומך בערכים של מניית Artifact.ArtifactType שכוללת ערכים כמו רקע, עיצוב, עמוד, עימוד ולא מוגדר).
- **Artifact.Type** – מקבל את סוג האובייקט (תומך בערכים של המנייה Artifact.ArtifactType שבה כוללים רקע, תבנית, דף, עימוד ולא מוגדר).
- **Artifact.Subtype** – מקבל את תת-הסוג של האובייקט (תומך בערכים של המנייה Artifact.ArtifactSubtype שבה כוללים רקע, כותרת תחתונה, כותרת עליונה, לא מוגדר, סימן מים).
- **Artifact.Image** – מקבל תמונה של אובייקט (אם קיימת תמונה, אחרת null).
- **Artifact.Text** – מקבל את הטקסט של אובייקט.
- **Artifact.Contents** – מקבל אוסף של אופרטורים פנימיים של אובייקט. הסוג הנתמך הוא System.Collections.ICollection.
- **Artifact.Form** – מקבל XForm של אובייקט (אם משתמשים ב-XForm). אובייקטים של סימן מים, כותרת עליונה, וכותרת תחתונה מכילים XForm שמציג את כל תוכן האובייקט.
- **Artifact.Rectangle** – מקבל מיקום של אובייקט בדף.
- **Artifact.Rotation** – מקבל סיבוב של אובייקט (במעלות, ערך חיובי מציין סיבוב נגד כיוון השעון).
- **Artifact.Opacity** – מקבל את האטימות של אובייקט.
- **Artifact.Opacity** – מקבל את שקיפות הארטיפקט.

הכיתות הבאות עשויות גם להיות שימושיות לעבודה עם ארטיפקטים:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## עבודה עם סימני מים קיימים

סימן מים שנוצר באמצעות Adobe Acrobat נקרא ארטיפקט (כפי שמתואר בסעיף 14.8.2.2 תוכן אמיתי וארטיפקטים של מפרט ה-PDF).

על מנת לקבל את כל סימני המים בדף מסוים, לכיתת [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) יש את התכונה Artifacts.

הקטע קוד הבא מראה איך לקבל את כל סימני המים בדף הראשון של קובץ PDF.

_Note:_ קוד זה עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).
_הערה:_ קוד זה פועל גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## עבודה עם רקעים כארטיפקטים

תמונות רקע יכולות לשמש להוספת סימן מים או עיצוב עדין אחר למסמכים. ב-Aspose.PDF עבור .NET, כל מסמך PDF הוא אוסף של דפים וכל דף מכיל אוסף של ארטיפקטים. ניתן להשתמש במחלקה [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) כדי להוסיף תמונת רקע לעצם דף.

הקטע הבא מראה כיצד להוסיף תמונת רקע לדפי PDF באמצעות האובייקט BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
אם ברצונך, מסיבה כלשהי, להשתמש ברקע בצבע אחיד, יש לשנות את הקוד הקודם באופן הבא:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## ספירת ארטיפקטים מסוג מסוים

כדי לחשב את הספירה הכוללת של ארטיפקטים מסוג מסוים (לדוגמה, מספר כולל של סימני מים), השתמש בקוד הבא:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Watermarks: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Backgrounds: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Headers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Footers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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

