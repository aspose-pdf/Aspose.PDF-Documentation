---
title: إنشاء PDF متوافق مع PDF/3-A وإرفاق فاتورة ZUGFeRD في C#
linktitle: إرفاق ZUGFeRD إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/attach-zugferd/
description: تعلم كيفية إنشاء مستند PDF مع ZUGFeRD في Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "اكتشف الوظيفة الجديدة التي تتيح للمطورين إنشاء مستندات PDF متوافقة مع PDF/A-3B وإرفاق فواتير ZUGFeRD بسلاسة باستخدام C#. تسهل هذه الميزة عملية تضمين بيانات الفاتورة في ملفات PDF، مما يضمن الحفاظ على المستندات على المدى الطويل والامتثال لمعايير الفوترة الإلكترونية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إرفاق ZUGFeRD إلى PDF

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

نوصي باتباع الخطوات التالية لإرفاق ZUGFeRD إلى PDF:

* تعريف متغير مسار يشير إلى مجلد حيث توجد ملفات PDF المدخلة والمخرجة.
* إنشاء كائن مستند عن طريق تحميل ملف PDF موجود (مثل "ZUGFeRD-test.pdf") من المسار.
* إنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) من خلال توفير المسار ووصف لملف آخر يسمى "factur-x.xml"، والذي يحتوي على بيانات الفاتورة المتوافقة مع معيار ZUGFeRD.
* إضافة خصائص إلى كائن مواصفة الملف، مثل الوصف ونوع MIME وعلاقة AF. تشير علاقة AF إلى كيفية ارتباط الملف المضمن بمستند PDF. في هذه الحالة، تم تعيينها إلى "بديل"، مما يعني أن الملف المضمن هو تمثيل بديل لمحتوى PDF.
* إضافة كائن مواصفة الملف إلى مجموعة الملفات المضمنة في المستند. يجب تحديد اسم الملف وفقًا لمعيار ZUGFeRD، مثل "factur-x.xml".
* تحويل المستند إلى تنسيق PDF/A-3B، وهو مجموعة فرعية من PDF تضمن الحفاظ على المستندات الإلكترونية على المدى الطويل. يسمح PDF/A-3B بتضمين ملفات من أي تنسيق في مستندات PDF.
* حفظ المستند المحول كملف PDF جديد (مثل "ZUGFeRD-res.pdf").

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

تأخذ طريقة التحويل دفقًا، وتنسيق PDF، وإجراء خطأ التحويل كمعلمات. يمكن استخدام معلمة الدفق لحفظ سجل التحويل. تحدد معلمة إجراء خطأ التحويل ما يجب القيام به إذا حدثت أي أخطاء أثناء التحويل. في هذه الحالة، تم تعيينها إلى "حذف"، مما يعني أنه سيتم حذف أي عناصر غير متوافقة مع تنسيق PDF/A-3B من المستند.