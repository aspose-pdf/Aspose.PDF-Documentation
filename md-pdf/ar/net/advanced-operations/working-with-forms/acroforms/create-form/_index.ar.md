---
title: Create AcroForm - Create Fillable PDF in C#
linktitle: Create AcroForm
type: docs
weight: 10
url: /net/create-form/
description: مع Aspose.PDF لـ .NET يمكنك إنشاء استمارة من البداية في ملف PDF الخاص بك
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create AcroForm",
    "alternativeHeadline": "كيفية إنشاء AcroForm في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, إنشاء acroform",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "مع Aspose.PDF لـ .NET يمكنك إنشاء استمارة من البداية في ملف PDF الخاص بك"
}
</script>
الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إنشاء نموذج من البداية

### إضافة حقل نموذج في مستند PDF

توفر فئة [الوثيقة](https://reference.aspose.com/pdf/net/aspose.pdf/document) مجموعة تُسمى [النموذج](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) التي تساعدك في إدارة حقول النموذج في مستند PDF.

لإضافة حقل نموذج:

1. قم بإنشاء حقل النموذج الذي ترغب في إضافته.
1. استدعي طريقة الإضافة لمجموعة [النموذج](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### إضافة حقل نصي

يوضح المثال أدناه كيفية إضافة [حقل نصي](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// إنشاء حقل
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "مربع النص";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// إضافة الحقل إلى المستند
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// حفظ PDF المعدل
pdfDocument.Save(dataDir);
```

### إضافة RadioButtonField

الأكواد التالية توضح كيفية إضافة [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) في مستند PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// إنشاء كائن Document
Document pdfDocument = new Document();
// إضافة صفحة إلى ملف PDF
pdfDocument.Pages.Add();
// توظيف كائن RadioButtonField مع رقم الصفحة كحجة
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// إضافة خيار الزر الأول وتحديد موقعه باستخدام كائن Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// إضافة خيار زر الراديو الثاني
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// إضافة زر الراديو إلى كائن النموذج من كائن المستند
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// حفظ ملف PDF
pdfDocument.Save(dataDir);
```
الشفرة التالية توضح الخطوات لإضافة حقل RadioButton مع ثلاث خيارات ووضعها داخل خلايا الجدول.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
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
// حفظ ملف PDF
doc.Save(dataDir);
```
### إضافة تسمية إلى RadioButtonField

يوضح الجزء التالي من الكود كيفية إضافة تسمية سترتبط بـ RadioButtonField:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// تحميل نموذج PDF المصدر
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

        // إنشاء كائن TextParagraph
        TextParagraph par = new TextParagraph();

        // تحديد موقع الفقرة
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // تحديد وضع التفاف الكلمات
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // إضافة TextFragment جديد إلى الفقرة
        par.AppendLine(updatedFragment);

        // إضافة TextParagraph باستخدام TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### إضافة حقل ComboBox

توضح أجزاء الشفرة التالية كيفية إضافة حقل ComboBox في مستند PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// إنشاء كائن المستند
Document doc = new Document();

// إضافة صفحة إلى كائن المستند
doc.Pages.Add();

// توضيح كائن حقل ComboBox
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// إضافة خيار إلى ComboBox
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// إضافة كائن صندوق التحرير والسرد إلى مجموعة حقول النموذج لكائن المستند
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// حفظ مستند PDF
doc.Save(dataDir);
```

### إضافة تلميح إلى حقل النموذج

توفر فئة الوثيقة مجموعة تُسمى Form تدير حقول النموذج في مستند PDF.
فئة Document توفر مجموعة تسمى Form تدير حقول النماذج في مستند PDF.

الأمثلة التالية توضح كيفية إضافة تلميح أدوات إلى حقل النموذج، أولاً باستخدام C# ثم Visual Basic.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// تحميل نموذج PDF مصدر
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// تعيين التلميح للحقل النصي
(doc.Form["textbox1"] as Field).AlternateName = "تلميح صندوق النص";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// حفظ المستند المُحدث
doc.Save(dataDir);
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

