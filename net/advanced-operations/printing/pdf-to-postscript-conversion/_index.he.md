---
title: המרת PDF ל-PostScript
linktitle: המרת PDF ל-PostScript
type: docs
weight: 30
url: /net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: יש לנו פתרון להמרת PDF ל-PostScript. השתמשו במשימה זו בהדפסה ובמחלקת PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "המרת PDF ל-PostScript",
    "alternativeHeadline": "המרת PDF ל-PostScript",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, pdf to postscript",
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
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "יש לנו פתרון להמרת PDF ל-PostScript. השתמשו במשימה זו בהדפסה ובמחלקת PdfViewer."
}
</script>
הקטע הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **PDF ל-Postscript ב-C#**

המחלקה PdfViewer מספקת את היכולת להדפיס מסמכי PDF ובעזרת מחלקה זו, אנו יכולים גם להמיר קבצי PDF לפורמט PostScript. לשם המרת קובץ PDF ל-PostScript, ראשית יש להתקין מדפסת PS כלשהי ולהדפיס לקובץ בעזרת PdfViewer. ניתן לעקוב אחר ההוראות שסיפקה אוניברסיטת הוואי על כיצד להתקין מדפסת PS. הקטע הבא מראה איך להדפיס ולהמיר PDF לפורמט PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // נתיב לתיקיית המסמכים.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // הגדרת הגדרות מדפסת והגדרות דף
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // הגדרת מדפסת PS, ניתן למצוא את הדרייבר הזה ברשימת דרייברים שמותקנים מראש במערכת הפעלה של Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // הגדרת שם קובץ הפלט ותכונת הדפסה לקובץ
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // ביטול דיאלוג דף ההדפסה
    viewer.PrintPageDialog = false;
    // העברת אובייקט הגדרות המדפסת לשיטה
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## בדיקת סטטוס משימת הדפסה

ניתן להדפיס קובץ PDF למדפסת פיזית כמו גם ל-Microsoft XPS Document Writer, ללא הצגת דיאלוג הדפסה, באמצעות המחלקה PdfViewer. כאשר מדפיסים קבצי PDF גדולים, התהליך עשוי לקחת זמן רב ולכן המשתמש עשוי לא להיות בטוח אם תהליך ההדפסה הושלם או נתקל בבעיה. לקביעת סטטוס משימת ההדפסה, השתמש במאפיין PrintStatus. קטע הקוד הבא מראה איך להדפיס את קובץ ה-PDF לקובץ XPS ולקבל את סטטוס ההדפסה.

```csharp
public static void CheckingPrintJobStatus()
{
    // לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // הנתיב לספריית המסמכים.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // יצירת אובייקט PdfViewer
    PdfViewer viewer = new PdfViewer();

    // קישור קובץ PDF מקורי
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // הסתרת דיאלוג הדפסה
    viewer.PrintPageDialog = false;

    // יצירת אובייקט הגדרות מדפסת
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // ציון שם המדפסת
    ps.PrinterName = "Microsoft XPS Document Writer";

    // שם התוצאה המודפסת
    ps.PrintFileName = "ResultantPrintout.xps";

    // הדפסת הפלט לקובץ
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // ציון גודל דף ההדפסה
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // הדפסת המסמך עם ההגדרות שצוינו לעיל
    viewer.PrintDocumentWithSettings(pgs, ps);

    // בדיקת סטטוס ההדפסה
    if (viewer.PrintStatus != null)
    {
        // נזרקה חריגה
        if (viewer.PrintStatus is Exception ex)
        {
            // קבלת הודעת החריגה
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // לא נמצאו שגיאות. משימת ההדפסה הושלמה בהצלחה
        Console.WriteLine("printing completed without any issue..");
    }
}
```
## קבל/הגדר שם בעלים של משימת הדפסה

לאחרונה קיבלנו דרישה לקבל/להגדיר את שם בעל המשימה של ההדפסה (המשתמש האמיתי שלחץ על כפתור ההדפסה בדף האינטרנט). מידע זה נדרש בעת הדפסת קובץ PDF. כדי לעמוד בדרישה זו, ניתן להשתמש במאפיין בשם PrinterJobName:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// קשר קובץ PDF מקורי
viewer.BindPdf(dataDir + "input.pdf");
// ציין את שם משימת ההדפסה
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // היישום תלוי בסוג היישום הרץ (ASP.NET, טפסים של Windows וכו').
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## שימוש בהתחזות

גישה נוספת לקבלת שם בעלים של משימת הדפסה היא להשתמש בהתחזות (הרצת פרוצדורות הדפסה בהקשר של משתמש אחר) או שהמשתמש יכול לשנות את שם הבעלים ישירות באמצעות שימוש בפונקציית SetJob.

אנא שימו לב שאין אפשרות להגדיר ערך בעלים באמצעות ממשק ה- API של הדפסה של Aspose.PDF משיקולי אבטחה. ניתן להשתמש בתכונה PrinterJobName כדי להגדיר ערך עמודת שם מסמך ביישום הדפסת תור. קטע הקוד ששותף לעיל מראה רק איך המשתמש יכול לשלב שם משתמש בעמודת שם המסמך (לדוגמה באמצעות תחביר UserName\documentName). אך הגדרת עמודות הבעלים יכולה להתבצע בדרכים הבאות ישירות על ידי המשתמש:

1) התחזות. מכיוון שערך עמודת הבעלים מכיל את ערך המשתמש שמריץ את קוד ההדפסה, קיימת דרך להפעיל את ממשק ה- API של הדפסת Aspose.PDF בהקשר של משתמש אחר. לדוגמה נא לעיין בפתרון שמתואר כאן. באמצעות מחלקה זו המשתמש יכול להשיג מטרה:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf(dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// לא לייצר דיאלוג מספר עמוד בעת ההדפסה
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName הוא ערך של עמודת הבעלים ביישום תור ההדפסה
    viewer.Close();
}
```
2) שימוש ב-API של Spooler ובפונקציה SetJob

הקטע הבא מדגים כיצד להדפיס כמה עמודים מקובץ PDF במצב Simplex וכמה עמודים במצב Duplex.

```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
ps.PrintToFile = true;
ps.FromPage = printingJobs[printingJobIndex].FromPage;
ps.ToPage = printingJobs[printingJobIndex].ToPage;
ps.Duplex = printingJobs[printingJobIndex].Mode;
ps.PrintRange = PrintRange.SomePages;

pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);
viewer.EndPrint += (sender, args) =>
{
    if (++printingJobIndex < printingJobs.Count)
    {
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF עבור .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "ארגון",
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

