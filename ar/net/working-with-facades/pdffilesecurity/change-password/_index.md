---
title: تغيير كلمة مرور ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/change-password/
description: استكشف كيفية تعديل كلمة مرور مستند PDF في .NET لتحسين أمان الملف باستخدام Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "قم بتحسين أمان PDF الخاص بك بسهولة عن طريق تغيير كلمة مروره باستخدام فئة PdfFileSecurity. تتيح هذه الوظيفة للمستخدمين تعديل كل من كلمات مرور المستخدم والمالك، مما يضمن حماية قوية ضد الوصول غير المصرح به أثناء إدارة الأذونات بشكل فعال. قم بتحسين إعدادات أمان مستندك بسهولة مع تنفيذ بسيط",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
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
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة بالإضافة إلى التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تغيير كلمة مرور ملف PDF

لتغيير كلمة مرور ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) ثم استدعاء طريقة [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). تحتاج إلى تمرير كلمة مرور المالك الحالية وكلمات المرور الجديدة للمستخدم والمالك إلى طريقة [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، فلن يفتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، والتحرير، والاستخراج، والتعليق، وما إلى ذلك. سيمنع Acrobat/Reader هذه الأمور بناءً على إعدادات الأذونات. سيتطلب Acrobat هذه الكلمة إذا كنت ترغب في تعيين/تغيير الأذونات.

{{% /alert %}}

تظهر الشيفرة البرمجية التالية كيفية تغيير كلمات مرور ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)    
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256);
                // Save PDF document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```