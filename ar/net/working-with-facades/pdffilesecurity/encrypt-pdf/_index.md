---
title: تشفير ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/encrypt-pdf-file/
description: يشرح هذا الموضوع كيفية تشفير ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "اكتشف كيفية تعزيز أمان مستنداتك الحساسة مع ميزة تشفير PDF الجديدة باستخدام فئة PdfFileSecurity. تتيح لك هذه الوظيفة حماية ملفات PDF بكلمة مرور، مما يضمن أن المستخدمين المصرح لهم فقط يمكنهم الوصول إليها. استكشف أنواع التشفير المختلفة والخوارزميات، بما في ذلك AES مع طول مفتاح يصل إلى 256 بت، لحماية قوية أثناء مشاركة الملفات والأرشفة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF تنفيذ المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تشفير مستند PDF يحمي محتواه من الوصول غير المصرح به من الخارج، خاصة أثناء مشاركة الملفات أو الأرشفة.

يمكن تشفير مستندات PDF السرية وحمايتها بكلمة مرور. فقط المستخدمون الذين يعرفون كلمة المرور سيكونون قادرين على فك التشفير وفتح وعرض هذه المستندات.

دعونا نلقي نظرة على كيفية عمل تشفير PDF مع مكتبة Aspose.PDF.

## تشفير ملف PDF باستخدام أنواع وخوارزميات تشفير مختلفة

لتشفير ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesecurity) ثم استدعاء طريقة [EncryptFile](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). يمكنك تمرير كلمة مرور المستخدم، وكلمة مرور المالك، والامتيازات إلى طريقة [EncryptFile](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). تحتاج أيضًا إلى تمرير قيم KeySize و Algorithm إلى هذه الطريقة.

راجع قائمة ممكنة من مثل هذه [CryptoAlgorithm](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cryptoalgorithm):

|**اسم العضو**|**القيمة**|**الوصف**|
| :- | :- | :- |
|RC4x40|0|RC4 مع طول مفتاح 40.|
|RC4x128|1|RC4 مع طول مفتاح 128.|
|AESx128|2|AES مع طول مفتاح 128.|
|AESx256|3|AES مع طول مفتاح 256.|

تظهر لك الشيفرة البرمجية التالية كيفية تشفير ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```