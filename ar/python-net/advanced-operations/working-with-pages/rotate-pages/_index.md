---
title: تدوير صفحات PDF باستخدام بايثون
linktitle: تدوير صفحات PDF
type: docs
weight: 110
url: /ar/python-net/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجيًا باستخدام بايثون.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تدوير صفحات PDF باستخدام بايثون",
    "alternativeHeadline": "كيفية تدوير صفحات PDF باستخدام بايثون",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, تدوير صفحة pdf",
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
    "url": "/python-net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجيًا باستخدام بايثون."
}
</script>


هذا الموضوع يوضح كيفية تحديث أو تغيير اتجاه الصفحات في ملف PDF موجود برمجيًا باستخدام Python.

## تغيير اتجاه الصفحة

تدعم Aspose.PDF لـ Python عبر .NET ميزات رائعة مثل تغيير اتجاه الصفحة من أفقي إلى عمودي والعكس. لتغيير اتجاه الصفحة، قم بتعيين MediaBox للصفحة باستخدام مقتطف الشيفرة التالي. يمكنك أيضًا تغيير اتجاه الصفحة عن طريق تعيين زاوية الدوران باستخدام طريقة 'rotate'.

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    for page in doc.pages:
        r = page.media_box
        newHeight = r.width
        newWidth = r.height
        newLLX = r.llx
        # يجب علينا تحريك الصفحة لأعلى لتعويض تغيير حجم الصفحة
        # (الحافة السفلى للصفحة هي 0,0 والمعلومات عادة ما توضع من
        # أعلى الصفحة. لهذا السبب نحرك الحافة السفلى للأعلى بالفرق بين
        # الارتفاع القديم والجديد.
        newLLY = r.lly + (r.height - newHeight)
        page.media_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)
        # أحيانا نحتاج أيضًا إلى تعيين CropBox (إذا كان مُعَيَّنًا في الملف الأصلي)
        page.crop_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)

        # تعيين زاوية دوران الصفحة
        page.rotate = ap.Rotation.ON90

    # حفظ الملف الناتج
    doc.save(output_pdf)
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
    "offers": {
        "@type": "عرض",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "تقييم مجمع",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>