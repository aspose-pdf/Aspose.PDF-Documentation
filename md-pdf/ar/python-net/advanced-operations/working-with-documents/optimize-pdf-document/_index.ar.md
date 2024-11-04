---
title: تحسين، ضغط أو تقليل حجم ملف PDF في بايثون
linktitle: تحسين PDF
type: docs
weight: 30
url: /python-net/optimize-pdf/
keywords: "optimize pdf python"
description: تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إلغاء تضمين الخطوط، إزالة الكائنات غير المستخدمة باستخدام بايثون.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تحسين PDF باستخدام بايثون",
    "alternativeHeadline": "كيف تحسن PDF باستخدام بايثون",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات pdf",
    "keywords": "pdf, python, تحسين pdf",
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
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إلغاء تضمين الخطوط، إزالة الكائنات غير المستخدمة باستخدام بايثون."
}
</script>


A PDF document قد يحتوي أحيانًا على بيانات إضافية. تقليل حجم ملف PDF سيساعدك على تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب، المشاركة على الشبكات الاجتماعية، الإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام عدة تقنيات لتحسين PDF:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إزالة تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة تسطيح حقول النماذج
- إزالة أو تسطيح التعليقات التوضيحية

{{% alert color="primary" %}}

 يمكن العثور على شرح مفصل لطرق التحسين في صفحة نظرة عامة على طرق التحسين.

{{% /alert %}}

## تحسين مستند PDF للويب

يشير التحسين، أو التخطية للويب، إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح ويب. لتحسين ملف لعرض الويب:

1. افتح مستند الإدخال في كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. استخدم طريقة [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. احفظ المستند المحسن باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يظهر الكود التالي كيفية تحسين مستند PDF للويب.

```python 

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # تحسين للويب
    document.optimize()

    # حفظ المستند الناتج
    document.save(output_pdf)
```

## تقليل حجم ملف PDF

تسمح لك طريقة [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) بتقليل حجم المستند عن طريق إزالة المعلومات غير الضرورية. افتراضيًا، تعمل هذه الطريقة كما يلي:

- تتم إزالة الموارد غير المستخدمة في صفحات المستند
- يتم دمج الموارد المتساوية في كائن واحد

- يتم حذف الكائنات غير المستخدمة

المقطع أدناه هو مثال. لكن لاحظ أن هذه الطريقة لا تضمن تصغير الوثيقة.

```python

    import aspose.pdf as ap

    # فتح الوثيقة
    document = ap.Document(input_pdf)
    # تحسين وثيقة PDF. لكن لاحظ أن هذه الطريقة لا تضمن تصغير الوثيقة
    document.optimize_resources()
    # حفظ الوثيقة المحدثة
    document.save(output_pdf)
```

## إدارة استراتيجية التحسين

يمكننا أيضًا تخصيص استراتيجية التحسين. حاليًا، تستخدم طريقة [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) خمس تقنيات. يمكن تطبيق هذه التقنيات باستخدام طريقة OptimizeResources() مع معلمة [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### تقليص أو ضغط جميع الصور

لدينا طريقتان للعمل مع الصور: تقليل جودة الصورة و/أو تغيير دقتها.
 في أي حال، يجب تطبيق [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/). في المثال التالي، نقوم بتقليص الصور عن طريق تقليل جودة الصورة إلى 50.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)
    # تهيئة خيارات التحسين
    optimizeOptions = ap.optimization.OptimizationOptions()
    # تعيين خيار ضغط الصور
    optimizeOptions.image_compression_options.compress_images = True
    # تعيين خيار جودة الصورة
    optimizeOptions.image_compression_options.image_quality = 50
    # تحسين مستند PDF باستخدام خيارات التحسين
    document.optimize_resources(optimizeOptions)
    # حفظ المستند المحدث
    document.save(output_pdf)
```

### إزالة الكائنات غير المستخدمة

يحتوي مستند PDF أحيانًا على الكائنات التي لا يتم الرجوع إليها من أي كائن آخر في المستند. قد يحدث هذا، على سبيل المثال، عندما تتم إزالة صفحة من شجرة صفحات المستند ولكن لم تتم إزالة كائن الصفحة نفسه. إزالة هذه الكائنات لا يجعل المستند غير صالح بل يجعله أصغر.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)
    # تعيين خيار RemoveUsedObject
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # تحسين مستند PDF باستخدام OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # حفظ المستند المحدث
    document.save(output_pdf)
```

### إزالة التدفقات غير المستخدمة

أحيانًا يحتوي المستند على تدفقات موارد غير مستخدمة. هذه التدفقات ليست "كائنات غير مستخدمة" لأنها مشار إليها من قاموس موارد الصفحة. وبالتالي، لا يتم إزالتها باستخدام طريقة "إزالة الكائنات غير المستخدمة". ولكن هذه التدفقات لا تُستخدم أبدًا مع محتويات الصفحة. قد يحدث هذا في حالات عندما تتم إزالة صورة من الصفحة ولكن ليس من موارد الصفحة. أيضًا، يحدث هذا الموقف في كثير من الأحيان عندما يتم استخراج الصفحات من المستند وتحتوي صفحات المستند على موارد "مشتركة"، أي نفس كائن Resources. يتم تحليل محتويات الصفحة لتحديد ما إذا كان تدفق الموارد مستخدمًا أم لا. يتم إزالة التدفقات غير المستخدمة. في بعض الأحيان يقلل ذلك من حجم المستند. استخدام هذه التقنية مشابه للخطوة السابقة:

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)
    # تعيين خيار RemoveUsedStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # تحسين مستند PDF باستخدام OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # احفظ المستند المحدث
    document.save(output_pdf)
```

### ربط التدفقات المكررة

يمكن أن تحتوي بعض المستندات على عدة تدفقات موارد متطابقة (مثل الصور، على سبيل المثال). قد يحدث هذا، على سبيل المثال، عندما يتم دمج مستند مع نفسه. يحتوي المستند الناتج على نسختين مستقلتين من نفس تدفق الموارد. نقوم بتحليل جميع تدفقات الموارد ونقارنها. إذا كانت التدفقات مكررة، يتم دمجها، أي تبقى نسخة واحدة فقط. يتم تغيير المراجع بشكل مناسب، ويتم إزالة نسخ الكائن. في بعض الحالات، يساعد ذلك في تقليل حجم المستند.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)
    # تعيين خيار LinkDuplcateStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # تحسين مستند PDF باستخدام OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # حفظ المستند المحدث
    document.save(output_pdf)
```

### إزالة تضمين الخطوط

إذا كان المستند يستخدم خطوطًا مدمجة، فهذا يعني أن جميع بيانات الخطوط مخزنة في المستند.
 الميزة هي أن المستند يمكن عرضه بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. ولكن تضمين الخطوط يجعل المستند أكبر. تزيل طريقة إزالة تضمين الخطوط جميع الخطوط المضمنة. وبالتالي، ينخفض حجم المستند لكن قد يصبح المستند نفسه غير قابل للقراءة إذا لم يتم تثبيت الخط الصحيح.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)
    # تعيين خيار UnembedFonts
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # تحسين مستند PDF باستخدام OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # حفظ المستند المحدث
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "حجم الملف الأصلي: {}. حجم الملف المخفض: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

تطبق موارد التحسين هذه الأساليب على المستند. إذا تم تطبيق أي من هذه الأساليب، فمن المحتمل أن يقل حجم المستند. إذا لم يتم تطبيق أي من هذه الأساليب، فلن يتغير حجم المستند وهو أمر واضح.

## طرق إضافية لتقليل حجم مستند PDF

### إزالة أو تسطيح التعليقات التوضيحية

يمكن حذف التعليقات التوضيحية عندما تكون غير ضرورية. عندما تكون ضرورية ولكن لا تتطلب تحريرًا إضافيًا، يمكن تسطيحها. كلتا هاتين الطريقتين ستقللان من حجم الملف.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)
    # تسطيح التعليقات التوضيحية
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # احفظ المستند المحدث
    document.save(output_pdf)
```

### إزالة حقول النماذج

إذا كان مستند PDF يحتوي على AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسطيح حقول النماذج.

```python

    import aspose.pdf as ap

    # تحميل نموذج PDF المصدر
    doc = ap.Document(input_pdf)

    # تسطيح النماذج
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # احفظ المستند المحدث
    doc.save(output_pdf)
```

### تحويل ملف PDF من نظام ألوان RGB إلى تدرج الرمادي

يتكون ملف PDF من نصوص وصور ومرفقات وتعليقات توضيحية ورسوم بيانية وأشياء أخرى. قد تواجه متطلبًا لتحويل ملف PDF من نظام الألوان RGB إلى تدرج الرمادي بحيث يكون أسرع عند طباعة تلك الملفات. أيضًا، عند تحويل الملف إلى تدرج الرمادي، يتم تقليل حجم المستند أيضًا، ولكن يمكن أن يؤدي ذلك إلى انخفاض في جودة المستند. يتم دعم هذه الميزة حاليًا بواسطة ميزة Pre-Flight في Adobe Acrobat، ولكن عند التحدث عن أتمتة المكتب، فإن Aspose.PDF هو الحل النهائي لتوفير مثل هذه المزايا لمعالجة المستندات. من أجل تحقيق هذا المتطلب، يمكن استخدام الكود التالي.

```python

    import aspose.pdf as ap

    # تحميل ملف PDF المصدر
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # تحويل صورة نظام الألوان RGB إلى نظام الألوان تدرج الرمادي
        strategy.convert(page)

    # حفظ الملف الناتج
    document.save(output_pdf)
```


### ضغط FlateDecode

يوفر Aspose.PDF for Python via .NET دعم ضغط FlateDecode لوظيفة تحسين PDF. يوضح مقطع الشيفرة التالي كيفية استخدام الخيار في التحسين لتخزين الصور باستخدام ضغط **FlateDecode**:

```python

    import aspose.pdf as ap

    # فتح المستند
    doc = ap.Document(input_pdf)
    # تهيئة خيارات التحسين
    optimizationOptions = ap.optimization.OptimizationOptions()
    # لتحسين الصورة باستخدام ضغط FlateDecode قم بتعيين خيارات التحسين إلى Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # تعيين خيارات التحسين
    doc.optimize_resources(optimizationOptions)
    # حفظ المستند
    doc.save(output_pdf)
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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