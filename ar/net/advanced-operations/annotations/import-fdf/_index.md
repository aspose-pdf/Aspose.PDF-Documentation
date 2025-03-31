---
title: استيراد تعليقات تنسيق FDF إلى PDF عبر C#
linktitle: استيراد تعليقات تنسيق FDF إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/import-fdf/
description: استخدم الطرق الموجودة Form.ImportFdf() أو PdfAnnotationEditor.ImportAnnotationsFromFdf() لاستيراد تعليقات تنسيق FDF إلى PDF مع Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "استيراد تعليقات تنسيق FDF إلى ملفات PDF بسلاسة باستخدام Aspose.PDF for .NET، مما يعزز قدرات إدارة PDF الخاصة بك. مع طرق Form.ImportFdf() و PdfAnnotationEditor.ImportAnnotationsFromFdf()، يمكنك دمج بيانات النموذج والتعليقات من ملفات FDF الخفيفة الوزن في مستندات PDF الخاصة بك، مما يسهل عمليات تقديم البيانات والتعليقات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

FDF (تنسيق بيانات النماذج) هو تنسيق ملف يخزن وينقل بيانات النموذج والتعليقات في مستندات PDF. إنه إصدار PDF خفيف الوزن يحتوي فقط على قيم حقول النموذج أو التعليقات، دون المحتوى الكامل لملف PDF الأصلي. غالبًا ما تُستخدم ملفات FDF عند تقديم بيانات النموذج إلى خادم، أو عند تبادل التعليقات دون الحاجة إلى إرسال ملف PDF بالكامل. يمكن استيرادها مرة أخرى إلى PDF لملء حقول النموذج أو تطبيق التعليقات.

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/) تحتوي على طريقة للعمل مع استيراد التعليقات من ملف FDF. توفر طريقة [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) الوظائف اللازمة لاستيراد التعليقات من مستند FDF إلى ملف PDF.

أيضًا، [فئة Form](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/) تتضمن طريقة [Form.ImportFdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/form/importfdf/) - تستورد محتوى الحقول من ملف FDF وتضعه في PDF جديد.

تظهر مقتطفات الشيفرة التالية كيفية استيراد تعليقات تنسيق FDF إلى PDF باستخدام طريقة Form.ImportFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

تظهر مقتطفات الشيفرة التالية كيفية استيراد تعليقات تنسيق FDF إلى PDF باستخدام طريقة PdfAnnotationEditor.ImportAnnotationsFromFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```