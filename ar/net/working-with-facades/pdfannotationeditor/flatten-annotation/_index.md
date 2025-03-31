---
title: تسطيح التعليقات من PDF إلى XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/flatten-annotation/
description: يشرح هذا القسم كيفية تصدير التعليقات من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Flatten Annotation from PDF to XFDF",
    "alternativeHeadline": "Export PDF Annotations as Non-Editable XFDF Format",
    "abstract": "تتيح ميزة تسطيح التعليقات من PDF إلى XFDF للمستخدمين تصدير التعليقات من ملفات PDF إلى تنسيق XFDF مع الحفاظ على تمثيلها البصري. تضمن هذه الوظيفة أن تظل التعليقات مرئية في الوثيقة ولكن تصبح غير قابلة للتعديل، مما يوفر وسيلة لتطبيق الملاحظات أو التعليقات بشكل دائم للعرضين الذين قد لا يدعمون ميزات التعليق.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "191",
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
    "url": "/net/flatten-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/flatten-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة فحسب، بل يمكنه أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تعني عملية التسطيح أنه عندما تتم إزالة تعليق من وثيقة، يتم الاحتفاظ بتمثيله البصري سليمًا. يظل التعليق المسطح مرئيًا ولكنه لم يعد قابلًا للتعديل من قبل المستخدمين أو من قبل تطبيقك. يمكن استخدام ذلك، على سبيل المثال، لتطبيق التعليقات بشكل دائم على وثيقتك أو لجعل التعليقات مرئية للعرضين الذين لا يمكنهم عرض التعليقات. إذا لم يتم تحديد ذلك، سيحتفظ التصدير بجميع التعليقات كما هي.

عند اختيار هذا الخيار، ستُدرج تعليقاتك في ملف PDF المصدّر كتعليقات وفقًا لمعايير PDF.

تحقق من كيفية استخدام طريقة [flatteningAnnotations](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) في مقتطف الكود التالي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Create FlattenSettings
        var flattenSettings = new Aspose.Pdf.Forms.Form.FlattenSettings
        {
            ApplyRedactions = true,
            CallEvents = false,
            HideButtons = true,
            UpdateAppearances = true
        };
        annotationEditor.FlatteningAnnotations(flattenSettings);
        // Save PDF document
        annotationEditor.Save(dataDir + "FlattenAnnotation_out.pdf");
    }
}
```