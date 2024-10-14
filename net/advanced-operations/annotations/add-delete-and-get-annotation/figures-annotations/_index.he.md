---
title: הוספת אנוטציות דמויות באמצעות C#
linktitle: אנוטציות דמויות
type: docs
weight: 30
url: /net/figures-annotation/
description: מאמר זה מתאר איך להוסיף, לקבל ולמחוק אנוטציות דמויות ממסמך PDF שלך עם Aspose.PDF עבור .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת אנוטציות דמויות באמצעות C#",
    "alternativeHeadline": "איך להוסיף אנוטציות דמויות ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, אנוטציות דמויות, אנוטציית פוליגון, אנוטציית קו, אנוטציית ריבוע, אנוטציית עיגול",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מתאר איך להוסיף, לקבל ולמחוק אנוטציות דמויות ממסמך PDF שלך עם Aspose.PDF עבור .NET"
}
</script>
אפליקציה לניהול מסמכי PDF מספקת מגוון כלים להוספת הערות למסמכים. מנקודת מבט של המבנה הפנימי של PDF, כלים אלה הם הערות. אנו תומכים בסוגי כלים לציור הבאים.

* הערת קו - כלי לציור קווים וחצים
* הערת ריבוע - לציור ריבועים ומלבנים
* הערת מעגל - לעיגולים ומעגלים
* הערת טקסט חופשי - להערת שיחה
* הערת פוליגון - לפוליגונים ועננים
* הערת פוליליניה - לקווים מחוברים

## הוספת צורות ודמויות על הדף

הגישה להוספת ההערה טיפוסית לכל אחת מהן.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. טען את קובץ ה-PDF או צור חדש באמצעות [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. צור הערה חדשה והגדר פרמטרים (Rectangle חדש, Point חדש, כותרת, צבע, רוחב וכו').
1. קשר אנוטציה מוקפצת עם המקורית.
1. הוסף אנוטציה לדף

## הוספת קווים או חצים

מטרת אנוטציית הקו היא להציג קו ישר או חץ על הדף.
כדי ליצור קו נזדקק לאובייקט LineAnnotation חדש.
בנאי של המחלקה LineAnnotation לוקח ארבעה פרמטרים:

* הדף בו תתווסף האנוטציה,
* המלבן שמגדיר את גבולות האנוטציה,
* ושני הנקודות המגדירות את התחלה והסוף של הקו.

כמו כן נצטרך לאתחל כמה מאפיינים:

* `Title` - לרוב, זהו שם המשתמש שהגיב
* `Subject` - יכול להיות כל מחרוזת, אך במקרים רבים זהו שם האנוטציה

כדי לעצב את הקו שלנו נצטרך להגדיר צבע, רוחב, סגנון התחלתי וסגנון סיומת.
כדי לעצב את הקו שלנו עלינו לקבוע צבע, רוחב, סגנון התחלתי וסגנון סיומת.

הקטע קוד הבא מראה איך להוסיף אנוטציה של קו לקובץ PDF:

```csharp
// טוען את קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// יוצר אנוטציה של קו
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

// מוסיף אנוטציה לדף
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## הוספת ריבוע או מעגל

האנוטציות [ריבוע](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) ו[מעגל](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) יציגו ריבוע או אליפסה על הדף.
האנוטציות [ריבוע](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) ו[מעגל](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) יציגו מלבן או אליפסה על הדף.

### הוספת אנוטציית מעגל

כדי לצייר אנוטציית מעגל או אליפסה חדשה, עלינו ליצור אובייקט CircleAnnotation חדש. בנאי המחלקה `CircleAnnotation` מקבל שני פרמטרים:

* הדף שבו תתווסף האנוטציה,
* והמלבן שמגדיר את גבולות האנוטציה

בנוסף אנו יכולים להגדיר כמה מאפיינים של אובייקט `CircleAnnotation`, כגון הכותרת, הצבע, צבע הפנים, השקיפות. מאפיינים אלה קובעים איך האנוטציה תיראה ותתנהג בתוכנת ה-PDF. כאן ולהלן באנוטציית הריבוע, צבע `InteriorColor` הוא צבע המילוי ו-`Color` הוא צבע הגבול.

### הוספת אנוטציית ריבוע

לצייר מלבן זהה לציור מעגל.
לצייר מלבן זהה לצייר מעגל.

```csharp
var dataDir = "<path-to-file>";
// טען את קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// צור אנוטציה של מעגל
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Circle",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// צור אנוטציה של ריבוע
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectangle",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// הוסף אנוטציה לעמוד
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
כדוגמא, נראה את התוצאה הבאה של הוספת אנוטציות ריבוע ומעגל למסמך PDF:

![הדגמת אנוטציית מעגל וריבוע](circle_demo.png)

## הוספת אנוטציות פוליגון ופולילין

כלי ה-Poly- מאפשר לך ליצור צורות וקווי תווך עם מספר שרירותי של צלעות על המסמך.

**אנוטציות פוליגון** מייצגות פוליגונים על דף. הן יכולות להיות עם כל מספר של קודקודים המחוברים בקווים ישרים.
**אנוטציות פולילין** דומות גם הן לפוליגונים, ההבדל היחיד הוא שהקודקוד הראשון והאחרון אינם מחוברים באופן מובלע.

### הוספת אנוטציית פוליגון

PolygonAnnotation אחראי על אנוטציות פוליגון. בנאי של מחלקת PolygonAnnotation לוקח שלושה פרמטרים:

* הדף בו תתווסף האנוטציה,
* המלבן שמגדיר את גבולות האנוטציה,
* ומערך של נקודות המגדירות את הקודקודים של הפוליגון.

`Color` ו-`InteriorColor` משמשים לצבעי הגבול והמילוי בהתאמה.

### הוספת אנוטציית פולילין
### הוספת אנוטציה של פוליליין

PolygonAnnotation אחראית על אנוטציות של פוליגון. בנאי המחלקה PolygonAnnotation מקבל שלושה פרמטרים:

* הדף בו האנוטציה תתווסף,
* המלבן שמגדיר את הגבול של האנוטציה,
* ומערך של נקודות המגדירות את קודקודי הפוליגון.

במקום `PolygonAnnotation` איננו יכולים למלא את הצורה, ולכן אין צורך להשתמש ב`InteriorColor`.

הדוגמה הבאה מראה כיצד להוסיף אנוטציות של פוליגון ופוליליין לקובץ PDF:

```csharp
// טעינת קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// יצירת אנוטציה של פוליגון
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// יצירת אנוטציה של פוליליין
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// הוספת האנוטציה לדף
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## קבלת דמויות

כל ההערות מאוחסנות באוסף `Annotations`. כל הערה יכולה להציג את סוגה דרך התכונה `AnnotationType`. לכן, אנו יכולים לבצע שאילתת LINQ כדי לסנן את ההערות הרצויות.

### קבלת הערות קו

הדוגמה למטה מסבירה כיצד להשיג את כל הערות הקו מהעמוד הראשון של מסמך PDF.

```csharp
// טעינת קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### קבלת הערות מעגל

הדוגמה למטה מסבירה כיצד להשיג את כל הערות הפוליליין מהעמוד הראשון של מסמך PDF.

```csharp
// טעינת קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### קבלת אנוטציות ריבוע

הדוגמה למטה מסבירה כיצד לקבל את כל אנוטציות הפוליליין מהעמוד הראשון של מסמך PDF.

```csharp
// טעינת קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### קבלת אנוטציות פוליליין

הדוגמה למטה מסבירה כיצד לקבל את כל אנוטציות הפוליליין מהעמוד הראשון של מסמך PDF.

```csharp
// טעינת קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### קבלת אנוטציות פוליגון
הדוגמה למטה מסבירה כיצד לקבל את כל האנוטציות הפוליגוניות מהעמוד הראשון של מסמך PDF.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## מחיקת דמויות

הגישה להסרת אנוטציה מ-PDF פשוטה למדי:

* בחר אנוטציות למחיקה (יצירת אוסף מסוים)
* עבור על האוסף באמצעות לולאת foreach, ומחק כל אנוטציה מאוסף האנוטציות באמצעות המתודה Delete.

### מחיקת אנוטציית קו

```csharp
// טען את קובץ ה-PDF
Document document = a new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### מחק עיגול וריבוע הערות

```csharp
// טען את קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### מחק מצולע ופולילין הערות

הקטע קוד הבא מראה כיצד למחוק מצולע ופולילין הערות מקובץ PDF.

```csharp
// טען את קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## כיצד להוסיף הערת דיו לקובץ PDF

הערת דיו מייצגת "כתב יד" חופשי המורכב מנתיב אחד או יותר שאינם מחוברים. כאשר היא נפתחת, היא צריכה להציג חלון קופץ המכיל את טקסט ההערה המקושרת.

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) מייצג כתב יד חופשי המורכב מנקודות שאינן מחוברות. אנא נסה להשתמש בקטע קוד הבא כדי להוסיף הערת דיו במסמך PDF.

```csharp
// טען את קובץ ה-PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// שמור את קובץ הפלט
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### שינוי רוחב קו של InkAnnotation

ניתן לשנות את רוחב הקו של [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) באמצעות אובייקטים LineInfo ו-Border.

```csharp
// לדוגמאות מלאות וקבצי מידע, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// שמור את קובץ הפלט
doc.Save(dataDir);
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
### מחיקת אנוטציה מעגלית

הקטע הבא מראה כיצד למחוק אנוטציה מעגלית מקובץ PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // טעינת קובץ ה-PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
