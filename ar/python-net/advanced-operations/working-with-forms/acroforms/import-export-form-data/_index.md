---
title: استيراد وتصدير بيانات النماذج
type: docs
weight: 80
url: /ar/python-net/import-export-form-data/
description: يوضح هذا القسم كيفية استيراد وتصدير بيانات النماذج.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: تقنيات الاستيراد والتصدير باستخدام Aspose.PDF للـ Python عبر .NET.
Abstract: هذه المجموعة تقدم مجموعة شاملة من تقنيات استيراد وتصدير بيانات النماذج باستخدام Aspose.PDF للـ Python عبر .NET. تغطي سير عمل دمج نماذج PDF مع صيغ البيانات الخارجية بما في ذلك XML وFDF وXFDF وJSON. يمكن للمستخدمين أتمتة تعبئة النماذج بالجملة عن طريق استيراد البيانات المهيكلة إلى الحقول التفاعلية، أو استخراج القيم للحقول للتحليل أو النسخ الاحتياطي أو التكامل مع أنظمة أخرى. تُظهر الأمثلة كيفية ربط نماذج PDF، نقل البيانات بين الصيغ، وحفظ المستندات المحدثة، مما يتيح معالجة مستندات قابلة للتوسع ومتسقة عبر تطبيقات متنوعة.
---

## استيراد بيانات النموذج من ملف XML

توضح المثال التالي كيفية استيراد بيانات النموذج من ملف XML إلى نموذج PDF موجود باستخدام Aspose.PDF للـ Python. من خلال ربط نموذج PDF، تحميل بيانات XML، وحفظ الملف المحدث، يمكنك ملء الحقول التفاعلية بسرعة دون الحاجة إلى تحرير كل صفحة يدويًا. هذه الطريقة مثالية لأتمتة تعبئة النماذج بالجملة، معالجة مجموعات بيانات كبيرة، وضمان اتساق البيانات عبر مستندات متعددة.

استخدم الخطوات التالية:

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط نموذج PDF.
1. تحميل بيانات XML.
1. استيراد XML إلى PDF.
1. حفظ PDF المحدث.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## تصدير بيانات حقول النموذج من مستند PDF إلى ملف XML

تظهر مكتبة Python كيفية تصدير بيانات حقول النموذج من مستند PDF إلى ملف XML باستخدام Aspose.PDF للـ Python. من خلال ربط نموذج PDF وحفظ قيم حقوله بصيغة XML، يمكنك بسهولة تخزين البيانات، معالجتها، أو إعادة استخدامها في تطبيقات أو سير عمل أخرى. هذا النهج مثالي للنسخ الاحتياطي للبيانات، التحليل، والتكامل مع أنظمة خارجية.

استخدم الخطوات التالية:

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط نموذج PDF
1. تصدير بيانات النموذج
1. حفظ قيم الحقول إلى XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## استيراد بيانات حقول النموذج من FDF

طريقة 'import_data_from_fdf' تستورد بيانات حقول النموذج من ملف FDF (تنسيق بيانات النماذج) إلى نموذج PDF موجود وتحفظ المستند المحدث. هذا النهج مفيد لملء النماذج مسبقًا أو تحديثها برمجيًا دون تعديل بنية المستند.

استخدم الخطوات التالية:

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط ملف PDF الإدخال.
1. استيراد بيانات النموذج باستخدام import_fdf().
1. حفظ PDF مع البيانات المستوردة إلى مسار ملف الإخراج المحدد.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## تصدير بيانات حقول النموذج إلى FDF

يوضح هذا المثال كيفية تصدير بيانات النموذج من مستند PDF إلى ملف FDF (تنسيق بيانات النماذج) باستخدام Aspose.PDF للـ Python عبر .NET.

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط مستند PDF.
1. تصدير بيانات النموذج باستخدام export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## استيراد بيانات حقول النموذج من XFDF

يوضح هذا المثال تصدير بيانات حقول النموذج من مستند PDF إلى ملف XFDF (تنسيق بيانات النماذج XML) ثم حفظ PDF المحدث باستخدام Aspose.PDF للـ Python عبر .NET.

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط مستند PDF بالنموذج.
1. تصدير بيانات النموذج إلى ملف XFDF.
1. حفظ النموذج المعالج.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## تصدير بيانات حقول النموذج إلى XFDF

يقوم هذا الكود باستخراج بيانات حقول النموذج من مستند PDF وتصديرها إلى ملف XFDF (تنسيق بيانات النماذج XML) باستخدام Aspose.PDF للـ Python.

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط مستند PDF بالنموذج.
1. تصدير بيانات النموذج إلى ملف FDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## استيراد البيانات من PDF آخر

يوضح مقطع الشيفرة هذا كيفية نقل بيانات حقول النموذج من PDF المصدر إلى PDF الوجهة. يتم تصدير بيانات النموذج إلى تدفق XFDF من PDF المصدر ثم استيرادها إلى PDF الهدف باستخدام Aspose.PDF للـ Python عبر .NET.

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. ربط مستند PDF بالنموذج.
1. تصدير بيانات النموذج من ملف PDF المصدر.
1. استيراد بيانات النموذج إلى ملف PDF الوجهة.
1. حفظ ملف PDF الوجهة المحدث.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## استخراج حقول النموذج إلى JSON

هذه الطريقة تستخرج حقول النموذج من ملف الإدخال وتصدرها إلى ملف JSON.

1. إنشاء كائن Form باستخدام Aspose.PDF.
1. فتح ملف الإخراج في وضع الكتابة باستخدام FileIO().
1. تصدير حقول النموذج إلى ملف JSON باستخدام طريقة form.export_json().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## استخراج حقول النموذج إلى مستند JSON

1. إنشاء كائن Form من ملف الإدخال.
1. تهيئة قاموس فارغ لتخزين بيانات حقول النموذج.
1. التكرار عبر جميع حقول النموذج واستخراج قيمها.
1. تسلسل قاموس بيانات النموذج إلى سلسلة JSON مع مسافة بادئة قدرها 4 مسافات.
1. كتابة سلسلة JSON إلى ملف الإخراج بترميز utf-8.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

