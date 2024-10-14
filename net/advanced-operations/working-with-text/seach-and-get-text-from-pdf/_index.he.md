---
title: חיפוש וקבלת טקסט מדפי PDF
linktitle: חיפוש וקבלת טקסט
type: docs
weight: 60
url: /net/search-and-get-text-from-pdf/
description: מאמר זה מסביר כיצד להשתמש בכלים שונים כדי לחפש ולקבל טקסט מ-Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "חיפוש וקבלת טקסט מדפי PDF",
    "alternativeHeadline": "כלים לחיפוש וקבלת טקסט מדפי PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, חיפוש טקסט, קבלת טקסט מ-pdf",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מסביר כיצד להשתמש בכלים שונים כדי לחפש ולקבל טקסט מ-Aspose.PDF עבור .NET."
}
</script>
הקטע הבא של קוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## חיפוש וקבלת טקסט מכל הדפים של מסמך PDF

המחלקה [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) מאפשרת לך למצוא טקסט התואם לביטוי מסוים, מכל דפי מסמך PDF. על מנת לחפש טקסט מכל המסמך, עליך לקרוא לשיטת ה-Accept של אוסף הדפים. שיטת ה-[Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) מקבלת אובייקט TextFragmentAbsorber כפרמטר, שמחזיר אוסף של עצמים מסוג TextFragment. תוכל לעבור על כל הפרגמנטים ולקבל את התכונות שלהם כמו טקסט, מיקום (XIndent, YIndent), שם הגופן, גודל הגופן, האם נגיש, האם משובץ, האם חלקי, צבע קדמי ועוד.

הקטע הבא של קוד מראה לך כיצד לחפש טקסט מכל הדפים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// יצירת אובייקט TextAbsorber למציאת כל המופעים של ביטוי החיפוש המבוקש
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// קבלת ה-absorber לכל הדפים
pdfDocument.Pages.Accept(textFragmentAbsorber);

// קבלת אוסף פרגמנטי הטקסט שהופקו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// חזרה על הפרגמנטים
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```
במקרה שאתה צריך לחפש טקסט בתוך דף PDF מסוים, אנא ציין את מספר הדף מתוך אוסף הדפים של מופע המסמך וקרא למתודת Accept עבור הדף הזה (כפי שמוצג בשורת הקוד למטה).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// קבל את ה-absorber לדף מסוים
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## חפש וקבל קטעי טקסט מכל דפי מסמך PDF

על מנת לחפש קטעי טקסט מכל הדפים, תחילה עליך לקבל את אובייקטי TextFragment מהמסמך.
כדי לחפש קטעי טקסט מכל הדפים, תחילה עליך לקבל את אובייקטי TextFragment מהמסמך.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// צור אובייקט TextAbsorber כדי למצוא את כל המופעים של ביטוי החיפוש המבוקש
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// קבל את ה-absorber לכל הדפים
pdfDocument.Pages.Accept(textFragmentAbsorber);
// קבל את קטעי הטקסט שנמשכו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// עבור על הקטעים
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("טקסט : {0} ", textSegment.Text);
        Console.WriteLine("מיקום : {0} ", textSegment.Position);
        Console.WriteLine("הזזה אופקית : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("הזזה אנכית : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("גופן - שם : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("גופן - נגיש : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("גופן - מוטמע : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("גופן - חלקי : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("גודל גופן : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("צבע קדמי : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```
כדי לחפש ולקבל קטעי טקסט מדף מסוים ב-PDF, עליך לציין את מפתח הדף בעת קריאה לשיטת Accept(..). אנא הסתכל על שורות הקוד הבאות.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// קבל את ה-absorber לכל הדפים
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## חיפוש וקבלת טקסט מכל הדפים באמצעות ביטוי רגולרי

TextFragmentAbsorber מסייע לך לחפש ולאחזר טקסט, מכל הדפים, בהתבסס על ביטוי רגולרי.
TextFragmentAbsorber מאפשר לך לחפש ולאחזר טקסט, מכל הדפים, בהתבסס על ביטוי רגולרי.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא גש ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// צור אובייקט TextAbsorber כדי למצוא את כל הביטויים התואמים לביטוי הרגולרי
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // כמו 1999-2000

// הגדר אפשרות חיפוש טקסט כדי לציין שימוש בביטוי רגולרי
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// קבל את ה-absorber לכל הדפים
pdfDocument.Pages.Accept(textFragmentAbsorber);

// קבל את אוספי קטעי הטקסט שנאספו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// עבור על קטעי הטקסט
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```
```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// על מנת לחפש התאמה מדויקת של מילה, ייתכן ותרצה לשקול שימוש בביטוי רגולרי.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// על מנת לחפש מחרוזת באותיות רישיות או קטנות, ייתכן ותרצה לשקול שימוש בביטוי רגולרי.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// על מנת לחפש את כל המחרוזות (לנתח את כל המחרוזות) בתוך מסמך PDF, אנא נסה להשתמש בביטוי הרגולרי הבא.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// מצא התאמה של מחרוזת החיפוש וקבל כל דבר לאחר המחרוזת עד סיום השורה.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// אנא השתמש בביטוי הרגולרי הבא כדי למצוא טקסט העוקב להתאמת הביטוי הרגולרי.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// על מנת לחפש קישורים/URLs בתוך מסמך PDF, אנא נסה להשתמש בביטוי הרגולרי הבא.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## חיפוש טקסט בהתבסס על Regex והוספת קישור תכני

אם ברצונך להוסיף קישור מעל ביטוי טקסט מסוים בהתבסס על ביטוי רגולרי, ראשית מצא את כל הביטויים התואמים את הביטוי הרגולרי הזה באמצעות TextFragmentAbsorber והוסף מעליהם קישור.

כדי למצוא ביטוי ולהוסיף מעליו קישור:

1. העבר את הביטוי הרגולרי כפרמטר לבנאי TextFragmentAbsorber.
2. צור אובייקט TextSearchOptions שמציין האם משתמשים בביטוי הרגולרי או לא.
3. קבל את הביטויים התואמים לתוך TextFragments.
4. עבור על התוצאות כדי לקבל את הממדים המלבניים שלהם, שנה את צבע הקידמה לכחול (אופציונלי - כדי שיראה כמו קישור וצור קישור באמצעות מחלקת PdfContentEditor ושיטת CreateWebLink(..)).
5. שמור את ה-PDF המעודכן באמצעות שיטת Save של אובייקט Document.
הדוגמה לקוד הבאה מראה איך לחפש טקסט בתוך קובץ PDF באמצעות ביטוי רגולרי ולהוסיף מעליו קישורים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// צור אובייקט מקשר למציאת כל המופעים של ביטוי החיפוש הנתון
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// הפעל חיפוש ביטוי רגולרי
absorber.TextSearchOptions = new TextSearchOptions(true);
// פתח מסמך
PdfContentEditor editor = new PdfContentEditor();
// קשר את קובץ PDF המקורי
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// קבל את המקשר לעמוד
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// עבור על הקטעים
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```
## חפש וצייר מלבן סביב כל קטע טקסט

Aspose.PDF עבור .NET תומך בתכונה לחיפוש וקבלת קואורדינטות של כל תו או קטעי טקסט. כך שכדי להיות בטוחים לגבי הקואורדינטות שמתקבלות עבור כל תו, ייתכן ונשקול להדגיש (להוסיף מלבן) סביב כל תו.

במקרה של פסקת טקסט, ייתכן ותרצה להשתמש בביטוי רגולרי כדי לקבוע את נקודת השבירה של הפסקה ולצייר מלבן סביבה. אנא הסתכל על קטע הקוד הבא. קטע הקוד הבא מקבל קואורדינטות של כל תו ויוצר מלבן סביב כל תו.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתח מסמך
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// צור אובייקט TextAbsorber כדי למצוא את כל הביטויים התואמים את הביטוי הרגולרי

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```
## הדגש כל תו במסמך PDF

{{% alert color="primary" %}}

ניתן לנסות לחפש טקסט במסמך באמצעות Aspose.PDF ולקבל את התוצאות באופן מקוון ב[קישור](https://products.aspose.app/pdf/search) הזה

{{% /alert %}}

Aspose.PDF עבור .NET תומך בתכונה לחיפוש ולקבלת הקואורדינטות של כל תו או קטעי טקסט. לכן, כדי להיות בטוחים לגבי הקואורדינטות שמוחזרות עבור כל תו, ייתכן שנשקול להדגיש (להוסיף מלבן) סביב כל תו. קטע הקוד הבא מקבל את הקואורדינטות של כל תו ויוצר מלבן סביב כל תו.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// צור אובייקט TextAbsorber כדי למצוא את כל המילים
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// קבל את קטעי הטקסט שהופקו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// עבור על הקטעים
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```
## הוספה וחיפוש טקסט חבוי

לפעמים אנחנו רוצים להוסיף טקסט חבוי במסמך PDF ואז לחפש את הטקסט החבוי ולהשתמש במיקומו לעיבוד מחדש. לנוחותכם, Aspose.PDF עבור .NET מספק את היכולות האלה. תוכלו להוסיף טקסט חבוי במהלך יצירת המסמך. כמו כן, תוכלו למצוא טקסט חבוי באמצעות TextFragmentAbsorber. לשם הוספת טקסט חבוי, הגדירו את TextState.Invisible ל-‘true’ עבור הטקסט שהוספתם. TextFragmentAbsorber מוצא את כל הטקסט שמתאים לתבנית (אם צוינה). זוהי התנהגות ברירת המחדל שאינה ניתנת לשינוי. כדי לוודא שהטקסט שנמצא הוא באמת בלתי נראה, ניתן להשתמש בתכונת TextState.Invisible. קטע הקוד להלן מראה כיצד להשתמש בתכון הזה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//יצירת מסמך עם טקסט חבוי
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("זהו טקסט רגיל.");
TextFragment frag2 = new TextFragment("זהו טקסט בלתי נראה.");

//הגדרת תכונת טקסט - בלתי נראה
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//חיפוש טקסט במסמך
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //עשייה משהו עם הקטעים
    Console.WriteLine("טקסט '{0}' במיקום {1} נסתרות: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## חיפוש טקסט עם Regex ב-.NET

Aspose.PDF עבור .NET מספקת את היכולת לחפש מסמכים באמצעות אפשרות ה-Regex הסטנדרטית של .NET. ניתן להשתמש ב-TextFragmentAbsorber למטרה זו כפי שמוצג בדוגמת הקוד למטה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// יצירת אובייקט Regex למציאת כל המילים
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// פתיחת מסמך
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// קבלת עמוד מסוים
Page page = document.Pages[1];

// יצירת אובייקט TextAbsorber למציאת כל המופעים של ה-regex המוזן
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// אישור ה-absorber לעמוד
page.Accept(textFragmentAbsorber);

// קבלת אוספי קטעי הטקסט שהופקו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// לולאה דרך הקטעים
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
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

