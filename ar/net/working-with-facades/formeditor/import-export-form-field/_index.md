---
title: استيراد وتصدير حقل النموذج
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/import-export-form-field/
description: ملء حقول النموذج باستخدام DataTable مع فئة FormEditor بواسطة Aspose.PDF for .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Form Field",
    "alternativeHeadline": "Streamline PDF Form Management with Import/Export Features",
    "abstract": "تتيح ميزة استيراد وتصدير حقل النموذج في Aspose.PDF for .NET للمستخدمين ملء وتعديل حقول نماذج PDF بسلاسة باستخدام مصادر بيانات متنوعة مثل FDF و XFDF و XML وحتى كائنات System.Data.DataTable. تمكّن هذه الواجهة البرمجية القوية من التعامل الآلي مع البيانات، مما يعزز كفاءة إدارة نماذج PDF ويسهل عملية إدخال البيانات",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "252",
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
    "url": "/net/import-export-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF تنفيذ المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

Aspose.PDF for .NET يوفر إمكانيات رائعة لإنشاء / تعديل حقول النموذج داخل مستند PDF. باستخدام هذه الواجهة البرمجية، يمكنك ملء حقول النموذج برمجيًا داخل ملف PDF، ملء حقول النموذج عن طريق [استيراد البيانات من FDF إلى ملف PDF](/pdf/ar/net/import-and-export-data/)، [استيراد البيانات من XFDF إلى ملف PDF](/pdf/ar/net/import-and-export-data/)، [استيراد البيانات من XML إلى ملف PDF](/pdf/ar/net/import-and-export-data/) أو حتى يمكنك استيراد البيانات من كائن [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Import data fdf
        using (var xfdfInputStream  = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(xfdfInputStream);
        }
                
        // Import data XML
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            form.ImportXml(xfdfInputStream);
        }
                
        // Import data XFDF
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xfdf", FileMode.Open))
        {
            form.ImportXfdf(xfdfInputStream);
        }
                
        // Save PDF document
        form.Save(dataDir + "ImportDataUpdated_out.pdf");
    }
}
```

## تصدير البيانات من FDF إلى ملف PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");
                
        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "data_out.fdf", FileMode.Create))
        {
            form.ExportXfdf(fdfOutputStream);
        }
                
        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "data_out.xml", FileMode.Create))
        {
            form.ExportXfdf(xmlOutputStream);
        }
            
        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "data_out.xfdf", FileMode.Create))
        {
            form.ExportXfdf(xfdfOutputStream);
        }              
    }
} 
```