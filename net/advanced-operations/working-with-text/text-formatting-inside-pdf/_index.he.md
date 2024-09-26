---
title: עיצוב טקסט בתוך PDF באמצעות C#
linktitle: עיצוב טקסט בתוך PDF
type: docs
weight: 30
url: /net/text-formatting-inside-pdf/
description: דף זה מסביר כיצד לעצב טקסט בתוך קובץ PDF שלך. כולל הוספת כניסה בשורה, הוספת מסגרת טקסט, הוספת קו תחתון לטקסט, וכו'.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עיצוב טקסט בתוך PDF באמצעות C#",
    "alternativeHeadline": "כיצד לעצב טקסט בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, עיצוב טקסט ב-pdf",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "דף זה מסביר כיצד לעצב טקסט בתוך קובץ PDF שלך. כולל הוספת כניסה בשורה, הוספת מסגרת טקסט, הוספת קו תחתון לטקסט, וכו'."
}
</script>
הקטע הבא בקוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## איך להוסיף הזחת שורה ל-PDF

Aspose.PDF עבור .NET מציע את התכונה SubsequentLinesIndent בתוך המחלקה [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). ניתן להשתמש בה כדי לציין הזחת שורות בתרחישי יצירת PDF עם אוסף TextFragment ו-Paragraphs.

אנא השתמש בקטע הקוד הבא כדי להשתמש בתכונה:

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לגשת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// יצירת אובייקט מסמך חדש
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// אתחול אפשרויות עיצוב טקסט עבור קטע הטקסט וציון ערך SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```

## איך להוסיף מסגרת לטקסט

הקוד הבא מראה, איך להוסיף מסגרת לטקסט באמצעות TextBuilder והגדרת המאפיין DrawTextRectangleBorder של TextState:

```csharp
// לדוגמאות מלאות וקבצי נתונים, בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// יצירת אובייקט מסמך חדש
Document pdfDocument = new Document();
// קבלת דף מסוים
Page pdfPage = (Page)pdfDocument.Pages.Add();
// יצירת קטע טקסט
TextFragment textFragment = new TextFragment("טקסט ראשי");
textFragment.Position = new Position(100, 600);
// הגדרת מאפייני טקסט
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// הגדרת מאפיין StrokingColor לציור מסגרת (קווי מתאר) סביב המלבן של הטקסט
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// הגדרת ערך המאפיין DrawTextRectangleBorder ל true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// שמירת המסמך
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## איך להוסיף טקסט עם קו תחתון

הקטע הבא מדגים איך להוסיף טקסט עם קו תחתון בעת יצירת קובץ PDF חדש.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// צור אובייקט מסמך
Document pdfDocument = new Document();
// הוסף עמוד למסמך PDF
pdfDocument.Pages.Add();
// צור TextBuilder לעמוד הראשון
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment עם טקסט לדוגמה
TextFragment fragment = new TextFragment("Test message");
// הגדר את הגופן עבור TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// הגדר את עיצוב הטקסט כקו תחתון
fragment.TextState.Underline = true;
// ציין את המיקום שבו יש לשים את TextFragment
fragment.Position = new Position(10, 800);
// הוסף את TextFragment לקובץ PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// שמור את המסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
## איך להוסיף מסגרת סביב טקסט שהתווסף

יש לך שליטה על המראה והתחושה של הטקסט שאתה מוסיף. הדוגמה להלן מראה איך להוסיף מסגרת סביב חלק מהטקסט שהוספת על ידי ציור מלבן סביבו. למידע נוסף על המחלקה [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// שמור את המסמך PDF המתקבל.
editor.Save(dataDir);
```

## איך להוסיף שורה חדשה
## איך להוסיף הזנת שורה חדשה

‏TextFragment אינו תומך בהזנת שורה בתוך הטקסט. עם זאת, על מנת להוסיף טקסט עם הזנת שורה, יש להשתמש ב‏TextFragment עם ‏TextParagraph:

- השתמש ב-"\r\n" או ‏Environment.NewLine ב‏TextFragment במקום "\n" בודד;
- צור אובייקט ‏TextParagraph. זה יוסיף טקסט עם פיצול שורות;
- הוסף את ‏TextFragment עם ‏TextParagraph.AppendLine;
- הוסף את ‏TextParagraph עם ‏TextBuilder.AppendParagraph.
אנא השתמש בקטע הקוד שלהלן.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// אתחל טקסט חדש עם טקסט המכיל את סימני השורה הנדרשים
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// הגדר את תכונות קטע הטקסט אם נדרש
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// צור אובייקט TextParagraph
TextParagraph par = new TextParagraph();

// הוסף קטע טקסט חדש לפסקה
par.AppendLine(textFragment);

// קבע את מיקום הפסקה
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// צור אובייקט TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// הוסף את TextParagraph באמצעות TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// שמור את מסמך PDF המתקבל.
pdfApplicationDoc.Save(dataDir);
```
## איך להוסיף טקסט בקו חוצה

מחלקת TextState מספקת את היכולות להגדיר עיצוב לקטעי טקסט שמוצבים בתוך מסמך PDF. ניתן להשתמש במחלקה זו כדי להגדיר עיצוב טקסט כמו מודגש, נטוי, קו תחתון והחל מהשחרור הזה, ה-API סיפק את היכולות לסמן עיצוב טקסט כקו חוצה. נסה להשתמש בקטע הקוד הבא כדי להוסיף TextFragment עם עיצוב קו חוצה.

אנא השתמש בקטע קוד מלא:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// פתח מסמך
Document pdfDocument = new Document();
// קבל עמוד מסוים
Page pdfPage = (Page)pdfDocument.Pages.Add();

// צור קטע טקסט
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// הגדר מאפייני טקסט
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// הגדר את מאפיין StrikeOut
textFragment.TextState.StrikeOut = true;
// סמן טקסט כמודגש
textFragment.TextState.FontStyle = FontStyles.Bold;

// צור אובייקט TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// הוסף את קטע הטקסט לעמוד PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddStrikeOutText_out.pdf";

// שמור את מסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
## החל צללית גרדיאנט על הטקסט

עיצוב הטקסט הועשר עוד יותר ב-API עבור תרחישים של עריכת טקסט וכעת ניתן להוסיף טקסט עם מרחב צבעים של דוגמה בתוך מסמך PDF. מחלקת Aspose.Pdf.Color הורחבה עוד יותר על ידי הכנסת מאפיין חדש של PatternColorSpace, אשר ניתן להשתמש בו לציון צבעי צללית לטקסט. מאפיין זה מוסיף צלליות גרדיאנט שונות לטקסט לדוגמה צללית צירית, צללית רדיאלית (סוג 3) כפי שמוצג בקטע הקוד הבא:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // יצירת צבע חדש עם מרחב צבעים של דוגמה
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>כדי להחיל גרדיאנט רדיאלי, ניתן להגדיר את המאפיין 'PatternColorSpace' שווה ל-'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' בקטע קוד שלעיל.

## כיצד ליישר טקסט לתוכן צף

Aspose.PDF תומך בהגדרת יישור טקסט לתוכן בתוך אלמנט תיבת צף. ניתן להשתמש במאפייני הישור של מופע Aspose.Pdf.FloatingBox כדי להשיג זאת, כפי שמוצג בדוגמת הקוד הבאה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```

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
    "applicationCategory": "ספריית עיבוד PDF ל.NET",
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

