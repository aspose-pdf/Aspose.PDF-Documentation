---
title: עבודה עם פעולות ב-PDF
linktitle: פעולות
type: docs
weight: 20
url: /net/actions/
description: סעיף זה מסביר כיצד להוסיף פעולות למסמך ולשדות טופס תכנותית באמצעות C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם פעולות ב-PDF",
    "alternativeHeadline": "כיצד להוסיף פעולות ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנדריי אנדרוחובסקי",
        "givenName": "אנדריי",
        "familyName": "אנדרוחובסקי",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, פעולות ב-pdf",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכים של Aspose.PDF",
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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "סעיף זה מסביר כיצד להוסיף פעולות למסמך ולשדות טופס תכנותית באמצעות C#."
}
</script>
הקטע הבא בקוד פועל גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת קישור היפרטקסט בקובץ PDF

ניתן להוסיף קישורי היפרטקסט לקבצי PDF, או לאפשר לקוראים לנווט לחלק אחר ב-PDF, או לתוכן חיצוני.

כדי להוסיף קישורי אינטרנט למסמכי PDF:

1. צור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. קבל את המחלקה [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) שברצונך להוסיף לה את הקישור.
1. צור אובייקט [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) באמצעות ה-Page ואובייקטים [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). אובייקט המלבן משמש לציון מיקום הקישור בדף.
1. הגדר את מאפיין ה-Action לאובייקט [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) שמציין את מיקום ה-URI המרוחק.
1. להוסיף טקסט חופשי:

- צור אובייקט [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). הוא גם מקבל אובייקטים מסוג עמוד ומלבן כארגומנט, ולכן ניתן לספק את אותם ערכים כפי שצוינו נגד בנאי ה-LinkAnnotation.
- באמצעות תכונת ה-Contents של אובייקט ה-[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), ציין את המחרוזת שצריכה להופיע ב-PDF הסופי.
- באופציה, הגדר את רוחב הגבול של אובייקטי ה-[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) ו-FreeTextAnnotation ל-0 כדי שלא יופיעו במסמך PDF.
- לאחר שאובייקטי ה-[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) ו-[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) הוגדרו, הוסף את הקישורים הללו לאוסף ההערות של אובייקט ה-[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- לאחר שהוגדרו אובייקטים [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) ו-[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), הוסף את הקישורים האלה לאוסף ההערות של אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- לבסוף, שמור את ה-PDF המעודכן באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

הדוגמה הבאה בקוד מראה איך להוסיף קישור היפרטקסט לקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// פתח מסמך
Document document = new Document(dataDir + "AddHyperlink.pdf");
// צור קישור
Page page = document.Pages[1];
// צור אובייקט אנוטציה של קישור
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// צור אובייקט גבול לאנוטציה של קישור
Border border = new Border(link);
// הגדר את ערך רוחב הגבול כ-0
border.Width = 0;
// הגדר את הגבול לאנוטציה של קישור
link.Border = border;
// ציין את סוג הקישור כ-URI מרוחק
link.Action = new GoToURIAction("www.aspose.com");
// הוסף את אנוטציית הקישור לאוסף ההערות של דף הראשון של קובץ ה-PDF
page.Annotations.Add(link);

// צור אנוטציה של טקסט חופשי
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// מחרוזת להוספה כטקסט חופשי
textAnnotation.Contents = "קישור לאתר Aspose";
// הגדר את הגבול לאנוטציית טקסט חופשי
textAnnotation.Border = border;
// הוסף את אנוטציית הטקסט החופשי לאוסף ההערות של דף הראשון של המסמך
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// שמור את המסמך המעודכן
document.Save(dataDir);
```
## יצירת קישורים לעמודים באותו קובץ PDF

Aspose.PDF עבור .NET מספקת תכונה נהדרת ליצירת PDF וגם לשינויו. היא גם מציעה את האפשרות להוסיף קישורים לעמודי PDF וקישור יכול להפנות לעמודים בקובץ PDF אחר, לכתובת אינטרנט, להפעיל אפליקציה או אפילו לעמודים באותו קובץ PDF. כדי להוסיף קישורים מקומיים (קישורים לעמודים באותו קובץ PDF), מחלקה בשם LocalHyperlink נוספת למרחב השמות של Aspose.PDF ולמחלקה זו יש מאפיין בשם TargetPageNumber, שמשמש לציון עמוד היעד/היעד של הקישור.

כדי להוסיף את הקישור המקומי, עלינו ליצור TextFragment כך שהקישור יוכל להיות מקושר איתו. למחלקת TextFragment יש מאפיין בשם Hyperlink שמשמש לקישור מופע של LocalHyperlink. קטע הקוד הבא מראה את השלבים להשגת דרישה זו.

```csharp
// Create a document
Document doc = new Document();
// Add a page to the document
Page page1 = doc.Pages.Add();
Page page2 = doc.Pages.Add();

// Create a text fragment
TextFragment textFragment = new TextFragment("Go to Page 2");
textFragment.Position = new Position(100, 700);

// Create a local hyperlink
LocalHyperlink localHyperlink = new LocalHyperlink();
localHyperlink.TargetPageNumber = 2;

// Associate hyperlink with the text fragment
textFragment.Hyperlink = localHyperlink;

// Add text fragment to the page
page1.Paragraphs.Add(textFragment);

// Save the document
doc.Save("output.pdf");
```
```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// צור מופע של מסמך
Document doc = new Document();
// הוסף דף לאוסף הדפים של קובץ PDF
Page page = doc.Pages.Add();
// צור מופע של קטע טקסט
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("בדיקת מספר עמוד קישור לעמוד 7");
// צור מופע של קישור היפרטקסט מקומי
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// קבע את עמוד היעד למופע של הקישור
link.TargetPageNumber = 7;
// קבע את הקישור ההיפרטקסטי לקטע הטקסט
text.Hyperlink = link;
// הוסף טקסט לאוסף הפסקאות של הדף
page.Paragraphs.Add(text);
// צור מופע חדש של קטע טקסט
text = new TextFragment("בדיקת מספר עמוד קישור לעמוד 1");
// קטע הטקסט צריך להתווסף לעמוד חדש
text.IsInNewPage = true;
// צור מופע נוסף של קישור היפרטקסט מקומי
link = new LocalHyperlink();
// קבע את עמוד היעד לקישור השני
link.TargetPageNumber = 1;
// קבע את הקישור לקטע הטקסט השני
text.Hyperlink = link;
// הוסף טקסט לאוסף הפסקאות של אובייקט הדף
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// שמור את המסמך המעודכן
doc.Save(dataDir);
```
## קבל יעד של קישור PDF (URL)

קישורים מיוצגים כאנוטציות בקובץ PDF וניתן להוסיף, לעדכן או למחוק אותם. Aspose.PDF עבור .NET תומך גם בקבלת היעד (URL) של הקישור בקובץ PDF.

כדי לקבל את כתובת ה-URL של קישור:

1. צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. קבל את ה[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) שממנו אתה רוצה לחלץ קישורים.
1. השתמש במחלקת [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) כדי לחלץ את כל אובייקטי [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) מהעמוד המצוין.
1. העבר את אובייקט [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) לשיטת Accept של אובייקט ה[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

type: docs
changefreq: "monthly"
1. לבסוף, חלץ את פעולת LinkAnnotation כ-GoToURIAction.

הקטע הבא מציג כיצד לקבל יעדי קישורים (URL) מקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// טען את קובץ ה-PDF
Document document = new Document(dataDir + "input.pdf");

// עבור דרך כל עמודי ה-PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // קבל את עטיפות הקישור מעמוד מסוים
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // צור רשימה המחזיקה את כל הקישורים
    IList<Annotation> list = selector.Selected;
    // עבור על כל פריט בתוך הרשימה
    foreach (LinkAnnotation a in list)
    {
        // הדפס את כתובת ה-URL של היעד
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## קבל טקסט היפר-קישור

להיפר-קישור יש שני חלקים: הטקסט שמופיע במסמך, וכתובת ה-URL היעד. במקרים מסוימים, זהו הטקסט ולא ה-URL שאנו זקוקים לו.

טקסט והערות/פעולות בקובץ PDF מיוצגים על ידי ישויות שונות. טקסט בדף הוא רק קבוצה של מילים ותווים, בעוד שהערות מביאות עמן אינטראקטיביות מסוימת כזו הכרוכה בהיפר-קישור.

כדי למצוא את תוכן ה-URL, עליך לעבוד גם עם הערה וגם עם טקסט. אובייקט ה-[Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) אינו מחזיק בטקסט בעצמו אך נמצא מתחת לטקסט בדף. כך שכדי לקבל את הטקסט, ה-Annotation נותן את גבולות ה-URL, בעוד שאובייקט ה-Text נותן את תוכן ה-URL. נא ראה את קטע הקוד הבא.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // נתיב לתיקייה שבה מסמכים.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // טען את קובץ ה-PDF
                Document document = new Document(dataDir + "input.pdf");
                // עבור על כל דף ב-PDF
                foreach (Page page in document.Pages)
                {
                    // הצג הערת קישור
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // הדפס את כתובת ה-URL של כל הערת קישור
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // הדפס את הטקסט המקושר עם היפר-קישור
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## הסר את פעולת פתיחת המסמך מקובץ PDF

[כיצד לציין דף PDF בעת צפייה במסמך](#how-to-specify-pdf-page-when-viewing-document) הסביר כיצד להורות למסמך להיפתח בדף שונה מהראשון. כאשר משרשרים מספר מסמכים, ולאחד או יותר מהם קיימת פעולת GoTo, כנראה תרצה להסיר אותם. לדוגמה, אם משלבים שני מסמכים ולמסמך השני יש פעולת GoTo שמעבירה אותך לדף השני, המסמך המשולב ייפתח בדף השני של המסמך השני במקום בדף הראשון של המסמך המשולב. כדי למנוע התנהגות זו, הסר את פקודת פעולת הפתיחה.

כדי להסיר פעולת פתיחה:

1. הגדר את התכונה [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ל-null.
1. שמור את ה-PDF המעודכן באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) של אובייקט ה-Document.

הקטע קוד הבא מראה כיצד להסיר פעולת פתיחת מסמך מקובץ PDF:
הקטע הבא מדגים כיצד להסיר פעולת פתיחה של מסמך מקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// פתיחת מסמך
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// הסרת פעולת פתיחת המסמך
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// שמירת המסמך המעודכן
document.Save(dataDir);
```

## כיצד לציין עמוד PDF בעת צפייה במסמך {#how-to-specify-pdf-page-when-viewing-document}

בעת צפייה בקבצי PDF בתוכנת צפייה כגון Adobe Reader, הקבצים בדרך כלל נפתחים בעמוד הראשון. עם זאת, ניתן להגדיר את הקובץ להיפתח בעמוד אחר.

המחלקה [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) מאפשרת לך לציין עמוד בקובץ PDF שברצונך לפתוח.
המחלקה [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) מאפשרת לך לציין דף בקובץ PDF שברצונך לפתוח.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// טען את קובץ ה-PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// קבל את מופע הדף השני של המסמך
Page page2 = doc.Pages[2];
// צור משתנה להגדרת גורם ההגדלה של הדף היעד
double zoom = 1;
// צור מופע של GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// עבור לדף 2
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// הגדר את פעולת הפתיחה של המסמך
doc.OpenAction = action;
// שמור את המסמך שעודכן
doc.Save(dataDir + "goto2page_out.pdf");
```

