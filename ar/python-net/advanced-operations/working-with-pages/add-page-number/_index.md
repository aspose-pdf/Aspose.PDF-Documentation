---
title: إضافة رقم الصفحة إلى PDF باستخدام Python
linktitle: إضافة رقم الصفحة
type: docs
weight: 30
url: ar/python-net/add-page-number/
description: Aspose.PDF لـ Python عبر .NET يتيح لك إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumberStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة رقم الصفحة إلى PDF باستخدام Python",
    "alternativeHeadline": "كيفية إضافة ختم رقم الصفحة إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, python, ختم رقم الصفحة",
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
    "url": "/python-net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF لـ Python عبر .NET يتيح لك إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumberStamp."
}
</script>


جميع الوثائق يجب أن تحتوي على أرقام الصفحات. يساعد رقم الصفحة القارئ في تحديد أجزاء مختلفة من الوثيقة.
**Aspose.PDF لـ Python عبر .NET** يتيح لك إضافة أرقام الصفحات باستخدام [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

يمكنك استخدام فئة [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) لإضافة ختم رقم الصفحة في ملف PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) فئة توفر الخصائص اللازمة لإنشاء ختم يعتمد على رقم الصفحة مثل التنسيق، الهوامش، المحاذاة، الرقم الابتدائي، إلخ. من أجل إضافة ختم رقم الصفحة، تحتاج إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) وكائن [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) الخاصة بـ [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) لإضافة الختم إلى ملف PDF. يمكنك أيضًا تعيين خصائص الخط لختم رقم الصفحة. يوضح لك مقتطف الشيفرة التالي كيفية إضافة أرقام الصفحات في ملف PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إنشاء ختم رقم الصفحة
    page_number_stamp = ap.PageNumberStamp()
    # ما إذا كان الختم في الخلفية
    page_number_stamp.background = False
    page_number_stamp.format = "الصفحة # من " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # تعيين خصائص النص
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.aqua

    # إضافة الختم إلى صفحة معينة
    document.pages[1].add_stamp(page_number_stamp)

    # حفظ المستند الناتج
    document.save(output_pdf)
```

## مثال حي

[إضافة أرقام الصفحات إلى PDF](https://products.aspose.app/pdf/page-number) هو تطبيق ويب مجاني عبر الإنترنت يسمح لك بالتحقيق في كيفية عمل وظيفة إضافة أرقام الصفحات.

[![كيفية إضافة رقم الصفحة في pdf باستخدام Python](page_number.png)](https://products.aspose.app/pdf/page-number)

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
    "applicationCategory": "PDF Manipulation Library for Python",
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