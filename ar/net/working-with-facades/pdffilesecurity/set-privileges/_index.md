---
title: تعيين الامتيازات على PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/set-privileges/
description: اكتشف كيفية تعديل امتيازات المستخدم في ملفات PDF، مع تقييد بعض الإجراءات باستخدام Aspose.PDF في .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "تقديم القدرة الجديدة على تعيين الامتيازات على ملفات PDF الموجودة باستخدام فئة PdfFileSecurity، مما يسمح للمستخدمين بتحديد الأذونات للإجراءات مثل الطباعة والنسخ. بالإضافة إلى ذلك، يمكن للمستخدمين الآن بسهولة إزالة الحقوق الموسعة من مستندات PDF، مما يضمن مزيدًا من التحكم في تعديلات المستندات والأمان. تعمل هذه الوظيفة على تبسيط إدارة PDF مع تعزيز الامتثال للأمان",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "436",
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
    "url": "/net/set-privileges/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تعيين الامتيازات على ملف PDF موجود

لتعيين امتيازات ملف PDF، قم بإنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) واستدعاء طريقة SetPrivilege. يمكنك تحديد الامتيازات باستخدام كائن DocumentPrivilege ثم تمرير هذا الكائن إلى طريقة SetPrivilege. يوضح مقتطف الكود التالي كيفية تعيين امتيازات ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilege1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege
        fileSecurity.SetPrivilege(privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivileges_out.pdf");
    }
}
```

انظر إلى الطريقة التالية مع تحديد كلمة مرور:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegeWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege and passwords
        fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivilegesPassword_out.pdf");
    }
}
```

## إزالة ميزة الحقوق الموسعة من PDF

تدعم مستندات PDF ميزة الحقوق الموسعة لتمكين المستخدم النهائي من ملء البيانات في حقول النموذج باستخدام Adobe Acrobat Reader ثم حفظ نسخة من النموذج المملوء. ومع ذلك، فإنه يضمن عدم تعديل ملف PDF وإذا تم إجراء أي تعديل على هيكل PDF، فإن ميزة الحقوق الموسعة تضيع. عند عرض مثل هذا المستند، يتم عرض رسالة خطأ، تفيد بأنه تم إزالة الحقوق الموسعة لأن المستند تم تعديله. مؤخرًا، تلقينا طلبًا لإزالة الحقوق الموسعة من مستند PDF.

لإزالة الحقوق الموسعة من ملف PDF، تمت إضافة طريقة جديدة تسمى RemoveUsageRights() إلى فئة PdfFileSignature. تمت إضافة طريقة أخرى تسمى ContainsUsageRights() لتحديد ما إذا كان PDF المصدر يحتوي على حقوق موسعة.

{{% alert color="primary" %}}
بدءًا من Aspose.PDF for .NET 9.5.0، تم تحديث أسماء الطرق التالية. يرجى ملاحظة أن الطرق السابقة لا تزال في واجهة برمجة التطبيقات ولكن تم وضع علامة عليها على أنها قديمة وسيتم إزالتها. لذلك، يُوصى بتجربة استخدام الطرق المحدثة.

- تم إعادة تسمية طريقة IsContainSignature(.) إلى ContainsSignature(..).
- تم إعادة تسمية طريقة IsCoversWholeDocument(..) إلى CoversWholeDocument(..).
{{% /alert %}}

يوضح الكود التالي كيفية إزالة حقوق الاستخدام من المستند:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveExtendedRights()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
    
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        if (pdfSign.ContainsUsageRights())
        {
            pdfSign.RemoveUsageRights();
        }
        // Save PDF document
        pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
    }
}
```