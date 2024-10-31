---
title: إضافة طوابع الصور في PDF باستخدام Python
linktitle: طوابع الصور في ملف PDF
type: docs
weight: 10
url: /python-net/image-stamps-in-pdf-page/
description: أضف طابع الصورة في مستند PDF الخاص بك باستخدام فئة ImageStamp مع مكتبة Aspose.PDF لـ Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة طوابع الصور في PDF باستخدام Python",
    "alternativeHeadline": "إضافة طوابع الصور في PDF باستخدام Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, python, إنشاء مستندات",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "أضف طابع الصورة في مستند PDF الخاص بك باستخدام فئة ImageStamp مع مكتبة Aspose.PDF لـ Python."
}
</script>


## إضافة ختم صورة في ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) لإضافة ختم صورة إلى ملف PDF. توفر فئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) الخصائص اللازمة لإنشاء ختم يعتمد على الصورة، مثل الارتفاع، العرض، الشفافية وغيرها.

لإضافة ختم صورة:

1. قم بإنشاء كائن Document وكائن ImageStamp باستخدام الخصائص المطلوبة.
2. استدعِ طريقة [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) لفئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) لإضافة الختم إلى ملف PDF.

يوضح مقطع الشيفرة التالي كيفية إضافة ختم صورة في ملف PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إنشاء ختم الصورة
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # إضافة الختم إلى صفحة معينة
    document.pages[1].add_stamp(image_stamp)

    # حفظ المستند الناتج
    document.save(output_pdf)
```


## التحكم في جودة الصورة عند إضافة ختم

عند إضافة صورة ككائن ختم، يمكنك التحكم في جودة الصورة. تُستخدم خاصية [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) في فئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) لهذا الغرض. تشير إلى جودة الصورة بالنسبة المئوية (القيم الصالحة هي 0..100).

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إنشاء ختم صورة
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # إضافة الختم إلى صفحة معينة
    document.pages[1].add_stamp(image_stamp)

    # حفظ المستند الناتج
    document.save(output_pdf)
```

## ختم الصورة كخلفية في صندوق عائم

تتيح لك Aspose.PDF لواجهة برمجة التطبيقات بايثون إضافة ختم صورة كخلفية في صندوق عائم.
 [الخاصية](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) الخلفية لفئة [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) يمكن استخدامها لتعيين ختم صورة الخلفية لصندوق عائم كما هو موضح في نموذج الكود التالي.

```python

    import aspose.pdf as ap

    # إنشاء كائن المستند
    document = ap.Document()
    # إضافة صفحة إلى مستند PDF
    page = document.pages.add()
    # إنشاء كائن FloatingBox
    box = ap.FloatingBox(200.0, 100.0)
    # ضبط الموضع الأيسر لـ FloatingBox
    box.left = 40
    # ضبط الموضع العلوي لـ FloatingBox
    box.top = 80
    # ضبط المحاذاة الأفقية لـ FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # إضافة مقطع نصي إلى مجموعة الفقرات لـ FloatingBox
    box.paragraphs.add(ap.text.TextFragment("النص الرئيسي"))
    # تعيين الحدود لـ FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # إضافة صورة الخلفية
    box.background_image = img
    # تعيين لون الخلفية لـ FloatingBox
    box.background_color = ap.Color.yellow
    # إضافة FloatingBox إلى مجموعة الفقرات لكائن الصفحة
    page.paragraphs.add(box)
    # حفظ مستند PDF
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لبايثون",
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