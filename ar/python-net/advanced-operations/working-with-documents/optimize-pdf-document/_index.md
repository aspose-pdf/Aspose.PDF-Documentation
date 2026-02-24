---
title: تحسين أو ضغط أو تقليل حجم PDF في بايثون
linktitle: تحسين PDF
type: docs
weight: 30
url: /ar/python-net/optimize-pdf/
description: تعلم كيفية تحسين مستندات PDF في بايثون لتحسين أداء الويب وتقليل حجم الملف باستخدام Aspose.PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ضغط صفحات PDF باستخدام بايثون
Abstract: تقدم هذه المقالة دليلًا شاملًا حول تحسين ملفات PDF لتقليل حجمها وتعزيز الأداء عبر منصات مختلفة، مثل صفحات الويب، والبريد الإلكتروني، وأنظمة التخزين. تشمل تقنيات التحسين تقليل أحجام الصور، وإزالة الموارد غير المستخدمة، وإلغاء تضمين الخطوط. يتم مناقشة أساليب محددة لتحسين ملفات PDF للويب وتقليل حجم الملف الإجمالي، باستخدام طريقتي `Optimize` و `OptimizeResources` في Aspose.PDF للبايثون. يمكن تخصيص استراتيجيات التحسين عبر `OptimizationOptions`، مما يسمح باتخاذ إجراءات مستهدفة مثل ضغط الصور، وإزالة الكائنات وتدفقات البيانات غير المستخدمة، وربط التدفقات المكررة، وإلغاء تضمين الخطوط. تغطي الاستراتيجيات الإضافية تسطيح التعليقات التوضيحية، وإزالة حقول النماذج، وتحويل ملفات PDF من RGB إلى تدرج الرمادي لتقليل الحجم أكثر. تُبرز المقالة أيضًا استخدام ضغط FlateDecode لتحسين الصور، لضمان إدارة فعالة لملفات PDF مع الحفاظ على الجودة والوظيفة.
---

قد يحتوي مستند PDF أحيانًا على بيانات إضافية. سيساعدك تقليل حجم ملف PDF على تحسين نقل الشبكة والتخزين. هذا مفيد خاصةً للنشر على صفحات الويب، ومشاركة على الشبكات الاجتماعية، وإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام عدة تقنيات لتحسين PDF:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تصغير أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إلغاء تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة تسطيح حقول النماذج
- إزالة أو تسطيح التعليقات التوضيحية

{{% alert color="primary" %}}

يمكن العثور على شرح مفصل لطرق التحسين في صفحة نظرة عامة على طرق التحسين.

{{% /alert %}}

## تحسين مستند PDF للويب

التحسين، أو الخطية للويب، يشير إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح ويب. لتحسين ملف للعرض على الويب:

1. افتح المستند الإدخالي في كائن [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. استخدم طريقة [تحسين](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. احفظ المستند المُحسَّن باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يوضح المقتطف البرمجي التالي كيفية تحسين مستند PDF للويب.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## تقليل حجم PDF

تتيح لك طريقة [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) تقليل حجم المستند عن طريق إزالة المعلومات غير الضرورية. بشكل افتراضي، تعمل هذه الطريقة على النحو التالي:

- تُزال الموارد التي لا تُستخدم في صفحات المستند
- يتم دمج الموارد المتكافئة في كائن واحد
- تُحذف الكائنات غير المستخدمة

المقتطف أدناه هو مثال. لاحظ، مع ذلك، أن هذه الطريقة لا تستطيع ضمان تقليص حجم المستند.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## إدارة استراتيجية التحسين

يمكننا أيضًا تخصيص استراتيجية التحسين. حاليًا، تستخدم طريقة [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 5 تقنيات. يمكن تطبيق هذه التقنيات باستخدام طريقة OptimizeResources() مع معامل [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### تصغير أو ضغط جميع الصور

لدينا طريقتان للتعامل مع الصور: تقليل جودة الصورة و/أو تغيير دقتها. في جميع الأحوال، يجب تطبيق [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/). في المثال التالي، نقوم بتصغير الصور عن طريق تقليل ImageQuality إلى 50.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### إزالة الكائنات غير المستخدمة

في بعض الأحيان يحتوي مستند PDF على كائنات PDF غير مُشار إليها من أي كائن آخر في المستند. قد يحدث ذلك، على سبيل المثال، عندما تُزيل صفحة من شجرة صفحات المستند لكن كائن الصفحة نفسه لا يُزال. إزالة هذه الكائنات لا يجعل المستند غير صالح بل يقلل حجمه.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### إزالة التدفقات غير المستخدمة

في بعض الأحيان يحتوي المستند على تدفقات موارد غير مستخدمة. هذه التدفقات ليست “كائنات غير مستخدمة” لأنها مُشار إليها من قاموس موارد الصفحة. لذلك، لا تُزال باستخدام طريقة “إزالة الكائنات غير المستخدمة”. لكن هذه التدفقات لا تُستَخدم أبدًا مع محتوى الصفحة. قد يحدث ذلك عندما تُزيل صورة من الصفحة ولكن لا تُزال من موارد الصفحة. كذلك، يتكرر هذا الوضع عندما تُستخرج صفحات من المستند وتكون صفحات المستند لديها موارد “مشتركة”، أي كائن Resources نفسه. يتم تحليل محتوى الصفحات لتحديد ما إذا كان تدفق المورد مستخدمًا أم لا. تُزال التدفقات غير المستخدمة. هذا أحيانًا يقلل من حجم المستند. استخدام هذه التقنية مشابه للخطوة السابقة:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### ربط التدفقات المكررة

بعض المستندات قد تحتوي على عدة تدفقات موارد متطابقة (مثل الصور، على سبيل المثال). قد يحدث ذلك، على سبيل المثال، عندما يُدمج المستند مع نفسه. يحتوي المستند الناتج على نسختين مستقلتين من نفس تدفق المورد. نقوم بتحليل جميع تدفقات الموارد ومقارنتها. إذا كانت التدفقات مكررة، يتم دمجها، أي يُبقى نسخة واحدة فقط. يتم تعديل المراجع وفقًا لذلك، وتُزال نسخ الكائن. في بعض الحالات، يساعد ذلك على تقليل حجم المستند.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### إلغاء تضمين الخطوط

إذا كان المستند يستخدم خطوطًا مضمَّنة، فهذا يعني أن جميع بيانات الخط مخزنة في المستند. الميزة هي أن المستند يمكن عرضه بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. ولكن تضمين الخطوط يجعل المستند أكبر حجمًا. تُزيل طريقة إلغاء تضمين الخطوط جميع الخطوط المضمنة. وبالتالي، ينخفض حجم المستند لكن قد يصبح المستند غير قابل للقراءة إذا لم يتم تثبيت الخط المناسب.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

تطبق موارد التحسين هذه الأساليب على المستند. إذا تم تطبيق أي من هذه الأساليب، فمن المرجح أن ينخفض حجم المستند. إذا لم يتم تطبيق أي من هذه الأساليب، فلن يتغير حجم المستند وهذا واضح.

## طرق إضافية لتقليل حجم مستند PDF

### إزالة أو تسوية التعليقات التوضيحية

يمكن حذف التعليقات التوضيحية عندما تكون غير ضرورية. عندما تكون مطلوبة ولكن لا تحتاج إلى تحرير إضافي، يمكن تسويتها. كلا هاتين الطريقتين سيقللان من حجم الملف.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### إزالة حقول النموذج

إذا كان مستند PDF يحتوي على نماذج AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسوية حقول النموذج.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### تحويل PDF من مساحة ألوان RGB إلى الرمادي

يتكون ملف PDF من نص، صورة، مرفق، تعليقات توضيحية، رسوم بيانية، وغيرها من الكائنات. قد تواجه الحاجة إلى تحويل PDF من مساحة ألوان RGB إلى الرمادي بحيث يصبح أسرع أثناء طباعة تلك الملفات. أيضًا، عند تحويل الملف إلى الرمادي، يتم تقليل حجم المستند أيضًا، ولكن قد يؤدي ذلك أيضًا إلى انخفاض جودة المستند. هذه الميزة مدعومة حاليًا بميزة Pre-Flight في Adobe Acrobat، ولكن عندما نتحدث عن أتمتة Office، يعد Aspose.PDF حلًا نهائيًا لتوفير مثل هذه الإمكانيات لتعديل المستندات. لتحقيق هذا المتطلب، يمكن استخدام مقتطف الشيفرة التالي.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### ضغط FlateDecode

يوفر Aspose.PDF للغة Python عبر .NET دعم ضغط FlateDecode لوظيفة تحسين PDF. يوضح مقتطف الشيفرة التالي كيفية استخدام الخيار في التحسين لتخزين الصور باستخدام ضغط **FlateDecode**:

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


