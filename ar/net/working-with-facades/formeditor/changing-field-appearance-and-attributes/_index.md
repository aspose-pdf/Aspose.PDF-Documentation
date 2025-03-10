---
title: مظهر الحقل والسمات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/changing-field-appearance-and-attributes/
description: يشرح هذا القسم كيفية تغيير مظهر الحقل والسمات باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "تتيح الميزة المقدمة في فئة FormEditor من مساحة أسماء Aspose.Pdf.Facades للمستخدمين تخصيص كل من مظهر وسمات حقول النموذج في ملفات PDF. من خلال استخدام طرق مثل SetFieldAppearance و SetFieldAttributes، يمكن للمطورين بسهولة تعديل العناصر المرئية والسلوكيات، بما في ذلك حدود الحقل، لتعزيز تفاعل المستخدم وكفاءة إدخال البيانات. توفر هذه الوظيفة مرونة أكبر في تصميم حقول النموذج المخصصة لتلبية احتياجات التطبيقات المحددة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تتيح لك فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) من [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) تغيير مظهر الحقل وسلوكه. في هذه المقالة، سنرى كيف يمكننا استخدام فئة FormEditor لتغيير مظهر الحقل، وسمات الحقل، وحدود الحقل أيضًا.

{{% /alert %}}

## تفاصيل التنفيذ

تستخدم طريقة [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) لتغيير مظهر حقل النموذج. تأخذ AnnotationFlag كمعامل. AnnotationFlag هو تعداد يحتوي على أعضاء مختلفين مثل Hidden أو NoRotate إلخ.

تستخدم طريقة [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) لتغيير سمة حقل النموذج. المعامل الممرر إلى هذه الطريقة هو تعداد PropertyFlag الذي يحتوي على أعضاء مثل ReadOnly أو Required إلخ.

توفر فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) أيضًا طريقة لتعيين حد الحقل. تخبر الحقل بعدد الأحرف التي يمكن ملؤها. يوضح لك مقتطف الكود أدناه كيفية استخدام كل هذه الطرق.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```