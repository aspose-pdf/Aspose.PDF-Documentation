---
title: إضافة إشارات مرجعية إلى ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/how-to-create-nested-bookmarks/
description: يشرح هذا القسم كيفية إنشاء إشارات مرجعية متداخلة باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Bookmarks to PDF file",
    "alternativeHeadline": "Create Nested Bookmarks in PDF Documents Easily",
    "abstract": "قم بتحسين مستندات PDF الخاصة بك مع ميزة الإشارات المرجعية المتداخلة الجديدة باستخدام فئة PdfContentEditor من Aspose.Pdf.Facades. تتيح لك هذه الوظيفة إنشاء إشارات مرجعية هرمية تنظم محتواك بشكل فعال، مما يمكّن المستخدمين من التنقل بسهولة عبر الفصول والصفحات المرتبطة داخل ملف PDF. قم بتبسيط تنقل المستندات وتحسين تجربة المستخدم مع هذا الحل المتقدم للإشارات المرجعية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "211",
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
    "url": "/net/how-to-create-nested-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-create-nested-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تتيح لك الإشارات المرجعية خيار تتبع/ربط صفحة معينة داخل مستند PDF. توفر فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) في [مساحة أسماء Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) ميزة تتيح لك إنشاء إشارة مرجعية خاصة بك بطريقة متطورة ولكن بديهية داخل ملف PDF موجود، في صفحة معينة أو جميع الصفحات.

## تفاصيل التنفيذ

بخلاف إنشاء الإشارات المرجعية البسيطة، أحيانًا يكون لديك متطلبات لإنشاء إشارة مرجعية على شكل فصول حيث تقوم بتعشيش الإشارات المرجعية الفردية داخل إشارات مرجعية الفصول بحيث عند النقر على علامة + لفصل ما، سترى الصفحات الداخلية عندما تتوسع الإشارات المرجعية، كما هو موضح في الصورة أدناه.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}