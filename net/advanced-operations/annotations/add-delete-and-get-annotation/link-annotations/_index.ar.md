---
title: استخدام تعليقات الرابط في PDF
linktitle: تعليقات الرابط
type: docs
weight: 70
url: /net/link-annotations/
description: يسمح لك Aspose.PDF لـ .NET بإضافة، الحصول على، وحذف تعليق الرابط من مستند PDF الخاص بك.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استخدام تعليق الرابط لـ PDF",
    "alternativeHeadline": "كيفية إضافة تعليق الرابط في PDF",
    "author": {
        "@type": "Person",
        "name": "أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, تعليق نص",
    "wordcount": "302",
    "proficiencyLevel": "مبتدئ",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "يسمح لك Aspose.PDF لـ .NET بإضافة، الحصول على، وحذف تعليق النص من مستند PDF الخاص بك."
}
</script>
## إضافة توصيف الرابط في ملف PDF موجود

> الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يمثل [توصيف الرابط](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) رابطًا هايبرتكستيًا، ووجهة ما في مكان آخر، ومستندًا. وفقًا للمعيار PDF، يمكن استخدام توصيف الرابط في ثلاث حالات: فتح عرض الصفحة، فتح ملف، وفتح صفحة ويب.

### استخدام توصيف الرابط لفتح عرض الصفحة

تم تنفيذ عدة خطوات إضافية لإنشاء التوصيف. استخدمنا TextFragmentAbsorber في حالتين للعثور على القطع للعرض. الأول لنص توصيف الرابط، والثاني يشير إلى بعض الأماكن في المستند.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
لإنشاء التعليق التوضيحي قمنا باتباع خطوات معينة:

1. إنشاء `LinkAnnotation` ومرر كائن الصفحة ومستطيل جزء النص الذي يتوافق مع التعليق التوضيحي.
1. تعيين `Action` كـ `GoToAction` ومرر `XYZExplicitDestination` كوجهة مرغوبة. لقد أنشأنا `XYZExplicitDestination` استنادًا إلى الصفحة وإحداثيات اليسار والأعلى والتكبير.
1. إضافة التعليق التوضيحي إلى مجموعة تعليقات الصفحة.
1. حفظ الوثيقة

### استخدام التعليق التوضيحي للوصلة مع وجهة مسماة

عند معالجة مستندات مختلفة، تنشأ موقف عندما تكون تكتب ولا تعرف إلى أين ستشير التعليق التوضيحي.
في هذه الحالة يمكنك استخدام وجهة خاصة (مسماة) وسيكون الكود كما يظهر هنا:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

في مكان آخر يمكنك إنشاء وجهة مسماة.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### استخدام تعليق الرابط لفتح ملف

يستخدم نفس النهج عند إنشاء تعليق لفتح ملف، كما في الأمثلة أعلاه.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

الفرق هو أننا سنستخدم `GoToRemoteAction` بدلاً من `GoToAction`. يأخذ بناء GoToRemoteAction معاملين: اسم الملف ورقم الصفحة.
يمكنك أيضًا استخدام شكل آخر وتمرير اسم الملف وبعض الوجهات. بالطبع، تحتاج إلى إنشاء هذه الوجهة قبل استخدامها.

### استخدام تعليق الرابط لفتح صفحة ويب

لفتح صفحة ويب فقط قم بتعيين `Action` مع كائن `GoToURIAction`.
يمكنك تمرير رابط هايبرتكست كمعامل بناء أو أي نوع آخر من URI. على سبيل المثال، يمكنك استخدام `callto` لتنفيذ الإجراء مع استدعاء رقم هاتف.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // إنشاء تعليق الرابط وتعيين الإجراء لاستدعاء رقم هاتف
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## إضافة تعليق توضيحي مزخرف للرابط

يمكنك تخصيص التعليق التوضيحي للرابط باستخدام الحدود. في المثال أدناه سنقوم بإنشاء حد متقطع باللون الأزرق بعرض 3 نقاط.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

مثال آخر يوضح كيفية محاكاة أسلوب المتصفح واستخدام خط تحتي للروابط.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### الحصول على التعليقات التوضيحية للروابط

يرجى محاولة استخدام الشفرة التالية للحصول على التعليق التوضيحي للرابط من مستند PDF.

```csharp
class ExampleLinkAnnotations
{
    // مسار مجلد المستندات.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // تحميل ملف PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // طباعة عنوان URL لكل تعليق توضيحي للرابط
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // طباعة النص المرتبط بالرابط الفائق
            Console.WriteLine(extractedText);
        }
    }
}
```
### حذف التعليقات التوضيحية للروابط

يوضح الجزء التالي من الكود كيفية حذف التعليق التوضيحي للرابط من ملف PDF. لهذا نحتاج إلى العثور على وإزالة جميع التعليقات التوضيحية للروابط في الصفحة الأولى. بعد ذلك سنحفظ المستند بدون التعليق التوضيحي.

```csharp
class ExampleLinkAnnotations
{
    // مسار دليل المستندات
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // تحميل ملف PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // العثور على وحذف جميع التعليقات التوضيحية للرابط في الصفحة الأولى
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // حفظ المستند بعد إزالة التعليق التوضيحي
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
