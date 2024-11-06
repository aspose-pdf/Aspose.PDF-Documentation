---
title: إضافة ختم صورة في PDF باستخدام C#
linktitle: ختم الصور في ملف PDF
type: docs
weight: 10
url: ar/net/image-stamps-in-pdf-page/
description: أضف ختم الصورة في مستند PDF باستخدام فئة ImageStamp مع مكتبة Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة ختم صورة في PDF باستخدام C#",
    "alternativeHeadline": "إضافة ختم صورة في PDF باستخدام C#",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "أضف ختم الصورة في مستند PDF باستخدام فئة ImageStamp مع مكتبة Aspose.PDF."
}
</script>
## إضافة ختم صورة في ملف PDF

يمكنك استخدام فئة ImageStamp لإضافة ختم صورة إلى ملف PDF. توفر فئة ImageStamp الخصائص اللازمة لإنشاء ختم يعتمد على الصورة، مثل الارتفاع، العرض، الشفافية وما إلى ذلك.

الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

لإضافة ختم صورة:

1. قم بإنشاء كائن Document وكائن ImageStamp باستخدام الخصائص المطلوبة.
1. استدعِ طريقة AddStamp للفئة Page لإضافة الختم إلى ملف PDF.

توضح الشفرة التالية كيفية إضافة ختم صورة في ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// إنشاء ختم الصورة
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// إضافة ختم إلى صفحة معينة
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// حفظ المستند الناتج
pdfDocument.Save(dataDir);
```
## التحكم في جودة الصورة عند إضافة ختم

عند إضافة صورة ككائن ختم، يمكنك التحكم في جودة الصورة. يستخدم خاصية الجودة في فئة ImageStamp لهذا الغرض. تشير إلى جودة الصورة بالنسبة المئوية (القيم الصالحة هي 0..100).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// إنشاء ختم الصورة
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## ختم الصورة كخلفية في صندوق عائم

تتيح لك واجهة برمجة تطبيقات Aspose.PDF إضافة ختم الصورة كخلفية في صندوق عائم.
API Aspose.PDF يتيح لك إضافة ختم صورة كخلفية في صندوق عائم.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// توثيق كائن الوثيقة
Document doc = new Document();
// إضافة صفحة إلى مستند PDF
Page page = doc.Pages.Add();
// إنشاء كائن FloatingBox
FloatingBox aBox = new FloatingBox(200, 100);
// تحديد الموضع الأيسر لـ FloatingBox
aBox.Left = 40;
// تحديد الموضع العلوي لـ FloatingBox
aBox.Top = 80;
// تحديد محاذاة أفقية لـ FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// إضافة جزء نص إلى مجموعة فقرات FloatingBox
aBox.Paragraphs.Add(new TextFragment("main text"));
// تعيين حدود لـ FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// إضافة صورة خلفية
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// تعيين لون خلفية لـ FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// إضافة FloatingBox إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(aBox);
// حفظ مستند PDF
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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

