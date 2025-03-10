---
title: نسخ الحقل الداخلي والخارجي
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/copy-inner-and-outer-field/
description: يشرح هذا القسم كيفية نسخ الحقل الداخلي والخارجي باستخدام Aspose.PDF Facades من خلال فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "تعمل وظيفة نسخ الحقل الداخلي والخارجي في Aspose.PDF for .NET على تعزيز تحرير النماذج من خلال السماح للمستخدمين بتكرار الحقول داخل نفس ملف PDF أو نقلها من ملف PDF خارجي. مع الطرق السهلة الاستخدام CopyInnerField و CopyOuterField المقدمة من فئة FormEditor، يمكن للمستخدمين إدارة حقول النموذج بكفاءة، مما يضمن الاتساق ويوفر الوقت في إعداد الوثائق.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) تتيح لك نسخ حقل في نفس الملف، في نفس الإحداثيات، على الصفحة المحددة. تتطلب هذه الطريقة اسم الحقل الذي تريد نسخه، واسم الحقل الجديد، ورقم الصفحة التي يحتاج الحقل ليتم نسخه فيها. توفر فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) هذه الطريقة. يوضح لك مقتطف الكود التالي كيفية نسخ الحقل في نفس الموقع في نفس الملف.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## نسخ الحقل الخارجي في ملف PDF موجود

تتيح لك طريقة [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) نسخ حقل نموذج من ملف PDF خارجي ثم إضافته إلى ملف PDF المدخل في نفس الموقع ورقم الصفحة المحدد. تتطلب هذه الطريقة ملف PDF الذي يحتاج الحقل ليتم نسخه منه، واسم الحقل، ورقم الصفحة التي يحتاج الحقل ليتم نسخه فيها. يتم توفير هذه الطريقة من قبل فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). يوضح لك مقتطف الكود التالي كيفية نسخ حقل من ملف PDF خارجي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```