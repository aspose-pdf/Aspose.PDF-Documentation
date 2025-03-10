---
title: استيراد وتصدير التعليقات التوضيحية إلى XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/import-export-annotations/
description: يشرح هذا القسم كيفية استيراد وتصدير التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Import and Export PDF Annotations with XFDF",
    "abstract": "Aspose.PDF for .NET يقدم وظيفة قوية لاستيراد وتصدير التعليقات التوضيحية إلى XFDF، مما يعزز قدرات معالجة PDF. تتيح هذه الميزة للمستخدمين نقل بيانات التعليقات التوضيحية بشكل انتقائي بتنسيق بيانات النماذج XML، مما يمكّن من التكامل السلس والأرشفة لتحسين إدارة الوثائق. مع طرق مخصصة لتحديد أنواع التعليقات التوضيحية، يمكن للمستخدمين إدارة تعليقاتهم التوضيحية في PDF بكفاءة ودقة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/import-export-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة، ولكنها أيضًا قادرة على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

XFDF تعني تنسيق بيانات النماذج XML. إنه تنسيق ملف قائم على XML. يُستخدم هذا التنسيق لتمثيل بيانات النماذج أو التعليقات التوضيحية الموجودة في نموذج PDF. يمكن استخدام XFDF لأغراض مختلفة، ولكن في حالتنا، يمكن استخدامه إما لإرسال أو استقبال بيانات النماذج أو التعليقات التوضيحية إلى أجهزة كمبيوتر أو خوادم أخرى، أو يمكن استخدامه لأرشفة بيانات النماذج أو التعليقات التوضيحية. في هذه المقالة، سنرى كيف أخذت Aspose.Pdf.Facades هذا المفهوم بعين الاعتبار وكيف يمكننا استيراد وتصدير بيانات التعليقات التوضيحية إلى ملف XFDF.

## استيراد وتصدير التعليقات التوضيحية إلى XFDF

[Aspose.PDF for .NET](/pdf/net/) هو مكون غني بالميزات عندما يتعلق الأمر بتحرير مستندات PDF. كما نعلم، فإن XFDF هو جانب مهم من جوانب معالجة نماذج PDF، وقد أخذت [مساحة الأسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/net/) هذا بعين الاعتبار بشكل جيد، وقدمت طرقًا لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF.

تحتوي فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF. توفر طريقة [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) الوظيفة لتصدير التعليقات التوضيحية من مستند PDF إلى ملف XFDF، بينما تتيح لك طريقة [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) استيراد التعليقات التوضيحية من ملف XFDF موجود. لاستيراد أو تصدير التعليقات التوضيحية، نحتاج إلى تحديد أنواع التعليقات التوضيحية. يمكننا تحديد هذه الأنواع في شكل تعداد ثم تمرير هذا التعداد كوسيط إلى أي من هذه الطرق. بهذه الطريقة، سيتم استيراد أو تصدير التعليقات التوضيحية من الأنواع المحددة فقط إلى ملف XFDF.

تظهر لك الشيفرة البرمجية التالية كيفية استيراد التعليقات التوضيحية إلى ملف XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Sources of PDF with annotations           
    var sources = new string[] { dataDir + "ImportAnnotations.pdf" };
            
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "input.pdf");
        annotationEditor.ImportAnnotations(sources);
        // Save PDF document
        annotationEditor.Save(dataDir + "ImportAnnotations_out.pdf");
    }
}
```

تصف الشيفرة البرمجية التالية كيفية استيراد/تصدير التعليقات التوضيحية إلى ملف XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
        }

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "exportannotations_out.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_out.pdf");
        }
    }
}
```

بهذه الطريقة، سيتم استيراد أو تصدير التعليقات التوضيحية من الأنواع المحددة فقط إلى ملف XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");

        // Export annotations
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            var annotationTypes = new[] {AnnotationType.FreeText, AnnotationType.Text};
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 1, 5, annotationTypes);
        }

        // Import annotations
        using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "annotations.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_XFDF02_out.pdf");
        }
    }
}
```