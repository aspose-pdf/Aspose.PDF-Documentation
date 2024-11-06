---
title: إضافة ختم نصي في PDF C#
linktitle: ختم نصي في ملف PDF
type: docs
weight: 20
url: ar/net/text-stamps-in-the-pdf-file/
description: أضف ختم نصي إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة ختم نصي في PDF C#",
    "alternativeHeadline": "إضافة ختم نصي في PDF C#",
    "author": {
        "@type": "Person",
        "name":"أندري أندروخوفسكي",
        "givenName": "أندري",
        "familyName": "أندروخوفسكي",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, c#, توليد المستندات",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "أضف ختم نصي إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF لـ .NET."
}
</script>
## إضافة ختم نصي باستخدام C#

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) لإضافة ختم نصي في ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط وغيرها. لإضافة ختم نصي، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الختم في ملف PDF.

يعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يوضح الشفرة التالية كيفية إضافة ختم نصي في ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// إنشاء ختم نصي
TextStamp textStamp = new TextStamp("Sample Stamp");
// تحديد ما إذا كان الختم في الخلفية
textStamp.Background = true;
// تعيين المنشأ
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// تدوير الختم
textStamp.Rotate = Rotation.on90;
// تعيين خصائص النص
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// إضافة ختم إلى صفحة محددة
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// حفظ المستند الناتج
pdfDocument.Save(dataDir);
```
## تعريف محاذاة لكائن TextStamp

إضافة العلامات المائية إلى مستندات PDF هي واحدة من الميزات المطلوبة بشكل متكرر ويتمتع Aspose.PDF لـ .NET بالقدرة الكاملة على إضافة علامات مائية نصية وصورية. لدينا فئة تسمى [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) والتي توفر الميزة لإضافة طوابع نصية فوق ملف PDF. مؤخرًا، كان هناك متطلب لدعم ميزة تحديد محاذاة النص عند استخدام كائن TextStamp. لذا من أجل تلبية هذا المتطلب، قدمنا خاصية TextAlignment في فئة TextStamp. باستخدام هذه الخاصية، يمكننا تحديد محاذاة النص الأفقية.

توضح الأجزاء التالية من الكود مثالاً على كيفية تحميل مستند PDF موجود وإضافة TextStamp فوقه.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// توثيق كائن المستند بملف الإدخال
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// توثيق كائن FormattedText بسلسلة عينة
FormattedText text = new FormattedText("This");
// إضافة سطر نص جديد إلى FormattedText
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// إنشاء كائن TextStamp باستخدام FormattedText
TextStamp stamp = new TextStamp(text);
// تحديد محاذاة النص الأفقية لطابع النص كمركز
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// تحديد محاذاة النص العمودية لطابع النص كمركز
stamp.VerticalAlignment = VerticalAlignment.Center;
// تحديد محاذاة النص الأفقية لطابع النص كمركز
stamp.TextAlignment = HorizontalAlignment.Center;
// تعيين هامش علوي لكائن الطابع
stamp.TopMargin = 20;
// إضافة كائن الطابع فوق الصفحة الأولى من المستند
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// حفظ المستند المحدث
doc.Save(dataDir);
```
## ملء النص المحاط بخط كختم في ملف PDF

لقد قمنا بتنفيذ إعداد وضع العرض لسيناريوهات إضافة وتحرير النص. لتقديم نص محاط بخط، يرجى إنشاء كائن TextState وتعيين RenderingMode إلى TextRenderingMode.StrokeText واختيار لون لخاصية StrokingColor. بعد ذلك، قم بربط TextState بالختم باستخدام الطريقة BindTextState().

يوضح الكود التالي إضافة نص ملء محاط بخط:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// إنشاء كائن TextState لنقل الخصائص المتقدمة
TextState ts = new TextState();
// تعيين لون للخط
ts.StrokingColor = Color.Gray;
// تعيين وضع عرض النص
ts.RenderingMode = TextRenderingMode.StrokeText;
// تحميل وثيقة PDF مدخلة
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// ربط TextState
stamp.BindTextState(ts);
// تعيين الأصل X,Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// إضافة الختم
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
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
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "بريطانيا العظمى",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
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
    "operatingSystem": "ويندوز، ماك أو إس، لينوكس",
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
Sure, I can help translate the document content to Arabic while preserving the markdown format and the specific instructions you provided. However, you'll need to provide the content of the document you want to translate. Please paste or describe the text, and I'll take care of the translation for you.
