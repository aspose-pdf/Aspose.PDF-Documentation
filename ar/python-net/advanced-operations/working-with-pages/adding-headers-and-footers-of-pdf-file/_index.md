---
title: إضافة رأس وتذييل إلى PDF باستخدام بايثون
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 50
url: ar/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF لبايثون عبر .NET يتيح لك إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة رأس وتذييل إلى PDF باستخدام بايثون",
    "alternativeHeadline": "كيفية إضافة رأس وتذييل إلى ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, إضافة رأس, إضافة تذييل في pdf",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF لبايثون عبر .NET يتيح لك إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp."
}
</script>


**Aspose.PDF لـ Python عبر .NET** يتيح لك إضافة رأس وتذييل في ملف PDF الحالي الخاص بك. يمكنك إضافة صور أو نص إلى مستند PDF. أيضًا، حاول إضافة رؤوس مختلفة في ملف PDF واحد باستخدام Python.

## إضافة نص في رأس ملف PDF

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) لإضافة نص في رأس ملف PDF. توفر فئة TextStamp خصائص ضرورية لإنشاء ختم نصي مثل حجم الخط، ونمط الخط، ولون الخط وغيرها. من أجل إضافة نص في الرأس، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة 'add_stamp' للصفحة لإضافة النص في رأس ملف PDF.

تحتاج إلى ضبط خاصية [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) بطريقة تضمن ضبط النص في منطقة الرأس من ملف PDF الخاص بك. تحتاج أيضًا إلى ضبط 'horizontal_alignment' إلى Center و'vertical_alignment' إلى Top.

يوضح لك مقتطف الشيفرة التالي كيفية إضافة نص في رأس ملف PDF باستخدام Python:

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # إنشاء رأس
    textStamp = ap.TextStamp("Header Text")
    # تعيين خصائص الختم
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # إضافة رأس على جميع الصفحات
    for page in document.pages:
        page.add_stamp(textStamp)

    # حفظ المستند المحدث
    document.save(output_pdf)
```

## إضافة نص في تذييل ملف PDF

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) لإضافة نص في تذييل ملف PDF.
 توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط إلخ. لإضافة نص في التذييل، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة 'add_stamp' الخاصة بالصفحة لإضافة النص في تذييل ملف PDF.

يُظهر لك جزء الشفرة التالي كيفية إضافة نص في تذييل ملف PDF باستخدام Python:

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)
    # أنشئ تذييل
    textStamp = ap.TextStamp("Footer Text")
    # ضبط خصائص الختم
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # أضف التذييل على جميع الصفحات
    for page in document.pages:
        page.add_stamp(textStamp)

    # احفظ ملف PDF المحدث
    document.save(output_pdf)
```

## إضافة صورة في رأس ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) لإضافة صورة في رأس ملف PDF. فئة Image Stamp توفر الخصائص اللازمة لإنشاء ختم يعتمد على الصورة مثل حجم الخط، نمط الخط، ولون الخط وما إلى ذلك. لإضافة صورة في الرأس، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة 'add_stamp' من الصفحة لإضافة الصورة في رأس ملف PDF.

يُظهر لك مقتطف الكود التالي كيفية إضافة صورة في رأس ملف PDF باستخدام Python:

```python 

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إنشاء الرأس
    image_stamp = ap.ImageStamp(input_image)
    # تعيين خصائص الختم
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # إضافة الرأس في جميع الصفحات
    for page in document.pages:
        page.add_stamp(image_stamp)

    # حفظ المستند المحدث
    document.save(output_pdf)
```

## إضافة صورة في تذييل ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) لإضافة صورة في تذييل ملف PDF. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) توفر الفئة الخصائص اللازمة لإنشاء ختم قائم على الصور مثل حجم الخط، ونمط الخط، ولون الخط وما إلى ذلك. لإضافة صورة في التذييل، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة 'add_stamp' للصفحة لإضافة الصورة في تذييل ملف PDF.

يوضح لك مقتطف الشيفرة التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام Python:

```python

    import aspose.pdf as ap

    # فتح الوثيقة
    document = ap.Document(input_pdf)
    # إنشاء تذييل
    image_stamp = ap.ImageStamp(input_image)
    # تعيين خصائص الختم
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # إضافة تذييل على جميع الصفحات
    for page in document.pages:
        page.add_stamp(image_stamp)

    # حفظ ملف PDF المحدث
    document.save(output_pdf)
```

## إضافة رؤوس مختلفة في ملف PDF واحد

نعلم أنه يمكننا إضافة نص مختوم في قسم الرأس/التذييل من المستند باستخدام خصائص [الهامش العلوي](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) أو [الهامش السفلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties)، ولكن في بعض الأحيان قد يكون لدينا حاجة لإضافة رؤوس/تذييلات متعددة في مستند PDF واحد. يوضح **Aspose.PDF for Python via .NET** كيفية القيام بذلك.

من أجل تحقيق هذا المتطلب، سنقوم بإنشاء كائنات نص مختوم فردية (يعتمد عدد الكائنات على عدد الرؤوس/التذييلات المطلوبة) وسنضيفها إلى مستند PDF.
 نحن قد نحدد أيضًا معلومات تنسيق مختلفة لكل كائن ختم فردي. في المثال التالي، قمنا بإنشاء كائن Document وثلاثة كائنات TextStamp ثم استخدمنا طريقة 'add_stamp' للصفحة لإضافة النص في قسم الرأس لملف PDF. يظهر لك مقطع الكود التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام Aspose.PDF لـ Python:

```python

    import aspose.pdf as ap

    # إنشاء ثلاثة طوابع
    stamp1 = ap.TextStamp("Header 1")
    stamp2 = ap.TextStamp("Header 2")
    stamp3 = ap.TextStamp("Header 3")

    # ضبط محاذاة الطابع (وضع الطابع في أعلى الصفحة، متمركز أفقيًا)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # تحديد نمط الخط كعريض
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # ضبط معلومات لون النص الأمامي كالأحمر
    stamp1.text_state.foreground_color = ap.Color.red
    # تحديد حجم الخط كـ 14
    stamp1.text_state.font_size = 14

    # الآن نحتاج إلى ضبط المحاذاة الرأسية لكائن الطابع الثاني كأعلى
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # ضبط معلومات المحاذاة الأفقية للطابع كمحاذاة الوسط
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # ضبط عامل التكبير لكائن الطابع
    stamp2.zoom = 10

    # ضبط تنسيق كائن الطابع الثالث
    # تحديد معلومات المحاذاة الرأسية لكائن الطابع كأعلى
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # ضبط معلومات المحاذاة الأفقية لكائن الطابع كمحاذاة الوسط
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # ضبط زاوية الدوران لكائن الطابع
    stamp3.rotate_angle = 35
    # ضبط اللون الوردي كلون خلفية للطابع
    stamp3.text_state.background_color = ap.Color.pink
    # تغيير معلومات نوع الخط للطابع إلى Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # يتم إضافة الطابع الأول على الصفحة الأولى;
    document.pages[1].add_stamp(stamp1)
    # يتم إضافة الطابع الثاني على الصفحة الثانية;
    document.pages[2].add_stamp(stamp2)
    # يتم إضافة الطابع الثالث على الصفحة الثالثة.
    document.pages[3].add_stamp(stamp3)

    # حفظ المستند المحدث
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
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "بريطانيا",
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