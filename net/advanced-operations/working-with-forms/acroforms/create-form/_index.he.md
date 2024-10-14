---
title: צור AcroForm - צור PDF מילוי ב-C#
linktitle: צור AcroForm
type: docs
weight: 10
url: /net/create-form/
description: עם Aspose.PDF ל-.NET תוכל ליצור טופס מאפס בקובץ ה-PDF שלך
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "צור AcroForm",
    "alternativeHeadline": "איך ליצור AcroForm ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "ייצור מסמכי PDF",
    "keywords": "pdf, c#, צור acroform",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "עם Aspose.PDF ל-.NET תוכל ליצור טופס מאפס בקובץ ה-PDF שלך"
}
</script>

הקטע הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## יצירת טופס מאפס

### הוספת שדה טופס במסמך PDF

המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) מספקת אוסף בשם [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) שעוזר לך לנהל שדות טופס במסמך PDF.

כדי להוסיף שדה טופס:

1. צור את שדה הטופס שברצונך להוסיף.
1. קרא לשיטת ה-Add של אוסף [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### הוספת TextBoxField

הדוגמה למטה מראה כיצד להוסיף [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// צור שדה
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// הוסף שדה למסמך
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// שמור את ה-PDF ששונה
pdfDocument.Save(dataDir);
```
### הוספת RadioButtonField

הקטעי קוד הבאים מראים איך להוסיף [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) במסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// יצירת אובייקט מסמך
Document pdfDocument = new Document();
// הוספת דף לקובץ PDF
pdfDocument.Pages.Add();
// יצירת אובייקט RadioButtonField עם מספר הדף כארגומנט
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// הוספת אפשרות רדיו ראשונה וגם ציון מקורה באמצעות אובייקט Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// הוספת אפשרות רדיו שנייה
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// הוספת כפתור הרדיו לאובייקט הטופס של אובייקט המסמך
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// שמירת קובץ ה-PDF
pdfDocument.Save(dataDir);
```
הדוגמא שלהלן מציגה את השלבים להוספת RadioButtonField עם שלוש אפשרויות ומיקומן בתוך תאים בטבלה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

opt1.OptionName = "Item1";
opt2.OptionName = "Item2";
opt3.OptionName = "Item3";

opt1.Width = 15;
opt1.Height = 15;
opt2.Width = 15;
opt2.Height = 15;
opt3.Width = 15;
opt3.Height = 15;

rf.Add(opt1);
rf.Add(opt2);
rf.Add(opt3);

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// שמירת קובץ ה-PDF
doc.Save(dataDir);
```

### הוספת כיתוב לשדה RadioButtonField

הקטע הבא מראה איך להוסיף כיתוב שיקשר לשדה RadioButtonField:

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לבקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// טען את טופס PDF המקורי
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Yes";
        fieldoption.PartialName = "Yesname";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // צור אובייקט TextParagraph
        TextParagraph par = new TextParagraph();

        // הגדר את מיקום הפסקה
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // ציין מצב גלילת מילים
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // הוסף TextFragment חדש לפסקה
        par.AppendLine(updatedFragment);

        // הוסף את ה-TextParagraph באמצעות TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### הוספת שדה ComboBox

הקטעי קוד הבאים מראים כיצד להוסיף שדה ComboBox במסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// יצירת אובייקט מסמך
Document doc = new Document();

// הוספת דף לאובייקט המסמך
doc.Pages.Add();

// יצירת אובייקט שדה ComboBox
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// הוספת אופציה ל-ComboBox
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// הוספת אובייקט תיבת ה-ComboBox לאוסף שדות הטופס של אובייקט המסמך
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// שמירת המסמך PDF
doc.Save(dataDir);
```

### הוספת תיאור כלי לשדה טופס

המחלקה Document מספקת אוסף בשם Form שמנהל שדות טופס במסמך PDF.
מחלקת Document מספקת אוסף בשם Form אשר מנהל שדות טופס במסמך PDF.

הדוגמאות הבאות מראות כיצד להוסיף תיאור כלי לשדה טופס, תחילה באמצעות C# ולאחר מכן Visual Basic.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// טען טופס PDF מקורי
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// הגדר את התיאור הכלי עבור textfield
(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// שמור את המסמך המעודכן
doc.Save(dataDir);
```

