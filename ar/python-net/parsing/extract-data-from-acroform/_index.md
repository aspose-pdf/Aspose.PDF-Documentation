---
title: استخراج البيانات من AcroForm باستخدام Python
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/python-net/extract-data-from-acroform/
description: يجعل Aspose.PDF من السهل استخراج بيانات حقل النموذج من ملفات PDF. تعرف على كيفية استخراج البيانات من AcroForms وحفظها بتنسيق JSON أو XML أو FDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من AcroForm عبر بايثون
Abstract: توفر المقالة دليلًا شاملاً حول استخدام Aspose.PDF لـ Python لإدارة حقول النموذج داخل مستندات PDF. يوضح بالتفصيل الطرق المختلفة لاستخراج بيانات النموذج ومعالجتها وتصديرها من ملفات PDF. تبدأ المقالة بتوضيح كيفية استخراج قيم حقول النموذج وتخزينها في قاموس، ثم إخراج البيانات بتنسيق JSON. كما يوضح أيضًا تصدير بيانات النموذج مباشرةً إلى ملفات JSON، مما يعزز إمكانات تسلسل البيانات. بالإضافة إلى ذلك، تتناول المقالة تصدير بيانات النموذج إلى تنسيقات أخرى مثل XML و FDF (تنسيق بيانات النماذج) و XFDF، والتي تعد مفيدة لتبادل البيانات وتخزين البيانات المهيكلة. يتضمن كل قسم مقتطفات شفرة Python للمساعدة في الفهم والتنفيذ. بشكل عام، تعد المقالة بمثابة مورد عملي للمطورين الذين يتطلعون إلى دمج معالجة نماذج PDF في تطبيقات Python الخاصة بهم.
---

## استخراج حقول النموذج من وثيقة PDF

[نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) من `aspose.pdf.facades` توفر مساحة الاسم طريقة مباشرة لقراءة بيانات حقل AcroForm دون فتح نموذج كائن المستند الكامل. قم بتكرار الغطاء `form.field_names` للحصول على اسم كل حقل موجود في النموذج، ثم اتصل `form.get_field(name)` لاسترداد قيمتها الحالية.

1. قم بإنشاء `Form` الكائن عن طريق تمرير مسار ملف الإدخال.
1. قم بتكرار الغطاء `form.field_names` لتعداد جميع أسماء الحقول.
1. اتصل `form.get_field(name)` لكل اسم وتخزين النتيجة في قاموس.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## استرداد قيمة حقل النموذج حسب العنوان

عندما تعرف اسم الحقل الدقيق (العنوان) المحدد في نموذج PDF، يمكنك استرداد قيمته مباشرة باستخدام `form.get_field(name)` دون التكرار على المجموعة الميدانية بأكملها. هذا هو الأسلوب الأسرع عندما تكون هناك حاجة إلى حقول محددة فقط.

1. قم بإنشاء [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) كائن بمسار ملف الإدخال.
1. اتصل `form.get_field("FieldName")` باستخدام عنوان الحقل الدقيق كما يظهر في PDF.
1. استخدم قيمة السلسلة التي تم إرجاعها حسب الحاجة في التطبيق الخاص بك.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## استخراج حقول النموذج من مستند PDF إلى JSON

هناك طريقتان لتصدير بيانات AcroForm إلى JSON. الأول يستخدم المدمج `export_json` تم تشغيل الطريقة [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form)، والذي يقوم بتسلسل جميع البيانات الميدانية مباشرة إلى دفق الملفات في مكالمة واحدة.

1. قم بإنشاء `Form` كائن بمسار ملف الإدخال.
1. افتح ملف الإخراج كتدفق ثنائي باستخدام `FileIO`.
1. اتصل `form.export_json(stream, True)` لكتابة إخراج JSON.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

الطريقة الثانية تبني قاموس Python من `field_names` و `get_field`، ثم يقوم بتسلسلها باستخدام `json.dumps`. استخدم هذا عندما تحتاج إلى تحويل البيانات أو تصفيتها قبل كتابتها.

1. قم بتكرار الغطاء `form.field_names` وقم بتعبئة القاموس بقيم الحقول.
1. قم بتسلسل القاموس باستخدام `json.dumps(form_data, indent=4)`.
1. اكتب سلسلة JSON الناتجة إلى ملف الإخراج.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## استخراج البيانات إلى XML من ملف PDF

تصدير XML مفيد لدمج بيانات نموذج PDF مع الأنظمة التي تستهلك خلاصات XML المهيكلة أو المخططات. ال [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) يوفر الفصل `export_xml` للتعامل مع التحويل في خطوة واحدة.

1. قم بإنشاء `Form` المثيل وربط ملف PDF بـ `form.bind_pdf(path)`.
1. افتح ملف الإخراج كتدفق ثنائي.
1. اتصل `form.export_xml(stream)` لكتابة جميع البيانات الميدانية بصيغة XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## تصدير البيانات إلى FDF من ملف PDF

FDF (تنسيق بيانات النماذج) هو تنسيق التبادل القياسي لبيانات AcroForm وهو مدعوم على نطاق واسع من قبل برامج عرض PDF وأدوات المعالجة. استخدم `export_fdf` على [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) فئة لإنتاج ملف FDF مستقل يمكن استيراده مرة أخرى إلى PDF الأصلي أو أي نموذج متوافق آخر.

1. قم بإنشاء `Form` المثيل وربط ملف PDF المصدر بـ `form.bind_pdf(path)`.
1. افتح ملف الإخراج كتدفق ثنائي.
1. اتصل `form.export_fdf(stream)` لكتابة بيانات FDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## تصدير البيانات إلى XFDF من ملف PDF

XFDF (تنسيق بيانات نماذج XML) هو خليفة FDF المستند إلى XML وهو أكثر ملاءمة للاستخدام في خدمات الويب وخطوط أنابيب البيانات الحديثة. مثل FDF، يمكن استيراد ملف XFDF مرة أخرى إلى نموذج PDF متوافق. استخدم `export_xfdf` على [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) فئة لتوليد الإخراج.

1. قم بإنشاء `Form` المثيل وربط ملف PDF المصدر بـ `form.bind_pdf(path)`.
1. افتح ملف الإخراج كتدفق ثنائي.
1. اتصل `form.export_xfdf(stream)` لكتابة بيانات XFDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```
