---
title: שימוש באנוטציות קישור ב-PDF
linktitle: אנוטציות קישור
type: docs
weight: 70
url: /net/link-annotations/
description: Aspose.PDF עבור .NET מאפשר לך להוסיף, לקבל ולמחוק אנוטציית קישור מהמסמך PDF שלך.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "שימוש באנוטציית קישור ל-PDF",
    "alternativeHeadline": "איך להוסיף אנוטציית קישור ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, אנוטציית טקסט",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך להוסיף, לקבל ולמחוק אנוטציית טקסט מהמסמך PDF שלך."
}
</script>

## הוספת אנוטציה של קישור לקובץ PDF קיים

> הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

אנוטציית [קישור](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) מייצגת היפרקישור, יעד במקום אחר, ומסמך. לפי תקן ה-PDF, ניתן להשתמש באנוטציית קישור בשלושה מקרים: פתיחת תצוגת עמוד, פתיחת קובץ, ופתיחת דף אינטרנט.

### שימוש באנוטציית קישור לפתיחת תצוגת עמוד

בוצעו מספר צעדים נוספים כדי ליצור את האנוטציה. השתמשנו ב-2 TextFragmentAbsorbers כדי למצוא קטעים להדגמה. הראשון הוא עבור טקסט אנוטציית הקישור, והשני מצביע על מקומות מסוימים במסמך.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
כדי ליצור את האנוטציה עקבנו אחרי מספר שלבים:

1. צור `LinkAnnotation` והעבר את אובייקט הדף ואת המלבן של קטע הטקסט שמתאים לאנוטציה.
1. הגדר `Action` כ`GoToAction` והעבר `XYZExplicitDestination` כיעד המבוקש. יצרנו `XYZExplicitDestination` מבוסס על דף, קואורדינטות שמאל ולמעלה וזום.
1. הוסף את האנוטציה לאוסף האנוטציות של הדף.
1. שמור את המסמך

### שימוש ב-Link Annotation עם יעד מסוים

כאשר מעבדים מסמכים שונים, נוצרת מצב בו אתה מקליד ואינך יודע לאן תצביע האנוטציה.
במקרה זה ניתן להשתמש ביעד מיוחד (מסוים) והקוד ייראה כך:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

במקום אחר ניתן ליצור יעד מסוים.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### שימוש באנוטציית קישור לפתיחת קובץ

הגישה זהה לזו שנעשתה בעת יצירת אנוטציה לפתיחת קובץ, כפי שנראה בדוגמאות לעיל.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

ההבדל הוא שנשתמש ב `GoToRemoteAction` במקום `GoToAction`. בנאי של GoToRemoteAction מקבל שני פרמטרים: שם קובץ ומספר עמוד.
ניתן גם להשתמש בטופס אחר ולהעביר שם קובץ ויעד מסוים. ברור שעליך ליצור יעד כזה לפני שתשתמש בו.

### שימוש באנוטציית קישור לפתיחת דף אינטרנט

כדי לפתוח דף אינטרנט פשוט הגדר `Action` עם אובייקט `GoToURIAction`.
ניתן להעביר היפרלינק כפרמטר לבנאי או כל סוג אחר של URI. לדוגמה, ניתן להשתמש ב `callto` כדי ליישם פעולה עם חיוג למספר טלפון.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## הוספת עיטור להערת קישור

ניתן להתאים אישית הערת קישור באמצעות מסגרות. בדוגמה שלהלן ניצור מסגרת מקווקוות כחולה ברוחב 3 נקודות.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

דוגמה נוספת מראה כיצד לחקות סגנון דפדפן ולהשתמש בקו תחתון לקישורים.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### קבלת הערות קישור

נסה להשתמש בקטע הקוד הבא כדי לקבל הערת קישור ממסמך PDF.

```csharp
class ExampleLinkAnnotations
{
    // הנתיב לתיקיית המסמכים.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // טען את קובץ ה-PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // הדפס את כתובת ה-URL של כל הערת קישור
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // הדפס את הטקסט הקשור לקישור ההיפר
            Console.WriteLine(extractedText);
        }
    }
}
```
### מחק הערות קישור

הקטע הבא מראה איך למחוק הערת קישור מקובץ PDF. לשם כך נצטרך למצוא ולהסיר את כל הערות הקישור בעמוד הראשון. לאחר מכן נשמור את המסמך עם ההערה שהוסרה.

```csharp
class ExampleLinkAnnotations
{
    // The path to the documents directory.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // Load the PDF file
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Find and delete all link annotation on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Save document with removed annotation
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
