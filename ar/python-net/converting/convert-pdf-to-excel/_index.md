---
title: تحويل PDF إلى Excel في بايثون
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: حوّل ملفات PDF إلى جداول Excel بسهولة باستخدام Aspose.PDF لبايثون عبر .NET. اتبع هذا الدليل للحصول على تحويلات دقيقة من PDF إلى XLSX
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى Excel في بايثون
Abstract: يوفر هذا المقال دليلًا شاملًا حول تحويل ملفات PDF إلى صيغ Excel مختلفة باستخدام بايثون، وتحديدا باستخدام مكتبة Aspose.PDF لبايثون عبر .NET. يوضح عمليات التحويل لصيغ XLS و XLSX و CSV و ODS. يشرح المستند الخطوات اللازمة لتحويل PDF إلى XLS و XLSX، مع التركيز على إنشاء كائنات Document و ExcelSaveOptions، واستخدام طريقة Document.Save() لتحديد صيغ الإخراج. يناقش المقال أيضًا ميزات مثل التحكم في إدراج الأعمدة الفارغة وتقليل عدد أوراق العمل أثناء التحويل. بالإضافة إلى ذلك، يقدم أمثلة على تحويل PDF إلى ورقة عمل Excel واحدة وصيغ أخرى مثل CSV و ODS، مؤكدًا على مرونة ووظائف Aspose.PDF. كما يذكر أداة عبر الإنترنت لتحويل PDF إلى XLSX، مما يتيح للمستخدمين استكشاف جودة التحويل. يختم المقال بقائمة من المواضيع ذات الصلة ومقاطع الكود لمزيد من المساعدة في فهم وتنفيذ هذه التحويلات برمجيًا.
---

## تحويل PDF إلى EXCEL عبر بايثون

**Aspose.PDF for Python via .NET** يدعم ميزة تحويل ملفات PDF إلى صيغ Excel و CSV.

Aspose.PDF لبايثون عبر .NET هو مكوّن لمعالجة PDF، وقد قدمنا ميزة تحويل ملفات PDF إلى دفتر عمل Excel (ملفات XLSX). أثناء هذا التحويل، تُحوَّل الصفحات الفردية لملف PDF إلى أوراق عمل في Excel.

{{% alert color="success" %}}
**جرّب تحويل PDF إلى Excel عبر الإنترنت**

يقدم لك Aspose.PDF تطبيقًا مجانيًا عبر الإنترنت ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك تجربة الوظيفة وجودتها.

[![تحويل Aspose.PDF من PDF إلى Excel مع التطبيق المجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

يوضح المقتطف البرمجي التالي عملية تحويل ملف PDF إلى صيغة XLS أو XLSX باستخدام Aspose.PDF لبايثون عبر .NET.

الخطوات: تحويل ملف PDF إلى صيغة Excel (XML Spreadsheet 2003)

1. تحميل مستند PDF.
1. إعداد خيارات حفظ Excel باستخدام [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. حفظ الملف المحوّل.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

الخطوات: تحويل ملف PDF إلى صيغة XLSX (Excel 2007+).

1. تحميل مستند PDF.
1. إعداد خيارات حفظ Excel باستخدام [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. حفظ الملف المحوّل.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى XLS مع التحكم في العمود

عند تحويل PDF إلى صيغة XLS، تتم إضافة عمود فارغ كعمود أول في الملف الناتج. يتم استخدام الخيار 'insert_blank_column_at_first' في فئة 'ExcelSaveOptions' للتحكم في هذا العمود. قيمته الافتراضية هي true.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى ورقة عمل Excel واحدة

يظهر Aspose.PDF لبايثون عبر .NET كيفية تحويل PDF إلى ملف Excel (.xlsx)، مع تمكين خيار 'minimize_the_number_of_worksheets'.

الخطوات: تحويل PDF إلى ورقة عمل XLS أو XLSX واحدة في بايثون

1. تحميل مستند PDF.
1. إعداد خيارات حفظ Excel باستخدام [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. خيار 'minimize_the_number_of_worksheets' يقلل عدد أوراق Excel عن طريق دمج صفحات PDF في عدد أقل من أوراق العمل (مثلاً، ورقة عمل واحدة للوثيقة بالكامل إذا كان ذلك ممكنًا).
1. حفظ الملف المحوّل.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل ملف PDF إلى ملف Excel بصيغة XLSM

يوضح هذا المثال في بايثون كيفية تحويل ملف PDF إلى ملف Excel بصيغة XLSM (دفتر عمل Excel مع تمكين الماكرو).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## التحويل إلى صيغ جداول أخرى

### التحويل إلى CSV

تقوم الدالة 'convert_pdf_to_excel_2007_csv' بنفس العملية السابقة، ولكن هذه المرة يكون الصيغة المستهدفة CSV (قيم مفصولة بفواصل) بدلاً من XLSM.

الخطوات: تحويل PDF إلى CSV في بايثون

1. إنشاء نسخة من كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام مستند PDF المصدر.
1. إنشاء نسخة من [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) باستخدام **ExcelSaveOptions.ExcelFormat.CSV**.
1. حفظه بصيغة **CSV** عن طريق استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* وتمرير إليها كائن [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### التحويل إلى ODS

الخطوات: تحويل PDF إلى ODS في بايثون

1. إنشاء نسخة من كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام مستند PDF المصدر.
1. إنشاء نسخة من [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) باستخدام **ExcelSaveOptions.ExcelFormat.ODS**
1. حفظه بصيغة **ODS** عن طريق استدعاء الدالة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وتمرير [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

التحويل إلى صيغة ODS يتم بنفس طريقة جميع الصيغ الأخرى.

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

