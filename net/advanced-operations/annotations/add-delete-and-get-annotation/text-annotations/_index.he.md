---
title: שימוש בסימון טקסט למסמך PDF
linktitle: סימון טקסט
type: docs
weight: 10
url: /net/text-annotation/
description: Aspose.PDF עבור .NET מאפשר לך להוסיף, לקבל ולמחוק סימון טקסט ממסמך PDF שלך.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "שימוש בסימון טקסט למסמך PDF",
    "alternativeHeadline": "איך להוסיף סימון טקסט ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, סימון טקסט",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך להוסיף, לקבל ולמחוק סימון טקסט ממסמך PDF שלך."
}
</script>
## כיצד להוסיף אנוטציה של טקסט לקובץ PDF קיים

הקטע קוד שלהלן עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

אנוטציה של טקסט היא אנוטציה המחוברת למיקום מסוים במסמך PDF. כאשר היא סגורה, האנוטציה מוצגת כסמל; כאשר היא נפתחת, היא אמורה להציג חלון קופץ המכיל את טקסט ההערה בגופן ובגודל שנבחרו על ידי הקורא.

האנוטציות מכילות את אוסף [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) של עמוד מסוים. אוסף זה מכיל את האנוטציות עבור אותו עמוד בלבד; לכל עמוד יש אוסף Annotations משלו.

כדי להוסיף אנוטציה לעמוד מסוים, הוסף אותה לאוסף Annotations של אותו עמוד באמצעות השיטה [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. תחילה, צור אנוטציה שברצונך להוסיף לקובץ PDF.
1. לאחר מכן פתח את קובץ PDF הקיים.
1.
1.

הקטע הקוד הבא מראה לך איך להוסיף אנוטציה בדף PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// צור אנוטציה
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "כותרת אנוטציה לדוגמה";
textAnnotation.Subject = "נושא לדוגמה";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "תוכן לדוגמה לאנוטציה";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// הוסף אנוטציה לאוסף האנוטציות של הדף
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// שמור קובץ פלט
pdfDocument.Save(dataDir);
```
## איך להוסיף הערה קופצת

הערה קופצת מציגה טקסט בחלון קופץ לצורך קליטה ועריכה. היא לא תופיע לבד אלא בשילוב עם הערה מסומנת, ההערה האב שלה, ותשמש לעריכת טקסט האב.

לא תהיה לה מראה זרימתי או פעולות משויכות משלה ותזוהה על ידי הערך Popup במילון ההערה של ההורה.

הקטע קוד הבא מראה איך להוסיף [הערה קופצת](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) בדף PDF באמצעות דוגמה להוספת [הערת קו](/pdf/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) של ההורה.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // נתיב לתיקיית המסמכים
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // טעינת קובץ ה-PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // יצירת הערת קו
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // הוספת הערה לדף
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## איך להוסיף (או ליצור) אנוטציה חופשית של טקסט

אנוטציית טקסט חופשית מציגה טקסט ישירות על הדף. השיטה [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) מאפשרת ליצור אנוטציה מסוג זה. בקטע הבא, אנו מוסיפים אנוטציה חופשית של טקסט מעל המופע הראשון של המחרוזת.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### הגדרת תכונת קריאה לאנוטציה חופשית של טקסט
### קביעת תכונת Callout ל-FreeTextAnnotation

לקונפיגורציה גמישה יותר של הערות במסמך PDF, Aspose.PDF עבור .NET מספקת תכונת [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) של מחלקת [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) המאפשרת לציין מערך של נקודות של קו הקריאה. קטע הקוד הבא מראה כיצד להשתמש בפונקציונליות זו:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### הגדרת תכונת Callout עבור קובץ XFDF

אם אתה משתמש בייבוא מקובץ XFDF אנא השתמש בשם callout-line במקום רק Callout. קטע הקוד הבא מראה איך להשתמש בפונקציונליות זו:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document( dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

השיטה הבאה משמשת ליצירת XFDF:

```csharp
/// <summary>
/// יצירת XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">זהו דוגמה</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### הפוך אנוטציית טקסט חופשי לבלתי נראית

לעיתים, יש צורך ליצור סימן מים שאינו נראה במסמך כאשר מצפים בו אך צריך להיות נראה כאשר המסמך מודפס. השתמש בדגלי אנוטציה למטרה זו. קטע הקוד הבא מראה איך לעשות זאת.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// שמור קובץ פלט
doc.Save(dataDir);
```
### הגדרת עיצוב של הערת טקסט חופשי

חלק זה בוחן איך לעצב את הטקסט בהערת טקסט חופשי.

הערות מכילות באוסף [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) של אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). בעת הוספת [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) למסמך PDF, ניתן לציין את המידע על העיצוב כגון גופן, גודל, צבע וכו' באמצעות מחלקת [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). כמו כן, ניתן לציין את המידע על העיצוב באמצעות מאפיין ה-TextStyle. יתרה מכך, ניתן לעדכן את עיצוב של כל FreeTextAnnotation שכבר נמצא במסמך PDF.

מחלקת [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) תומכת בעבודה עם ערך הסגנון המוגדר כברירת מחדל.
המחלקה [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) תומכת בעבודה עם ערך סגנון ברירת המחדל.

- המאפיין FontName מאחזר או מגדיר את שם הגופן (string).
- המאפיין FontSize מאחזר ומגדיר את גודל הטקסט המוגדר כברירת מחדל (double).
- המאפיין System.Drawing.Color מאחזר ומגדיר את צבע הטקסט (color).
- המאפיין TextAlignment מאחזר ומגדיר את יישור הטקסט של ההערה (alignment).

הקטע קוד הבא מראה כיצד להוסיף FreeTextAnnotation עם עיצוב טקסט מסוים.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

כאשר אתה משנה את התוכן או סגנון הטקסט של הערת טקסט חופשי, מראה ההערה מתחדש כדי לשקף את השינויים.

{{% /alert %}}

### קו חוצה מילים באמצעות StrikeOutAnnotation

Aspose.PDF עבור .NET מאפשר לך להוסיף, למחוק ולעדכן הערות במסמכי PDF.
Aspose.PDF for .NET מאפשר לך להוסיף, למחוק ולעדכן הערות במסמכי PDF.

לקו החוצה קטע טקסט מסוים:

1. חפש קטע טקסט בקובץ PDF.
1. קבל את קואורדינטות אובייקט קטע הטקסט.
1. השתמש בקואורדינטות כדי ליצור אובייקט StrikeOutAnnotation.

הקטע קוד הבא מראה איך לחפש קטע טקסט מסוים ולהוסיף לו StrikeOutAnnotation.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

תכונה זו נתמכת על ידי גרסה 19.6 או גבוהה יותר.

{{% /alert %}}

## מחק את כל ההערות מדף של קובץ PDF

אוסף [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) של אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) מכיל את כל ההערות עבור הדף המסוים הזה.
אובייקט [דף](https://reference.aspose.com/pdf/net/aspose.pdf/page) כולל אוסף של [אוסף הערות](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) שמכיל את כל ההערות לאותו דף מסוים.

הקטע קוד הבא מראה איך למחוק את כל ההערות מדף מסוים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// מחיקת הערה מסוימת
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// שמירת המסמך המעודכן
pdfDocument.Save(dataDir);
```

## מחיקת הערה מסוימת מקובץ PDF

{{% alert color="primary" %}}

ניתן לבדוק את איכות Aspose.PDF ולקבל את התוצאות באופן מקוון בקישור הבא:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF מאפשר לך להסיר אנוטציה מסוימת מקובץ PDF. נושא זה מסביר איך לעשות זאת.

כדי למחוק אנוטציה מסוימת מקובץ PDF, קרא לשיטת המחיקה של אוסף [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). אוסף זה שייך לאובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). שיטת המחיקה דורשת את האינדקס של האנוטציה שברצונך למחוק. לאחר מכן, שמור את קובץ ה-PDF המעודכן. קטע הקוד הבא מראה איך למחוק אנוטציה מסוימת.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// מחק אנוטציה מסוימת
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// שמור מסמך מעודכן
pdfDocument.Save(dataDir);
```
## קבל את כל ההערות מדף של מסמך PDF

Aspose.PDF מאפשר לך לקבל הערות ממסמך שלם, או מדף נתון. כדי לקבל את כל ההערות מהדף במסמך PDF, עבור על אוסף [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) של משאבי הדף הרצוי. קטע הקוד הבא מראה לך איך לקבל את כל ההערות של דף.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// עבור על כל ההערות
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // קבל את תכונות ההערה
    Console.WriteLine("כותרת : {0} ", annotation.Title);
    Console.WriteLine("נושא : {0} ", annotation.Subject);
    Console.WriteLine("תוכן : {0} ", annotation.Contents);
}
```
שימו לב שכדי לקבל את כל ההערות מכל ה-PDF, עליכם לעבור על אוסף המחלקות של PageCollection של המסמך לפני שתנווטו דרך אוסף המחלקות של AnnotationCollection. ניתן לקבל כל הערה מאוסף ההערות בסוג בסיס של הערה הנקראת מחלקת MarkupAnnotation ולאחר מכן להציג את התכונות שלה.

## קבלת הערה מסוימת מקובץ PDF

הערות משויכות לדפים פרטיים ומאוחסנות באוסף של [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) של אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

הערות מקושרות לדפים יחידים ושמורות באוסף [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) של אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// קבל הערה מסוימת
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// קבל תכונות ההערה
Console.WriteLine("Title : {0} ", textAnnotation.Title);
Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
```

## קבל משאב של הערה

Aspose.PDF מאפשר לך לקבל משאב של הערה ממסמך שלם או מדף נתון.
Aspose.PDF מאפשר לך לקבל משאב של אנוטציה ממסמך שלם או מדף נתון.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document doc = new Document(dataDir + "AddAnnotation.pdf");
// צור אנוטציה
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// שמור מסמך
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// פתח מסמך
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

// קבל את פעולת האנוטציה
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

// קבל את ההצגה של פעולת ההצגה
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

// מדיה קליפ
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
// נתוני המדיה נגישים בFileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
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

