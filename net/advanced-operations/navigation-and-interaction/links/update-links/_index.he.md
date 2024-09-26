---
title: עדכון קישורים ב-PDF
linktitle: עדכון קישורים
type: docs
weight: 20
url: /net/update-links/
description: עדכון קישורים ב-PDF באופן תכנותי. המדריך הזה עוסק באופן עדכון קישורים ב-PDF בשפת C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עדכון קישורים ב-PDF",
    "alternativeHeadline": "איך לעדכן קישורים ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, עדכון קישור ב-PDF",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "עדכון קישורים ב-PDF באופן תכנותי. המדריך הזה עוסק באופן עדכון קישורים ב-PDF בשפת C#."
}
</script>

הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## עדכון קישורים בקובץ PDF

כפי שדובר בנושא הוספת קישור היפרטקסט בקובץ PDF, המחלקה [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) מאפשרת להוסיף קישורים בקובץ PDF. ישנה גם מחלקה דומה המשמשת לאחזור קישורים קיימים מתוך קבצי PDF. השתמש בזה אם אתה צריך לעדכן קישור קיים. לעדכון קישור קיים:

1. טען קובץ PDF.
1. עבור לעמוד מסוים בקובץ PDF.
1. ציין את יעד הקישור באמצעות תכונת היעד של האובייקט [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction).
1. העמוד היעד מצוין באמצעות בנאי [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination).

### הגדרת יעד קישור לעמוד באותו מסמך

הקטע קוד הבא מראה כיצד לעדכן קישור בקובץ PDF ולהגדיר את יעדו לעמוד השני במסמך.
הקטע הבא מראה איך לעדכן קישור בקובץ PDF ולהגדיר את היעד שלו לעמוד השני של המסמך.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// טעינת קובץ ה-PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// קבלת האנוטציה הראשונה של הקישור מעמוד הראשון של המסמך
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// שינוי הקישור: שינוי יעד הקישור
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// ציון היעד לאובייקט הקישור
// הפרמטר הראשון הוא אובייקט המסמך, השני הוא מספר עמוד היעד.
// הארגומנט החמישי הוא גורם ההגדלה בעת הצגת העמוד המתאים. כאשר משתמשים ב-2, העמוד יוצג בהגדלה של 200%
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// שמירת המסמך עם הקישור המעודכן
doc.Save(dataDir);
```
### קבע יעד לקישור לכתובת אינטרנט

כדי לעדכן את הקישור כך שיצביע על כתובת אינטרנט, יש ליצור אובייקט [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) ולהעבירו לתכונת הפעולה של LinkAnnotation. קטע הקוד הבא מראה כיצד לעדכן קישור בקובץ PDF ולקבוע את מטרתו לכתובת אינטרנט.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// טען את קובץ ה-PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// קבל את הקישור הראשון מעמוד הראשון של המסמך
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// שינוי קישור: שינוי פעולת הקישור והגדרת היעד ככתובת אינטרנט
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// שמור את המסמך עם הקישור המעודכן
doc.Save(dataDir);
```
### הגדר יעד קישור לקובץ PDF אחר

הקטע קוד הבא מראה כיצד לעדכן קישור בקובץ PDF ולהגדיר את יעדו לקובץ PDF אחר.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// טען את קובץ ה-PDF
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// שורה זו מעדכנת יעד, אל תעדכן קובץ
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// שורה זו מעדכנת קובץ
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// שמור את המסמך עם הקישור המעודכן
document.Save(dataDir);
```

### עדכן צבע טקסט של LinkAnnotation

הקישור המוסבר אינו מכיל טקסט.
הקישורית אינה מכילה טקסט.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// טעינת קובץ ה-PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // חיפוש הטקסט מתחת להערה
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // שינוי צבע הטקסט.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// שמירת המסמך עם קישור מעודכן
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF עבור ספריית .NET",
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

