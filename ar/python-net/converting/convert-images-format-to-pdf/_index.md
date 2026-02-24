---
title: تحويل صيغ الصور المختلفة إلى PDF باستخدام Python
linktitle: تحويل الصور إلى PDF
type: docs
weight: 60
url: /ar/python-net/convert-images-format-to-pdf/
lastmod: "2025-09-01"
description: تحويل صيغ الصور المختلفة مثل BMP و CGM و DICOM و PNG و TIFF و EMF و SVG إلى PDF باستخدام Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل الصور إلى PDF باستخدام Python
Abstract: تقدم هذه المقالة دليلًا شاملاً حول تحويل صيغ الصور المختلفة إلى PDF باستخدام Python، مع الاستفادة بشكل خاص من مكتبة Aspose.PDF للـ Python عبر .NET. تغطي المقالة مجموعة من صيغ الصور بما في ذلك BMP و CGM و DICOM و EMF و GIF و PNG و SVG و TIFF. يوضح كل قسم الخطوات المطلوبة لإجراء التحويل، مع توفير مقتطفات من الشيفرة لتوضيح العملية. على سبيل المثال، يتضمن تحويل BMP إلى PDF إنشاء مستند PDF جديد، تعريف موضع الصورة، إدراج الصورة، وحفظ المستند. وبالمثل، بالنسبة لصيغ مثل CGM و DICOM وغيرها، يتم توضيح خيارات التحميل المحددة وخطوات المعالجة. كما تسلط المقالة الضوء على مزايا استخدام Aspose.PDF لهذه المهام، مثل دعمه لطرق ترميز مختلفة والقدرة على معالجة كل من الصور ذات الإطار الواحد والمتعدد.
---

## تحويلات صور Python إلى PDF

**Aspose.PDF for Python via .NET**  يتيح لك تحويل صيغ مختلفة من الصور إلى ملفات PDF. تُظهر مكتبتنا مقتطفات من الشيفرة لتحويل أشهر صيغ الصور، مثل - BMP و CGM و DICOM و EMF و JPG و PNG و SVG و TIFF.

## تحويل BMP إلى PDF

تحويل ملفات BMP إلى مستند PDF باستخدام مكتبة **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> الصور هي ملفات ذات امتداد. BMP يمثل ملفات صورة نقطية تُستخدم لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسومات وتُعرف أيضًا بملف صورة نقطية مستقل عن الجهاز (DIB).

يمكنك تحويل BMP إلى ملفات PDF باستخدام Aspose.PDF for Python عبر .NET API. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

خطوات تحويل BMP إلى PDF باستخدام Python:

1. إنشاء مستند PDF فارغ.
1. إنشاء الصفحة المطلوبة، على سبيل المثال أنشأنا A4، لكن يمكنك تحديد تنسيقك الخاص.
1. وضع الصورة (من infile) داخل الصفحة باستخدام المستطيل المحدد.
1. حفظ المستند كملف PDF.

إذن فإن المقتطف البرمجي التالي يتبع هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرب تحويل BMP إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["BMP إلى PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)، حيث يمكنك تجربة الوظيفة وجودتها.

[![تحويل Aspose.PDF BMP إلى PDF باستخدام التطبيق المجاني](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## تحويل CGM إلى PDF

تحويل ملف CGM (Computer Graphics Metafile) إلى PDF (أو تنسيق مدعوم آخر) باستخدام Aspose.PDF للـ Python عبر .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> هو امتداد ملف لتنسيق Computer Graphics Metafile يُستخدم عادةً في تطبيقات CAD (التصميم المدعوم بالحاسوب) وتطبيقات الرسوم التقديمية. CGM هو تنسيق رسومات متجهية يدعم ثلاث طرق ترميز مختلفة: ثنائي (أفضل لسرعة قراءة البرنامج)، معتمد على الأحرف (ينتج أصغر حجم ملف ويسمح بنقل بيانات أسرع) أو ترميز نصي واضح (يتيح للمستخدمين قراءة وتعديل الملف باستخدام محرر نصوص).

تحقق من المقتطف البرمجي التالي لتحويل ملفات CGM إلى تنسيق PDF.

خطوات تحويل CGM إلى PDF باستخدام Python:

1. تحديد مسارات الملفات
1. تعيين خيارات التحميل لـ CGM.
1. تحويل CGM إلى PDF
1. طباعة رسالة التحويل

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = apdf.CgmLoadOptions()

    # Open PDF document
    document = apdf.Document(path_infile, options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## تحويل DICOM إلى PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> هو تنسيق معيار صناعي طبي لإنشاء وتخزين ونقل وعرض الصور الطبية الرقمية والمستندات للمرضى المفحوصين.

**Aspose.PDF for Python** يتيح لك تحويل صور DICOM و SVG، ولكن لأسباب تقنية عند إضافة الصور تحتاج إلى تحديد نوع الملف الذي سيُضاف إلى PDF.

المقتطف البرمجي التالي يوضح كيفية تحويل ملفات DICOM إلى تنسيق PDF باستخدام Aspose.PDF. يجب تحميل صورة DICOM، وضع الصورة على صفحة في ملف PDF وحفظ الناتج كملف PDF. نستخدم مكتبة pydicom الإضافية لتعيين أبعاد هذه الصورة. إذا رغبت في تحديد موضع الصورة على الصفحة، يمكنك تخطي هذا المقتطف.

1. تهيئة كائن 'ap.Document()' جديد وإضافة صفحة
1. إدراج صورة DICOM. إنشاء apdf.Image()، ضبط نوعها إلى DICOM، وتعيين مسار الملف.
1. تعديل حجم الصفحة. مطابقة أبعاد صفحة PDF مع حجم صورة DICOM، وإزالة الهوامش.
1. إضافة الصورة إلى الصفحة، حفظ المستند إلى ملف الإخراج.

1. تحميل ملف DICOM.
1. استخراج أبعاد الصورة.
1. طباعة حجم الصورة.
1. إنشاء مستند PDF جديد.
1. إعداد صورة DICOM للتحويل إلى PDF.
1. تعيين حجم صفحة PDF وهوامشها.
1. إضافة الصورة إلى الصفحة.
1. حفظ ملف PDF.
1. طباعة رسالة التحويل.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    # Load the DICOM file
    dicom_file = pydicom.dcmread(path_infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = apdf.Document()
    page = document.pages.add()
    image = apdf.Image()
    image.file_type = apdf.ImageFileType.DICOM
    image.file = path_infile

    # Set page dimensions

    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرب تحويل DICOM إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)، حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من DICOM إلى PDF باستخدام التطبيق المجاني](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## تحويل EMF إلى PDF

<abbr title="Enhanced metafile format">EMF</abbr> يخزن الصور الرسومية بشكل مستقل عن الجهاز. تتألف ملفات الميتا الخاصة بـ EMF من سجلات بطول متغير بترتيب زمني يمكنها عرض الصورة المخزنة بعد التحليل على أي جهاز إخراج.

توضح الشفرة البرمجية التالية كيفية تحويل EMF إلى PDF باستخدام Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(path_infile, rectangle)

    # Save the file into PDF format
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرب تحويل EMF إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من EMF إلى PDF باستخدام التطبيق المجاني](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## تحويل GIF إلى PDF

تحويل ملفات GIF إلى مستند PDF باستخدام مكتبة **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> قادر على تخزين البيانات المضغوطة دون فقدان الجودة في صيغة لا تزيد عن 256 لونًا. تم تطوير صيغة GIF المستقلة عن الأجهزة في عام 1987 (GIF87a) بواسطة CompuServe لنقل الصور النقطية عبر الشبكات.

لذا توضح الشفرة البرمجية التالية هذه الخطوات وتظهر كيفية تحويل BMP إلى PDF باستخدام Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرب تحويل GIF إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من GIF إلى PDF باستخدام التطبيق المجاني](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## تحويل PNG إلى PDF

**Aspose.PDF for Python via .NET** يدعم ميزة تحويل صور PNG إلى صيغة PDF. تحقق من الشفرة البرمجية التالية لإنجاز مهمتك.

<abbr title="Portable Network Graphics">PNG</abbr> يُشير إلى نوع من تنسيقات ملفات الصور النقطية التي تستخدم ضغطًا بدون فقد، مما يجعلها شائعة بين مستخدميها.

يمكنك تحويل صورة PNG إلى PDF باستخدام الخطوات التالية:

1. إنشاء مستند PDF جديد.
1. تحديد موضع الصورة.
1. حفظ ملف PDF.
1. طباعة رسالة التحويل.

علاوة على ذلك، توضح الشفرة البرمجية أدناه كيفية تحويل PNG إلى PDF باستخدام Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرب تحويل PNG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PNG إلى PDF باستخدام التطبيق المجاني](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## تحويل SVG إلى PDF

**Aspose.PDF for Python via .NET** يوضح كيفية تحويل صور SVG إلى صيغة PDF وكيفية الحصول على أبعاد ملف SVG المصدر.

الرسومات المتجهية القابلة للتوسع (SVG) هي عائلة من المواصفات لتنسيق ملف قائم على XML للرسومات المتجهية ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). تم تطوير مواصفة SVG كمعيار مفتوح تحت تطوير اتحاد الشبكة العالمية (W3C) منذ عام 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> الصور وسلوكياتها معرفة في ملفات نصية XML. وهذا يعني أنه يمكن البحث عنها، فهرستها، برمجتها، وإذا لزم الأمر، ضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نصوص، لكن غالبًا ما يكون من الأكثر ملاءمة إنشاؤها باستخدام برامج الرسم مثل Inkscape.

{{% alert color="success" %}}
**جرب تحويل صيغة SVG إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF for Python via .NET تطبيقًا مجانيًا عبر الإنترنت ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من SVG إلى PDF باستخدام التطبيق المجاني](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

المقتطف البرمجي التالي يوضح عملية تحويل ملف SVG إلى تنسيق PDF باستخدام Aspose.PDF للغة Python.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.SvgLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## تحويل TIFF إلى PDF

**Aspose.PDF** تنسيق ملف مدعوم، سواء كان إطارًا واحدًا أو صورة TIFF متعددة الإطارات. يعني ذلك أنه يمكنك تحويل صورة TIFF إلى PDF.

TIFF أو TIF، Tagged Image File Format، يمثل الصور النقطية التي تُستخدم على مجموعة متنوعة من الأجهزة التي تتوافق مع معيار تنسيق الملف هذا. يمكن أن يحتوي صورة TIFF على عدة إطارات بصور مختلفة. تنسيق ملف Aspose.PDF مدعوم أيضًا، سواء كان إطارًا واحدًا أو صورة TIFF متعددة الإطارات.

يمكنك تحويل TIFF إلى PDF بنفس الطريقة كما هو الحال مع بقية رسومات تنسيقات ملفات الصور النقطية:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## تحويل CDR إلى PDF

المقتطف البرمجي التالي يوضح كيفية تحميل ملف CorelDRAW (CDR) وحفظه كملف PDF باستخدام 'CdrLoadOptions' في Aspose.PDF للغة Python عبر .NET.

1. إنشاء 'CdrLoadOptions()' لتكوين طريقة تحميل ملف CDR.
1. تهيئة كائن Document باستخدام ملف CDR وخيارات التحميل.
1. حفظ المستند كملف PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.CdrLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## تحويل JPEG إلى PDF

هذا المثال يوضح كيفية تحويل JPEG إلى ملف PDF باستخدام Aspose.PDF للغة Python عبر .NET.

1. إنشاء مستند PDF جديد.
1. إضافة صفحة جديدة.
1. تحديد مستطيل الموضع (بحجم A4: 595x842 نقطة).
1. إدراج الصورة في الصفحة.
1. حفظ ملف PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

