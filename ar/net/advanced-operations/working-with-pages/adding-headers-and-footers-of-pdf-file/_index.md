---
title: إضافة رأس وتذييل إلى ملف PDF
linktitle: إضافة رأس وتذييل إلى ملف PDF
type: docs
weight: 70
url: /ar/net/add-headers-and-footers-of-pdf-file/
description: يسمح لك Aspose.PDF لـ .NET بإضافة رأس وتذييل إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة رأس وتذييل إلى ملف PDF",
    "alternativeHeadline": "كيفية إضافة رأس وتذييل إلى ملف PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, إضافة رأس, إضافة تذييل في pdf",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "يسمح لك Aspose.PDF لـ .NET بإضافة رأس وتذييل إلى ملف PDF الخاص بك باستخدام فئة TextStamp."
}
</script>
**Aspose.PDF لـ .NET** يتيح لك إضافة رأس وتذييل في ملف PDF الخاص بك. يمكنك إضافة صور أو نص إلى مستند PDF. كما يمكنك محاولة إضافة رؤوس مختلفة في ملف PDF واحد باستخدام C#.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة نص في رأس ملف PDF

يمكنك استخدام الفئة [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) لإضافة نص في رأس ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط وغيرها. من أجل إضافة نص في الرأس، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة النص في رأس ملف PDF.

تحتاج إلى تعيين خاصية TopMargin بطريقة تضبط النص في منطقة الرأس لملف PDF الخاص بك. كما تحتاج إلى تعيين HorizontalAlignment إلى Center و VerticalAlignment إلى Top. 

الشفرة التالية تظهر لك كيفية إضافة نص في رأس ملف PDF باستخدام C#.
```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// إنشاء رأس الصفحة
TextStamp textStamp = new TextStamp("نص الرأس");
// ضبط خصائص الطابع
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// إضافة رأس إلى جميع الصفحات
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// حفظ المستند المحدث
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## إضافة نص في تذييل ملف PDF

يمكنك استخدام فئة TextStamp لإضافة نص في تذييل ملف PDF.
يمكنك استخدام فئة TextStamp لإضافة نص في تذييل ملف PDF.

{{% alert color="primary" %}}

تحتاج إلى ضبط خاصية الهامش السفلي بطريقة تضبط النص في منطقة التذييل لملف PDF الخاص بك. يجب عليك أيضًا ضبط التوجيه الأفقي على الوسط والتوجيه الرأسي على الأسفل

{{% /alert %}}

يوضح الكود التالي كيفية إضافة نص في تذييل ملف PDF باستخدام C#.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// إنشاء تذييل
TextStamp textStamp = new TextStamp("نص التذييل");
// تعيين خصائص الطابع
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// إضافة التذييل على جميع الصفحات
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// حفظ الملف الناتج
pdfDocument.Save(dataDir + "TextinFooter_out.pdf");
```

## إضافة صورة في رأس ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) لإضافة صورة في رأس ملف PDF. توفر فئة الطابع الصوري خصائص ضرورية لإنشاء طابع قائم على الصورة مثل حجم الخط، نمط الخط، ولون الخط وغيرها. لإضافة صورة في الرأس، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) الخاصة بالصفحة لإضافة الصورة في رأس الPDF.

{{% alert color="primary" %}}

تحتاج إلى ضبط خاصية TopMargin بطريقة تعدل الصورة في منطقة الرأس لملف PDF الخاص بك. يجب عليك أيضاً ضبط HorizontalAlignment على Center و VerticalAlignment على Top.

{{% /alert %}}

يظهر الجزء التالي من الشفرة كيفية إضافة صورة في رأس ملف PDF باستخدام C#.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// إنشاء رأس
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// ضبط خصائص الطابع
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// إضافة رأس لجميع الصفحات
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// حفظ الملف الناتج
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## إضافة صورة في تذييل ملف PDF

يمكنك استخدام فئة ختم الصورة لإضافة صورة في تذييل ملف PDF. توفر فئة ختم الصورة الخصائص اللازمة لإنشاء ختم يعتمد على الصورة مثل حجم الخط، ونمط الخط، ولون الخط وغيرها. لإضافة صورة في التذييل، تحتاج إلى إنشاء كائن مستند وكائن ختم صورة باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الصورة في تذييل PDF.

{{% alert color="primary" %}}

تحتاج إلى ضبط خاصية [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) بطريقة تضبط الصورة في منطقة التذييل لملف PDF الخاص بك. يجب عليك أيضًا ضبط [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) على `Center` و [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) على `Bottom`.

{{% /alert %}}

يظهر الجزء التالي من الكود كيفية إضافة صورة في تذييل ملف PDF باستخدام C#.
الشفرة التالية توضح لك كيفية إضافة صورة في تذييل ملف PDF باستخدام C#.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// إنشاء تذييل
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// تعيين خصائص الطابع
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// إضافة تذييل على جميع الصفحات
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// حفظ الملف الناتج
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## إضافة رؤوس مختلفة في ملف PDF واحد

نعلم أننا يمكن أن نضيف TextStamp في قسم الرأس/التذييل من المستند باستخدام خصائص TopMargin أو Bottom Margin، ولكن أحيانًا قد يكون لدينا متطلب لإضافة رؤوس/تذييلات متعددة في مستند PDF واحد.
نعلم أنه يمكننا إضافة TextStamp في قسم الرأس/التذييل للمستند باستخدام خصائص TopMargin أو Bottom Margin، لكن في بعض الأحيان قد يكون لدينا متطلب لإضافة عدة رؤوس/تذييلات في مستند PDF واحد.

لتحقيق هذا المطلب، سنقوم بإنشاء كائنات TextStamp فردية (عدد الكائنات يعتمد على عدد الرؤوس/التذييلات المطلوبة) وسنضيفها إلى مستند PDF. قد نحدد أيضًا معلومات تنسيق مختلفة لكل كائن طابع. في المثال التالي، قمنا بإنشاء كائن Document وثلاث كائنات TextStamp ثم استخدمنا طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) الخاصة بالصفحة لإضافة النص في قسم الرأس من ملف PDF. يوضح قطعة الكود التالية كيفية إضافة صورة في تذييل ملف PDF باستخدام Aspose.PDF لـ .NET.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح مستند المصدر
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// إنشاء ثلاثة طوابع
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Header 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Header 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Header 3");

// تعيين محاذاة الطابع (وضع الطابع في أعلى الصفحة، مركزًا أفقيًا)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// تحديد نمط الخط كغامق
stamp1.TextState.FontStyle = FontStyles.Bold;
// تعيين معلومات لون الخلفية للنص كأحمر
stamp1.TextState.ForegroundColor = Color.Red;
// تحديد حجم الخط كـ 14
stamp1.TextState.FontSize = 14;

// الآن نحتاج إلى تعيين محاذاة الطابع الثاني رأسيًا كأعلى
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// تعيين معلومات محاذاة أفقية للطابع كمركز
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// تعيين عامل التكبير لكائن الطابع
stamp2.Zoom = 10;

// تعيين تنسيق كائن الطابع الثالث
// تحديد معلومات محاذاة رأسية لكائن الطابع كأعلى
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// تعيين معلومات محاذاة أفقية لكائن الطابع كمركز
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// تعيين زاوية الدوران لكائن الطابع
stamp3.RotateAngle = 35;
// تعيين اللون الوردي كلون خلفية للطابع
stamp3.TextState.BackgroundColor = Color.Pink;
// تغيير معلومات نوع الخط للطابع إلى Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// يتم إضافة الطابع الأول في الصفحة الأولى؛
doc.Pages[1].AddStamp(stamp1);
// يتم إضافة الطابع الثاني في الصفحة الثانية؛
doc.Pages[2].AddStamp(stamp2);
// يتم إضافة الطابع الثالث في الصفحة الثالثة.
doc.Pages[3].AddStamp(stamp3);
// حفظ المستند المحدث
doc.Save(dataDir + "MultiHeader_out.pdf");
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
    "applicationCategory": "مكتبة التعامل مع ملفات PDF لـ .NET",
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

