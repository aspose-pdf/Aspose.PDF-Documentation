---
title: إضافة صورة إلى ملف PDF باستخدام Python
linktitle: إضافة صورة
type: docs
weight: 10
url: /ar/python-net/add-image-to-existing-pdf-file/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة Python.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة صورة إلى ملف PDF باستخدام Python",
    "alternativeHeadline": "كيفية إضافة صورة إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, إضافة صورة إلى pdf",
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
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة Python."
}
</script>


## إضافة صورة في ملف PDF موجود

يُظهر مقتطف الشيفرة التالي كيفية إضافة صورة في ملف PDF.

1. قم بتحميل ملف PDF المدخل.
2. حدد رقم الصفحة التي سيتم وضع الصورة عليها.
3. لتعريف موضع الصورة على الصفحة، استدعِ طريقة [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) في فئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
4. استدعِ طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) في فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## إضافة صورة في ملف PDF موجود (واجهات)

هناك أيضًا طريقة بديلة وأسهل لإضافة صورة إلى ملف PDF.
 يمكنك استخدام [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) طريقة من فئة [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/). تتطلب طريقة [add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) إضافة الصورة، رقم الصفحة التي يجب إضافة الصورة فيها ومعلومات الإحداثيات. بعد ذلك، احفظ ملف PDF المحدث وأغلق كائن PdfFileMend باستخدام طريقة [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods). يوضح لك مقتطف الكود التالي كيفية إضافة صورة في ملف PDF موجود.

```python

    import aspose.pdf as ap

    # فتح المستند
    mender = ap.facades.PdfFileMend()

    # إنشاء كائن PdfFileMend لإضافة النص
    mender.bind_pdf(input_file)

    # إضافة الصورة في ملف PDF
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # حفظ التغييرات
    mender.save(output_pdf)

    # إغلاق كائن PdfFileMend
    mender.close()

```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لبايثون عبر مكتبة .NET",
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
    "applicationCategory": "مكتبة معالجة ملفات PDF لبايثون",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>