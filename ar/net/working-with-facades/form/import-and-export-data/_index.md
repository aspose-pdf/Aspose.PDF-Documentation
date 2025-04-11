---
title: استيراد وتصدير البيانات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/import-and-export-data/
description: يشرح هذا القسم كيفية استيراد وتصدير البيانات باستخدام واجهات Aspose.PDF باستخدام فئة النموذج.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "تتيح ميزة استيراد وتصدير البيانات في Aspose.PDF for .NET تكامل سلس لإدارة بيانات الوثائق من خلال تمكين المستخدمين من استيراد وتصدير بيانات نماذج PDF باستخدام تنسيقات XML وFDF وXFDF وJSON. تعزز هذه الوظيفة قدرات التعامل مع البيانات، مما يسهل أتمتة سير العمل والحفاظ على سجلات دقيقة مباشرة من مستندات PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

[Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class يسمح لك باستيراد البيانات من ملف XML إلى ملف PDF باستخدام [ImportXml](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.form/importxml/methods/1) method. لاستيراد البيانات من XML، تحتاج إلى إنشاء كائن من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class ثم استدعاء [ImportXml](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/importxml/index) method باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/save) method من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class. يوضح لك الكود التالي كيفية استيراد البيانات من ملف XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## تصدير البيانات إلى XML من ملف PDF

[Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class يسمح لك بتصدير البيانات إلى ملف XML من ملف PDF باستخدام [ExportXml](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/exportxml) method. لتصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class ثم استدعاء [ExportXml](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/exportxml) method باستخدام كائن FileStream. أخيرًا، يمكنك إغلاق كائن FileStream والتخلص من كائن Form. يوضح لك الكود التالي كيفية تصدير البيانات إلى ملف XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## استيراد البيانات من FDF إلى ملف PDF

[Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class يسمح لك باستيراد البيانات من ملف FDF إلى ملف PDF باستخدام [ImportFdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/importfdf) method. لاستيراد البيانات من FDF، تحتاج إلى إنشاء كائن من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class ثم استدعاء [ImportFdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/importfdf) method باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/save) method من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class. يوضح لك الكود التالي كيفية استيراد البيانات من ملف FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## تصدير البيانات إلى FDF من ملف PDF

[Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class يسمح لك بتصدير البيانات إلى ملف FDF من ملف PDF باستخدام [ExportFdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/exportfdf) method. لتصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class ثم استدعاء [ExportFdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/exportfdf) method باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/save) method من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class. يوضح لك الكود التالي كيفية تصدير البيانات إلى ملف FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## استيراد البيانات من XFDF إلى ملف PDF

[Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class يسمح لك باستيراد البيانات من ملف XFDF إلى ملف PDF باستخدام [ImportXfdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/importxfdf) method. لاستيراد البيانات من XFDF، تحتاج إلى إنشاء كائن من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class ثم استدعاء [ImportXfdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/importxfdf) method باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/save) method من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class. يوضح لك الكود التالي كيفية استيراد البيانات من ملف XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## تصدير البيانات إلى XFDF من ملف PDF

[Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class يسمح لك بتصدير البيانات إلى ملف XFDF من ملف PDF باستخدام [ExportXfdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/exportxfdf) method. لتصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class ثم استدعاء [ExportXfdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/methods/exportxfdf) method باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/save) method من [Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/form) class. يوضح لك الكود التالي كيفية تصدير البيانات إلى ملف XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## تصدير القيم من الحقول إلى ملف JSON

توفر Aspose.Pdf.Facades واجهة برمجة تطبيقات بديلة للعمل مع حقول النموذج. توضح هذه الشيفرة كيفية تصدير واستيراد قيم الحقول باستخدام هذه الواجهة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## استيراد القيم إلى الحقول من ملف JSON

توضح هذه الشيفرة كيفية استيراد القيم إلى حقول النموذج في مستند PDF من ملف JSON باستخدام واجهة برمجة تطبيقات Aspose.Pdf.Facades. يتم استخدام FileStream للتعامل مع ملف JSON.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```