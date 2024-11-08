---
title: إضافة علامة مائية إلى PDF باستخدام بايثون
linktitle: إضافة علامة مائية
type: docs
weight: 40
url: /ar/python-net/add-watermarks/
description: تشرح هذه المقالة ميزات العمل مع القطع الأثرية والحصول على العلامات المائية في ملفات PDF باستخدام البرمجة بلغة بايثون.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة علامة مائية إلى PDF باستخدام بايثون",
    "alternativeHeadline": "كيفية إضافة علامة مائية إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf,python, إضافة علامة مائية",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
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
    "url": "/python-net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "تشرح هذه المقالة ميزات العمل مع القطع الأثرية والحصول على العلامات المائية في ملفات PDF باستخدام بايثون."
}
</script>


**Aspose.PDF for Python عبر .NET** يسمح بإضافة العلامات المائية إلى مستند PDF الخاص بك باستخدام القطع الفنية. يرجى التحقق من هذه المقالة لحل مهمتك.

للعمل مع القطع الفنية، يحتوي Aspose.PDF على فئتين: [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) و [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

من أجل الحصول على جميع القطع الفنية في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) على خاصية القطع الفنية. يشرح هذا الموضوع كيفية العمل مع القطع الفنية في ملفات PDF.

## العمل مع القطع الفنية

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) على الخصائص التالية:

**contents** – يحصل على مجموعة من المشغلين الداخليين للقطعة الفنية. النوع المدعوم هو System.Collections.ICollection.
**form** – يحصل على XForm للقطعة الفنية (إذا تم استخدام XForm). تحتوي القطع الفنية للعلامات المائية، الرأس والتذييل على XForm الذي يعرض جميع محتويات القطعة الفنية.

**image** – يحصل على صورة القطعة الفنية (إذا كانت الصورة موجودة، وإلا null).
**text** – يحصل على نص القطعة الأثرية.  
**rectangle** – يحصل على موضع القطعة الأثرية على الصفحة.  
**rotation** – يحصل على دوران القطعة الأثرية (بالدرجات، تشير القيمة الموجبة إلى الدوران عكس اتجاه عقارب الساعة).  
**opacity** – يحصل على شفافية القطعة الأثرية. القيم الممكنة تكون في النطاق 0...1، حيث 1 تعني غير شفاف تمامًا.

## عينات برمجية: كيفية إضافة علامة مائية على ملفات PDF

يوضح مقتطف الكود التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام Python.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    artifact = ap.WatermarkArtifact()

    ts = ap.text.TextState()
    ts.font_size = 72
    ts.foreground_color = ap.Color.blue
    ts.font = ap.text.FontRepository.find_font("Courier")

    artifact.set_text_and_state("WATERMARK", ts)
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    artifact.rotation = 45
    artifact.opacity = 0.5
    artifact.is_background = True
    document.pages[1].artifacts.append(artifact)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python عبر مكتبة .NET",
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
    "applicationCategory": "مكتبة معالجة PDF لـ Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>