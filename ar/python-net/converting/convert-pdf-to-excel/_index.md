---
title: تحويل PDF إلى Excel في Python
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/python-net/convert-pdf-to-excel/
lastmod: "2026-06-05"
description: تعرّف على كيفية تحويل PDF إلى Excel في Python، بما في ذلك XLS و XLSX و CSV و ODS، وإخراج ورقة عمل واحدة، ومعالجة الأعمدة باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حوّل PDF إلى Excel و XLSX و CSV و ODS في Python
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى صيغ جداول البيانات باستخدام Aspose.PDF for Python via .NET. تغطي مخرجات XLS و XLSX و XLSM و CSV و ODS، بالإضافة إلى خيارات التحكم في الأعمدة الفارغة وتقليل عدد أوراق العمل المُنشأة.
---

## تحويل PDF إلى Excel في Python

**Aspose.PDF for Python via .NET** يدعم تحويل ملفات PDF إلى Excel وغيرها من صيغ جداول البيانات من خلال كود Python.

استخدم هذه الصفحة عندما تحتاج إلى تحويل ملف PDF إلى XLS أو XLSX أو CSV أو ODS لاستخراج الجداول، وإعادة استخدام التقارير، والترتيب، والتصفية، أو التحليل اللاحق. أثناء تحويل PDF إلى Excel، يمكن تحويل صفحات PDF الفردية إلى أوراق عمل Excel.

المثال الأول يحول ملف PDF إلى تنسيق XML لبرنامج Spreadsheet 2003. توضح الأقسام اللاحقة صيغ XLSX و XLSM و CSV و ODS وإخراج ورقة عمل واحدة.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF يقدم لك تطبيقًا عبر الإنترنت [PDF إلى XLSX](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Excel باستخدام التطبيق](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

تُظهر القطعة البرمجية التالية العملية لتحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF for Python via .NET.

الخطوات: تحويل ملف PDF إلى تنسيق Excel (XML Spreadsheet 2003)

1. قم بتحميل مستند PDF.
1. إعداد خيارات حفظ Excel باستخدام [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. احفظ الملف المحول.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى XLSX باستخدام بايثون

الخطوات: تحويل ملف PDF إلى تنسيق XLSX (Excel 2007+)

1. قم بتحميل مستند PDF.
1. إعداد خيارات حفظ Excel باستخدام [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. احفظ الملف المحول.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى XLSX مع التحكم في الأعمدة

عند تحويل ملف PDF إلى تنسيق Excel، يمكن إضافة عمود فارغ كأول عمود في ملف الإخراج. استخدم `insert_blank_column_at_first` خيار الـ `ExcelSaveOptions` فئة للتحكم في هذا السلوك. القيمة الافتراضية لها هي `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى ورقة عمل Excel واحدة

يوضح Aspose.PDF for Python via .NET كيفية تحويل ملف PDF إلى ملف Excel (.xlsx) مع تمكين خيار 'minimize_the_number_of_worksheets'.

الخطوات: تحويل PDF إلى XLS أو XLSX ورقة عمل واحدة في Python

1. قم بتحميل مستند PDF.
1. إعداد خيارات حفظ Excel باستخدام [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. الخيار 'minimize_the_number_of_worksheets' يقلل عدد أوراق Excel عن طريق دمج صفحات PDF في أوراق عمل أقل (مثلاً، ورقة عمل واحدة للوثيقة بأكملها إذا كان ذلك ممكنًا).
1. احفظ الملف المحول.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى Excel 2007 مع تمكين الماكرو (XLSM)

يعرض مثال بايثون هذا كيفية تحويل ملف PDF إلى ملف Excel بصيغة XLSM (مصنف Excel مع تمكين الماكرو).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل إلى صيغ جداول بيانات أخرى

### تحويل PDF إلى CSV

تقوم الدالة 'convert_pdf_to_excel_2007_csv' بأداء نفس العملية كما من قبل، ولكن هذه المرة يكون تنسيق الهدف هو CSV (القيم المفصولة بفواصل) بدلاً من XLSM.

الخطوات: تحويل PDF إلى CSV في Python

1. إنشاء نسخة من [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن مع مستند PDF المصدر.
1. إنشاء نسخة من [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **ExcelSaveOptions.ExcelFormat.CSV**
1. احفظه بتنسيق **CSV** عن طريق الاستدعاء [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* الطريقة وتمريرها [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى ODS

الخطوات: تحويل PDF إلى ODS في Python

1. إنشاء نسخة من [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن مع مستند PDF المصدر.
1. إنشاء نسخة من [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **ExcelSaveOptions.ExcelFormat.ODS**
1. احفظه إلى تنسيق **ODS** عن طريق الاستدعاء [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة وتمريرها [خيارات حفظ Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

يتم التحويل إلى تنسيق ODS بنفس الطريقة التي يتم بها التحويل إلى جميع الصيغ الأخرى.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## التحويلات ذات الصلة

- [تحويل PDF إلى Word](/pdf/ar/python-net/convert-pdf-to-word/) إذا كانت أولويتك تدفق النص القابل للتحرير بدلاً من بنية الجدول.
- [تحويل PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) عند الحاجة إلى مخرجات صديقة للمتصفح.
- [تحويل PDF إلى صيغ أخرى](/pdf/ar/python-net/convert-pdf-to-other-files/) لـ EPUB، Markdown، النص، XPS، وتدفقات العمل المتعلقة بالتصدير.
