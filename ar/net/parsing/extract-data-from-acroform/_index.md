---
title: استخراج البيانات من AcroForm باستخدام C#
linktitle: استخراج البيانات من AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/extract-data-from-acroform/
description: تجعل Aspose.PDF من السهل استخراج بيانات حقول النموذج من ملفات PDF. تعلم كيفية استخراج البيانات من AcroForms وحفظها في تنسيق JSON أو XML أو FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "اكتشف الوظيفة الجديدة في Aspose.PDF for .NET التي تبسط استخراج بيانات حقول النموذج من AcroForms في مستندات PDF. مع القدرة على تصدير البيانات إلى تنسيقات JSON و XML و FDF و XFDF، يمكن للمستخدمين إدارة بيانات النموذج بكفاءة مع الاستفادة من أمثلة التعليمات البرمجية المختصرة للتكامل السلس في التطبيقات",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج حقول النموذج من مستند PDF

بالإضافة إلى تمكينك من إنشاء حقول النموذج وملء حقول النموذج، تجعل Aspose.PDF for .NET من السهل استخراج بيانات حقول النموذج أو معلومات حول حقول النموذج من ملفات PDF.

في كود المثال أدناه، نوضح كيفية التكرار عبر كل صفحة في ملف PDF لاستخراج معلومات حول جميع AcroForm في PDF بالإضافة إلى قيم حقول النموذج. يفترض هذا الكود أن لديك معرفة مسبقة بأسماء حقول النموذج.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

إذا كنت تعرف أسماء حقول النموذج التي ترغب في استخراج القيم منها، يمكنك استخدام الفهرس في مجموعة Documents.Form لاسترجاع هذه البيانات بسرعة. انظر إلى أسفل هذه المقالة للحصول على كود مثال حول كيفية استخدام هذه الوظيفة.

## استرجاع قيمة حقل النموذج حسب العنوان

تسمح لك خاصية قيمة حقل النموذج بالحصول على قيمة حقل معين. للحصول على القيمة، احصل على حقل النموذج من مجموعة Form لكائن Document. يختار هذا المثال حقل TextBoxField ويسترجع قيمته باستخدام خاصية القيمة.

## استخراج حقول النموذج من مستند PDF إلى JSON

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## استخراج البيانات إلى XML من ملف PDF

تسمح لك فئة Form بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. لتصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. أخيرًا، يمكنك إغلاق كائن FileStream والتخلص من كائن Form. توضح مقتطفات الكود التالية كيفية تصدير البيانات إلى ملف XML.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## تصدير البيانات إلى FDF من ملف PDF

تسمح لك فئة Form بتصدير البيانات إلى ملف FDF من ملف PDF باستخدام طريقة ExportFdf. لتصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportFdf باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام طريقة Save من فئة Form. توضح مقتطفات الكود التالية كيفية تصدير البيانات إلى ملف FDF.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## تصدير البيانات إلى XFDF من ملف PDF

تسمح لك فئة Form بتصدير البيانات إلى ملف XFDF من ملف PDF باستخدام طريقة ExportXfdf. لتصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXfdf باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام طريقة Save من فئة Form. توضح مقتطفات الكود التالية كيفية تصدير البيانات إلى ملف XFDF.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```