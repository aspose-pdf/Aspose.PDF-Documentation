---
title: אנוטציה מולטימדיה ב-PDF באמצעות C#
linktitle: אנוטציה מולטימדיה
type: docs
weight: 40
url: /net/multimedia-annotation/
description: Aspose.PDF ל-.NET מאפשר לך להוסיף, לקבל ולמחוק אנוטציה מולטימדיה ממסמך PDF שלך.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "אנוטציה מולטימדיה ב-PDF באמצעות C#",
    "alternativeHeadline": "כיצד להוסיף אנוטציה מולטימדיה ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, אנוטציה מולטימדיה, אנוטציה על מסך, אנוטציה קולית, אנוטציה של וידג'ט, אנוטציה תלת-מימדית",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות המסמכים של Aspose.PDF",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF ל-.NET מאפשר לך להוסיף, לקבל ולמחוק אנוטציה מולטימדיה ממסמך PDF שלך."
}
</script>
הערות במסמך PDF מכילות באוסף הערות של אובייקט [דף](https://reference.aspose.com/pdf/net/aspose.pdf/page). אוסף זה מכיל את כל ההערות עבור אותו דף בלבד: לכל דף יש אוסף הערות משלו. כדי להוסיף הערה לדף מסוים, יש להוסיפה לאוסף ההערות של אותו דף באמצעות השיטה Add.

השתמשו במחלקה [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) במרחב השמות Aspose.PDF.InteractiveFeatures.Annotations כדי לכלול קבצי SWF כהערות במסמך PDF. הערת מסך מציינת אזור בדף שעליו ניתן לנגן קטעי מדיה.

כאשר יש צורך להוסיף קישור לווידאו חיצוני במסמך PDF, ניתן להשתמש ב-[MovieAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
הערת סרט מכילה גרפיקה מונפשת וקול להצגה על מסך המחשב ודרך הרמקולים.

הערת [קול](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) דומה להערת טקסט אך במקום הערת טקסט, היא מכילה קול שהוקלט ממיקרופון המחשב או שיובא מקובץ.
הגדרת [הערת צליל](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) דומה להערת טקסט, אך במקום הערת טקסט, היא מכילה צליל שהוקלט מהמיקרופון של המחשב או שיבוא מקובץ.

עם זאת, כאשר יש צורך לשבץ מדיה בתוך מסמך PDF, יש להשתמש ב[הערת מדיה עשירה](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

ניתן להשתמש בשיטות/תכונות הבאות של הכיתה RichMediaAnnotation.

- Stream CustomPlayer { set; }: מאפשר להגדיר את הנגן המשמש לניגון וידאו.
- string CustomFlashVariables { set; }: מאפשר להגדיר משתנים שמועברים ליישום פלאש. שורה זו היא קבוצה של זוגות "מפתח=ערך" המופרדים באמצעות '&'.
- void AddCustomData(strig name, Stream data): הוספת נתונים נוספים לנגן. לדוגמה source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: אירוע שמפעיל את הנגן; ערכים אפשריים הם Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): הגדרת נתוני וידאו/שמע לניגון.
- void SetContent(Stream stream, string name): הגדר נתוני וידאו / אודיו לנגינה.
- void Update(): צור מבנה של ההערה. יש לקרוא לשיטה זו בסוף.
- void SetPoster(Stream): הגדר פוסטר לווידאו כלומר התמונה שמוצגת כאשר הנגן אינו פעיל.

הדוגמה הבאה עובדת גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת הערת מסך

הדוגמה הבאה מראה איך להוסיף הערת מסך לקובץ PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // הנתיב לספריית המסמכים.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // טען את קובץ ה-PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // צור הערת מסך
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## הוספת אנוטציית קול

הקטע קוד הבא מראה איך להוסיף אנוטציית קול לקובץ PDF:

```csharp
        public static void AddSoundAnnotation()
        {
            // טעינת קובץ ה-PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // יצירת אנוטציית קול
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "הדגמה של אנוטציית קול",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## הוספת אנוטציית RichMedia

הקטע קוד הבא מראה איך להוסיף אנוטציית RichMedia לקובץ PDF:
הקטע הבא מראה כיצד להוסיף RichMediaAnnotation לקובץ PDF:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //תן שם לנתוני וידאו. הנתונים האלו ישובצו במסמך תחת שם זה ויתוחזקו ממשתני פלאש תחת שם זה.
            //videoName לא צריך להכיל נתיב לקובץ; זהו יותר "מפתח" לגישה לנתונים בתוך מסמך PDF
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //כמו כן אנו משתמשים בעור לנגן וידאו
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //כאן עלינו לציין זרם המכיל את קוד הנגן וידאו
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //הרכב שורת משתני פלאש לנגן. שים לב שנגנים שונים עשויים להשתמש בפורמטים שונים של שורת משתני פלאש. ראה בתיעוד של הנגן שלך.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //הוסף קוד עור.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //הגדר פוסטר לווידאו
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //הגדר תוכן וידאו
            rma.SetContent(videoName, fs);

            //הגדר סוג התוכן (וידאו)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //הפעל נגן בלחיצה
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //עדכן נתוני הערה. יש לקרוא למתודה זו לאחר כל ההקצאות/הגדרות. מתודה זו מאתחלת את מבנה הנתונים של ההערה ומשבצת את הנתונים הנדרשים.
            rma.Update();

            //הוסף הערה בעמוד.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### קבלת MultimediaAnnotation

נסה להשתמש בקטע הקוד הבא כדי לקבל MultimediaAnnotation ממסמך PDF.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // טען את קובץ ה-PDF
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### מחיקת MultimediaAnnotation

קטע הקוד הבא מציג איך למחוק MultimediaAnnotation מקובץ PDF.

```csharp
        public static void DeletePolyAnnotation()
        {
            // טען את קובץ ה-PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## הוספת אנוטציות ווידג'ט

טפסים אינטראקטיביים משתמשים ב[אנוטציות ווידג'ט](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) כדי לייצג את המראה של שדות ולנהל אינטראקציות משתמש.
אנו משתמשים באלמנטים אלו שמתווספים ל-PDF כדי להקל על הזנה, שליחת מידע או ביצוע אינטראקציות משתמש אחרות.

אנוטציות ווידג'ט הן הייצוג הגרפי של שדה טופס בדפים מסוימים, לכן לא ניתן ליצור אותן ישירות כאנוטציה.

לכל אנוטציית ווידג'ט יהיה גרפיקה מתאימה (מראה) בהתאם לסוגה. לאחר היצירה, ניתן לשנות פרטים חזותיים מסוימים, כגון סגנון הגבול וצבע הרקע.
תכונות אחרות כמו צבע הטקסט והגופן ניתנות לשינוי דרך השדה, לאחר הקשר אליו.

במקרים מסוימים, ייתכן שתרצה ששדה יופיע ביותר מדף אחד, תוך חזרה על אותו הערך.
במקרים מסוימים, ייתכן שתרצה ששדה יופיע ביותר מדף אחד, תוך שחזור אותו ערך.
מי שממלא את הטופס יכול להשתמש בכל אחד מהווידג'טים האלו כדי לעדכן את ערך השדה, וזה משתקף בכל הווידג'טים האחרים גם כן.

כל שדה טופס עבור כל מקום במסמך מייצג רשומת וידג'ט אחת. הנתונים הספציפיים למיקום של רשומת וידג'ט מתווספים לדף המסוים. לכל שדה טופס יש מספר וריאציות. כפתור יכול להיות כפתור רדיו, תיבת סימון, או כפתור לחיצה. וידג'ט בחירה יכול להיות תיבת רשימה או תיבת קומבו.

בדוגמה זו, נלמד כיצד להוסיף כפתורי לחיצה לניווט במסמך.

### הוספת כפתור למסמך

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "הדפס מסמך נוכחי",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "הדפס מסמך"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
כפתור זה מכיל מסגרת וקובע רקע. כמו כן אנו מגדירים שם לכפתור (שם), תיאור קצר (שם חלופי), תווית (תיאור רגיל), וצבע של טקסט התווית (צבע).

### שימוש בפעולות ניווט במסמך

קיים דוגמה מורכבת יותר לשימוש ביישום הערות הווידג'ט - ניווט במסמך PDF. זה עשוי להיות נחוץ להכנת מצגת מסמך PDF.

הדוגמה הזו מראה איך ליצור 4 כפתורים:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "לך לעמוד הראשון", "לך לעמוד הקודם", "לך לעמוד הבא", "לך לעמוד האחרון" };
var normalCaptions = new[] { "ראשון", "קודם", "הבא", "אחרון" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

יש ליצור את הכפתורים מבלי לצרף אותם לעמוד.
יש ליצור את הכפתורים מבלי לקשור אותם לדף.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

יש לשכפל את מערך הכפתורים בכל דף במסמך.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

אנו קוראים למתודה [Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) עם הפרמטרים הבאים: שדה, שם, ואינדקס הדפים שאליהם יתווסף השדה.
אנו קוראים [לשיטת Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) עם הפרמטרים הבאים: שדה, שם, ומדד הדפים אליהם השדה יתווסף.

וכדי לקבל את התוצאה המלאה, עלינו לנטרל את הכפתורים "ראשון" ו"קודם" בדף הראשון ואת הכפתורים "הבא" ו"אחרון" בדף האחרון.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

למידע נוסף ולאפשרויות של יכולות אלו ראה גם ב[עבודה עם טפסים](/pdf/net/acroforms/).

במסמכי PDF ניתן לצפות ולנהל תוכן תלת-ממדי איכותי המיוצר באמצעות תוכנות CAD תלת-ממדיות או תוכנות דגמות תלת-ממדיות ומוטמע במסמך ה-PDF. ניתן לסובב את האלמנטים התלת-ממדיים בכל הכיוונים כאילו היית מחזיק בהם בידיים.

למה בכלל צריך הצגה תלת-ממדית של תמונות?

במהלך השנים האחרונות, הטכנולוגיה עשתה פריצות דרך עצומות בכל התחומים הודות להדפסה תלת-ממדית.
במהלך השנים האחרונות, טכנולוגיה עשתה פריצות דרך עצומות בכל התחומים בזכות הדפסה תלת-ממדית.

המשימה העיקרית של דגמות תלת-ממד היא הרעיון של עצם או עצם בעתיד משום ש, כדי לשחרר עצם, דרושה הבנה של תכונות העיצוב שלו בכל פרט לשחזור רצוף בעיצוב תעשייתי או אדריכלות.

## הוסף אנוטציה תלת-ממדית

אנוטציה תלת-ממדית מתווספת באמצעות מודל שנוצר בפורמט U3D.

1. צור מסמך חדש
1. טען את נתוני הדגם התלת-ממדי הרצוי (במקרה שלנו "Ring.u3d") כדי ליצור תוכן PDF3D
1. צור אובייקט 3dArtWork וקשר אותו למסמך ולתוכן 3D
1. כוון את אובייקט pdf3dArtWork:

    - 3DLightingScheme - (נקבע `CAD` בדוגמה)
    - 3DRenderMode - (נקבע `Solid` בדוגמה)
    - מלא את `ViewArray`, צור לפחות תצוגה תלת-ממדית אחת והוסף אותה למערך.
- מלא את `ViewArray`, צור לפחות תצוגה אחת [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) והוסף אותה למערך.

1. הגדר 3 פרמטרים בסיסיים בעיטור:
    - ה`page` שעליו יופיע העיטור,
    - ה`rectangle`, בתוך שבו העיטור,
    - ואובייקט `3dArtWork`.
1. לתצוגה טובה יותר של האובייקט 3D, הגדר מסגרת גבול
1. הגדר את התצוגה המוגדרת כברירת מחדל (לדוגמה - TOP)
1. הוסף כמה פרמטרים נוספים: שם, פוסטר תצוגה מקדימה וכו'.
1. הוסף עיטור ל[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. שמור את התוצאה

### דוגמה

אנא עיין בדוגמת הקוד הבאה להוספת עיטור 3D.

```csharp
    public static void Add3dAnnotation()
    {
    // טען את קובץ ה-PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //הגדר תמונת תצוגה מקדימה אם נדרש
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
דוגמה זו לקוד מראה לנו מודל כזה:

![הדגמת אנוטציה תלת-ממדית](3d_demo.png)

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
    "applicationCategory": "ספרייה לניהול PDF עבור .NET",
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
changefreq: "monthly"
type: docs

