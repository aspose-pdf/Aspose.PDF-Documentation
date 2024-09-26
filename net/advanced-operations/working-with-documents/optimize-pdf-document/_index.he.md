---
title: לייעל, לדחוס או להקטין גודל PDF ב-C#
linktitle: לייעל PDF
type: docs
weight: 30
url: /net/optimize-pdf/
keywords: "optimize pdf c#"
description: לייעל קובץ PDF, לצמצם את כל התמונות, להקטין גודל PDF, לבטל שיבוץ גופנים, להסיר אובייקטים שלא בשימוש באמצעות C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/changing-page-sizes-in-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "לייעל PDF באמצעות C#",
    "alternativeHeadline": "כיצד לייעל PDF עם .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, לייעל pdf",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "לייעל קובץ PDF, לצמצם את כל התמונות, להקטין גודל PDF, לבטל שיבוץ גופנים, להסיר אובייקטים שלא בשימוש באמצעות C#."
}
</script>
מסמך PDF עשוי להכיל לעיתים נתונים נוספים. צמצום גודל של קובץ PDF יעזור לך לייעל העברה ברשת ואחסון. זה מועיל במיוחד לפרסום בדפי אינטרנט, שיתוף ברשתות חברתיות, שליחה בדואר אלקטרוני, או ארכוב באחסון. אנו יכולים להשתמש בטכניקות שונות כדי לייעל PDF:

- ייעול תוכן העמוד לגלישה מקוונת
- כיווץ או צמצום כל התמונות
- אפשר שימוש חוזר בתוכן העמוד
- מיזוג זרמים כפולים
- הוצאת גופנים מהשימוש
- הסרת אובייקטים שאינם בשימוש
- הסרת שטחי טופס משופעים
- הסרה או השטחה של הערות

{{% alert color="primary" %}}

הסבר מפורט של שיטות הייעול ניתן למצוא בדף סקירת שיטות הייעול.

{{% /alert %}}

## ייעול מסמך PDF לרשת

ייעול, או ליניאריזציה לרשת, מתייחס לתהליך של הפיכת קובץ PDF למתאים לגלישה מקוונת באמצעות דפדפן אינטרנט. כדי לייעל קובץ לתצוגה ברשת:

1. פתח את המסמך הנכנס באובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1.
1. שמור את המסמך הממוטב באמצעות השיטה [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

הקטע קוד הבא גם עובד עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

הקטע קוד הבא מראה איך למטב מסמך PDF לשימוש באינטרנט.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// מטב לשימוש באינטרנט
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// שמור מסמך פלט
pdfDocument.Save(dataDir);
```

## צמצום גודל PDF

השיטה [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) מאפשרת לך לצמצם את גודל המסמך על ידי הסרת מידע לא נחוץ.
השיטה [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) מאפשרת לך להקטין את גודל המסמך על ידי הסרת מידע לא נחוץ.

- משאבים שאינם משמשים בדפי המסמך מוסרים
- משאבים שווים מתאחדים לאובייקט אחד
- אובייקטים שאינם בשימוש נמחקים

הקטע להלן הוא דוגמה. שים לב, עם זאת, ששיטה זו אינה יכולה להבטיח צמצום בגודל המסמך.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתח מסמך
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// אופטימיזציה של מסמך PDF. שים לב, עם זאת, ששיטה זו אינה יכולה להבטיח צמצום בגודל המסמך
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir);
```

## ניהול אסטרטגיית אופטימיזציה

אנו יכולים גם להתאים אישית את אסטרטגיית האופטימיזציה.
אנו יכולים גם להתאים את אסטרטגיית האופטימיזציה.

### צמצום או דחיסת כל התמונות

יש לנו שתי דרכים לעבוד עם תמונות: להקטין את איכות התמונה ו/או לשנות את הרזולוציה שלהן. בכל מקרה, יש להחיל [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions). בדוגמה הבאה, אנו מצמצמים תמונות על ידי הקטנת [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) ל-50.

`ImageQuality` פועל באופן דומה לאיכות JPEG, שבו הערך 0 הוא הנמוך ביותר והערך 100 הוא הגבוה ביותר.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// פתח מסמך
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// אתחל אפשרויות אופטימיזציה
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// הגדר את אפשרות CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// הגדר את אפשרות ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// אופטימיזציה של מסמך PDF באמצעות OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// שמור מסמך מעודכן
pdfDocument.Save(dataDir);
```
דרך נוספת היא לשנות את גודל התמונות לרזולוציה נמוכה יותר. במקרה זה, עלינו להגדיר את ResizeImages לערך true ואת MaxResolution לערך המתאים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// אתחול זמן
var time = DateTime.Now.Ticks;
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// אתחול אפשרויות אופטימיזציה
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// הגדרת אפשרות CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// הגדרת אפשרות ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// הגדרת אפשרות ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// הגדרת אפשרות MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// אופטימיזציה של מסמך PDF באמצעות אפשרויות האופטימיזציה
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// שמירת המסמך המעודכן
pdfDocument.Save(dataDir);
```
עניין חשוב נוסף הוא זמן הביצוע. אך שוב, גם זה ניתן לניהול. כרגע ניתן להשתמש בשני אלגוריתמים - רגיל ומהיר. כדי לשלוט על זמן הביצוע יש להגדיר את המאפיין [Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). הקטע הבא מדגים את האלגוריתם המהיר:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// אתחול זמן
var time = DateTime.Now.Ticks;
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// אתחול אפשרויות אופטימיזציה
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// הגדרת אפשרות דחיסת תמונות
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// הגדרת אפשרות איכות תמונה
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// הגדרת גרסת דחיסת תמונה למהירה
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// אופטימיזציה של מסמך PDF באמצעות אפשרויות אופטימיזציה
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// שמירת המסמך המעודכן
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### הסרת אובייקטים שאינם בשימוש

מסמך PDF לעיתים כולל אובייקטים של PDF שאינם מקושרים לאף אובייקט אחר במסמך. זה יכול לקרות, לדוגמא, כאשר דף מוסר מעץ הדפים של המסמך אך האובייקט של הדף עצמו לא מוסר. הסרת אובייקטים אלו אינה מבטלת את תקפות המסמך אלא מקטינה אותו.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתח מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// הגדר את אפשרות הסרת אובייקטים שאינם בשימוש
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// אופטימיזציה של מסמך PDF באמצעות OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir);
```

### הסרת זרמים שאינם בשימוש

לעיתים המסמך מכיל זרמי משאבים שאינם בשימוש.
לעיתים המסמך מכיל זרמי משאבים שאינם בשימוש.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא מעבר לכתובת https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתח מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// הגדר את האופציה RemoveUsedStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// בצע אופטימיזציה למסמך PDF באמצעות OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir);
```

### קישור זרמים כפולים

חלק מהמסמכים יכולים להכיל מספר זרמי משאבים זהים (כמו תמונות, לדוגמה).
ישנם מסמכים היכולים להכיל מספר זרמי משאבים זהים (כמו תמונות, לדוגמה).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתח מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// הגדר את אפשרות LinkDuplcateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// שפר את המסמך PDF באמצעות OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir);
```

בנוסף, ניתן להשתמש בהגדרות [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
בנוסף, אנו יכולים להשתמש בהגדרות [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// הגדרת אופציית AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("התחלה");
// אופטימיזציה של מסמך PDF באמצעות OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// שמירת המסמך המעודכן
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("סיום");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("גודל קובץ מקורי: {0}. גודל קובץ מופחת: {1}", fi1.Length, fi2.Length);
```
### ביטול שיבוץ גופנים

אם המסמך משתמש בגופנים מושבצים, זה אומר שכל נתוני הגופן מאוחסנים במסמך. היתרון הוא שניתן לצפות במסמך ללא תלות בהתקנת הגופן במכונת המשתמש. אך שיבוץ גופנים גורם למסמך להיות גדול יותר. שיטת ביטול שיבוץ הגופנים מסירה את כל הגופנים המושבצים. כתוצאה מכך, גודל המסמך יורד אך המסמך עצמו עשוי להיות בלתי קריא אם הגופן הנכון אינו מותקן.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// הגדרת האופציה UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Start");
// אופטימיזציה של מסמך PDF באמצעות OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// שמירת המסמך המעודכן
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finished");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
```
המשאבי אופטימיזציה מחילים את השיטות הללו על המסמך. אם חלק מהשיטות הללו מיושמות, גודל המסמך יקטן בהסתברות גבוהה. אם אף אחת מהשיטות הללו לא מיושמת, גודל המסמך לא ישתנה, מה שברור מאליו.

## דרכים נוספות להקטין את גודל מסמך PDF

### הסרה או החלקת הערות

ניתן למחוק הערות כאשר הן אינן נחוצות. כאשר הן נחוצות אך אינן דורשות עריכה נוספת, ניתן להחליק אותן. שתי הטכניקות הללו יקטינו את גודל הקובץ.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב אל ספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// החלקת הערות
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// שמירת המסמך המעודכן
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### הסרת שדות טופס

אם מסמך ה-PDF מכיל AcroForms, אנו יכולים לנסות להקטין את גודל הקובץ על ידי החלקת שדות הטופס.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// טעינת טופס PDF מקורי
Document doc = new Document(dataDir + "input.pdf");

// החלקת טפסים
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// שמירת המסמך המעודכן
doc.Save(dataDir);
```

### המרת PDF ממרחב צבעי RGB לגווני אפור

קובץ PDF מורכב מטקסט, תמונה, קובץ מצורף, הערות, גרפים ואובייקטים אחרים.
קובץ PDF מכיל טקסט, תמונה, קובץ מצורף, הערות, גרפים ואובייקטים אחרים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// טעינת קובץ PDF מקורי
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // קבלת מופע של דף מסוים בתוך ה-PDF
        Page page = document.Pages[idxPage];
        // המרת תמונה במרחב הצבעים RGB למרחב צבעים של אפור
        strategy.Convert(page);
    }
    // שמירת הקובץ המתקבל
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### דחיסת FlateDecode

{{% alert color="primary" %}}

תכונה זו נתמכת על ידי גרסה 18.12 או גדולה יותר.

{{% /alert %}}

Aspose.PDF for .NET תומך בדחיסת FlateDecode עבור פונקציונליות אופטימיזציה של PDF.
Aspose.PDF עבור .NET תומכת בדחיסת FlateDecode לפונקציונליות אופטימיזציה של PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **שמירת תמונה ב-XImageCollection**

Aspose.PDF עבור .NET מספקת את היכולת לאחסן תמונות חדשות ב-**XImageCollection** עם דחיסת FlateDecode. כדי לאפשר אפשרות זו תוכל להשתמש בדגל **ImageFilterType.Flate**. קטע הקוד הבא מראה כיצד להשתמש בפונקציונליות זו:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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


