---
title: تحسين ملفات PDF في بايثون
linktitle: تحسين ملف PDF
type: docs
weight: 30
url: /ar/python-net/optimize-pdf/
description: تعرف على كيفية تحسين حجم ملف PDF وضغطه وتقليله في Python باستخدام Aspose.PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ضغط صفحات PDF باستخدام بايثون
Abstract: توفر هذه المقالة دليلًا شاملاً حول تحسين ملفات PDF لتقليل حجمها وتحسين الأداء عبر منصات مختلفة، مثل صفحات الويب ورسائل البريد الإلكتروني وأنظمة التخزين. تتضمن تقنيات التحسين تقليل أحجام الصور وإزالة الموارد غير المستخدمة وإلغاء تضمين الخطوط. تمت مناقشة طرق محددة لتحسين ملفات PDF للويب وتقليل الحجم الإجمالي للملف، وذلك باستخدام أساليب «Optimize» و «OptimizeResources» في Aspose.PDF لـ Python. يمكن تخصيص استراتيجيات التحسين من خلال «OptimizationOptions»، مما يسمح بالإجراءات المستهدفة مثل ضغط الصور وإزالة الكائنات والتدفقات غير المستخدمة وربط التدفقات المكررة وإلغاء تضمين الخطوط. تشمل الاستراتيجيات الإضافية تسوية التعليقات التوضيحية وإزالة حقول النموذج وتحويل ملفات PDF من RGB إلى درجات الرمادي لتقليل الحجم بشكل أكبر. تسلط المقالة الضوء أيضًا على استخدام ضغط FlateDecode لتحسين الصورة، مما يضمن إدارة ملفات PDF الفعالة مع الحفاظ على الجودة والوظائف.
---

قد تحتوي وثيقة PDF أحيانًا على بيانات إضافية. سيساعدك تقليل حجم ملف PDF على تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب أو المشاركة على الشبكات الاجتماعية أو الإرسال عبر البريد الإلكتروني أو الأرشفة في التخزين. يمكننا استخدام العديد من التقنيات لتحسين PDF:

استخدم هذه الصفحة عندما تحتاج إلى تقليل حجم PDF للتسليم عبر الويب أو مشاركة البريد الإلكتروني أو توفير التخزين أو الإخراج السهل الطباعة دون إعادة إنشاء المستند من البداية.

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص جميع الصور أو ضغطها
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- الخطوط غير المضمّنة
- قم بإزالة الكائنات غير المستخدمة
- إزالة حقول نموذج التسوية
- إزالة التعليقات التوضيحية أو تسويتها

{{% alert color="primary" %}}

 يمكن العثور على شرح مفصل لطرق التحسين في صفحة نظرة عامة على طرق التحسين.

{{% /alert %}}

## تحسين مستند PDF للويب

يشير التحسين، أو التخطيط الخطي للويب، إلى عملية إنشاء ملف PDF مناسب للتصفح عبر الإنترنت باستخدام متصفح الويب. لتحسين ملف لعرضه على الويب:

1. افتح مستند الإدخال في [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن.
1. استخدم [تحسين](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.
1. احفظ المستند المحسّن باستخدام [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

يوضح مقتطف الشفرة التالي كيفية تحسين مستند PDF للويب.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## تصغير حجم PDF

ال [تحسين الموارد ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) تسمح لك الطريقة بتقليل حجم المستند عن طريق إزالة المعلومات غير الضرورية. بشكل افتراضي، تعمل هذه الطريقة كما يلي:

- تتم إزالة الموارد غير المستخدمة في صفحات المستند
- يتم ضم الموارد المتساوية إلى كائن واحد
- يتم حذف الكائنات غير المستخدمة

المقتطف أدناه هو مثال. لاحظ، مع ذلك، أن هذه الطريقة لا تضمن تقليص المستند.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## إدارة استراتيجية التحسين

يمكننا أيضًا تخصيص استراتيجية التحسين. حاليًا، فإن [تحسين الموارد ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) تستخدم الطريقة 5 تقنيات. يمكن تطبيق هذه التقنيات باستخدام طريقة OptimizeResources () مع [خيارات التحسين](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) المعلمة.

### تقليص أو ضغط جميع الصور

لدينا طريقتان للعمل مع الصور: تقليل جودة الصورة و/أو تغيير دقتها. على أي حال، [خيارات ضغط الصور](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) يجب تطبيقها. في المثال التالي، نقوم بتقليص الصور عن طريق تقليل ImageEquality إلى 50.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### إزالة الكائنات غير المستخدمة

تحتوي وثيقة PDF أحيانًا على كائنات PDF التي لم تتم الإشارة إليها من أي كائن آخر في المستند. قد يحدث هذا، على سبيل المثال، عند إزالة صفحة من شجرة صفحة المستند ولكن كائن الصفحة نفسه لا تتم إزالته. لا تؤدي إزالة هذه الكائنات إلى جعل المستند غير صالح بل يؤدي إلى تقليصه.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### إزالة التدفقات غير المستخدمة

في بعض الأحيان يحتوي المستند على تدفقات الموارد غير المستخدمة. هذه التدفقات ليست «كائنات غير مستخدمة» لأنها تمت الإشارة إليها من قاموس موارد الصفحة. وبالتالي، لا تتم إزالتها باستخدام طريقة «إزالة الكائنات غير المستخدمة». ولكن لا يتم استخدام هذه التدفقات أبدًا مع محتويات الصفحة. قد يحدث هذا في الحالات التي تتم فيها إزالة صورة من الصفحة ولكن ليس من موارد الصفحة. أيضًا، يحدث هذا الموقف غالبًا عندما يتم استخراج الصفحات من المستند وتحتوي صفحات المستند على موارد «مشتركة»، أي نفس كائن الموارد. يتم تحليل محتويات الصفحة لتحديد ما إذا كان تدفق الموارد مستخدمًا أم لا. تتم إزالة التدفقات غير المستخدمة. في بعض الأحيان يقلل حجم المستند. استخدام هذه التقنية مشابه للخطوة السابقة:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### ربط التدفقات المكررة

يمكن أن تحتوي بعض المستندات على العديد من تدفقات الموارد المتطابقة (مثل الصور، على سبيل المثال). قد يحدث هذا، على سبيل المثال عندما يكون المستند متسلسلًا مع نفسه. يحتوي مستند الإخراج على نسختين مستقلتين من نفس تدفق الموارد. نحن نحلل جميع تدفقات الموارد ونقارنها. في حالة تكرار التدفقات، يتم دمجها، أي تبقى نسخة واحدة فقط. يتم تغيير المراجع بشكل مناسب، وتتم إزالة نسخ الكائن. في بعض الحالات، يساعد ذلك على تقليل حجم المستند.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### إلغاء تضمين الخطوط

إذا كان المستند يستخدم خطوطًا مضمنة، فهذا يعني أن جميع بيانات الخط مخزنة في المستند. الميزة هي أن المستند قابل للعرض بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. لكن تضمين الخطوط يجعل المستند أكبر. تقوم طريقة إلغاء تضمين الخطوط بإزالة جميع الخطوط المضمنة. وبالتالي، يقل حجم المستند ولكن المستند نفسه قد يصبح غير قابل للقراءة إذا لم يتم تثبيت الخط الصحيح.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

تقوم موارد التحسين بتطبيق هذه الأساليب على المستند. في حالة تطبيق أي من هذه الطرق، سينخفض حجم المستند على الأرجح. إذا لم يتم تطبيق أي من هذه الطرق، فلن يتغير حجم المستند وهو أمر واضح.

## طرق إضافية لتقليل حجم مستند PDF

### إزالة التعليقات التوضيحية أو تسويتها

يمكن حذف التعليقات التوضيحية عندما تكون غير ضرورية. عند الحاجة إليها ولكن لا تتطلب تحريرًا إضافيًا، يمكن تسويتها. ستؤدي كلتا الطريقتين إلى تقليل حجم الملف.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### إزالة حقول النموذج

إذا كانت وثيقة PDF تحتوي على AcroForms، فيمكننا محاولة تقليل حجم الملف عن طريق تسوية حقول النموذج.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### قم بتحويل ملف PDF من مساحة ألوان RGB إلى درجات الرمادي

يتكون ملف PDF من النص والصورة والمرفقات والتعليقات التوضيحية والرسوم البيانية والكائنات الأخرى. قد تواجه مطلبًا لتحويل ملف PDF من مساحة ألوان RGB إلى درجات الرمادي بحيث يكون أسرع أثناء طباعة ملفات PDF هذه. أيضًا، عندما يتم تحويل الملف إلى درجات الرمادي، يتم تقليل حجم المستند أيضًا، ولكن يمكن أن يتسبب ذلك أيضًا في انخفاض جودة المستند. هذه الميزة مدعومة حاليًا من خلال ميزة Pre-Flight في Adobe Acrobat، ولكن عند الحديث عن التشغيل الآلي للمكتب، يعد Aspose.PDF حلاً نهائيًا لتوفير مثل هذه الروافع لمعالجة المستندات. من أجل تحقيق هذا المطلب، يمكن استخدام مقتطف الشفرة التالي.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### ضغط فك الشفرة المسطح

يوفر Aspose.PDF لبيثون عبر .NET دعمًا لضغط FlateDecode لوظيفة تحسين PDF. يوضح مقتطف الشفرة التالي أدناه كيفية استخدام الخيار في التحسين لتخزين الصور باستخدام ضغط **FlateDecode**:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## موضوعات المستندات ذات الصلة

- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [دمج ملفات PDF في بايثون](/pdf/ar/python-net/merge-pdf-documents/)
- [تقسيم ملفات PDF في بايثون](/pdf/ar/python-net/split-document/)
- [معالجة مستندات PDF في Python](/pdf/ar/python-net/manipulate-pdf-document/)

