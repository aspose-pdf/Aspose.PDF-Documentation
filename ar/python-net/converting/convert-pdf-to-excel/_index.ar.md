---
title: تحويل PDF إلى Excel في بايثون
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: تحويل PDF إلى Excel باستخدام بايثون، تحويل PDF إلى XLS باستخدام بايثون، تحويل PDF إلى XLSX باستخدام بايثون، تصدير جدول من PDF إلى Excel في بايثون.
description: تتيح لك مكتبة Aspose.PDF for Python تحويل PDF إلى تنسيق Excel باستخدام بايثون. تشمل هذه التنسيقات XLS، XLSX، XML 2003 Spreadsheet، CSV، ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى تنسيقات Excel باستخدام بايثون**. يغطي المواضيع التالية.

_التنسيق_: **XLS**

- [بايثون PDF إلى XLS](#python-pdf-to-xls)
- [بايثون تحويل PDF إلى XLS](#python-pdf-to-xls)
- [بايثون كيفية تحويل ملف PDF إلى XLS](#python-pdf-to-xls)

_التنسيق_: **XLSX**

- [بايثون PDF إلى XLSX](#python-pdf-to-xlsx)
- [بايثون تحويل PDF إلى XLSX](#python-pdf-to-xlsx)
- [بايثون كيفية تحويل ملف PDF إلى XLSX](#python-pdf-to-xlsx)


_التنسيق_: **Excel**

- [Python PDF إلى Excel](#python-pdf-to-xlsx)
- [Python PDF إلى Excel XLS](#python-pdf-to-xls)
- [Python PDF إلى Excel XLSX](#python-pdf-to-xlsx)

_التنسيق_: **CSV**

- [Python PDF إلى CSV](#python-pdf-to-csv)
- [Python تحويل PDF إلى CSV](#python-pdf-to-csv)
- [Python كيفية تحويل ملف PDF إلى CSV](#python-pdf-to-csv)

_التنسيق_: **ODS**

- [Python PDF إلى ODS](#python-pdf-to-ods)
- [Python تحويل PDF إلى ODS](#python-pdf-to-ods)
- [Python كيفية تحويل ملف PDF إلى ODS](#python-pdf-to-ods)

## تحويل PDF إلى EXCEL عبر Python

يدعم **Aspose.PDF for Python عبر .NET** ميزة تحويل ملفات PDF إلى تنسيقات Excel وCSV.

Aspose.PDF for Python عبر .NET هو مكون لمعالجة ملفات PDF، وقد قدمنا ميزة تقوم بتحويل ملف PDF إلى دفتر عمل Excel (ملفات XLSX). خلال هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى أوراق عمل Excel.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

يقدم لك Aspose.PDF تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

يعرض المقتطف البرمجي التالي العملية لتحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF for Python عبر .NET.

<a name="python-pdf-to-xls"><strong>الخطوات: تحويل PDF إلى XLS في بايثون</strong></a>

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع وثيقة PDF المصدر.
2. إنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. حفظه بتنسيق **XLS** مع تحديد **امتداد .xls** من خلال استدعاء الطريقة [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وتمريره [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # حفظ الملف بتنسيق MS Excel
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>الخطوات: تحويل PDF إلى XLSX في بايثون</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.
2. قم بإنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. احفظه بصيغة **XLSX** مع تحديد **امتداد .xlsx** عن طريق استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وتمريرها إلى [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # احفظ الملف بصيغة MS Excel
    document.save(output_pdf, save_option)
```

## تحويل PDF إلى XLS مع التحكم في العمود

عند تحويل PDF إلى صيغة XLS، يتم إضافة عمود فارغ إلى ملف الإخراج كأول عمود.
 في الخيار 'InsertBlankColumnAtFirst' في فئة 'ExcelSaveOptions' يُستخدم للتحكم في هذا العمود. القيمة الافتراضية له هي true.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # احفظ الملف بتنسيق MS Excel
    document.save(output_pdf, save_option)
```

## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF يحتوي على الكثير من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel. وذلك لأن الخاصية MinimizeTheNumberOfWorksheets يتم تعيينها إلى false بشكل افتراضي. لضمان تصدير جميع الصفحات إلى ورقة واحدة في ملف Excel الناتج، قم بتعيين الخاصية MinimizeTheNumberOfWorksheets إلى true.

<a name="python-pdf-to-excel-single"><strong>الخطوات: تحويل PDF إلى XLS أو XLSX ورقة عمل واحدة في بايثون</strong></a>
1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.
2. قم بإنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **MinimizeTheNumberOfWorksheets = true**.
3. احفظه بتنسيق **XLS** أو **XLSX** بوجود ورقة عمل واحدة عن طريق استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وتمريرها إلى [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # احفظ الملف بتنسيق MS Excel
    document.save(output_pdf, save_option)

```


## التحويل إلى صيغ جداول أخرى

### التحويل إلى CSV

يتم التحويل إلى صيغة CSV بالطريقة نفسها كما هو موضح أعلاه. كل ما تحتاج إليه هو تعيين الصيغة المناسبة.

<a name="python-pdf-to-csv"><strong>الخطوات: تحويل PDF إلى CSV باستخدام Python</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام مستند PDF المصدر.
2. قم بإنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. احفظه بصيغة **CSV** عن طريق استدعاء [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* وتمريره [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # احفظ الملف
    document.save(output_pdf, save_option)
```


### تحويل إلى ODS

<a name="python-pdf-to-ods"><strong>الخطوات: تحويل PDF إلى ODS في بايثون</strong></a>

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.
2. إنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) مع **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. احفظه بتنسيق **ODS** عن طريق استدعاء [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وتمريره إلى [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

يتم التحويل إلى تنسيق ODS بالطريقة نفسها التي يتم بها جميع التنسيقات الأخرى.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # حفظ الملف
    document.save(output_pdf, save_option)
```


## انظر أيضا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_التنسيق_: **Excel**
- [كود تحويل PDF إلى Excel باستخدام بايثون](#python-pdf-to-xlsx)
- [API تحويل PDF إلى Excel باستخدام بايثون](#python-pdf-to-xlsx)
- [برمجة تحويل PDF إلى Excel باستخدام بايثون](#python-pdf-to-xlsx)
- [مكتبة تحويل PDF إلى Excel باستخدام بايثون](#python-pdf-to-xlsx)
- [حفظ PDF كملف Excel باستخدام بايثون](#python-pdf-to-xlsx)
- [توليد Excel من PDF باستخدام بايثون](#python-pdf-to-xlsx)
- [إنشاء Excel من PDF باستخدام بايثون](#python-pdf-to-xlsx)
- [محول PDF إلى Excel باستخدام بايثون](#python-pdf-to-xlsx)

_التنسيق_: **XLS**
- [كود تحويل PDF إلى XLS باستخدام بايثون](#python-pdf-to-xls)
- [API تحويل PDF إلى XLS باستخدام بايثون](#python-pdf-to-xls)
- [برمجة تحويل PDF إلى XLS باستخدام بايثون](#python-pdf-to-xls)
- [مكتبة تحويل PDF إلى XLS باستخدام بايثون](#python-pdf-to-xls)
- [حفظ PDF كملف XLS باستخدام بايثون](#python-pdf-to-xls)
- [توليد XLS من PDF باستخدام بايثون](#python-pdf-to-xls)
- [إنشاء XLS من PDF باستخدام بايثون](#python-pdf-to-xls)
- [محول PDF إلى XLS باستخدام بايثون](#python-pdf-to-xls)

_التنسيق_: **XLSX**

- [كود تحويل PDF إلى XLSX باستخدام بايثون](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_صيغة_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_صيغة_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)

- [Python Save PDF as ODS](#python-pdf-to-ods)
- [بايثون توليد ODS من PDF](#python-pdf-to-ods)
- [بايثون إنشاء ODS من PDF](#python-pdf-to-ods)
- [محول بايثون من PDF إلى ODS](#python-pdf-to-ods)