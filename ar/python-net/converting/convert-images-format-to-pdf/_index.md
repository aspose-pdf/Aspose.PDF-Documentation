---
title: تحويل تنسيقات الصور إلى PDF في Python
linktitle: تحويل الصور إلى PDF
type: docs
weight: 60
url: /ar/python-net/convert-images-format-to-pdf/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل BMP و CGM و DICOM و PNG و TIFF و EMF و SVG وتنسيقات الصور الأخرى إلى PDF في بايثون باستخدام Aspose.PDF لبيثون عبر.NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل الصور إلى PDF في Python
Abstract: توفر هذه المقالة دليلًا شاملاً حول تحويل تنسيقات الصور المختلفة إلى PDF باستخدام Python، وتحديدًا الاستفادة من مكتبة Aspose.PDF لـ Python عبر .NET. تتناول المقالة مجموعة من تنسيقات الصور بما في ذلك BMP و CGM و DICOM و EMF و GIF و PNG و SVG و TIFF. يفصل كل قسم الخطوات المطلوبة لإجراء التحويل، مع توفير مقتطفات التعليمات البرمجية لتوضيح العملية. على سبيل المثال، يتضمن تحويل BMP إلى PDF إنشاء مستند PDF جديد، وتحديد موضع الصورة، وإدراج الصورة، وحفظ المستند. وبالمثل، بالنسبة لتنسيقات مثل CGM و DICOM وغيرها، يتم تحديد خيارات تحميل وخطوات معالجة محددة. تسلط المقالة الضوء أيضًا على مزايا استخدام Aspose.PDF لمثل هذه المهام، مثل دعمها لطرق التشفير المختلفة والقدرة على معالجة الصور أحادية الإطار ومتعددة الإطارات.
---

## التحويلات ذات الصلة

- [تحويل PDF إلى تنسيقات صور](/pdf/ar/python-net/convert-pdf-to-images-format/) عندما تحتاج إلى سير العمل العكسي.
- [تحويل HTML إلى PDF](/pdf/ar/python-net/convert-html-to-pdf/) لمحتوى الويب ومصادر MHTML.
- [تحويل تنسيقات الملفات الأخرى إلى PDF](/pdf/ar/python-net/convert-other-files-to-pdf/) لإدخالات EPUB وXPS والنص وغير ذلك من المدخلات غير المصورة.

## تحويل صور بايثون إلى PDF

**Aspose.pdf لبايثون عبر .NET** يسمح لك بتحويل تنسيقات مختلفة من الصور إلى ملفات PDF. تعرض مكتبتنا مقتطفات التعليمات البرمجية لتحويل تنسيقات الصور الأكثر شيوعًا، مثل تنسيقات BMP و CGM و DICOM و EMF و JPG و PNG و SVG و TIFF.

## تحويل BMP إلى PDF

قم بتحويل ملفات BMP إلى مستند PDF باستخدام**aspose.pdf لبيثون عبر مكتبة.NET**.

<abbr title="Bitmap Image File">صيغة بيتماب</abbr> الصور هي ملفات لها امتداد. تمثل BMP ملفات الصور النقطية المستخدمة لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسومات وتسمى أيضًا تنسيق ملف الصورة النقطية المستقل للجهاز (DIB).

يمكنك تحويل ملفات BMP إلى PDF باستخدام Aspose.PDF لبيثون عبر .NET API. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

خطوات تحويل BMP إلى PDF في بايثون:

1. قم بإنشاء مستند PDF فارغ.
1. قم بإنشاء الصفحة التي تحتاجها، على سبيل المثال، أنشأنا A4، ولكن يمكنك تحديد التنسيق الخاص بك.
1. يضع الصورة (من infile) داخل الصفحة باستخدام المستطيل المحدد.
1. احفظ المستند كملف PDF.

لذلك يتبع مقتطف الشفرة التالي هذه الخطوات ويوضح كيفية تحويل BMP إلى PDF باستخدام Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل BMP إلى PDF عبر الإنترنت**

يقدم لك Aspose التطبيق عبر الإنترنت [«BMP إلى PDF»](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل BMP إلى PDF باستخدام التطبيق](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## تحويل CGM إلى PDF

قم بتحويل ملف CGM (ملف تعريف رسومات الكمبيوتر) إلى PDF (أو أي تنسيق آخر مدعوم) باستخدام Aspose.PDF لبيثون عبر .NET.

<abbr title="Computer Graphics Metafile">سي جي إم</abbr> هو امتداد ملف لتنسيق ملف تعريف رسومات الكمبيوتر الذي يشيع استخدامه في CAD (التصميم بمساعدة الكمبيوتر) وتطبيقات رسومات العرض التقديمي. CGM هو تنسيق رسومي متجه يدعم ثلاث طرق ترميز مختلفة: ثنائي (الأفضل لسرعة قراءة البرنامج)، قائم على الأحرف (ينتج أصغر حجم للملف ويسمح بنقل البيانات بشكل أسرع) أو ترميز النص الواضح (يسمح للمستخدمين بقراءة وتعديل الملف باستخدام محرر نصوص).

تحقق من مقتطف الشفرة التالي لتحويل ملفات CGM إلى تنسيق PDF.

خطوات تحويل CGM إلى PDF في بايثون:

1. تعريف مسارات الملفات
1. قم بتعيين خيارات التحميل لـ CGM.
1. تحويل CGM إلى PDF
1. طباعة رسالة تحويل

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل DICOM إلى PDF

<abbr title="Digital Imaging and Communications in Medicine">ديكوم</abbr> الشكل هو معيار الصناعة الطبية لإنشاء وتخزين ونقل وتصور الصور الطبية الرقمية ووثائق المرضى الذين تم فحصهم.

**Aspose.pdf for Python** يسمح لك بتحويل صور DICOM و SVG، ولكن لأسباب فنية لإضافة الصور تحتاج إلى تحديد نوع الملف المراد إضافته إلى PDF.

يوضح مقتطف الشفرة التالي كيفية تحويل ملفات DICOM إلى تنسيق PDF باستخدام Aspose.PDF. يجب عليك تحميل صورة DICOM ووضع الصورة على صفحة في ملف PDF وحفظ الإخراج كملف PDF. نحن نستخدم مكتبة pydicom الإضافية لتعيين أبعاد هذه الصورة. إذا كنت ترغب في وضع الصورة على الصفحة، يمكنك تخطي مقتطف الشفرة هذا.

1. قم بتحميل ملف DICOM.
1. استخراج أبعاد الصورة.
1. حجم صورة الطباعة.
1. قم بإنشاء مستند PDF جديد.
1. قم بإعداد صورة DICOM لـ PDF.
1. قم بتعيين حجم صفحة PDF والهوامش.
1. أضف الصورة إلى الصفحة.
1. احفظ ملف PDF.
1. طباعة رسالة تحويل.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل DICOM إلى PDF عبر الإنترنت**

يقدم لك Aspose التطبيق عبر الإنترنت [«DICOM إلى PDF»](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل DICOM إلى PDF باستخدام التطبيق](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## تحويل EMF إلى PDF

<abbr title="Enhanced metafile format">EMF</abbr> يخزن الصور الرسومية بشكل مستقل عن الجهاز. تتكون ملفات التعريف الخاصة بـ EMF من سجلات متغيرة الطول بترتيب زمني يمكنها عرض الصورة المخزنة بعد التحليل على أي جهاز إخراج.

يوضح مقتطف الشفرة التالي كيفية تحويل EMF إلى PDF باستخدام Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل EMF إلى PDF عبر الإنترنت**

يقدم لك Aspose التطبيق عبر الإنترنت [«EMF إلى PDF»](https://products.aspose.app/pdf/conversion/emf-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل EMF إلى PDF باستخدام التطبيق](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## تحويل GIF إلى PDF

قم بتحويل ملفات GIF إلى مستند PDF باستخدام**aspose.pdf لبيثون عبر مكتبة.NET**.

<abbr title="Graphics Interchange Format">صورة</abbr> قادر على تخزين البيانات المضغوطة دون فقدان الجودة بتنسيق لا يزيد عن 256 لونًا. تم تطوير تنسيق GIF المستقل عن الأجهزة في عام 1987 (GIF87a) بواسطة CompuServe لنقل الصور النقطية عبر الشبكات.

لذلك يتبع مقتطف الشفرة التالي هذه الخطوات ويوضح كيفية تحويل BMP إلى PDF باستخدام Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل GIF إلى PDF عبر الإنترنت**

يقدم لك Aspose التطبيق عبر الإنترنت [«GIF إلى PDF»](https://products.aspose.app/pdf/conversion/gif-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل GIF إلى PDF باستخدام التطبيق](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## تحويل PNG إلى PDF

**Aspose.pdf لبيثون عبر ميزة دعم.NET** لتحويل صور PNG إلى صيغة PDF. تحقق من مقتطف الشفرة التالي لتحقيق مهمتك.

<abbr title="Portable Network Graphics">PNG</abbr> يشير إلى نوع من تنسيقات ملفات الصور النقطية التي تستخدم ضغطًا بدون فقدان، مما يجعلها شائعة بين مستخدميها.

يمكنك تحويل PNG إلى صورة PDF باستخدام الخطوات التالية:

1. قم بإنشاء مستند PDF جديد.
1. تحديد موضع الصورة.
1. احفظ ملف PDF.
1. طباعة رسالة تحويل.

علاوة على ذلك، يوضح مقتطف الشفرة أدناه كيفية تحويل PNG إلى PDF باستخدام Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل PNG إلى PDF عبر الإنترنت**

يقدم لك Aspose التطبيق عبر الإنترنت [«PNG إلى PDF»](https://products.aspose.app/pdf/conversion/png-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل PNG إلى PDF باستخدام التطبيق](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## تحويل SVG إلى PDF

**Aspose.pdf لـ Python عبر .NET** يشرح كيفية تحويل صور SVG إلى صيغة PDF وكيفية الحصول على أبعاد ملف SVG المصدر.

تعد Scalable Vector Graphics (SVG) مجموعة من مواصفات تنسيق ملف يستند إلى XML للرسومات المتجهة ثنائية الأبعاد، سواء الثابتة أو الديناميكية (التفاعلية أو المتحركة). مواصفات SVG هي معيار مفتوح تم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> يتم تعريف الصور وسلوكياتها في ملفات XML النصية. وهذا يعني أنه يمكن البحث عنها وفهرستها وكتابتها وضغطها إذا لزم الأمر. كملفات XML، يمكن إنشاء صور SVG وتحريرها باستخدام أي محرر نصوص، ولكن غالبًا ما يكون إنشاؤها باستخدام برامج الرسم مثل Inkscape أكثر ملاءمة.

{{% alert color="success" %}}
** حاول تحويل تنسيق SVG إلى PDF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«SVG إلى PDF»](https://products.aspose.app/pdf/conversion/svg-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF | تحويل SVG إلى PDF مع التطبيق](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

يعرض مقتطف الشفرة التالي عملية تحويل ملف SVG إلى تنسيق PDF باستخدام Aspose.PDF لـ Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل TIFF إلى PDF

**Aspose.pdf** يتم دعم تنسيق الملف، سواء كان ذلك في إطار واحد أو صورة TIFF متعددة الإطارات. هذا يعني أنه يمكنك تحويل صورة TIFF إلى PDF.

يمثل TIFF أو TIF، تنسيق ملفات الصور ذات العلامات، صورًا نقطية مخصصة للاستخدام على مجموعة متنوعة من الأجهزة التي تتوافق مع معيار تنسيق الملفات هذا. يمكن أن تحتوي صورة TIFF على عدة إطارات بصور مختلفة. تنسيق ملف Aspose.PDF مدعوم أيضًا، سواء كان إطارًا واحدًا أو صورة TIFF متعددة الإطارات.

يمكنك تحويل TIFF إلى PDF بنفس الطريقة مثل رسومات تنسيقات الملفات النقطية المتبقية:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل CDR إلى PDF

يوضح مقتطف الشفرة التالي كيفية تحميل ملف CorelDraw (CDR) وحفظه كملف PDF باستخدام «CDRloadOptions» في Aspose.PDF لبيثون عبر.NET.

1. قم بإنشاء 'cdrloadOptions () 'لتكوين كيفية تحميل ملف CDR.
1. قم بتهيئة كائن مستند باستخدام ملف CDR وخيارات التحميل.
1. احفظ المستند كملف PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل JPEG إلى PDF

يوضح هذا المثال كيفية تحويل JPEG إلى ملف PDF باستخدام Aspose.PDF لبيثون عبر .NET.

1. قم بإنشاء مستند PDF جديد.
1. إضافة صفحة جديدة.
1. حدد مستطيل الموضع (حجم A4:595 × 842 نقطة).
1. أدخل الصورة في الصفحة.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
