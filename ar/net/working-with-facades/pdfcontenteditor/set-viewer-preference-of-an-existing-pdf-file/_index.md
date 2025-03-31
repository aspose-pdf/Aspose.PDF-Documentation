---
title: تعيين تفضيلات عرض PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/set-viewer-preference-of-an-existing-pdf-file/
description: يوضح هذا القسم كيفية تعيين تفضيلات عرض ملف PDF موجود باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "قم بتحسين تجربة المستخدم لمستندات PDF الخاصة بك من خلال استخدام ميزة تعيين تفضيلات العرض. تتيح هذه الوظيفة للمطورين تخصيص أوضاع العرض، مثل توسيط النافذة، وإخفاء شريط القوائم، وتمكين وضع ملء الشاشة، باستخدام فئة PdfContentEditor. قم بتبسيط عرض المستندات وضمان عرض مثالي لجمهورك مع هذه الإعدادات المخصصة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "338",
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
    "url": "/net/set-viewer-preference-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-viewer-preference-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تعيين تفضيلات عرض ملف PDF موجود

[ViewerPreference](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/viewerpreference) تمثل أوضاع عرض ملفات PDF؛ على سبيل المثال، وضع نافذة المستند في وسط الشاشة، وإخفاء شريط قوائم تطبيق العرض، إلخ.

تتيح لك طريقة [ChangeViewerPreference](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) في فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) تغيير تفضيلات العرض. للقيام بذلك، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

بعد ذلك، يمكنك استدعاء طريقة [ChangeViewerPreference](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) لتعيين أي تفضيل. أخيرًا، يجب عليك حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index). يوضح لك مقتطف الكود التالي كيفية تغيير تفضيلات العرض في ملف PDF موجود.

على سبيل المثال، نحدد المعامل [CenterWindow](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) الذي نستخدمه لتوسيط النافذة، بعد إزالة شريط الأدوات العلوي باستخدام [HideMenubar](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) ومع [PageModeUseNone](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) لفتح وضع ملء الشاشة.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Change Viewer Preferences
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.CenterWindow);
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.HideMenubar);
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Change Viewer Preferences
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.CenterWindow);
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.HideMenubar);
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}