---
title: تدوير النص داخل PDF باستخدام Python
linktitle: تدوير النص داخل PDF
type: docs
weight: 50
url: /ar/python-net/rotate-text-inside-pdf/
description: تعرف على طرق مختلفة لتدوير النص في PDF. يتيح لك Aspose.PDF تدوير النص إلى أي زاوية، تدوير جزء من النص أو فقرة كاملة.
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تدوير النص داخل PDF باستخدام Python",
    "alternativeHeadline": "كيفية تدوير النص في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, document generation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "تعرف على طرق مختلفة لتدوير النص في PDF. يتيح لك Aspose.PDF تدوير النص إلى أي زاوية، تدوير جزء من النص أو فقرة كاملة."
}
</script>


## تدوير النص داخل ملف PDF باستخدام خاصية التدوير

باستخدام خاصية التدوير في فئة [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment)، يمكنك تدوير النص بزاويا مختلفة. يمكن استخدام تدوير النص في سيناريوهات مختلفة لتوليد المستندات. يمكنك تحديد زاوية التدوير بالدرجات لتدوير النص حسب متطلباتك. يرجى التحقق من السيناريوهات المختلفة التالية، والتي يمكنك من خلالها تنفيذ تدوير النص.

## تنفيذ التدوير باستخدام TextFragment و TextBuilder

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// تهيئة كائن المستند
Document pdfDocument = new Document();
// الحصول على الصفحة المعينة
Page pdfPage = (Page)pdfDocument.Pages.Add();
// إنشاء جزء نصي
TextFragment textFragment1 = new TextFragment("النص الرئيسي");
textFragment1.Position = new Position(100, 600);
// تعيين خصائص النص
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// إنشاء جزء نصي مدوّر
TextFragment textFragment2 = new TextFragment("النص المدور");
textFragment2.Position = new Position(200, 600);
// تعيين خصائص النص
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// إنشاء جزء نصي مدوّر
TextFragment textFragment3 = new TextFragment("النص المدور");
textFragment3.Position = new Position(300, 600);
// تعيين خصائص النص
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// إضافة الجزء النصي إلى صفحة الـ PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// حفظ المستند
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## تنفيذ الدوران باستخدام TextParagraph و TextBuilder (القطع الدوارة)

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// تهيئة كائن الوثيقة
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// إنشاء جزء نصي
TextFragment textFragment1 = new TextFragment("نص مدور");
// تعيين خصائص النص
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// تعيين الدوران
textFragment1.TextState.Rotation = 45;
// إنشاء جزء نصي
TextFragment textFragment2 = new TextFragment("النص الرئيسي");
// تعيين خصائص النص
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// إنشاء جزء نصي
TextFragment textFragment3 = new TextFragment("نص مدور آخر");
// تعيين خصائص النص
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// تعيين الدوران
textFragment3.TextState.Rotation = -45;
// إضافة الأجزاء النصية إلى الفقرة
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// إضافة الفقرة النصية إلى صفحة PDF
textBuilder.AppendParagraph(paragraph);
// حفظ الوثيقة
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## تنفيذ التدوير باستخدام TextFragment و Page.Paragraphs

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// تهيئة كائن الوثيقة
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();
// إنشاء جزء نصي
TextFragment textFragment1 = new TextFragment("main text");
// تعيين خصائص النص
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// إنشاء جزء نصي
TextFragment textFragment2 = new TextFragment("rotated text");
// تعيين خصائص النص
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// تعيين التدوير
textFragment2.TextState.Rotation = 315;
// إنشاء جزء نصي
TextFragment textFragment3 = new TextFragment("rotated text");
// تعيين خصائص النص
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// تعيين التدوير
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// حفظ الوثيقة
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## تنفيذ التدوير باستخدام TextParagraph وTextBuilder (تدوير الفقرة بالكامل)

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// تهيئة كائن المستند
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // تحديد التدوير
    paragraph.Rotation = i * 90 + 45;
    // إنشاء جزء نصي
    TextFragment textFragment1 = new TextFragment("نص الفقرة");
    // إنشاء جزء نصي
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // إنشاء جزء نصي
    TextFragment textFragment2 = new TextFragment("السطر الثاني من النص");
    // تعيين خصائص النص
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // إنشاء جزء نصي
    TextFragment textFragment3 = new TextFragment("والمزيد من النص...");
    // تعيين خصائص النص
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // إنشاء كائن TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // إلحاق الجزء النصي بصفحة PDF
    textBuilder.AppendParagraph(paragraph);
}
// حفظ المستند
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لمكتبة .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>