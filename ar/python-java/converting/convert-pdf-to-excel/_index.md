---
title: تحويل PDF إلى Excel في بايثون
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: ar/python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: تحويل PDF إلى Excel باستخدام بايثون، تحويل PDF إلى XLS باستخدام بايثون، تحويل PDF إلى XLSX باستخدام بايثون، تصدير جدول من PDF إلى Excel في بايثون.
description: تتيح لك مكتبة Aspose.PDF for Python تحويل PDF إلى تنسيق Excel باستخدام بايثون. تشمل هذه التنسيقات XLS، XLSX، XML 2003 Spreadsheet، CSV، ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

توضح هذه المقالة كيفية **تحويل PDF إلى تنسيقات Excel باستخدام بايثون**. تغطي المقالة المواضيع التالية.

_تنسيق_: **XLS**
- [تحويل PDF إلى XLS باستخدام بايثون](#python-pdf-to-xls)
- [بايثون تحويل PDF إلى XLS](#python-pdf-to-xls)
- [بايثون كيفية تحويل ملف PDF إلى XLS](#python-pdf-to-xls)

_تنسيق_: **XLSX**
- [تحويل PDF إلى XLSX باستخدام بايثون](#python-pdf-to-xlsx)
- [بايثون تحويل PDF إلى XLSX](#python-pdf-to-xlsx)
- [بايثون كيفية تحويل ملف PDF إلى XLSX](#python-pdf-to-xlsx)

_تنسيق_: **Excel**
- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF to Excel XLS](#python-pdf-to-xls)
- [Python PDF to Excel XLSX](#python-pdf-to-xlsx)

_الصيغة_: **CSV**
- [Python PDF إلى CSV](#python-pdf-to-csv)
- [Python تحويل PDF إلى CSV](#python-pdf-to-csv)
- [Python كيفية تحويل ملف PDF إلى CSV](#python-pdf-to-csv)

_الصيغة_: **ODS**
- [Python PDF إلى ODS](#python-pdf-to-ods)
- [Python تحويل PDF إلى ODS](#python-pdf-to-ods)
- [Python كيفية تحويل ملف PDF إلى ODS](#python-pdf-to-ods)

## تحويل PDF إلى EXCEL عبر Python

يدعم **Aspose.PDF for Python عبر .NET** ميزة تحويل ملفات PDF إلى صيغ Excel وCSV.

Aspose.PDF for Python عبر Java هو مكون معالجة PDF، وقد قدمنا ميزة تقوم بتحويل ملف PDF إلى كتاب عمل Excel (ملفات XLSX). خلال هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى أوراق عمل Excel.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

يقدم لك Aspose.PDF تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك تجربة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF لتحويل PDF إلى Excel باستخدام تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

يعرض مقتطف الشفرة التالي عملية تحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF لـ Python عبر Java.

<a name="python-pdf-to-xls"><strong>الخطوات: تحويل PDF إلى XLS في Python</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) مع مستند PDF المصدر.
2. قم بإنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. احفظه بتنسيق **XLS** بتحديد امتداد **.xls** عن طريق استدعاء طريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) وتمريرها [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

# تهيئة الرخصة
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# التحويل من مصفوفة بايت
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# التحويل من ملف
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# التحويل من مصفوفة بايت
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# التحويل من ملف
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>خطوات: تحويل PDF إلى XLSX في بايثون</strong></a>

1. إنشاء نسخة من كائن [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) باستخدام مستند PDF المصدر.
2. إنشاء نسخة من [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. احفظه بصيغة **XLSX** محدداً **امتداد .xlsx** عن طريق استدعاء طريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) وتمريرها [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## تحويل PDF إلى XLS مع التحكم في العمود

عند تحويل PDF إلى صيغة XLS، يتم إضافة عمود فارغ إلى الملف الناتج كأول عمود.
 The in 'ExcelSaveOptions class' الخيار InsertBlankColumnAtFirst يُستخدم للتحكم في هذا العمود. القيمة الافتراضية له هي true.

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF يحتوي على الكثير من الصفحات إلى XLS، يتم تصدير كل صفحة إلى شيت مختلف في ملف Excel. هذا لأن الخاصية MinimizeTheNumberOfWorksheets تكون مضبوطة على false بشكل افتراضي. لضمان تصدير جميع الصفحات إلى شيت واحد في ملف Excel الناتج، قم بضبط الخاصية MinimizeTheNumberOfWorksheets إلى true.

<a name="python-pdf-to-excel-single"><strong>الخطوات: تحويل PDF إلى ورقة عمل XLS أو XLSX واحدة في Python</strong></a>
1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) مع مستند PDF المصدر.
2. قم بإنشاء مثيل من [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) مع **MinimizeTheNumberOfWorksheets = True**.
3. احفظه بتنسيق **XLS** أو **XLSX** بوجود ورقة عمل واحدة عن طريق استدعاء [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) وتمريره [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# احفظ الملف بتنسيق MS Excel
doc.save(documentOutName, save_option)

```

## التحويل إلى صيغ جداول بيانات أخرى

### التحويل إلى CSV

تحويل إلى تنسيق CSV يتم بنفس الطريقة المذكورة أعلاه. كل ما تحتاجه هو تعيين التنسيق المناسب.

<a name="python-pdf-to-csv"><strong>الخطوات: تحويل PDF إلى CSV في بايثون</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام مستند PDF المصدر.
2. قم بإنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) مع **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. احفظه بتنسيق **CSV** عن طريق استدعاء طريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) وتمريرها إلى [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).


```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### تحويل إلى ODS

<a name="python-pdf-to-ods"><strong>الخطوات: تحويل PDF إلى ODS في Python</strong></a>

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.
2. إنشاء مثيل لـ [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) مع **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. حفظه إلى تنسيق **ODS** عن طريق استدعاء [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) وتمريره إلى [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

يتم التحويل إلى تنسيق ODS بنفس الطريقة كما في جميع التنسيقات الأخرى.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## انظر أيضا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها أعلاه.

_تنسيق_: **Excel**
- [Python PDF إلى Excel كود](#python-pdf-to-xlsx)
- [Python PDF إلى Excel API](#python-pdf-to-xlsx)
- [Python PDF إلى Excel برمجيًا](#python-pdf-to-xlsx)
- [Python PDF إلى Excel مكتبة](#python-pdf-to-xlsx)
- [Python حفظ PDF كـ Excel](#python-pdf-to-xlsx)
- [Python إنشاء Excel من PDF](#python-pdf-to-xlsx)
- [Python إنشاء Excel من PDF](#python-pdf-to-xlsx)
- [Python PDF إلى Excel محول](#python-pdf-to-xlsx)

_تنسيق_: **XLS**
- [Python PDF إلى XLS كود](#python-pdf-to-xls)
- [Python PDF إلى XLS API](#python-pdf-to-xls)
- [Python PDF إلى XLS برمجيًا](#python-pdf-to-xls)
- [Python PDF إلى XLS مكتبة](#python-pdf-to-xls)
- [Python حفظ PDF كـ XLS](#python-pdf-to-xls)
- [Python إنشاء XLS من PDF](#python-pdf-to-xls)
- [Python إنشاء XLS من PDF](#python-pdf-to-xls)
- [Python PDF إلى XLS محول](#python-pdf-to-xls)

_تنسيق_: **XLSX**

- [Python PDF إلى XLSX كود](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_الصيغة_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_الصيغة_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)

- [Python Save PDF as ODS](#python-pdf-to-ods)
- [Python توليد ODS من PDF](#python-pdf-to-ods)
- [Python إنشاء ODS من PDF](#python-pdf-to-ods)
- [Python محول PDF إلى ODS](#python-pdf-to-ods)