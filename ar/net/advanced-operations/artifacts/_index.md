---
title: العمل مع الأدوات في .NET
linktitle: العمل مع الأدوات
type: docs
weight: 110
url: ar/net/artifacts/
description: يتيح لك Aspose.PDF لـ .NET إضافة صورة خلفية لصفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع الأدوات في .NET",
    "alternativeHeadline": "الأدوات في مستند PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, الأدوات في pdf",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "يتيح لك Aspose.PDF لـ .NET إضافة صورة خلفية لصفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact."
}
</script>
الأشياء في ملفات PDF هي عناصر جرافيك أو عناصر أخرى ليست جزءًا من المحتوى الفعلي للمستند. عادةً ما تستخدم هذه الأشياء لأغراض الزينة، التخطيط، أو الخلفية. أمثلة على الأشياء تشمل رؤوس الصفحات، تذييلات الصفحات، الفواصل، أو الصور التي لا تنقل أي معنى.

الغرض من الأشياء في ملفات PDF هو السماح بالتمييز بين عناصر المحتوى وعناصر غير المحتوى. هذا مهم للوصولية، حيث يمكن لقارئات الشاشة وتقنيات المساعدة الأخرى تجاهل الأشياء والتركيز على المحتوى ذي الصلة. كما يمكن للأشياء أن تحسن أداء وجودة مستندات PDF، حيث يمكن حذفها من الطباعة، البحث، أو النسخ.

لإنشاء عنصر كشيء في PDF، تحتاج إلى استخدام الفئة [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
تحتوي على الخصائص المفيدة التالية:

- **Artifact.Type** – تحصل على نوع الشيء (تدعم قيم تعداد Artifact.ArtifactType حيث تشمل القيم Background، Layout، Page، Pagination و Undefined).
- **Artifact.Type** – يحصل على نوع العنصر (يدعم قيم تعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، التخطيط، الصفحة، الترقيم، وغير محدد).
- **Artifact.Subtype** – يحصل على نوع العنصر الفرعي (يدعم قيم تعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية، التذييل، الرأس، غير محدد، العلامة المائية).
- **Artifact.Image** – يحصل على صورة العنصر (إذا كانت هناك صورة، وإلا null).
- **Artifact.Text** – يحصل على نص العنصر.
- **Artifact.Contents** – يحصل على مجموعة من المشغلات الداخلية للعنصر. نوع الدعم هو System.Collections.ICollection.
- **Artifact.Form** – يحصل على XForm للعنصر (إذا تم استخدام XForm). عناصر العلامات المائية، الرأس، والتذييل تحتوي على XForm الذي يعرض جميع محتويات العنصر.
- **Artifact.Rectangle** – يحصل على موقع العنصر على الصفحة.
- **Artifact.Rotation** – يحصل على دوران العنصر (بالدرجات، القيمة الموجبة تشير إلى الدوران عكس عقارب الساعة).
- **Artifact.Opacity** – يحصل على شفافية العنصر.
- **Artifact.Opacity** – يحصل على شفافية القطعة الأثرية.

الفئات التالية قد تكون مفيدة أيضاً في العمل مع القطع الأثرية:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## العمل مع العلامات المائية الموجودة

العلامة المائية التي تم إنشاؤها باستخدام Adobe Acrobat تسمى قطعة أثرية (كما هو موضح في 14.8.2.2 المحتوى الحقيقي والقطع الأثرية لمواصفات PDF).

من أجل الحصول على كل العلامات المائية على صفحة معينة، فإن فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) لديها خاصية Artifacts.

يوضح الكود التالي كيفية الحصول على كل العلامات المائية على الصفحة الأولى من ملف PDF.

_ملاحظة:_ هذا الكود يعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
_ملاحظة:_ هذا الكود يعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## العمل مع الخلفيات كمواد أثرية

يمكن استخدام صور الخلفية لإضافة علامة مائية، أو تصميم خفي آخر، إلى الوثائق. في Aspose.PDF لـ .NET، كل وثيقة PDF هي مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من المواد الأثرية. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) لإضافة صورة خلفية إلى كائن صفحة.

يوضح الكود التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
إذا كنت ترغب، لسبب ما، في استخدام خلفية بلون صلب، يرجى تغيير الكود السابق على النحو التالي:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## عد العناصر من نوع معين

لحساب العدد الإجمالي للعناصر من نوع معين (مثلاً، العدد الإجمالي للعلامات المائية)، استخدم الكود التالي:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Watermarks: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Backgrounds: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Headers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Footers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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

