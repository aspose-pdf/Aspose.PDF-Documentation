---
title: إضافة علامة مائية إلى PDF باستخدام C#
linktitle: إضافة علامة مائية
type: docs
weight: 90
url: /net/add-watermarks/
description: يشرح هذا المقال ميزات العمل مع الأدوات والحصول على العلامات المائية في ملفات PDF باستخدام C# برمجيًا.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة علامة مائية إلى PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة علامة مائية إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء وثيقة PDF",
    "keywords": "pdf, c#, إضافة علامة مائية",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال ميزات العمل مع الأدوات والحصول على العلامات المائية في ملفات PDF باستخدام C# برمجيًا."
}
</script>
**Aspose.PDF لـ .NET** يتيح إضافة العلامات المائية لمستند PDF الخاص بك باستخدام الأدوات. يرجى مراجعة هذه المقالة لحل مهمتك.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

العلامة المائية المُنشأة بواسطة Adobe Acrobat تُسمى أداة (كما ورد في 14.8.2.2 المحتوى الحقيقي والأدوات في مواصفات PDF). من أجل العمل مع الأدوات، لدى Aspose.PDF فئتان: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

للحصول على جميع الأدوات على صفحة معينة، فإن فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) لديها خاصية Artifacts. يشرح هذا الموضوع كيفية العمل مع الأداة في ملفات PDF.

## العمل مع الأدوات

فئة [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) تحتوي على الخصائص التالية:

**Artifact.Type** – يحصل على نوع الأداة (يدعم قيم تعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، التخطيط، الصفحة، الترقيم، وغير محدد).
**Artifact.Type** – يحصل على نوع العنصر (يدعم قيم تعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، التخطيط، الصفحة، الترقيم وغير محدد).
**Artifact.Subtype** – يحصل على نوع فرعي للعنصر (يدعم قيم تعداد Artifact.ArtifactSubtype حيث تشمل الخلفية، التذييل، الرأس، غير محدد، العلامة المائية).

{{% alert color="primary" %}}

يرجى ملاحظة أن العلامات المائية المنشأة بواسطة Adobe Acrobat لها نوع الترقيم ونوع فرعي العلامة المائية.

{{% /alert %}}

**Artifact.Contents** – يحصل على مجموعة من المشغلات الداخلية للعنصر. نوع المدعوم هو System.Collections.ICollection.
**Artifact.Form** – يحصل على XForm للعنصر (إذا تم استخدام XForm). تحتوي عناصر العلامات المائية والرأس والتذييل على XForm الذي يعرض كل محتويات العنصر.
**Artifact.Image** – يحصل على صورة العنصر (إذا كانت الصورة موجودة، وإلا null).
**Artifact.Text** – يحصل على نص العنصر.
**Artifact.Rectangle** – يحصل على موقع العنصر على الصفحة.
**Artifact.Rotation** – يحصل على دوران العنصر (بالدرجات، القيمة الموجبة تشير إلى الدوران عكس عقارب الساعة).
**Artifact.Rotation** – يحصل على دوران العنصر (بالدرجات، القيمة الموجبة تشير إلى الدوران عكس عقارب الساعة).
**Artifact.Opacity** – يحصل على شفافية العنصر. القيم الممكنة تتراوح بين 0…1، حيث 1 يعني العتامة التامة.

## أمثلة برمجية: كيفية إضافة علامة مائية على ملفات PDF

الشفرة التالية توضح كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام C#.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
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
    "applicationCategory": "مكتبة لتعديل ملفات PDF لـ .NET",
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

