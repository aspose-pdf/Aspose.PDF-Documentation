---
title: تعيين الامتيازات، تشفير وفك تشفير PDF
linktitle: تشفير وفك تشفير ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: تشفير ملف PDF باستخدام C# باستخدام أنواع وخوارزميات تشفير مختلفة. أيضًا، فك تشفير ملفات PDF باستخدام كلمة مرور المالك.
lastmod: "2024-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges, Encrypt and Decrypt PDF",
    "alternativeHeadline": "Set PDF Privileges and Secure with Encryption with C#",
    "abstract": "تتيح الميزة الجديدة للمستخدمين تشفير وفك تشفير ملفات PDF بكفاءة باستخدام C# مع مجموعة متنوعة من أنواع التشفير والخوارزميات. من خلال استخدام كلمات مرور المستخدم والمالك، توفر تحكمًا قويًا في الوصول إلى المستندات والأذونات، مما يضمن سرية وسلامة محتوى PDF مع تبسيط إدارة الأمان للمطورين",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1586",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "تشفير ملف PDF باستخدام C# باستخدام أنواع وخوارزميات تشفير مختلفة. أيضًا، فك تشفير ملفات PDF باستخدام كلمة مرور المالك."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## تعيين الامتيازات على ملف PDF موجود

لتعيين الامتيازات على ملف PDF، قم بإنشاء كائن من فئة [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) وحدد الحقوق التي تريد تطبيقها على المستند. بمجرد تعريف الامتيازات، قم بتمرير هذا الكائن كوسيط إلى طريقة [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) . يوضح مقتطف الشيفرة التالي كيفية تعيين امتيازات ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegesOnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate Document Privileges object
        // Apply restrictions on all privileges
        var documentPrivilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
        // Only allow screen reading
        documentPrivilege.AllowScreenReaders = true;
        // Encrypt the file with User and Owner password
        // Need to set the password, so that once the user views the file with user password
        // Only screen reading option is enabled
        document.Encrypt("user", "owner", documentPrivilege, Aspose.Pdf.CryptoAlgorithm.AESx128, false);
        // Save PDF document
        document.Save(dataDir + "SetPrivileges_out.pdf");
    }
}
```

## تشفير ملف PDF باستخدام أنواع وخوارزميات تشفير مختلفة

يمكنك استخدام طريقة [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) لتشفير ملف PDF. يمكنك تمرير كلمة مرور المستخدم، وكلمة مرور المالك، والأذونات إلى طريقة [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) . بالإضافة إلى ذلك، يمكنك تمرير أي قيمة من تعداد [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) . يوفر هذا التعداد مجموعات مختلفة من خوارزميات التشفير وأحجام المفاتيح. يمكنك تمرير القيمة التي تختارها. أخيرًا، احفظ ملف PDF المشفر باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .

>يرجى تحديد كلمات مرور مستخدم ومالك مختلفة أثناء تشفير ملف PDF.

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، فلن يفتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، والتحرير، والاستخراج، والتعليق، وما إلى ذلك. سيمنع Acrobat/Reader هذه الأشياء بناءً على إعدادات الأذونات. سيطلب Acrobat هذه الكلمة إذا كنت تريد تعيين/تغيير الأذونات.

يوضح مقتطف الشيفرة التالي كيفية تشفير ملفات PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Encrypt.pdf"))
    {
        // Encrypt PDF
        document.Encrypt("user", "owner", 0, Aspose.Pdf.CryptoAlgorithm.RC4x128);
        // Save PDF document
        document.Save(dataDir + "Encrypt_out.pdf");
    }
}
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

تبادل المستخدمون بشكل متزايد ملفات PDF مع التشفير لمنع الوصول غير المصرح به إلى المستندات، مثل الطباعة/النسخ/المشاركة / استخراج المعلومات حول محتويات ملف PDF. اليوم، يعد الخيار الأفضل لتشفير ملف PDF لأنه يحافظ على سرية وسلامة المحتوى.
في هذا الصدد، هناك حاجة للوصول إلى ملف PDF المشفر، حيث لا يمكن الحصول على هذا الوصول إلا من قبل مستخدم مخول. أيضًا، يبحث الناس عن حلول مختلفة لفك تشفير ملفات PDF عبر الإنترنت.

من الأفضل حل هذه المشكلة مرة واحدة باستخدام مكتبة Aspose.PDF.

لفك تشفير ملف PDF، تحتاج أولاً إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وفتح PDF باستخدام كلمة مرور المالك. بعد ذلك، تحتاج إلى استدعاء طريقة [Decrypt](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) . أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) . يوضح مقتطف الشيفرة التالي كيفية فك تشفير ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "Decrypt.pdf", "password"))
    {
        // Decrypt PDF
        document.Decrypt();
        // Save PDF document
        document.Save(dataDir + "Decrypt_out.pdf");
    }
}
```

## تغيير كلمة مرور ملف PDF

إذا كنت ترغب في تغيير كلمة مرور ملف PDF، تحتاج أولاً إلى فتح ملف PDF باستخدام كلمة مرور المالك مع كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) . بعد ذلك، تحتاج إلى استدعاء طريقة [ChangePasswords](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) . تحتاج إلى تمرير كلمة مرور المالك الحالية مع كلمة مرور المستخدم الجديدة وكلمة مرور المالك الجديدة إلى هذه الطريقة. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .

>- كلمة مرور المستخدم، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، فلن يفتح المستند.
>- كلمة مرور المالك، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، والتحرير، والاستخراج، والتعليق، وما إلى ذلك. سيمنع Acrobat/Reader هذه الأشياء بناءً على إعدادات الأذونات. سيطلب Acrobat هذه الكلمة إذا كنت تريد تعيين/تغيير الأذونات.

يوضح مقتطف الشيفرة التالي كيفية تغيير كلمة مرور ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "ChangePassword.pdf", "owner"))
    {
        // Change password
        document.ChangePasswords("owner", "newuser", "newowner");
        // Save PDF document
        document.Save(dataDir + "ChangePassword_out.pdf");
    }
}
```

## كيفية - تحديد ما إذا كان ملف PDF المصدر محمي بكلمة مرور

تقدم **Aspose.PDF for .NET** قدرات رائعة للتعامل مع مستندات PDF. عند استخدام فئة Document من مساحة أسماء Aspose.PDF لفتح مستند PDF محمي بكلمة مرور، نحتاج إلى تقديم معلومات كلمة المرور كوسيط إلى مُنشئ Document وفي حالة عدم تقديم هذه المعلومات، يتم إنشاء رسالة خطأ. في الواقع، عند محاولة فتح ملف PDF باستخدام كائن Document، يحاول المُنشئ قراءة محتويات ملف PDF وفي حالة عدم تقديم كلمة مرور صحيحة، يتم إنشاء رسالة خطأ (يحدث ذلك لمنع الوصول غير المصرح به إلى المستند).

عند التعامل مع ملفات PDF المشفرة، قد تواجه سيناريو حيث قد تكون مهتمًا بالكشف عما إذا كان PDF يحتوي على كلمة مرور مفتوحة و/أو كلمة مرور تحرير. أحيانًا تكون هناك مستندات لا تتطلب معلومات كلمة المرور أثناء فتحها، ولكنها تتطلب معلومات من أجل تحرير محتويات الملف. لذا، لتلبية المتطلبات المذكورة أعلاه، توفر فئة PdfFileInfo الموجودة تحت Aspose.PDF.Facades الخصائص التي يمكن أن تساعد في تحديد المعلومات المطلوبة.

### الحصول على معلومات حول أمان مستند PDF

تحتوي PdfFileInfo على ثلاث خصائص للحصول على معلومات حول أمان مستند PDF.

1. خاصية PasswordType تعيد قيمة تعداد PasswordType:
    - PasswordType.None - المستند غير محمي بكلمة مرور.
    - PasswordType.User - تم فتح المستند بكلمة مرور المستخدم (أو كلمة مرور فتح المستند).
    - PasswordType.Owner - تم فتح المستند بكلمة مرور المالك (أو الأذونات، التحرير).
    - PasswordType.Inaccessible - المستند محمي بكلمة مرور ولكن هناك حاجة إلى كلمة المرور لفتحه بينما تم تقديم كلمة مرور غير صحيحة (أو لا توجد كلمة مرور).
2. خاصية boolean HasOpenPassword - تُستخدم لتحديد ما إذا كان الملف المدخل يتطلب كلمة مرور عند فتحه.
3. خاصية boolean HasEditPassword - تُستخدم لتحديد ما إذا كان الملف المدخل يتطلب كلمة مرور لتحرير محتوياته.

### تحديد كلمة المرور الصحيحة من مصفوفة

أحيانًا تكون هناك حاجة لتحديد كلمة المرور الصحيحة من مصفوفة كلمات المرور وفتح المستند باستخدام كلمة المرور الصحيحة. يوضح مقتطف الشيفرة التالي الخطوات للتكرار عبر مصفوفة كلمات المرور ومحاولة فتح المستند باستخدام كلمة المرور الصحيحة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineCorrectPasswordFromArray()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var info = new  Aspose.Pdf.Facades.PdfFileInfo())
    {
        // Bind PDF document
        info.BindPdf(dataDir + "IsPasswordProtected.pdf");
        // Determine if the source PDF is encrypted
        Console.WriteLine("File is password protected " + info.IsEncrypted);
    
        String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
    
        for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
        {
            try
            {
                using (var document = new Aspose.Pdf.Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]))
                {
                    if (document.Pages.Count > 0)
                    {
                        Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
                    }
                }
            }
            catch (Aspose.Pdf.InvalidPasswordException)
            {
                Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>