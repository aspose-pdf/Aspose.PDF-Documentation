---
title: עיטורים נוספים באמצעות C#
linktitle: עיטורים נוספים
type: docs
weight: 60
url: /net/extra-annotations/
description: סעיף זה מתאר כיצד להוסיף, לקבל ולמחוק סוגים נוספים של עיטורים ממסמך PDF שלך.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עיטורים נוספים באמצעות C#",
    "alternativeHeadline": "כיצד להוסיף עיטורים נוספים ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, עיטור קישור, עיטור סימן עיתון",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות Aspose.PDF Doc",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "סעיף זה מתאר כיצד להוסיף, לקבל ולמחוק סוגים נוספים של עיטורים ממסמך PDF שלך."
}
</script>

## איך להוסיף אנוטציה של סמן טיפול בקובץ PDF קיים

אנוטציה של סמן טיפול היא סמל שמציין עריכת טקסט. אנוטציה של סמן טיפול היא גם אנוטציה של סימון, כך שהמחלקה Caret נגזרת מהמחלקה Markup וגם מספקת פונקציות לקבל או להגדיר מאפיינים של אנוטציה של סמן טיפול ולאפס את זרימת הופעת הסמן טיפול.

הקטע קוד הבא עובד גם עם ספרייה [Aspose.PDF.Drawing](/pdf/net/drawing/).

שלבים בהם אנו יוצרים אנוטציה של סמן טיפול:

1. טען את קובץ ה-PDF - [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) חדש.
2. צור אנוטציה [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) חדשה והגדר פרמטרים של סמן (Rectangle חדש, כותרת, נושא, דגלים, צבע, רוחב, StartingStyle ו-EndingStyle). האנוטציה הזו משמשת לציון הוספת טקסט.
1. צור [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) חדש והגדר פרמטרים (Rectangle חדש, כותרת, צבע, QuadPoints חדשים ונקודות חדשות, נושא, InReplyTo, ReplyType).
1. לאחר מכן ניתן להוסיף אנוטציות לדף.

הקטע הבא מראה כיצד להוסיף אנוטציית Caret לקובץ PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // נתיב לתיקיית המסמכים
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // טען את קובץ ה-PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // אנוטציה זו משמשת לציון הוספת טקסט
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "משתמש Aspose",
                Subject = "טקסט מוכנס 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // אנוטציה זו משמשת לציון החלפת טקסט
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "טקסט מוכנס 2",
                Title = "משתמש Aspose",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "קו חוצה",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
### קבל אנוטציית קארט

אנא נסה להשתמש בקטע הקוד הבא כדי לקבל אנוטציית קארט במסמך PDF

```csharp
public static void GetCaretAnnotation()
{
    // טען את קובץ ה-PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### מחק אנוטציית קארט

קטע הקוד הבא מראה כיצד למחוק אנוטציית קארט מקובץ PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // טען את קובץ ה-PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## הסתרת אזור מסוים בעמוד באמצעות Redaction Annotation באמצעות Aspose.PDF עבור .NET

Aspose.PDF עבור .NET תומך בתכונה להוסיף ולטפל בהערות בקובץ PDF קיים. לאחרונה, כמה מלקוחותינו פרסמו דרישה להסתיר (להסיר טקסט, תמונה וכו' מ) אזור מסוים בעמוד של מסמך PDF. כדי לענות על דרישה זו, מוצעת מחלקה בשם RedactionAnnotation, שניתן להשתמש בה כדי להסתיר אזורים מסוימים בעמוד או לטפל ב-RedactionAnnotations קיימים ולהסתיר אותם (כלומר להחליק את ההערה ולהסיר את הטקסט שמתחתיה).

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// פתח מסמך
Document doc = new Document(dataDir + "input.pdf");

// צור מופע של RedactionAnnotation לאזור עמוד מסוים
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// טקסט להדפסה על הערת ההסתרה
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// חזור על טקסט הכיסוי מעל הערת ההסתרה
annot.Repeat = true;
// הוסף הערה לאוסף ההערות של העמוד הראשון
doc.Pages[1].Annotations.Add(annot);
// החלק את ההערה ומסתיר את תוכן העמוד (כלומר מסיר טקסט ותמונה
// מתחת להערת ההסתרה)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### גישת ממשקים

המרחב השם Aspose.PDF.Facades כולל גם מחלקה בשם [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) המספקת יכולת לתפעל אנוטציות קיימות בתוך קובץ PDF. המחלקה כוללת מתודה בשם [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) שמספקת את היכולת להסיר אזורים מסוימים בדף.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// להסתיר אזור מסוים בדף
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
```

<script type="application/ld+json">

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

