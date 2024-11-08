---
title: تحديث الروابط في ملف PDF
linktitle: تحديث الروابط
type: docs
weight: 20
url: /ar/net/update-links/
description: تحديث الروابط في ملف PDF برمجيًا. هذا الدليل يتعلق بكيفية تحديث الروابط في ملف PDF بلغة C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تحديث الروابط في ملف PDF",
    "alternativeHeadline": "كيفية تحديث الروابط في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, c#, تحديث الرابط في ملف pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "تحديث الروابط في ملف PDF برمجيًا. هذا الدليل يتعلق بكيفية تحديث الروابط في ملف PDF بلغة C#."
}
</script>
يعمل الجزء التالي من الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## تحديث الروابط في ملف PDF

كما نوقش في إضافة ارتباط تشعبي في ملف PDF، فإن فئة [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) تتيح إمكانية إضافة روابط في ملف PDF. هناك أيضًا فئة مشابهة تُستخدم للحصول على الروابط الموجودة داخل ملفات PDF. استخدم هذا إذا كنت بحاجة لتحديث رابط موجود. لتحديث رابط موجود:

1. تحميل ملف PDF.
1. انتقل إلى صفحة معينة في ملف PDF.
1. حدد وجهة الرابط باستخدام خاصية Destination لكائن [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction).
1. يتم تحديد صفحة الوجهة باستخدام منشئ [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination).

### تعيين هدف الرابط إلى صفحة في نفس المستند

يظهر الجزء التالي من الكود كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى الصفحة الثانية من المستند.
يوضح الجزء التالي من الكود كيفية تحديث رابط في ملف PDF وتحديد هدفه إلى الصفحة الثانية من المستند.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// تحميل ملف PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// الحصول على أول تعليق توضيحي للرابط من الصفحة الأولى للمستند
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// تعديل الرابط: تغيير وجهة الرابط
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// تحديد وجهة لكائن الرابط
// الوسيطة الأولى هي كائن المستند، والثانية هي رقم صفحة الوجهة.
// الوسيطة الخامسة هي عامل التكبير عند عرض الصفحة المعنية. عند استخدام 2، سيتم عرض الصفحة بتكبير 200%
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// حفظ المستند مع الرابط المحدث
doc.Save(dataDir);
```
### تعيين وجهة الرابط إلى عنوان ويب

لتحديث الرابط الهايبرلينك بحيث يشير إلى عنوان ويب، قم بإنشاء كائن [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) ومرره إلى خاصية Action الخاصة بـ LinkAnnotation. يوضح الكود التالي كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى عنوان ويب.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// تحميل ملف PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// الحصول على أول تعليق توضيحي للرابط من أول صفحة من المستند
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// تعديل الرابط: تغيير إجراء الرابط وتعيين الهدف كعنوان ويب
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// حفظ المستند بالرابط المحدث
doc.Save(dataDir);
```
### تعيين وجهة الرابط إلى ملف PDF آخر

الكود التالي يوضح كيفية تحديث رابط في ملف PDF وتعيين وجهته إلى ملف PDF آخر.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// تحميل ملف PDF
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// السطر التالي يحدث الوجهة، لا يحدث الملف
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// السطر التالي يحدث الملف
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// حفظ المستند بالرابط المحدث
document.Save(dataDir);
```

### تحديث لون نص LinkAnnotation

التعليق التوضيحي للرابط لا يحتوي على نص.
التعليق التوضيحي للرابط لا يحتوي على نص.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// تحميل ملف PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // البحث عن النص تحت التعليق التوضيحي
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // تغيير لون النص.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// حفظ المستند برابط محدث
doc.Save(dataDir);
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
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

