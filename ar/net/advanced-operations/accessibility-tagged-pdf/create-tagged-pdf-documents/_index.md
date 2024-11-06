---
title: إنشاء PDF موسوم باستخدام C#
linktitle: إنشاء PDF موسوم
type: docs
weight: 10
url: ar/net/create-tagged-pdf/
description: يشرح هذا المقال كيفية إنشاء عناصر الهيكل لمستند PDF موسوم برمجيًا باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إنشاء PDF موسوم باستخدام C#",
    "alternativeHeadline": "كيفية إنشاء PDF موسوم",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "إنشاء, موسوم, pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق توثيق Aspose.PDF",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية إنشاء عناصر الهيكل لمستند PDF موسوم برمجيًا باستخدام Aspose.PDF لـ .NET."
}
</script>
إن إنشاء PDF موسوم يعني إضافة (أو إنشاء) عناصر معينة إلى الوثيقة والتي ستمكّن الوثيقة من المصادقة عليها وفقًا لمتطلبات PDF/UA. تسمى هذه العناصر غالبًا بعناصر الهيكل.

يعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إنشاء PDF موسوم (سيناريو بسيط)

من أجل إنشاء عناصر الهيكل في وثيقة PDF موسومة، تقدم Aspose.PDF طرقًا لإنشاء عنصر هيكل باستخدام واجهة [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). يوضح الشفرة التالية كيفية إنشاء PDF موسوم يحتوي على عنصرين: رأس وفقرة.

```csharp
private static void CreateTaggedPdfDocument01()
{
    // إنشاء وثيقة PDF
    var document = new Document();

    // الحصول على المحتوى للعمل مع TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // تعيين العنوان واللغة للوثيقة
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

    // حفظ وثيقة PDF الموسومة
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```
سنحصل على الوثيقة التالية بعد الإنشاء:

![وثيقة PDF موسومة بعنصرين - رأس وفقرة](taggedpdf-01.png)

## إنشاء PDF موسوم بعناصر متداخلة (إنشاء شجرة عناصر البنية)

في بعض الحالات، نحتاج إلى إنشاء بنية أكثر تعقيداً، مثل وضع اقتباسات في فقرة.
لإنشاء شجرة عناصر البنية يجب استخدام طريقة [AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild).
يوضح الجزء التالي من الكود كيفية إنشاء شجرة عناصر بنية لوثيقة PDF الموسومة:

```csharp
private static void CreateTaggedPdfDocument02()
{
    // إنشاء وثيقة PDF
    var document = new Document();

    // الحصول على المحتوى للعمل مع TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // تعيين العنوان واللغة للوثيقة
    taggedContent.SetTitle("وثيقة PDF موسومة");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("مستوى الرأس 1");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    paragraphWithQuotes.StructureTextState.MarginInfo = new MarginInfo(10, 5, 10, 5);

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

    // حفظ وثيقة PDF الموسومة
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```
سنحصل على الوثيقة التالية بعد الإنشاء:
![وثيقة PDF موسومة بعناصر متداخلة - span و quotes](taggedpdf-02.png)

## تنسيق هيكل النص

من أجل تنسيق هيكل النص في وثيقة PDF موسومة، تقدم Aspose.PDF خصائص [الخط](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font)، [حجم الخط](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize)، [نمط الخط](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) و [لون الخلفية](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) لفئة [حالة نص الهيكل](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate). يوضح الجزء التالي من الكود كيفية تنسيق هيكل النص في وثيقة PDF موسومة:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء وثيقة Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للوثيقة
taggedContent.SetTitle("وثيقة PDF موسومة");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// تحت التطوير
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("نص أحمر مائل.");

// حفظ وثيقة PDF موسومة
document.Save(dataDir + "StyleTextStructure.pdf");
```
## توضيح عناصر الهيكل

لتوضيح عناصر الهيكل في مستند PDF الموسوم، تقدم Aspose.PDF فئة [IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement). يوضح شظية الكود التالية كيفية توضيح عناصر الهيكل في مستند PDF موسوم:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// تحت التطوير
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "الشكل الأول";
figure1.Title = "الصورة 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// حفظ مستند PDF الموسوم
document.Save(dataDir + "IllustrationStructureElements.pdf");

```
## التحقق من صحة PDF الموسوم

يوفر Aspose.PDF لـ .NET القدرة على التحقق من صحة مستند PDF/UA الموسوم. يدعم التحقق من معيار PDF/UA:

- التحقق من XObjects
- التحقق من الإجراءات
- التحقق من المحتوى الاختياري
- التحقق من الملفات المضمنة
- التحقق من حقول Acroform (التحقق من اللغة الطبيعية والاسم البديل والتواقيع الرقمية)
- التحقق من حقول نموذج XFA
- التحقق من إعدادات الأمان
- التحقق من التنقل
- التحقق من التعليقات التوضيحية

يوضح جزء الكود أدناه كيفية التحقق من صحة مستند PDF الموسوم. سيتم عرض المشاكل المقابلة في تقرير سجل XML.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
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
    "name": "مكتبة Aspose.PDF لـ .NET",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
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

