---
title: العمل مع عنصر القائمة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/working-with-list-item/
description: يشرح هذا القسم كيفية العمل مع عنصر القائمة باستخدام واجهات Aspose.PDF من خلال فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "قم بتحسين نماذج PDF الخاصة بك مع ميزة عنصر القائمة في Aspose.PDF for .NET. أضف أو احذف العناصر بسهولة من حقول ListBox باستخدام فئة FormEditor، مما يسمح بإدخال مستخدم ديناميكي وقابل للتخصيص. تعمل هذه الوظيفة على تبسيط إدارة النماذج، مما يجعل من الأسهل تخصيص المحتوى وفقًا لاحتياجاتك",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة عنصر قائمة في ملف PDF موجود

تسمح لك طريقة [AddListItem](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/addlistitem) بإضافة عنصر في حقل [ListBox](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/listboxfield). الحجة الأولى هي اسم الحقل والحجة الثانية هي عنصر الحقل. يمكنك إما تمرير عنصر حقل واحد أو يمكنك تمرير مصفوفة من السلاسل تحتوي على قائمة من العناصر. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor). يوضح لك مقتطف الكود التالي كيفية إضافة عناصر قائمة في ملف PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## حذف عنصر قائمة من ملف PDF موجود

تسمح لك طريقة [DelListItem](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor/methods/dellistitem) بحذف عنصر معين من [ListBox](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/listboxfield). المعامل الأول هو اسم الحقل بينما المعامل الثاني هو العنصر الذي تريد حذفه من القائمة. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formeditor). يوضح لك مقتطف الكود التالي كيفية حذف عنصر قائمة من ملف PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```