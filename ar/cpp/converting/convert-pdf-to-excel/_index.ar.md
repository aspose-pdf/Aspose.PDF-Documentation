---
title: تحويل PDF إلى Excel في C++
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: يسمح لك Aspose.PDF for C++ بتحويل PDF إلى تنسيق Excel باستخدام C++. أثناء ذلك، يتم تحويل الصفحات الفردية لملف PDF إلى أوراق عمل Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

توضح هذه المقالة كيفية **تحويل PDF إلى تنسيقات Excel باستخدام C++**. وهي تشمل الموضوعات التالية.

_تنسيق_: **XLS**
- [تحويل PDF إلى XLS في C++](#cpp-pdf-to-xls)
- [C++ تحويل PDF إلى XLS](#cpp-pdf-to-xls)
- [كيفية تحويل ملف PDF إلى XLS في C++](#cpp-pdf-to-xls)

_تنسيق_: **XLSX**
- [تحويل PDF إلى XLSX في C++](#cpp-pdf-to-xlsx)
- [C++ تحويل PDF إلى XLSX](#cpp-pdf-to-xlsx)
- [كيفية تحويل ملف PDF إلى XLSX في C++](#cpp-pdf-to-xlsx)

_تنسيق_: **تنسيق Microsoft Excel XLS**
- [تحويل PDF إلى Excel في C++](#cpp-pdf-to-excel-xls)
- [C++ تحويل PDF إلى Excel](#cpp-pdf-to-excel-xls)
- [كيفية تحويل ملف PDF إلى Excel في C++](#cpp-pdf-to-excel-xls)

_تنسيق_: **تنسيق Microsoft Excel XLSX**
```

- [C++ PDF to Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Convert PDF to Excel](#cpp-pdf-to-excel-xlsx)
- [C++ How to convert PDF file to Excel](#cpp-pdf-to-excel-xlsx)

المواضيع الأخرى التي يغطيها هذا المقال
- [انظر أيضًا](#see-also)

## تحويل C++ PDF إلى Excel

يدعم **Aspose.PDF for C++** ميزة تحويل ملفات PDF إلى تنسيقات Excel.

Aspose.PDF for C++ هو مكون لمعالجة ملفات PDF، وقد قمنا بتقديم ميزة تقوم بتحويل ملف PDF إلى دفتر عمل Excel (ملفات XLS). أثناء هذا التحويل، يتم تحويل الصفحات الفردية من ملف PDF إلى أوراق عمل Excel.

من أجل تحويل ملفات PDF إلى تنسيق <abbr title="Microsoft Excel Spreadsheet">XLS</abbr>، يحتوي Aspose.PDF على فئة تسمى ExcelSaveOptions. يتم تمرير كائن من فئة ExcelSaveOptions كحجة ثانية إلى منشئ Document.Save(..).

يوضح مقتطف الشيفرة التالي عملية تحويل ملف PDF إلى تنسيق XLS باستخدام Aspose.PDF for C++.

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>الخطوات: تحويل PDF إلى XLS في C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>الخطوات: تحويل PDF إلى تنسيق Excel XLS في C++</strong></a>
```

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) باستخدام مستند PDF المصدر.
2. احفظه بتنسيق _XLS_ عن طريق استدعاء طريقة **Document->Save()**.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Save the output in XLS format
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحويل PDF إلى XLS مع التحكم في العمود

عند تحويل ملف PDF إلى تنسيق XLS، يتم إضافة عمود فارغ إلى الملف الناتج كأول عمود. يتم استخدام خيار InsertBlankColumnAtFirst في فئة ExcelSaveOptions للتحكم في هذا العمود. القيمة الافتراضية له هي true.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate ExcelSave Option object
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // The in ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // Save the output in XLS format
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF يحتوي على الكثير من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel. هذا لأن الخاصية MinimizeTheNumberOfWorksheets تكون مضبوطة على false بشكل افتراضي. لضمان تصدير جميع الصفحات إلى ورقة واحدة في ملف Excel الناتج، قم بتعيين الخاصية MinimizeTheNumberOfWorksheets إلى true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate ExcelSave Option object
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // Save the output in XLS format
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## التحويل إلى تنسيق XLSX

بشكل افتراضي، يستخدم Aspose.PDF صيغة XML Spreadsheet 2003 لتخزين البيانات. 
من أجل تحويل ملفات PDF إلى تنسيق XLSX، تحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) مع 'Format'. يتم تمرير كائن من الفئة [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) كمعامل ثانٍ إلى طريقة [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

يظهر مقتطف الشيفرة التالي عملية تحويل ملف PDF إلى تنسيق XLSX.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>الخطوات: تحويل PDF إلى XLSX في C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>الخطوات: تحويل PDF إلى تنسيق Excel XLSX في C++</strong></a>

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع وثيقة PDF المصدر.
2.
``` قم بإنشاء مثيل من [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. قم بتعيين التنسيق كـ _ExcelSaveOptions::ExcelFormat::XLSX_.
4. احفظه بتنسيق _XLSX_ عن طريق استدعاء طريقة **Document->Save()** وتمريره مثيل من _ExcelSaveOptions_.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // احفظ المخرجات بتنسيق XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**حاول تحويل PDF إلى Excel عبر الإنترنت**
Aspose.PDF for C++ يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى Excel باستخدام تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## انظر أيضًا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما هو موضح أعلاه.

_تنسيق_: **تنسيق Microsoft Excel XLS**
- [كود C++ لتحويل PDF إلى Excel XLS](#cpp-pdf-to-excel-xls)
- [تحويل PDF إلى Excel XLS برمجيًا باستخدام C++](#cpp-pdf-to-excel-xls)
- [مكتبة C++ لتحويل PDF إلى Excel XLS](#cpp-pdf-to-excel-xls)
- [حفظ PDF كـ Excel XLS باستخدام C++](#cpp-pdf-to-excel-xls)
- [إنشاء Excel XLS من PDF باستخدام C++](#cpp-pdf-to-excel-xls)
- [إنشاء Excel XLS من PDF باستخدام C++](#cpp-pdf-to-excel-xls)
- [محول C++ من PDF إلى Excel XLS](#cpp-pdf-to-excel-xls)

_تنسيق_: **تنسيق Microsoft Excel XLSX**
- [كود C++ لتحويل PDF إلى Excel XLSX](#cpp-pdf-to-excel-xlsx)

- [تحويل PDF إلى Excel XLSX برمجيًا باستخدام C++](#cpp-pdf-to-excel-xlsx)

- [مكتبة C++ لتحويل PDF إلى Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ حفظ PDF كـ Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ توليد Excel XLSX من PDF](#cpp-pdf-to-excel-xlsx)
- [C++ إنشاء Excel XLSX من PDF](#cpp-pdf-to-excel-xlsx)
- [محول C++ من PDF إلى Excel XLSX](#cpp-pdf-to-excel-xlsx)

_تنسيق_: **XLS**
- [شفرة C++ لتحويل PDF إلى XLS](#cpp-pdf-to-xls)
- [C++ تحويل PDF إلى XLS برمجيًا](#cpp-pdf-to-xls)
- [مكتبة C++ لتحويل PDF إلى XLS](#cpp-pdf-to-xls)
- [C++ حفظ PDF كـ XLS](#cpp-pdf-to-xls)
- [C++ توليد XLS من PDF](#cpp-pdf-to-xls)
- [C++ إنشاء XLS من PDF](#cpp-pdf-to-xls)
- [محول C++ من PDF إلى XLS](#cpp-pdf-to-xls)

_تنسيق_: **XLSX**
- [شفرة C++ لتحويل PDF إلى XLSX](#cpp-pdf-to-xlsx)
- [C++ تحويل PDF إلى XLSX برمجيًا](#cpp-pdf-to-xlsx)
- [مكتبة C++ لتحويل PDF إلى XLSX](#cpp-pdf-to-xlsx)
- [C++ حفظ PDF كـ XLSX](#cpp-pdf-to-xlsx)
- [C++ توليد XLSX من PDF](#cpp-pdf-to-xlsx)
- [C++ إنشاء XLSX من PDF](#cpp-pdf-to-xlsx)
- [محول C++ من PDF إلى XLSX](#cpp-pdf-to-xlsx)
```