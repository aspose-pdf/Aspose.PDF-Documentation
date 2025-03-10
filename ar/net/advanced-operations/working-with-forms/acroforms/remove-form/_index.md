---
title: حذف النماذج من PDF في C#
linktitle: حذف النماذج
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/remove-form/
description: إزالة النص بناءً على النوع الفرعي/النموذج باستخدام مكتبة Aspose.PDF for .NET. إزالة جميع النماذج من PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Forms from PDF in C#",
    "alternativeHeadline": "Effortless Removal of Forms from PDFs in C#",
    "abstract": "تقديم الوظيفة الجديدة لحذف النماذج من مستندات PDF في C# باستخدام مكتبة Aspose.PDF. تعمل هذه الميزة على تسهيل إزالة عناصر النموذج المحددة، مثل النموذج الفرعي، أو حتى جميع النماذج من ملف PDF، مما يعزز إدارة المستندات وقدرات التخصيص للمطورين. قم بتحسين عمليات تحرير PDF الخاصة بك مع مقتطفات كود دقيقة تضمن إزالة فعالة لقطع النص وحفظ المستند.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "delete forms, remove text, PDF C#, Aspose.PDF for .NET library, TextFragmentAbsorber, remove all forms",
    "wordcount": "378",
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
    "url": "/net/remove-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-form/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لمكتبة Aspose.PDF أداء المهام البسيطة والسلسة ولكنها أيضًا قادرة على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إزالة النص بناءً على النوع الفرعي/النموذج

يخلق مقتطف الكود التالي كائن مستند جديد باستخدام متغير إدخال يحتوي على مسار ملف PDF. يصل المثال إلى النماذج المعروضة في الصفحة 2 من المستند ويتحقق من النماذج ذات الخصائص المحددة. إذا تم العثور على نموذج من النوع "Typewriter" والنوع الفرعي "Form"، فإنه يستخدم TextFragmentAbsorber لزيارة وإزالة جميع قطع النص في هذا النموذج.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ClearTextInForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }	
}
```

## إزالة النماذج ذات "Typewriter" ونوع فرعي "Form" من PDF

يبحث هذا المقتطف البرمجي في النماذج الموجودة في الصفحة الأولى من مستند PDF عن نماذج ذات نية (IT) "Typewriter" ونوع فرعي (Subtype) "Form". إذا تم استيفاء كلا الشرطين، يتم حذف النموذج من PDF. ثم يتم حفظ المستند المعدل في ملف الإخراج المحدد.

توفر مكتبة Aspose.PDF طريقتين لإزالة مثل هذه النماذج من PDF:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

الطريقة 2:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

## إزالة جميع النماذج من PDF

يقوم هذا الكود بإزالة جميع عناصر النموذج من الصفحة الأولى من مستند PDF ثم يحفظ المستند المعدل في المسار المحدد للإخراج.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllForms(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```