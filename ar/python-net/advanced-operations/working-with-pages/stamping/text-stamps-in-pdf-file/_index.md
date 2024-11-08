---
title: إضافة أختام نصية في PDF عبر بايثون
linktitle: الأختام النصية في ملف PDF
type: docs
weight: 20
url: /ar/python-net/text-stamps-in-the-pdf-file/
description: إضافة ختم نصي إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF لبايثون.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة أختام نصية في PDF بايثون",
    "alternativeHeadline": "إضافة أختام نصية في PDF بايثون",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, توليد المستندات",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق توثيق Aspose.PDF",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "إضافة ختم نصي إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF لبايثون."
}
</script>


## إضافة ختم نصي باستخدام بايثون

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) لإضافة ختم نصي في ملف PDF. توفر فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط وغيرها. من أجل إضافة ختم نصي، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) الخاصة بصفحة لإضافة الختم في ملف PDF. يوضح لك مقتطف الشيفرة التالي كيفية إضافة ختم نصي في ملف PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إنشاء ختم نصي
    text_stamp = ap.TextStamp("ختم تجريبي")
    # تعيين ما إذا كان الختم في الخلفية
    text_stamp.background = True
    # تعيين الأصل
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # تدوير الختم
    text_stamp.rotate = ap.Rotation.ON90
    # تعيين خصائص النص
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # إضافة الختم إلى صفحة معينة
    document.pages[1].add_stamp(text_stamp)

    # حفظ المستند الناتج
    document.save(output_pdf)
```


## تعريف المحاذاة لكائن TextStamp

إضافة العلامات المائية إلى مستندات PDF هي واحدة من الميزات المطلوبة بشكل متكرر وAspose.PDF لبايثون قادر تمامًا على إضافة الصور وكذلك العلامات المائية النصية. لدينا فئة تُسمى [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) التي توفر ميزة إضافة الأختام النصية فوق ملف PDF. مؤخرًا كانت هناك متطلبات لدعم ميزة تحديد محاذاة النص عند استخدام كائن TextStamp. لذلك من أجل تلبية هذا المتطلب، قمنا بإدخال خاصية [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) في فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). باستخدام هذه الخاصية، يمكننا تحديد محاذاة النص [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties).

توضح مقتطفات الشيفرة التالية مثالًا على كيفية تحميل مستند PDF موجود وإضافة TextStamp عليه.

```python

    import aspose.pdf as ap

    # إنشاء كائن Document باستخدام الملف المدخل
    doc = ap.Document(input_pdf)
    # إنشاء كائن FormattedText مع سلسلة نصية تجريبية
    text = ap.facades.FormattedText("This")
    # إضافة سطر نصي جديد إلى FormattedText
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # إنشاء كائن TextStamp باستخدام FormattedText
    stamp = ap.TextStamp(text)
    # تحديد المحاذاة الأفقية للختم النصي كمركز
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # تحديد المحاذاة العمودية للختم النصي كمركز
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # تحديد المحاذاة الأفقية للنص لـ TextStamp كمركز
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # ضبط الهامش العلوي لكائن الختم
    stamp.top_margin = 20
    # إضافة كائن الختم على الصفحة الأولى من المستند
    doc.pages[1].add_stamp(stamp)

    # حفظ المستند المحدث
    doc.save(output_pdf)
```


## ملء نص الحدود كختم في ملف PDF

لقد قمنا بتنفيذ إعداد وضع العرض لسيناريوهات إضافة وتحرير النص. لعرض نص الحدود، يرجى إنشاء كائن TextState لنقل الخصائص المتقدمة. حدد اللون للحدود. بعد ذلك، قم بتعيين وضع عرض النص، الخطوة التالية هي ربط TextState وإضافة الختم.

يوضح جزء الشفرة التالي كيفية إضافة نص ملء الحدود:

```python

    import aspose.pdf as ap

    # إنشاء كائن TextState لنقل الخصائص المتقدمة
    ts = ap.text.TextState()
    # تحديد اللون للحدود
    ts.stroking_color = ap.Color.gray
    # تعيين وضع عرض النص
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # تحميل مستند PDF المدخل
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # ربط TextState
    stamp.bind_text_state(ts)
    # تعيين أصل X, Y
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # إضافة الختم
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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