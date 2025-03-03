---
title: יצירת PDF מתויג באמצעות C#
linktitle: יצירת PDF מתויג
type: docs
weight: 10
url: /ar/net/create-tagged-pdf/
description: מאמר זה מסביר כיצד ליצור אלמנטים מובנים עבור מסמך PDF מתויג תוכניתית באמצעות Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "יצירת PDF מתויג באמצעות C#",
    "alternativeHeadline": "איך ליצור PDF מתויג",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "יצירה, מתויג, PDF",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מסביר איך ליצור אלמנטים מובנים למסמך PDF מתויג באופן תוכניתי באמצעות Aspose.PDF עבור .NET."
}
</script>
יצירת PDF מתויג פירושה להוסיף (או ליצור) אלמנטים מסוימים למסמך שיאפשרו לוודא את המסמך בהתאם לדרישות PDF/UA. לאלמנטים אלו קוראים לעיתים אלמנטי מבנה.

הקטע קוד הבא פועל גם עם ספריית [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## יצירת PDF מתויג (תרחיש פשוט)

על מנת ליצור אלמנטי מבנה במסמך PDF מתויג, Aspose.PDF מציעה שיטות ליצירת אלמנט מבנה באמצעות ממשק [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). הקטע קוד הבא מראה איך ליצור PDF מתויג שמכיל שני אלמנטים: כותרת ראשית ופסקה.

```csharp
private static void CreateTaggedPdfDocument01()
{
    // יצירת מסמך PDF
    var document = new Document();

    // קבלת תוכן לעבודה עם TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // הגדרת כותרת ושפה למסמך
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // 
    HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("Main Header");

    ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
    "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
    "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
    "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
    "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
    "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
    "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
    "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
    "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // שמירת מסמך PDF מתויג
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```
נקבל את המסמך הבא לאחר יצירתו:

![מסמך PDF עם תיוג עם 2 אלמנטים - כותרת ופסקה](taggedpdf-01.png)

## יצירת מסמך PDF עם תיוג עם אלמנטים מקוננים (יצירת עץ אלמנטים של מבנה)

במקרים מסוימים, אנו צריכים ליצור מבנה מורכב יותר, לדוגמה, להציב ציטוטים בפסקה.
כדי ליצור עץ אלמנטים של מבנה עלינו להשתמש בשיטת [AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild).
קטע הקוד הבא מראה כיצד ליצור עץ אלמנטים של מבנה של מסמך PDF עם תיוג:

```csharp
private static void CreateTaggedPdfDocument02()
{
    // יצירת מסמך Pdf
    var document = new Document();

    // קבלת תוכן לעבודה עם TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // הגדרת כותרת ושפה למסמך
    taggedContent.SetTitle("מסמך PDF עם תיוג");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("רמת כותרת 1");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    // Adjust position
    paragraphWithQuotes.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
        {
            Margin = new Aspose.Pdf.MarginInfo(10, 5, 10, 5)
        });

    SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
    SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // שמירת מסמך PDF עם תיוג
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```
נראה את המסמך הבא לאחר יצירה:
![מסמך PDF מתויג עם אלמנטים מקוננים - span ומרכאות](taggedpdf-02.png)

## עיצוב מבנה טקסט

כדי לעצב מבנה טקסט במסמך PDF מתויג, Aspose.PDF מציע את התכונות [Font](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font), [FontSize](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize), [FontStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) ו-[ForegroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) של מחלקת [StructureTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate). קטע הקוד הבא מראה כיצד לעצב מבנה טקסט במסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת מסמך PDF
Document document = new Document();

// קבלת תוכן לעבודה עם TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// הגדרת כותרת ושפה למסמך
taggedContent.SetTitle("מסמך PDF מתויג");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// בפיתוח
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("טקסט אדום נטוי.");

// שמירת מסמך PDF מתויג
document.Save(dataDir + "StyleTextStructure.pdf");
```
## המחשת אלמנטים מבניים

על מנת להמחיש אלמנטים מבניים במסמך PDF מתויג, Aspose.PDF מציעה את המחלקה [IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement). הקטע הבא מציג כיצד להמחיש אלמנטים מבניים במסמך PDF מתויג:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת מסמך PDF
Document document = new Document();

// קבלת תוכן לעבודה עם PDF מתויג
ITaggedContent taggedContent = document.TaggedContent;

// הגדרת כותרת ושפה למסמך
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// תחת פיתוח
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "דמות אחת";
figure1.Title = "תמונה 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// שמירת מסמך PDF מתויג
document.Save(dataDir + "IllustrationStructureElements.pdf");

```

## אימות PDF מתויג

Aspose.PDF עבור .NET מספקת את היכולת לאמת מסמך PDF/UA מתויג. אימות תקן PDF/UA תומך:

- בדיקות עבור XObjects
- בדיקות עבור Actions
- בדיקות עבור תוכן אופציונלי
- בדיקות עבור קבצים מוטמעים
- בדיקות עבור שדות Acroform (אימות שפה טבעית ושם חלופי וחתימות דיגיטליות)
- בדיקות עבור שדות טופס XFA
- בדיקות עבור הגדרות אבטחה
- בדיקות עבור ניווט
- בדיקות עבור הערות

הקטע קוד להלן מראה איך לבצע אימות של מסמך PDF מתויג. בעיות תואמות יוצגו בדו"ח הלוג ב-XML.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inputFileName = dataDir + "StructureElements.pdf";
string outputLogName = dataDir + "ua-20.xml";

using (var document = new Aspose.Pdf.Document(inputFileName))
{
    bool isValid = document.Validate(outputLogName, Aspose.Pdf.PdfFormat.PDF_UA_1);

}
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

