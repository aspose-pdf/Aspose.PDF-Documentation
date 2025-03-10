---
title: إضافة توقيع رقمي أو توقيع PDF رقمي في C#
linktitle: توقيع PDF رقمي
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/digitally-sign-pdf-file/
description: توقيع مستندات PDF رقميًا باستخدام C# أو VB.NET. تحقق أو تحقق من صحة ملفات PDF الموقعة رقميًا باستخدام C# أو VB.NET.
lastmod: "2025-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add digital signature or digitally sign PDF in C#",
    "alternativeHeadline": "Working with digitally sign PDF",
    "abstract": "Aspose.PDF for .NET يقدم قدرات قوية لتوقيع مستندات PDF رقميًا باستخدام C# أو VB.NET، مما يعزز من سلامة وأمان المستندات. يمكن للمستخدمين تنفيذ أنواع توقيع مختلفة، بما في ذلك التوقيعات غير المنفصلة والمنفصلة مع دعم PKCS7 و ECDSA، مما يسمح بعمليات توقيع قابلة للتخصيص تتناسب مع معايير التشفير المحددة. هذه الميزة لا تتحقق فقط من صحة المستندات ولكنها تتيح أيضًا توقيع الوقت والشهادة، مما يضمن التعامل الموثوق مع المستندات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "digital signature, digitally sign PDF, C#, PDF signing, PKCS12 certificate, verify PDF signature, ECDSA signing, timestamp server, custom hash signing, Aspose.PDF for .NET",
    "wordcount": "2020",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2025-02-07",
    "description": "توقيع مستندات PDF رقميًا باستخدام C# أو VB.NET. تحقق أو تحقق من صحة ملفات PDF الموقعة رقميًا باستخدام C# أو VB.NET."
}
</script>

Aspose.PDF for .NET يدعم ميزة توقيع ملفات PDF رقميًا باستخدام فئة SignatureField. يمكنك أيضًا اعتماد ملف PDF مع شهادة PKCS12. شيء مشابه لـ [إضافة توقيعات وأمان في Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

عند توقيع مستند PDF باستخدام توقيع، فإنك تؤكد أساسًا محتوياته "كما هي". وبالتالي، فإن أي تغييرات أخرى تطرأ بعد ذلك تبطل التوقيع وبالتالي، ستعرف إذا تم تعديل المستند. بينما، اعتماد مستند أولاً يتيح لك تحديد التغييرات التي يمكن للمستخدم إجراؤها على المستند دون إبطال الاعتماد.

بعبارة أخرى، سيظل المستند يعتبر محتفظًا بسلامته ويمكن للمستلم أن يثق في المستند. لمزيد من التفاصيل، يرجى زيارة اعتماد وتوقيع PDF. بشكل عام، يمكن مقارنة اعتماد مستند بتوقيع كود تنفيذ .NET.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## ميزات توقيع Aspose.PDF for .NET

يمكننا استخدام الفئات والأساليب التالية لتوقيع PDF

- فئة [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature).
- تعداد [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions).
- خاصية [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) في فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature).

لإنشاء توقيع رقمي بناءً على شهادات PKCS12 (امتدادات الملفات .p12، pfx)، يجب عليك إنشاء مثيل من فئة `PdfFileSignature`، مع تمرير كائن المستند إليها.
بعد ذلك، يجب عليك تحديد طريقة التوقيع الرقمي المطلوبة عن طريق إنشاء كائن من إحدى الفئات:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_يمكنك تعيين خوارزمية التجزئة فقط لـ `PKCS7Detached`. بالنسبة لـ `PKCS1` و `PKCS7`، يتم دائمًا تعيين خوارزمية التجزئة إلى SHA-1._

بعد ذلك، تحتاج إلى استخدام كائن خوارزمية التوقيع المستلمة في طريقة `PdfFileSignature.Sign()` .
سيتم تعيين التوقيع الرقمي للمستند بعد حفظه.

## توقيع PDF بتوقيعات رقمية

المثال أدناه ينشئ توقيع PKCS7 غير منفصل مع خوارزمية تجزئة SHA-1.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345");
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

المثال أدناه ينشئ توقيعًا منفصلًا بتنسيق PKCS7Detached مع خوارزمية تجزئة SHA-256. تعتمد خوارزمية المفتاح على مفتاح الشهادة. يتم دعم DSA و RSA و ECDSA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object using the opened document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password, Aspose.Pdf.DigestHashAlgorithm.Sha256);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

يمكنك التحقق من التوقيعات باستخدام طريقة PdfFileSignature.VerifySignature() .
في السابق، كانت طريقة `GetSignNames()` تُستخدم للحصول على أسماء التوقيع. بدءًا من الإصدار 25.02، يجب استخدام طريقة `GetSignatureNames()`، التي تعيد قائمة بـ `SignatureName` .
تمنع `SignatureName` التصادمات عند التحقق من التوقيعات بنفس الأسماء.
يجب أيضًا استخدام الطرق التي تقبل نوع `SignatureName` بدلاً من اسم توقيع نصي.

_ملاحظات، طريقة __PdfFileSignature.VerifySigned()__ قديمة._

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {         
            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## إضافة طابع زمني إلى التوقيع الرقمي

### كيفية توقيع PDF رقميًا مع طابع زمني

Aspose.PDF for .NET يدعم توقيع PDF رقميًا مع خادم طابع زمني أو خدمة ويب.

لتحقيق هذا المتطلب، تمت إضافة فئة [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) إلى مساحة أسماء Aspose.PDF. يرجى إلقاء نظرة على مقتطف الكود التالي الذي يحصل على الطابع الزمني ويضيفه إلى مستند PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithTimeStampServer(string pfxFilePath, string password)
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);
            // Create TimestampSettings settings
            var timestampSettings = new Aspose.Pdf.TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password can be omitted
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Create any of the three signature types
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySignWithTimeStamp_out.pdf");
        }
    }
}
```

## توقيع PDF مع X509Certificate2 بتنسيق base64

هذا الكود يوقع PDF باستخدام شهادة خارجية، ربما يتفاعل مع خادم لاسترداد التجزئة الموقعة وإدراج التوقيع في مستند PDF.

خطوات توقيع PDF:

1. إنشاء مثيل من PdfFileSignature.
1. تحديد تجزئة التوقيع المخصص.
1. تحميل الشهادة.
1. توقيع البيانات.
1. ربط وتوقيع PDF.
1. حفظ PDF الموقع.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create a delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving a response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## توقيع PDF باستخدام وظيفة توقيع HASH

باستخدام وظيفة توقيع تجزئة مخصصة، يمكن لسلطة التوقيع تنفيذ معايير تشفير محددة أو سياسات أمان داخلية تتجاوز طرق التوقيع القياسية، مما يضمن سلامة المستند.
تساعد هذه الطريقة في التحقق من أن المستند لم يتم تعديله منذ تطبيق التوقيع وتوفر توقيعًا رقميًا ملزمًا قانونيًا مع دليل قابل للتحقق على هوية الموقع باستخدام شهادة PFX.

توضح مقتطفات الكود هذه توقيع مستند PDF رقميًا باستخدام شهادة PFX (PKCS#12) مع وظيفة توقيع تجزئة مخصصة في C#.

لنلقِ نظرة أقرب على عملية توقيع DPF:

1. تحديد مسارات الملفات ومعلومات الشهادة:

- inputPdf: المسار إلى مستند PDF المدخل الذي يحتاج إلى التوقيع.
- inputP12: المسار إلى ملف الشهادة .p12 (PFX) المستخدم للتوقيع.
- inputPfxPassword: كلمة المرور لشهادة PFX.
- outputPdf: المسار حيث سيتم حفظ PDF الموقع.

2. عملية التوقيع:

- يتم إنشاء كائن `PdfFileSignature` ويرتبط بـ PDF المدخل.
- يتم تهيئة كائن `PKCS7` باستخدام شهادة PFX وكلمتها السرية. يتم تعيين طريقة 'CustomSignHash' كوظيفة توقيع التجزئة المخصصة.
- يتم استدعاء طريقة `Sign`، مع تحديد رقم الصفحة (1 في هذه الحالة)، تفاصيل التوقيع (السبب، المحتوى، الموقع)، والموقع (مستطيل بإحداثيات (0، 0، 500، 500)) للتوقيع.
- ثم يتم حفظ PDF الموقع إلى المسار المحدد.

3. توقيع التجزئة المخصص:

- تقبل طريقة `CustomSignHash` مصفوفة بايت signableHash (التجزئة التي سيتم توقيعها).
- يتم تحميل نفس شهادة PFX واسترداد مفتاحها الخاص.
- يتم استخدام المفتاح الخاص لتوقيع التجزئة باستخدام `RSACryptoServiceProvider` وخوارزمية SHA-1.
- يتم إرجاع البيانات الموقعة (مصفوفة بايت) لتطبيقها على توقيع PDF.

يمكن تحديد خوارزمية التجزئة في مُنشئ PKCS7Detached. يمكن استدعاء خدمة طرف ثالث في مفوض CustomSignHash. يجب أن تتطابق خوارزمية التوقيع المستخدمة في CustomSignHash مع خوارزمية المفتاح في الشهادة المرسلة إلى PKCS7/PKCS7Detached.

المثال أدناه ينشئ توقيعًا غير منفصل باستخدام خوارزمية RSA وخوارزمية تجزئة SHA-1.
إذا كنت تستخدم PKCS7Detached بدلاً من PKCS7، يمكنك استخدام ECDCA وتعيين خوارزمية التجزئة المطلوبة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

لإنشاء توقيع، يلزم تقدير أولي لطول التوقيع الرقمي المستقبلي.
إذا كنت تستخدم SignHash لإنشاء توقيع رقمي، قد تجد أن المفوض يتم استدعاؤه مرتين خلال عملية حفظ المستند.
إذا لم تتمكن لأي سبب من تحمل استدعاءين، على سبيل المثال، إذا حدث طلب رمز PIN أثناء الاستدعاء، يمكنك استخدام خيار `AvoidEstimatingSignatureLength` لفئات PKCS1 و PKCS7 و PKCS7Detached و ExternalSignature.
تعيين هذا الخيار يتجنب خطوة تقدير طول التوقيع عن طريق تعيين قيمة ثابتة كطول متوقع - `DefaultSignatureLength`. القيمة الافتراضية لخاصية DefaultSignatureLength هي 3000 بايت.
يعمل خيار AvoidEstimatingSignatureLength فقط إذا تم تعيين مفوض SignHash في خاصية CustomSignHash.
إذا تجاوز طول التوقيع الناتج الطول المتوقع المحدد بواسطة خاصية DefaultSignatureLength، ستتلقى استثناء `SignatureLengthMismatchException` يشير إلى الطول الفعلي.
يمكنك ضبط قيمة معلمة DefaultSignatureLength حسب تقديرك.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Set an option to avoiding twice SignHash calling.
        pkcs7.AvoidEstimatingSignatureLength = true;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

## توقيع مستندات PDF باستخدام ECDSA

توقيع مستندات PDF باستخدام ECDSA (خوارزمية التوقيع الرقمي المنحني) يتضمن استخدام تشفير المنحنيات البيانية لإنشاء توقيعات رقمية. يوفر هذا أمانًا عاليًا وكفاءة، خاصة في البيئات المحمولة والمحدودة الموارد. تضمن هذه الطريقة أن مستندات PDF الخاصة بك موقعة رقميًا مع مزايا الأمان لتشفير المنحنيات البيانية.

يدعم Aspose.PDF إنشاء وتحقق التوقيع الرقمي القائم على ECDSA.
تدعم المنحنيات البيانية التالية لإنشاء وتحقق التوقيع الرقمي:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

الخوارزمية الافتراضية للتجزئة هي SHA2 مع طول يعتمد على حجم مفتاح ECDSA.
يمكنك تحديد خوارزمية التجزئة في مُنشئ `PKCS7Detached`.

يمكن توقيع توقيعات رقمية ECDSA مع خوارزميات التجزئة التالية: SHA-256، SHA-384، SHA3–512، SHA3–256، SHA3–384، SHA3–512.
يمكن التحقق من توقيعات رقمية ECDSA مع خوارزميات التجزئة التالية: SHA-256، SHA-384، SHA3–512، SHA3–256، SHA3–384، SHA3–512.

يمكنك التحقق من التوقيع والتحقق من خلال إنشاء شهادة PFX(output.pfx) في OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

أسماء المنحنيات المتاحة للتوقيع والتحقق في Aspose.PDF (يمكن الحصول على قائمة المنحنيات في OpenSSL باستخدام الأمر 'openssl ecparam -list_curves'): prime256v1، secp384r1، secp521r1، brainpoolP256r1، brainpoolP384r1، brainpoolP512r1.

لتوقيع مستند PDF باستخدام ECDSA، ستكون الخطوات العامة في C# كالتالي:

1. ستحتاج إلى شهادة ECDSA بتنسيق PFX أو P12. تحتوي هذه الشهادات على كل من المفاتيح العامة والخاصة اللازمة للتوقيع.
1. باستخدام مكتبة Aspose.PDF، تقوم بربط المستند بمعالج التوقيع.
1. استخدم المفتاح الخاص ECDSA لتوقيع تجزئة محتوى المستند.
1. ضع التوقيع الناتج داخل ملف PDF مع بيانات التعريف مثل سبب التوقيع، الموقع، وتفاصيل الاتصال.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifyEcda()
{
   // The path to the documents directory
   var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

   // Open PDF document
   using (var document = new Aspose.Pdf.Document(dataDir + "signed_ecdsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Check if the document contains any digital signatures
            if (!signature.ContainsSignature())
            {
                throw new Exception("Not contains signature");
            }

            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}

private static void SignEcdsa(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures(); 

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create an instance of PdfFileSignature to sign the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create a PKCS7Detached object using the provided certificate and password
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, "12345", Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Sign the first page of the document, setting the signature's appearance at the specified location
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);

            // Save PDF document
            signature.Save(dataDir + "SignEcdsa_out.pdf");
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