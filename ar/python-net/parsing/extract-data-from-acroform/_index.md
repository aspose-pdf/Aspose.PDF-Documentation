---
title: استخراج البيانات من AcroForm باستخدام بايثون
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/python-net/extract-data-from-acroform/
description: Aspose.PDF يجعل من السهل استخراج بيانات حقول النماذج من ملفات PDF. تعرف على كيفية استخراج البيانات من AcroForms وحفظها بصيغة JSON أو XML أو FDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من AcroForm عبر بايثون
Abstract: توفر المقالة دليلًا شاملاً حول استخدام Aspose.PDF لبايثون لإدارة حقول النماذج داخل مستندات PDF. توضح المقالة طرقًا مختلفة لاستخراج البيانات ومعالجتها وتصديرها من ملفات PDF. تبدأ المقالة بعرض كيفية استخراج قيم حقول النماذج وتخزينها في قاموس، ثم إخراج البيانات بصيغة JSON. كما توضح تصدير بيانات النماذج مباشرةً إلى ملفات JSON، مما يعزز قدرات تسلسل البيانات. بالإضافة إلى ذلك، تغطي المقالة تصدير بيانات النماذج إلى صيغ أخرى مثل XML وFDF (صيغة بيانات النماذج) وXFDF، وهي مفيدة لتبادل البيانات وتخزينها بطريقة منظمة. يتضمن كل قسم مقتطفات كود بايثون لمساعدة القارئ على الفهم والتنفيذ. بشكل عام، تُعد المقالة مصدرًا عمليًا للمطورين الذين يرغبون في دمج معالجة نماذج PDF في تطبيقاتهم المكتوبة ببايثون.
---

## استخراج حقول النموذج من مستند PDF

إلى جانب تمكينك من إنشاء حقول نماذج وتعبئتها، يجعل Aspose.PDF لبايثون من السهل استخراج بيانات حقول النماذج أو معلومات حول حقول النماذج من ملفات PDF.

يقوم مقتطف الكود بإنشاء قاموس لتخزين قيم جميع الحقول في نموذج PDF. يت iterates عبر أسماء الحقول في النموذج، يستخرج قيمها، ويملأ القاموس بهذه البيانات. أخيرًا، يطبع القيم المجمعة للنموذج.

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

## استرجاع قيمة حقل النموذج حسب العنوان

## استخراج حقول النموذج من مستند PDF إلى JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

يستخرج مقتطف الكود Python المقدم قيم حقوله ويسلسل هذه البيانات إلى صيغة JSON. يستورد الوحدات اللازمة، يُنشئ مسارات ملفات الإدخال والإخراج، يستخرج أسماء الحقول وقيمها من نموذج PDF، ويكتب سلسلة JSON المسلسلة إلى ملف الإخراج المحدد.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## استخراج البيانات إلى XML من ملف PDF

يقوم مقتطف الكود Python التالي بإنشاء كائن نموذج، وربط مستند PDF بهذا الكائن، وتصدير بيانات النموذج إلى ملف XML. يقوم الكود باستخراج البيانات تلقائيًا من نموذج PDF وحفظها بصيغة XML منظمة.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

يقوم مقتطف الكود التالي بإنشاء كائن نموذج، وربط مستند PDF بهذا النموذج، ثم تصدير بيانات النموذج إلى ملف FDF (صيغة بيانات النماذج). يُعد ملف FDF تنسيقًا يُستخدم لتخزين بيانات النماذج من مستندات PDF، مما يتيح تبادل البيانات بسهولة.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

