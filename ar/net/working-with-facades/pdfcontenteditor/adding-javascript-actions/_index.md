---
title: إضافة إجراءات جافا سكريبت PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/adding-javascript-actions/
description: اكتشف كيفية إضافة إجراءات جافا سكريبت، مثل نقرات الأزرار أو إرسال النماذج، إلى ملفات PDF في .NET باستخدام Aspose.PDF.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Javascript actions PDF",
    "alternativeHeadline": "Enhance PDF with Interactive JavaScript Actions",
    "abstract": "قم بتحسين PDF الخاص بك من خلال دمج إجراءات جافا سكريبت التفاعلية مع Aspose.PDF for .NET PdfContentEditor class. تتيح هذه الميزة للمستخدمين إنشاء روابط ديناميكية وتنفيذ إجراءات عناصر القائمة المحددة، مما يثري تجربة الوثيقة بعناصر تفاعلية مخصصة. قم بتبسيط سير العمل الخاص بك من خلال إضافة إجراءات قائمة على الأحداث تستجيب لتفاعلات المستخدم بسهولة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "216",
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
    "url": "/net/adding-javascript-actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-javascript-actions/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تقدم فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/PdfContentEditor) الموجودة تحت حزمة Aspose.Pdf.Facades المرونة لإضافة إجراءات جافا سكريبت إلى ملف PDF. يمكنك إنشاء رابط مع الإجراءات التسلسلية المقابلة لتنفيذ عنصر قائمة في عارض PDF. توفر هذه الفئة أيضًا ميزة إنشاء إجراءات إضافية لأحداث الوثيقة.

أولاً وقبل كل شيء، يتم رسم كائن في [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document)، في مثالنا [مستطيل](https://reference.aspose.com/pdf/ar/net/aspose.pdf.drawing/rectangle). ثم يتم تعيين الإجراء [createJavaScriptLink](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) إلى المستطيل. بعد ذلك يمكنك حفظ مستندك.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Create Javascript link
        var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

        var code = "app.alert('Welcome to Aspose!');";
        editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

        // Save PDF document
        editor.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    // Create Javascript link
    var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

    var code = "app.alert('Welcome to Aspose!');";
    editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

    // Save PDF document
    editor.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}