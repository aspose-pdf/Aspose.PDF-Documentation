---
title: עבודה עם אופרטורים
linktitle: עבודה עם אופרטורים
type: docs
weight: 170
url: /net/operators/
description: הנושא הזה מסביר איך להשתמש באופרטורים עם Aspose.PDF. מחלקות האופרטור מספקות יכולות נהדרות למניפולציה של קבצי PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם אופרטורים",
    "alternativeHeadline": "איך להשתמש באופרטורים של PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, אופרטורים ב-pdf, השתמש באופרטורים של pdf",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "הנושא הזה מסביר איך להשתמש באופרטורים עם Aspose.PDF. מחלקות האופרטור מספקות יכולות נהדרות למניפולציה של קבצי PDF."
}
</script>
## הקדמה לאופרטורים של PDF והשימוש בהם

אופרטור הוא מילת מפתח ב-PDF המציינת פעולה מסוימת שיש לבצע, כגון ציור צורה גרפית על הדף. מילת מפתח של אופרטור מובחנת מאובייקט בעל שם באמצעות היעדר תו קו נטוי ראשוני (2Fh). אופרטורים הם בעלי משמעות רק בתוך זרם התוכן.

זרם תוכן הוא אובייקט זרם של PDF שנתוניו מורכבים מהוראות המתארות את האלמנטים הגרפיים שיש לצייר על דף. ניתן למצוא פרטים נוספים על אופרטורי PDF ב[מפרט ה-PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### פרטי יישום

נושא זה מסביר כיצד להשתמש באופרטורים עם Aspose.PDF.
נושא זה מסביר כיצד להשתמש באופרטורים עם Aspose.PDF.

- האופרטור **GSave** שומר את מצב הגרפיקה הנוכחי של ה-PDF.
- האופרטור **ConcatenateMatrix** (מטריצת שרשור) משמש להגדרת אופן הצבת התמונה על דף ה-PDF.
- האופרטור **Do** מצייר את התמונה על הדף.
- האופרטור **GRestore** משחזר את מצב הגרפיקה.

להוספת תמונה לקובץ PDF:

1. צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ופתח את מסמך ה-PDF הקלט.
1. קבל את הדף הספציפי שאליו תתווסף התמונה.
1. הוסף את התמונה לאוסף המשאבים של הדף.
1. השתמש באופרטורים כדי למקם את התמונה על הדף:
   - תחילה, השתמש באופרטור GSave כדי לשמור את מצב הגרפיקה הנוכחי.
   - לאחר מכן השתמש באופרטור ConcatenateMatrix כדי לציין היכן תמוקם התמונה.
   - השתמש באופרטור Do כדי לצייר את התמונה על הדף.
1. לבסוף, השתמש באופרטור GRestore כדי לשמור את מצב הגרפיקה המעודכן.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).
הקטע הבא בקוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

הקטע הבא בקוד מראה כיצד להשתמש באופרטורים של PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// הגדרת קואורדינטות
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// קבל את הדף שבו יש להוסיף תמונה
Page page = pdfDocument.Pages[1];
// טען תמונה לזרם
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// הוסף תמונה לאוסף התמונות של משאבי הדף
page.Resources.Images.Add(imageStream);
// שימוש באופרטור GSave: אופרטור זה שומר את מצב הגרפיקה הנוכחי
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// צור אובייקטים מסוג מלבן ומטריצה
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// שימוש באופרטור ConcatenateMatrix (שרשור מטריצות): מגדיר איך תמונה צריכה להיות ממוקמת
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// שימוש באופרטור Do: אופרטור זה מצייר תמונה
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// שימוש באופרטור GRestore: אופרטור זה משחזר מצב גרפיקה
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir);
```
## שרטוט XForm על דף באמצעות אופרטורים

נושא זה מדגים איך להשתמש באופרטורים GSave/GRestore, באופרטור ContatenateMatrix למיקום xForm ובאופרטור Do כדי לשרטט xForm על דף.

הקוד למטה מעטף תוכן קיים בקובץ PDF באמצעות זוג האופרטורים GSave/GRestore. גישה זו עוזרת לקבל את מצב הגרפיקה ההתחלתי בסוף התוכן הקיים. בלי גישה זו, ייתכן שישארו המרות לא רצויות בסוף שרשרת האופרטורים הקיימת.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לבקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // הדגמת שימוש באופרטורים GSave/GRestore
    // שימוש באופרטור ContatenateMatrix למיקום xForm
    // שימוש באופרטור Do לשרטוט xForm על דף

    // עטיפת תוכן קיים עם זוג אופרטורים GSave/GRestore
    //        זה כדי לקבל מצב גרפיקה התחלתי בסוף התוכן הקיים
    //        אחרת ייתכן שישארו המרות לא רצויות בסוף שרשרת האופרטורים הקיימת
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // הוספת אופרטור שמירת מצב גרפיקה לניקוי נכון של מצב הגרפיקה לאחר פקודות חדשות
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region יצירת xForm

    // יצירת xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // הגדרת רוחב וגובה תמונה
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // טעינת תמונה לזרם
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // הוספת תמונה לאוסף התמונות של משאבי XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // שימוש באופרטור Do: אופרטור זה משרטט תמונה
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // מיקום הטופס בקואורדינטות x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // שרטוט הטופס עם אופרטור Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // מיקום הטופס בקואורדינטות x=100 y=300
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // שרטוט הטופס עם אופרטור Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // שחזור מצב גרפיקה עם GRestore לאחר GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## הסרת אובייקטי גרפיקה באמצעות מחלקות אופרטור

מחלקות האופרטור מספקות יכולות נהדרות למניפולציה של קבצי PDF. כאשר קובץ PDF מכיל גרפיקה שלא ניתן להסיר באמצעות שיטת [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) של המחלקה [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), ניתן להשתמש במחלקות האופרטור כדי להסיר אותה במקום זאת.

הקטע קוד הבא מראה כיצד להסיר גרפיקה. יש לשים לב, אם קובץ ה-PDF מכיל תוויות טקסט לגרפיקה, יתכן שהן ימשיכו להופיע בקובץ ה-PDF בעקבות שימוש בשיטה זו. לכן, יש לחפש באופרטורים הגרפיים שיטה חלופית למחיקת תמונות כאלה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// שימוש באופרטורים לציור דרך
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF ל-.NET",
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

