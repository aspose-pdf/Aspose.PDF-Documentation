---
title: إزالة التوقيع من ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/remove-signature-from-pdf/
description: يشرح هذا القسم كيفية إزالة التوقيع من ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "تتيح هذه الوظيفة للمستخدمين إزالة التوقيعات الرقمية من ملفات PDF بكفاءة باستخدام فئة PdfFileSignature. توفر هذه الميزة المرونة، مما يمكّن من إزالة توقيعات معينة مع الاحتفاظ بخانات التوقيع للاستخدام المستقبلي، مما يعزز قدرات إدارة الوثائق.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "434",
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
    "url": "/net/remove-signature-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-signature-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة، بالإضافة إلى التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إزالة التوقيع الرقمي من ملف PDF

عندما يتم إضافة توقيع إلى ملفات PDF، من الممكن إزالته. يمكنك إزالة توقيع معين، أو جميع التوقيعات في ملف. أسرع طريقة لإزالة التوقيع تزيل أيضًا خانة التوقيع، ولكن من الممكن إزالة التوقيع فقط، مع الاحتفاظ بخانة التوقيع حتى يمكن توقيع الملف مرة أخرى.

تتيح لك طريقة RemoveSignature في فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) إزالة توقيع من ملف PDF. تأخذ هذه الطريقة اسم التوقيع كمدخل. إما أن تحدد اسم التوقيع مباشرة، لإزالة جميع التوقيعات، أو الحصول على أسماء التوقيعات باستخدام طريقة [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

تظهر الشيفرة التالية كيفية إزالة التوقيع الرقمي من ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignature()
{  
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdFileSignature.GetSignNames();
        // Remove all the signatures from the PDF file
        for (int index = 0; index < sigNames.Count; index++)
        {
            Console.WriteLine($"Removed {sigNames[index]}");
            pdFileSignature.RemoveSignature(sigNames[index]);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

### إزالة التوقيع ولكن الاحتفاظ بخانة التوقيع

كما هو موضح أعلاه، تتيح لك طريقة [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) في فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) إزالة خانات التوقيع من ملفات PDF. عند استخدام هذه الطريقة مع الإصدارات السابقة لـ 9.3.0، تتم إزالة كل من التوقيع وخانة التوقيع. يرغب بعض المطورين في إزالة التوقيع فقط والاحتفاظ بخانة التوقيع حتى يمكن استخدامها لإعادة توقيع الوثيقة. للاحتفاظ بخانة التوقيع وإزالة التوقيع فقط، يرجى استخدام الشيفرة التالية.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        pdFileSignature.RemoveSignature("Signature1", false);

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

تظهر المثال التالي كيفية إزالة جميع التوقيعات من الخانات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        var sigNames = pdFileSignature.GetSignatureNames();
        foreach (var sigName in sigNames)
        {
            pdFileSignature.RemoveSignature(sigName, false);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```