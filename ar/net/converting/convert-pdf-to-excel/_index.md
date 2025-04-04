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
    "abstract": "اكتشف القدرة القوية لمكتبة Aspose.PDF for .NET لتحويل مستندات PDF بسهولة إلى تنسيقات Excel المختلفة، بما في ذلك XLS و XLSX و CSV و ODS، باستخدام C#. هذه الميزة لا تسمح فقط بتحويل صفحات PDF الفردية إلى أوراق عمل Excel منفصلة ولكنها تقدم أيضًا خيارات للأوراق المدمجة، مما يوفر مرونة للمستخدمين لإدارة بيانات PDF الخاصة بهم بكفاءة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1411",
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
    "dateModified": "2025-04-04",
    "description": "يمكن لمكتبة Aspose.PDF أداء المهام البسيطة والسلسة ولكنها أيضًا قادرة على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى تنسيقات Excel باستخدام C#**. تغطي المواضيع التالية.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

- [تحويل PDF إلى XLS](#csharp-pdf-to-xls)
- [تحويل PDF إلى XLSX](#csharp-pdf-to-xlsx)
- [تحويل PDF إلى Excel](#csharp-pdf-to-xlsx)
- [تحويل PDF إلى XLS مع ورقة عمل واحدة](#csharp-pdf-to-excel-single)
- [تحويل PDF إلى XLSX مع ورقة عمل واحدة](#csharp-pdf-to-excel-single)
- [تحويل PDF إلى XML Excel](#csharp-pdf-to-excel-xml-2003)
- [تحويل PDF إلى CSV](#csharp-pdf-to-csv)
- [تحويل PDF إلى ODS](#csharp-pdf-to-ods)
- [تحويل PDF إلى XLSM](#csharp-pdf-to-xlsm)

## تحويل PDF إلى Excel باستخدام C#

**Aspose.PDF for .NET** تدعم ميزة تحويل ملفات PDF إلى تنسيقات Excel 2007 و CSV و SpeadsheetML.

Aspose.PDF for .NET هو مكون لمعالجة PDF، وقد قدمنا ميزة تقوم بتحويل ملف PDF إلى مصنف Excel (ملفات XLSX). خلال هذا التحويل، يتم تحويل الصفحات الفردية من ملف PDF إلى أوراق عمل Excel.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF for .NET تقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![Aspose.PDF تحويل PDF إلى Excel مع تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

لتحويل ملفات PDF إلى تنسيق <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>، تحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/excelsaveoptions). يتم تمرير كائن من فئة ExcelSaveOptions كوسيط ثانٍ إلى مُنشئ Document.Save(..).

تظهر مقتطفات الشيفرة التالية العملية لتحويل ملف PDF إلى تنسيق XLS أو XLSX باستخدام Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>تحويل PDF إلى XLS</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions**.
3. حفظه بتنسيق **XLS** مع تحديد **.xls extension** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>تحويل PDF إلى XLSX</strong></a>

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

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>تحويل PDF إلى XLS أو XLSX ورقة عمل واحدة</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions** مع **MinimizeTheNumberOfWorksheets = true**.
3. حفظه بتنسيق **XLS** أو **XLSX** مع ورقة عمل واحدة عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

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

### تحويل إلى تنسيق XML Spreadsheet 2003

منذ الإصدار 20.8، تستخدم Aspose.PDF تنسيق ملف Microsoft Excel Open XML Spreadsheet 2007 كافتراضي لتخزين البيانات. لتحويل ملفات PDF إلى تنسيق XML Spreadsheet 2003، تحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/excelsaveoptions) مع [Format](https://reference.aspose.com/pdf/ar/net/aspose.pdf/excelsaveoptions/properties/format). يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/excelsaveoptions) كوسيط ثانٍ إلى طريقة [Document.Save(..)](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index).

تظهر مقتطفات الشيفرة التالية العملية لتحويل ملف PDF إلى تنسيق XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>تحويل PDF إلى تنسيق Excel 2003 XML</strong></a>

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

### تحويل إلى CSV

يتم التحويل إلى تنسيق CSV بنفس الطريقة المذكورة أعلاه. كل ما تحتاجه هو تعيين التنسيق المناسب.

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>تحويل PDF إلى CSV</strong></a>

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

### تحويل إلى ODS

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>تحويل PDF إلى ODS</strong></a>

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

### تحويل إلى XLSM

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>تحويل PDF إلى XLSM</strong></a>

1. إنشاء مثيل من كائن **Document** مع مستند PDF المصدر.
2. إنشاء مثيل من **ExcelSaveOptions** مع **Format = ExcelSaveOptions.ExcelFormat.XLSM**.
3. حفظه بتنسيق **XLSM** عن طريق استدعاء **Document.Save()** وتمرير **ExcelSaveOptions**.

يتم التحويل إلى تنسيق XLSM بنفس الطريقة كما هو الحال مع جميع التنسيقات الأخرى.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```