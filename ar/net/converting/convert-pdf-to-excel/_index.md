---
title: تحويل PDF إلى Excel في .NET
linktitle: تحويل PDF إلى Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: مكتبة Aspose.PDF for .NET تتيح لك تحويل PDF إلى تنسيق Excel باستخدام C#. تشمل هذه التنسيقات XLS و XLSX و XML 2003 Spreadsheet و CSV و ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "اكتشف القدرة القوية لمكتبة Aspose.PDF for .NET لتحويل مستندات PDF بسهولة إلى تنسيقات Excel متنوعة، بما في ذلك XLS و XLSX و CSV و ODS، باستخدام C#. لا تتيح هذه الميزة فقط تحويل صفحات PDF الفردية إلى أوراق عمل Excel منفصلة، بل تقدم أيضًا خيارات للأوراق المدمجة، مما يوفر مرونة للمستخدمين لإدارة بيانات PDF بكفاءة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1780",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لمكتبة Aspose.PDF أداء المهام البسيطة والسلسة، ولكنها أيضًا قادرة على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى تنسيقات Excel باستخدام C#**. تغطي المواضيع التالية.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

_التنسيق_: **XLS**

- [C# PDF إلى XLS](#csharp-pdf-to-xls)
- [C# تحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [C# كيفية تحويل ملف PDF إلى XLS](#csharp-pdf-to-xls)

_التنسيق_: **XLSX**

- [C# PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [C# تحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [C# كيفية تحويل ملف PDF إلى XLSX](#csharp-pdf-to-xlsx)

_التنسيق_: **Excel**

- [C# PDF إلى Excel](#csharp-pdf-to-xlsx)
- [C# PDF إلى Excel XLS](#csharp-pdf-to-xls)
- [C# PDF إلى Excel XLSX](#csharp-pdf-to-xlsx)

_التنسيق_: **ورقة عمل Excel واحدة**

- [C# تحويل PDF إلى XLS مع ورقة عمل واحدة](#csharp-pdf-to-excel-single)
- [C# تحويل PDF إلى XLSX مع ورقة عمل واحدة](#csharp-pdf-to-excel-single)

_التنسيق_: **تنسيق XML Spreadsheet 2003**

- [C# PDF إلى XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# تحويل PDF إلى XML Excel Spreadsheet](#csharp-pdf-to-excel-xml-2003)

_التنسيق_: **CSV**

- [C# PDF إلى CSV](#csharp-pdf-to-csv)
- [C# تحويل PDF إلى CSV](#csharp-pdf-to-csv)
- [C# كيفية تحويل ملف PDF إلى CSV](#csharp-pdf-to-csv)

_التنسيق_: **ODS**

- [C# PDF إلى ODS](#csharp-pdf-to-ods)
- [C# تحويل PDF إلى ODS](#csharp-pdf-to-ods)
- [C# كيفية تحويل ملف PDF إلى ODS](#csharp-pdf-to-ods)

## تحويلات C# PDF إلى Excel

**Aspose.PDF for .NET** تدعم ميزة تحويل ملفات PDF إلى تنسيقات Excel 2007 و CSV و SpeadsheetML.

Aspose.PDF for .NET هي مكون لمعالجة PDF، وقد قدمنا ميزة تقوم بتحويل ملف PDF إلى مصنف Excel (ملفات XLSX). خلال هذا التحويل، يتم تحويل الصفحات الفردية من ملف PDF إلى أوراق عمل Excel.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

تقدم لك Aspose.PDF for .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى Excel مع تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

لتحويل ملفات PDF إلى تنسيق <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>، تحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions). يتم تمرير كائن من فئة ExcelSaveOptions كوسيط ثانٍ إلى مُنشئ Document.Save(..).

تظهر مقتطفات الشيفرة التالية العملية لتحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls"><strong>الخطوات: تحويل PDF إلى XLS في C#</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions**.
3. حفظه بتنسيق **XLS** مع تحديد **.xls extension** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx"><strong>الخطوات: تحويل PDF إلى XLSX في C#</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions**.
3. حفظه بتنسيق **XLSX** مع تحديد **.xlsx extension** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## تحويل PDF إلى XLS مع عمود تحكم

عند تحويل PDF إلى تنسيق XLS، يتم إضافة عمود فارغ إلى ملف الإخراج كأول عمود. يتم استخدام خيار InsertBlankColumnAtFirst في فئة ExcelSaveOptions للتحكم في هذا العمود. القيمة الافتراضية هي `false`، مما يعني أنه لن يتم إدراج أعمدة فارغة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF يحتوي على العديد من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel. وذلك لأن خاصية MinimizeTheNumberOfWorksheets تم تعيينها على false بشكل افتراضي. لضمان تصدير جميع الصفحات إلى ورقة واحدة فقط في ملف Excel الناتج، قم بتعيين خاصية MinimizeTheNumberOfWorksheets إلى true.

<a name="csharp-pdf-to-excel-single"><strong>الخطوات: تحويل PDF إلى XLS أو XLSX ورقة عمل واحدة في C#</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions** مع **MinimizeTheNumberOfWorksheets = true**.
3. حفظه بتنسيق **XLS** أو **XLSX** مع وجود ورقة عمل واحدة عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## التحويل إلى تنسيقات جداول بيانات أخرى

### التحويل إلى تنسيق XML Spreadsheet 2003

منذ الإصدار 20.8، تستخدم Aspose.PDF تنسيق ملف Microsoft Excel Open XML Spreadsheet 2007 كافتراضي لتخزين البيانات. لتحويل ملفات PDF إلى تنسيق XML Spreadsheet 2003، تحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) مع [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) كوسيط ثانٍ إلى طريقة [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

تظهر مقتطفات الشيفرة التالية العملية لتحويل ملف PDF إلى تنسيق XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>الخطوات: تحويل PDF إلى تنسيق Excel 2003 XML في C#</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions** مع **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**.
3. حفظه بتنسيق **XLS - Excel 2003 XML Format** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### التحويل إلى CSV

يتم التحويل إلى تنسيق CSV بنفس الطريقة المذكورة أعلاه. كل ما تحتاجه هو تعيين التنسيق المناسب.

<a name="csharp-pdf-to-csv"><strong>الخطوات: تحويل PDF إلى CSV في C#</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions** مع **Format = ExcelSaveOptions.ExcelFormat.CSV**.
3. حفظه بتنسيق **CSV** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### التحويل إلى ODS

<a name="csharp-pdf-to-ods"><strong>الخطوات: تحويل PDF إلى ODS في C#</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions** مع **Format = ExcelSaveOptions.ExcelFormat.ODS**.
3. حفظه بتنسيق **ODS** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

يتم التحويل إلى تنسيق ODS بنفس الطريقة كما هو الحال مع جميع التنسيقات الأخرى.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

## انظر أيضًا 

تغطي هذه المقالة أيضًا هذه المواضيع. الشيفرات هي نفسها كما هو مذكور أعلاه.

_التنسيق_: **Excel**
- [C# PDF إلى Excel Code](#csharp-pdf-to-xlsx)
- [C# PDF إلى Excel API](#csharp-pdf-to-xlsx)
- [C# PDF إلى Excel برمجيًا](#csharp-pdf-to-xlsx)
- [C# PDF إلى Excel Library](#csharp-pdf-to-xlsx)
- [C# حفظ PDF كـ Excel](#csharp-pdf-to-xlsx)
- [C# توليد Excel من PDF](#csharp-pdf-to-xlsx)
- [C# إنشاء Excel من PDF](#csharp-pdf-to-xlsx)
- [C# PDF إلى Excel Converter](#csharp-pdf-to-xlsx)

_التنسيق_: **XLS**
- [C# PDF إلى XLS Code](#csharp-pdf-to-xls)
- [C# PDF إلى XLS API](#csharp-pdf-to-xls)
- [C# PDF إلى XLS برمجيًا](#csharp-pdf-to-xls)
- [C# PDF إلى XLS Library](#csharp-pdf-to-xls)
- [C# حفظ PDF كـ XLS](#csharp-pdf-to-xls)
- [C# توليد XLS من PDF](#csharp-pdf-to-xls)
- [C# إنشاء XLS من PDF](#csharp-pdf-to-xls)
- [C# PDF إلى XLS Converter](#csharp-pdf-to-xls)

_التنسيق_: **XLSX**
- [C# PDF إلى XLSX Code](#csharp-pdf-to-xlsx)
- [C# PDF إلى XLSX API](#csharp-pdf-to-xlsx)
- [C# PDF إلى XLSX برمجيًا](#csharp-pdf-to-xlsx)
- [C# PDF إلى XLSX Library](#csharp-pdf-to-xlsx)
- [C# حفظ PDF كـ XLSX](#csharp-pdf-to-xlsx)
- [C# توليد XLSX من PDF](#csharp-pdf-to-xlsx)
- [C# إنشاء XLSX من PDF](#csharp-pdf-to-xlsx)
- [C# PDF إلى XLSX Converter](#csharp-pdf-to-xlsx)

_التنسيق_: **CSV**
- [C# PDF إلى CSV Code](#csharp-pdf-to-csv)
- [C# PDF إلى CSV API](#csharp-pdf-to-csv)
- [C# PDF إلى CSV برمجيًا](#csharp-pdf-to-csv)
- [C# PDF إلى CSV Library](#csharp-pdf-to-csv)
- [C# حفظ PDF كـ CSV](#csharp-pdf-to-csv)
- [C# توليد CSV من PDF](#csharp-pdf-to-csv)
- [C# إنشاء CSV من PDF](#csharp-pdf-to-csv)
- [C# PDF إلى CSV Converter](#csharp-pdf-to-csv)

_التنسيق_: **ODS**
- [C# PDF إلى ODS Code](#csharp-pdf-to-ods)
- [C# PDF إلى ODS API](#csharp-pdf-to-ods)
- [C# PDF إلى ODS برمجيًا](#csharp-pdf-to-ods)
- [C# PDF إلى ODS Library](#csharp-pdf-to-ods)
- [C# حفظ PDF كـ ODS](#csharp-pdf-to-ods)
- [C# توليد ODS من PDF](#csharp-pdf-to-ods)
- [C# إنشاء ODS من PDF](#csharp-pdf-to-ods)
- [C# PDF إلى ODS Converter](#csharp-pdf-to-ods)