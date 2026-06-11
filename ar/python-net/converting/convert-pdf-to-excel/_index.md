---
title: تحويل PDF إلى إكسيل في بايثون
linktitle: تحويل ملفات PDF إلى إكسيل
type: docs
weight: 20
url: /ar/python-net/convert-pdf-to-excel/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل PDF إلى Excel في Python، بما في ذلك XLS و XLSX و CSV و ODS وإخراج ورقة العمل الفردية ومعالجة الأعمدة باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل ملفات PDF إلى إكسيل وXLSX وCSV وODS في بايثون
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى تنسيقات جداول البيانات باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي مخرجات XLS و XLSX و XLSM و CSV و ODS، بالإضافة إلى خيارات للتحكم في الأعمدة الفارغة وتقليل عدد أوراق العمل التي تم إنشاؤها.
---

## تحويل PDF إلى إكسيل في بايثون

**Aspose.pdf لبيثون عبر .NET** يدعم تحويل ملفات PDF إلى Excel وتنسيقات جداول البيانات الأخرى من كود Python.

استخدم هذه الصفحة عندما تحتاج إلى تحويل PDF إلى XLS أو XLSX أو CSV أو ODS لاستخراج الجدول أو إعادة استخدام التقارير أو الفرز أو التصفية أو التحليل النهائي. أثناء تحويل PDF إلى Excel، يمكن عرض صفحات PDF الفردية كأوراق عمل Excel.

يقوم المثال الأول بتحويل ملف PDF إلى تنسيق XML لجدول البيانات 2003. تعرض الأقسام اللاحقة مخرجات XLSX و XLSM و CSV و ODS ومخرجات ورقة العمل الفردية.

{{% alert color="success" %}}
** حاول تحويل PDF إلى Excel عبر الإنترنت**

يقدم لك Aspose.PDF التطبيق عبر الإنترنت [«PDF إلى XLSX»](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل ملف PDF إلى إكسيل باستخدام التطبيق](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

يعرض مقتطف الشفرة التالي عملية تحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF لـ Python عبر .NET.

الخطوات: تحويل ملف PDF إلى تنسيق Excel (جدول بيانات XML 2003)

1. قم بتحميل وثيقة PDF.
1. قم بإعداد خيارات حفظ Excel باستخدام [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

## تحويل PDF إلى XLSX في بايثون

الخطوات: تحويل ملف PDF إلى تنسيق XLSX (Excel 2007+)

1. قم بتحميل وثيقة PDF.
1. قم بإعداد خيارات حفظ Excel باستخدام [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

## تحويل PDF إلى XLSX باستخدام التحكم في العمود

عند تحويل PDF إلى تنسيق Excel، يمكن إضافة عمود فارغ كأول عمود في ملف الإخراج. استخدم `insert_blank_column_at_first` خيار من `ExcelSaveOptions` فئة للتحكم في هذا السلوك. قيمتها الافتراضية هي `true`.

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

يُظهر ملف Aspose.PDF لبيثون عبر .NET كيفية تحويل ملف PDF إلى ملف Excel (.xlsx)، مع تمكين خيار «minimize_the_number_of_workets».

الخطوات: تحويل PDF إلى ورقة عمل XLS أو XLSX الفردية في بايثون

1. قم بتحميل وثيقة PDF.
1. قم بإعداد خيارات حفظ Excel باستخدام [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. يعمل خيار «minimize_the_number_of_workets» على تقليل عدد أوراق Excel من خلال دمج صفحات PDF في عدد أقل من أوراق العمل (على سبيل المثال، ورقة عمل واحدة للمستند بأكمله إن أمكن).
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

## تحويل ملفات PDF إلى إكسيل 2007 بتقنية الماكرو (XLSM)

يوضح مثال Python هذا كيفية تحويل ملف PDF إلى ملف Excel بتنسيق XLSM (مصنف Excel الذي يدعم ماكرو).

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

## قم بالتحويل إلى تنسيقات جداول بيانات أخرى

### تحويل ملفات PDF إلى CSV

تقوم الدالة 'convert_pdf_to_excel_2007_csv' بنفس العملية السابقة، ولكن التنسيق الهدف هذه المرة هو CSV (القيم المفصولة بفواصل) بدلاً من XLSM.

الخطوات: تحويل PDF إلى CSV في بايثون

1. قم بإنشاء مثيل لـ [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن مع مستند PDF المصدر.
1. قم بإنشاء مثيل لـ [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **خيارات الحفظ في إكسل.excelformat.csv**
1. احفظه بتنسيق**CSV** عن طريق الاتصال [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* الطريقة وتمريرها [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### تحويل ملفات PDF إلى ODS

الخطوات: تحويل PDF إلى ODS في بايثون

1. قم بإنشاء مثيل لـ [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن مع مستند PDF المصدر.
1. قم بإنشاء مثيل لـ [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **خيارات الحفظ في إكسل.excelformat.ods**
1. احفظه بتنسيق**ODS** عن طريق الاتصال [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الطريقة وتمريرها [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

يتم التحويل إلى تنسيق ODS بنفس الطريقة مثل جميع التنسيقات الأخرى.

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

- [تحويل ملفات PDF إلى وورد](/pdf/ar/python-net/convert-pdf-to-word/) إذا كانت أولويتك هي تدفق النص القابل للتحرير بدلاً من بنية جدول البيانات.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) عندما تحتاج إلى مخرجات ملائمة للمتصفح.
- [تحويل PDF إلى تنسيقات أخرى](/pdf/ar/python-net/convert-pdf-to-other-files/) لعمليات سير عمل EPUB وMarkdown والنص وXPS وعمليات سير عمل التصدير ذات الصلة.
