---
title: تحويل PDF إلى Excel في .NET
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: تحويل PDF إلى Excel باستخدام c#, تحويل PDF إلى XLS باستخدام csharp, تحويل PDF إلى XLSX باستخدام csharp, تصدير الجدول من PDF إلى Excel في csharp.
description: مكتبة Aspose.PDF لـ .NET تتيح لك تحويل PDF إلى تنسيق Excel باستخدام C#. تشمل هذه التنسيقات XLS، XLSX، جدول بيانات XML 2003، CSV، ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## نظرة عامة

يشرح هذا المقال كيفية **تحويل PDF إلى تنسيقات Excel باستخدام C#**. يغطي الموضوعات التالية.

يعمل الكود التالي أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

_تنسيق_: **XLS**

- [C# PDF إلى XLS](#csharp-pdf-to-xls)
- [C# تحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [C# كيفية تحويل ملف PDF إلى XLS](#csharp-pdf-to-xls)

_تنسيق_: **XLSX**

- [C# PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [C# تحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [C# كيفية تحويل ملف PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [C# كيفية تحويل ملف PDF إلى XLSX](#csharp-pdf-to-xlsx)

_التنسيق_: **Excel**

- [C# تحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [C# تحويل PDF إلى Excel XLS](#csharp-pdf-to-xls)
- [C# تحويل PDF إلى Excel XLSX](#csharp-pdf-to-xlsx)

_التنسيق_: **ورقة عمل Excel واحدة**

- [C# تحويل PDF إلى XLS بورقة عمل واحدة](#csharp-pdf-to-excel-single)
- [C# تحويل PDF إلى XLSX بورقة عمل واحدة](#csharp-pdf-to-excel-single)

_التنسيق_: **تنسيق جدول XML 2003**

- [C# تحويل PDF إلى Excel XML](#csharp-pdf-to-excel-xml-2003)
- [C# تحويل PDF إلى جدول Excel XML](#csharp-pdf-to-excel-xml-2003)

_التنسيق_: **CSV**

- [C# تحويل PDF إلى CSV](#csharp-pdf-to-csv)
- [C# تحويل PDF إلى CSV](#csharp-pdf-to-csv)
- [C# كيفية تحويل ملف PDF إلى CSV](#csharp-pdf-to-csv)

_التنسيق_: **ODS**

- [C# تحويل PDF إلى ODS](#csharp-pdf-to-ods)
- [C# تحويل PDF إلى ODS](#csharp-pdf-to-ods)
- [C# كيفية تحويل ملف PDF إلى ODS](#csharp-pdf-to-ods)

## تحويلات C# PDF إلى Excel

**Aspose.PDF for .NET** يدعم ميزة تحويل ملفات PDF إلى تنسيقات Excel 2007، CSV و SpeadsheetML.
**Aspose.PDF لـ .NET** يدعم ميزة تحويل ملفات PDF إلى صيغ Excel 2007، CSV و SpeadsheetML.

Aspose.PDF لـ .NET هو مكون للتعامل مع ملفات PDF، لقد قدمنا ميزة تحول ملف PDF إلى مصنف Excel (ملفات XLSX). خلال هذه التحويلة، يتم تحويل الصفحات الفردية لملف PDF إلى أوراق عمل Excel.

{{% alert color="success" %}}
**جرب تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF لـ .NET يقدم لك تطبيق مجاني عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى Excel بتطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

لتحويل ملفات PDF إلى صيغة <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>، يمتلك Aspose.PDF فئة تُسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).
لتحويل ملفات PDF إلى تنسيق <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>، يحتوي Aspose.PDF على فئة تُدعى [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).

يوضح الجزء التالي من الكود عملية تحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF لـ .NET.

<a name="csharp-pdf-to-xls"><strong>خطوات: تحويل PDF إلى XLS في C#</strong></a>

1. إنشاء نموذج من كائن **Document** مع مستند PDF المصدر.
2. إنشاء نموذج من **ExcelSaveOptions**.
3. حفظه بتنسيق **XLS** مع تحديد **امتداد .xls** من خلال استدعاء طريقة **Document.Save()** وتمرير **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>خطوات: تحويل PDF إلى XLSX في C#</strong></a>

1. إنشاء نموذج من كائن **Document** مع مستند PDF المصدر.
2. إنشاء نموذج من **ExcelSaveOptions**.
3. حفظه بتنسيق **XLSX** مع تحديد **امتداد .xlsx** من خلال استدعاء طريقة **Document.Save()** وتمرير **ExcelSaveOptions**

```csharp
```
```csharp
// للحصول على أمثلة كاملة وملفات البيانات، الرجاء الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// تحميل مستند PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// إنشاء كائن خيارات حفظ Excel
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// حفظ الناتج بتنسيق XLS
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## تحويل PDF إلى XLS مع التحكم في العمود الأول

عند تحويل مستند PDF إلى تنسيق XLS، يتم إضافة عمود فارغ إلى الملف الناتج كأول عمود. يُستخدم خيار InsertBlankColumnAtFirst في فئة ExcelSaveOptions للتحكم في هذا العمود. القيمة الافتراضية هي `false`، مما يعني أن الأعمدة الفارغة لن تُدرج.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // للحصول على أمثلة كاملة وملفات البيانات، الرجاء الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // تحميل مستند PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // إنشاء كائن خيارات حفظ Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // حفظ الناتج بتنسيق XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF به العديد من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel. وذلك لأن خاصية MinimizeTheNumberOfWorksheets مضبوطة على false بشكل افتراضي. لضمان تصدير جميع الصفحات إلى ورقة واحدة في ملف Excel الناتج، قم بضبط خاصية MinimizeTheNumberOfWorksheets على true.

<a name="csharp-pdf-to-excel-single"><strong>الخطوات: تحويل PDF إلى ورقة XLS أو XLSX واحدة في C#</strong></a>

1. إنشاء نموذج من كائن **Document** بالمستند PDF المصدر.
2. إنشاء نموذج من **ExcelSaveOptions** مع **MinimizeTheNumberOfWorksheets = true**.
3. حفظه بصيغة **XLS** أو **XLSX** ذات ورقة عمل واحدة من خلال استدعاء طريقة **Document.Save()** وتمرير **ExcelSaveOptions** إليها.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // تحميل مستند PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // إنشاء نموذج من كائن ExcelSave Option
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // حفظ الناتج بصيغة XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## تحويل إلى صيغ جداول بيانات أخرى

### تحويل إلى صيغة جدول بيانات XML لعام 2003

منذ الإصدار 20.8، يستخدم Aspose.PDF صيغة ملف Microsoft Excel Open XML Spreadsheet 2007 كافتراضي لتخزين البيانات. لتحويل ملفات PDF إلى صيغة جدول بيانات XML لعام 2003، يحتوي Aspose.PDF على فئة تُسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) مع [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) كعنصر ثاني إلى طريقة [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

يوضح الكود التالي العملية لتحويل ملف PDF إلى صيغة XLS Excel XML لعام 2003.

<a name="csharp-pdf-to-excel-xml-2003"><strong>خطوات: تحويل PDF إلى صيغة Excel 2003 XML في C#</strong></a>

1. إنشاء نموذج من كائن **Document** مع مستند PDF المصدر.
2.
2.
3. احفظه بتنسيق **XLS - Excel 2003 XML Format** من خلال استدعاء طريقة **Document.Save()** وتمريرها **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // تحميل وثيقة PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // إنشاء كائن خيارات حفظ Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // حفظ الناتج بتنسيق XLS
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### التحويل إلى CSV

يتم التحويل إلى تنسيق CSV بنفس الطريقة كما هو موضح أعلاه. كل ما تحتاجه هو تحديد التنسيق المناسب.

<a name="csharp-pdf-to-csv"><strong>الخطوات: تحويل PDF إلى CSV في C#</strong></a>

1. إنشاء نموذج لكائن **Document** مع وثيقة PDF المصدر.
2.
2.
3. احفظه بتنسيق **CSV** من خلال استدعاء طريقة **Document.Save()** وتمريرها **ExcelSaveOptions**.


```csharp
 // إنشاء كائن ExcelSave Option
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### التحويل إلى ODS

<a name="csharp-pdf-to-ods"><strong>الخطوات: تحويل PDF إلى ODS في C#</strong></a>

1. إنشاء نموذج من كائن **Document** مع وثيقة PDF المصدر.
2. إنشاء نموذج من **ExcelSaveOptions** مع **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. احفظه بتنسيق **ODS** من خلال استدعاء طريقة **Document.Save()** وتمريرها **ExcelSaveOptions**.


التحويل إلى تنسيق ODS يتم بنفس الطريقة كما في جميع التنسيقات الأخرى.

```csharp
 // إنشاء كائن ExcelSave Option
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## انظر أيضا

هذا المقال يغطي أيضا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_Format_: **Excel**
- [كود C# لتحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [واجهة برمجة تطبيقات C# لتحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [واجهة برمجة تطبيقات C# لتحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [برمجيًا C# لتحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [مكتبة C# لتحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [حفظ PDF كـ Excel في C#](#csharp-pdf-to-xlsx)
- [توليد Excel من PDF في C#](#csharp-pdf-to-xlsx)
- [إنشاء Excel من PDF في C#](#csharp-pdf-to-xlsx)
- [محول PDF إلى Excel في C#](#csharp-pdf-to-xlsx)

_Format_: **XLS**
- [كود C# لتحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [واجهة برمجة تطبيقات C# لتحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [برمجيًا C# لتحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [مكتبة C# لتحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [حفظ PDF كـ XLS في C#](#csharp-pdf-to-xls)
- [توليد XLS من PDF في C#](#csharp-pdf-to-xls)
- [إنشاء XLS من PDF في C#](#csharp-pdf-to-xls)
- [محول PDF إلى XLS في C#](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [كود C# لتحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [واجهة برمجة تطبيقات C# لتحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [برمجيًا C# لتحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [مكتبة C# لتحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [حفظ PDF كـ XLSX في C#](#csharp-pdf-to-xlsx)
- [توليد XLSX من PDF في C#](#csharp-pdf-to-xlsx)
- [C# توليد XLSX من PDF](#csharp-pdf-to-xlsx)
- [C# إنشاء XLSX من PDF](#csharp-pdf-to-xlsx)
- [C# محول PDF إلى XLSX](#csharp-pdf-to-xlsx)

_Format_: **CSV**
- [C# كود PDF إلى CSV](#csharp-pdf-to-csv)
- [C# واجهة برمجة تطبيقات PDF إلى CSV](#csharp-pdf-to-csv)
- [C# PDF إلى CSV برمجيًا](#csharp-pdf-to-csv)
- [C# مكتبة PDF إلى CSV](#csharp-pdf-to-csv)
- [C# حفظ PDF كـ CSV](#csharp-pdf-to-csv)
- [C# توليد CSV من PDF](#csharp-pdf-to-csv)
- [C# إنشاء CSV من PDF](#csharp-pdf-to-csv)
- [C# محول PDF إلى CSV](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# كود PDF إلى ODS](#csharp-pdf-to-ods)
- [C# واجهة برمجة تطبيقات PDF إلى ODS](#csharp-pdf-to-ods)
- [C# PDF إلى ODS برمجيًا](#csharp-pdf-to-ods)
- [C# مكتبة PDF إلى ODS](#csharp-pdf-to-ods)
- [C# حفظ PDF كـ ODS](#csharp-pdf-to-ods)
- [C# توليد ODS من PDF](#csharp-pdf-to-ods)
- [C# إنشاء ODS من PDF](#csharp-pdf-to-ods)
- [C# محول PDF إلى ODS](#csharp-pdf-to-ods)
