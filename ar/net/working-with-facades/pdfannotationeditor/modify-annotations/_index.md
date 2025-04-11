---
title: تعديل التعليقات في ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/modify-annotations/
description: يشرح هذا القسم كيفية تعديل التعليقات من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modify Annotations in your PDF",
    "alternativeHeadline": "Enhance Your PDF Annotations with New Modifications",
    "abstract": "تتيح ميزة تعديل التعليقات للمستخدمين تعديل السمات الرئيسية للتعليقات في ملفات PDF بسهولة باستخدام Aspose.PDF Facades. تشمل هذه الوظيفة تغيير الموضوع، المؤلف، اللون، والمزيد، بالإضافة إلى خيارات لحذف التعليقات حسب النوع، مما يسهل عملية إدارة تعليقات PDF. قم بتحسين سير عمل PDF الخاص بك من خلال الاستفادة من هذه القدرات القوية لتعديل التعليقات",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "290",
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
    "url": "/net/modify-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modify-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة، ولكنها أيضًا قادرة على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تعديل التعليق

تتيح لك طريقة [ModifyAnnotations](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) تغيير السمات الأساسية للتعليق مثل الموضوع، تاريخ التعديل، المؤلف، لون التعليق، وعلم الفتح. يمكنك أيضًا تعيين المؤلف مباشرة باستخدام طريقة ModifyAnnotations. توفر هذه الفئة أيضًا طريقتين مفرطتين لحذف التعليقات. الطريقة الأولى المسماة DeleteAnnotations تحذف جميع التعليقات من ملف PDF.

على سبيل المثال، في الكود التالي، اعتبر تغيير المؤلف في تعليقنا باستخدام [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotationsAuthor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Modify annotations author
        annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        // Save PDF document
        annotationEditor.Save(dataDir + "ModifyAnnotationsAuthor_out.pdf");
    }
}
```

تتيح لك الطريقة الثانية تعديل التعليقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        // Create PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Create a new object of type Annotation
            TextAnnotation newTextAnnotation = new TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
            newTextAnnotation.Title = "Updated title";
            newTextAnnotation.Subject = "Updated subject";
            newTextAnnotation.Contents = "Updated sample contents for the annotation";
            // Modify annotations in the PDF file
            annotationEditor.ModifyAnnotations(1, 1, newTextAnnotation);
            // Save PDF document
            annotationEditor.Save(dataDir + "ModifyAnnotations_out.pdf");
        }
    }
}
```