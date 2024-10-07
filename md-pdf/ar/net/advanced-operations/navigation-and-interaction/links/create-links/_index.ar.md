---
title: إنشاء روابط في ملف PDF باستخدام C#
linktitle: إنشاء روابط
type: docs
weight: 10
url: /net/create-links/
description: توضح هذه القسم كيفية إنشاء روابط في مستند PDF الخاص بك باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إنشاء روابط في ملف PDF باستخدام C#",
    "alternativeHeadline": "كيفية إنشاء روابط في PDF",
    "author": {
        "@type": "Person",
        "name":"أنستاسيا هولوب",
        "givenName": "أنستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, إنشاء رابط في pdf",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "توضح هذه القسم كيفية إنشاء روابط في مستند PDF الخاص بك باستخدام C#."
}
</script>
يعمل الجزء التالي من الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إنشاء الروابط

من خلال إضافة رابط إلى تطبيق في مستند، يصبح من الممكن الربط بالتطبيقات من خلال المستند. هذا مفيد عندما تريد من القراء اتخاذ إجراء معين في نقطة محددة في الدليل التعليمي، على سبيل المثال، أو لإنشاء مستند غني بالميزات. لإنشاء رابط تطبيق:

1. [إنشاء مستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. احصل على [الصفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) التي تريد إضافة رابط إليها.
1. إنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) باستخدام كائني الصفحة و[المستطيل](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. تعيين خصائص الرابط باستخدام كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. عند إنشاء كائن [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction)، حدد التطبيق الذي تريد تشغيله.
1. أضف الرابط إلى خاصية [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) لكائن الصفحة.
1. أخيرًا، احفظ ملف PDF المُحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن الوثيقة.

الشفرة البرمجية التالية توضح كيفية إنشاء رابط لتطبيق في ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// فتح المستند
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// إنشاء رابط
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// حفظ المستند المحدث
document.Save(dataDir);
```
### إنشاء رابط مستند PDF في ملف PDF

يتيح لك Aspose.PDF لـ .NET إضافة رابط إلى ملف PDF خارجي بحيث يمكنك ربط عدة مستندات معًا. لإنشاء رابط مستند PDF:

1. أولاً، قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. ثم، احصل على [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) الذي تريد إضافة الرابط إليه.
1. قم بإنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) باستخدام كائني Page و [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. قم بتعيين خصائص الرابط باستخدام كائن [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. قم بتعيين خاصية العمل إلى كائن [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1. أضف الرابط إلى مجموعة التعليقات التوضيحية لكائن الصفحة.
1. احفظ ملف PDF المُحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن الوثيقة.

الشفرة التالية توضح كيفية إنشاء رابط مستند PDF في ملف PDF.

 ```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// فتح الوثيقة
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// إنشاء رابط
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// حفظ الوثيقة المُحدثة
document.Save(dataDir);
```

<script type="application/ld+json">

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لمكتبة .NET",
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
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "بريطانيا",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

