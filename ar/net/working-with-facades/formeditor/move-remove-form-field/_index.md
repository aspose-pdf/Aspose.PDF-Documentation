---
title: نقل وإزالة حقل النموذج
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/move-remove-form-field/
description: استكشف كيفية إدارة حقول النموذج في ملفات PDF، بما في ذلك نقلها أو إزالتها، باستخدام Aspose.PDF for .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "تتيح ميزة نقل وإزالة حقل النموذج في فئة FormEditor للمستخدمين إعادة وضع وإزالة حقول النموذج بسلاسة ضمن مستندات PDF الموجودة. من خلال استخدام طرق MoveField و RemoveField، يمكن للمستخدمين تخصيص النماذج بكفاءة، مما يعزز قابلية الاستخدام وإدارة المستندات. تمكن هذه الوظيفة المستخدمين من تحسين تخطيطات PDF الخاصة بهم دون الحاجة إلى خبرة تقنية واسعة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نقل حقل النموذج إلى موقع جديد في ملف PDF موجود

إذا كنت ترغب في نقل حقل نموذج إلى موقع جديد، يمكنك استخدام [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). تحتاج فقط إلى تقديم اسم الحقل والموقع الجديد لهذا الحقل إلى طريقة [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). تحتاج أيضًا إلى حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). يوضح لك مقتطف الكود التالي كيفية نقل حقل نموذج إلى موقع جديد في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "MoveField.pdf");
        editor.MoveField("textbox1", 262.56f, 496.75f, 382.28f, 514.03f);
        // Save PDF document
        editor.Save(dataDir + "MoveField_out.pdf");
    }
}
```

## حذف حقل النموذج من ملف PDF موجود

لحذف حقل نموذج من ملف PDF موجود، يمكنك استخدام طريقة RemoveField من فئة FormEditor. تأخذ هذه الطريقة حجة واحدة فقط: اسم الحقل. تحتاج إلى إنشاء كائن من فئة FormEditor، واستدعاء طريقة [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) لإزالة حقل معين من PDF ثم استدعاء طريقة Save لحفظ ملف PDF المحدث. يوضح لك مقتطف الكود التالي كيفية حذف حقول النموذج من ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RemoveField("textbox1");
        // Save PDF document
        editor.Save(dataDir + "RemoveField_out.pdf");
    }
}
```

## إعادة تسمية حقول النموذج في PDF

يمكنك أيضًا إعادة تسمية حقل باستخدام طريقة [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenameFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RenameField("textbox1", "FirstName");
        // Save PDF document
        editor.Save(dataDir + "RenameField_out.pdf");
    }
}
```