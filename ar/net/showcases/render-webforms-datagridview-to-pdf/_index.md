---
title: تحويل WebForms DataGridView إلى PDF
linktitle: تحويل WebForms DataGridView إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/render-webforms-datagridview-to-pdf/
description: توضح هذه العينة كيفية استخدام مكتبة Aspose.PDF لتحويل WebForm إلى PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "تتيح هذه الميزة تحويل WebForms DataGridView إلى PDF بسلاسة باستخدام مكتبة Aspose.PDF for .NET. تبسط هذه الوظيفة عملية تصدير البيانات من خلال دمج عنصر تحكم تصدير GridView مخصص، مما يضمن تقديم PDF عالي الجودة مباشرة من تطبيقات الويب. مثالي للمطورين الذين يبحثون عن حلول فعالة لتوليد الوثائق",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "224",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2025-04-11",
    "description": "يمكن لمكتبة Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## كيفية تصدير WebForm إلى PDF باستخدام Aspose.PDF/Aspose.HTML

### مقدمة

بشكل عام، لتحويل WebForm إلى مستند PDF، يتم استخدام أدوات إضافية. توضح هذه العينة كيفية استخدام مكتبة Aspose.PDF لتحويل WebForm إلى PDF. تم تضمين عنصر تحكم Aspose Export GridView To Pdf أيضًا في هذه العينة لإظهار كيفية تحويل _عنصر تحكم GridView إلى مستند PDF_.

## كيفية تحويل WebForm إلى PDF

الفكرة الأصلية لتحويل WebForm إلى PDF هي إنشاء فئة مساعدة، والتي ترث من [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)، وتجاوز طريقة Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

هناك أداتان من Aspose يمكن استخدامهما لتحويل HTML إلى PDF:

- Aspose.PDF for .NET.
- عنصر تحكم Aspose Export GridView (المبني على Aspose.PDF).

## ملفات المصدر

يمكنك العثور على الكود الخاص بالمشروع بالكامل [هنا](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.Pdf.GridViewExport).

- _Default.aspx_ توضح التصدير إلى PDF باستخدام Aspose.PDF.
- _Report2.aspx_ توضح التصدير إلى PDF باستخدام عنصر تحكم Aspose Export GridView (المبني على Aspose.PDF).

## ملفات إضافية

`Helpers\PdfPage.cs` - تحتوي على فئة مساعدة، توضح كيفية استخدام واجهة برمجة تطبيقات Aspose.PDF.</em>

يحتوي مشروع Aspose.Pdf.GridViewExport على عنصر تحكم GridView موسع للعرض في `Report2.aspx`