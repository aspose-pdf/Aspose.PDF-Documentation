---
title: طباعة ملفات PDF في إطار .NET
linktitle: طباعة ملفات PDF في إطار .NET
type: docs
weight: 10
url: ar/net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: يمكنك طباعة ملفات PDF إلى الطابعة الافتراضية باستخدام إعدادات الطابعة والصفحة مع C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "طباعة ملفات PDF في إطار .NET",
    "alternativeHeadline": "كيفية طباعة ملفات PDF في إطار .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, pdf في إطار .NET",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك طباعة ملفات PDF إلى الطابعة الافتراضية باستخدام إعدادات الطابعة والصفحة مع C#."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **طباعة ملف PDF في C# - طباعة ملف PDF إلى الطابعة الافتراضية باستخدام إعدادات الطابعة والصفحة**

يصف هذا المقال كيفية طباعة ملف PDF إلى الطابعة الافتراضية باستخدام إعدادات الطابعة والصفحة في C#.

تسمح فئة [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) بطباعة ملف PDF إلى الطابعة الافتراضية. تحتاج إلى إنشاء كائن PdfViewer وفتح PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). لتحديد إعدادات الطباعة المختلفة، استخدم فئات `PageSettings` و `PrinterSettings`. أخيرًا، استدعي طريقة [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) لطباعة PDF إلى الطابعة الافتراضية. توضح الشفرة التالية كيفية طباعة PDF إلى الطابعة الافتراضية مع إعدادات الطابعة والصفحة.

```csharp
public static void SimplePrint()
{
    // إنشاء كائن PdfViewer
    PdfViewer viewer = new PdfViewer();

    // فتح ملف PDF الإدخال
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // تعيين السمات للطباعة
    viewer.AutoResize = true;         // طباعة الملف بحجم معدل
    viewer.AutoRotate = true;         // طباعة الملف بدوران معدل
    viewer.PrintPageDialog = false;   // عدم إنتاج حوار رقم الصفحة عند الطباعة

    // إنشاء كائنات لإعدادات الطابعة والصفحة و PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // تعيين اسم الطابعة
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // تعيين حجم الصفحة (إذا لزم الأمر)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // تعيين هوامش الصفحة (إذا لزم الأمر)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // طباعة المستند باستخدام إعدادات الطابعة والصفحة
    viewer.PrintDocumentWithSettings(pgs, ps);

    // إغلاق ملف PDF بعد الطباعة
    viewer.Close();
}
```
لعرض مربع حوار الطباعة، حاول استخدام الشفرة التالية:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // كود طباعة المستند يذهب هنا
    // طباعة المستند باستخدام إعدادات الطابعة والصفحة
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```

