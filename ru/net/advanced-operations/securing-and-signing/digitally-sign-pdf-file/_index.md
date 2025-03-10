---
title: Добавить цифровую подпись или цифровую подпись PDF в C#
linktitle: Цифровая подпись PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/digitally-sign-pdf-file/
description: Цифровая подпись PDF-документов с использованием C# или VB.NET. Проверка или валидация цифровых подписей PDF с использованием C# или VB.NET.
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
    "abstract": "Aspose.PDF for .NET представляет мощные возможности для цифровой подписи PDF-документов с использованием C# или VB.NET, повышая целостность и безопасность документов. Пользователи могут реализовать различные типы подписей, включая недетачированные и детачированные подписи с поддержкой PKCS7 и ECDSA, что позволяет настраивать процессы подписания в соответствии с конкретными криптографическими стандартами. Эта функция не только проверяет подлинность документов, но и позволяет добавлять временные метки и сертификацию, обеспечивая надежную обработку документов.",
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
    "description": "Цифровая подпись PDF-документов с использованием C# или VB.NET. Проверка или валидация цифровых подписей PDF с использованием C# или VB.NET."
}
</script>

Aspose.PDF for .NET поддерживает возможность цифровой подписи PDF-файлов с использованием класса SignatureField. Вы также можете сертифицировать PDF-файл с помощью сертификата PKCS12. Что-то похожее на [Добавление подписей и безопасности в Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

При подписании PDF-документа с использованием подписи вы, по сути, подтверждаете его содержимое "как есть". Следовательно, любые другие изменения, внесенные после этого, аннулируют подпись, и таким образом вы будете знать, если документ был изменен. В то время как сертификация документа сначала позволяет вам указать изменения, которые пользователь может внести в документ, не аннулируя сертификацию.

Другими словами, документ по-прежнему будет считаться целостным, и получатель все еще сможет доверять документу. Для получения дополнительной информации, пожалуйста, посетите Сертификация и подпись PDF. В общем, сертификация документа может быть сопоставлена с кодовой подписью .NET исполняемого файла.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Возможности подписания Aspose.PDF for .NET

Мы можем использовать следующие классы и методы для подписания PDF

- Класс [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature).
- Перечисление [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions).
- Свойство [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) в классе [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature).

Чтобы создать цифровую подпись на основе сертификатов PKCS12 (расширения файлов .p12, pfx), вы должны создать экземпляр класса `PdfFileSignature`, передав ему объект документа.
Затем вы должны указать желаемый метод цифровой подписи, создав объект одного из классов:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_Вы можете установить алгоритм дайджеста только для `PKCS7Detached`. Для `PKCS1` и `PKCS7` алгоритм дайджеста всегда устанавливается на SHA-1._

Затем вам нужно использовать полученный объект алгоритма подписи в методе `PdfFileSignature.Sign()`.
Цифровая подпись будет установлена для документа после его сохранения.

## Подписать PDF с цифровыми подписями

Пример ниже создает недетачированную подпись PKCS7 с алгоритмом дайджеста SHA-1.
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

Пример ниже создает детачированную подпись в формате PKCS7Detached с алгоритмом дайджеста SHA-256. Алгоритм ключа зависит от ключа сертификата. Поддерживаются DSA, RSA, ECDSA.

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

Вы можете проверить подписи, используя метод PdfFileSignature.VerifySignature().
Ранее метод `GetSignNames()` использовался для получения имен подписей. Начиная с версии 25.02, следует использовать метод `GetSignatureNames()`, который возвращает список `SignatureName`.
`SignatureName` предотвращает коллизии при проверке подписей с одинаковыми именами.
Методы, которые принимают тип `SignatureName` вместо строкового имени подписи, также должны использоваться.

_Примечания, метод __PdfFileSignature.VerifySigned()__ устарел._

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

## Добавить временную метку к цифровой подписи

### Как цифровая подпись PDF с временной меткой

Aspose.PDF for .NET поддерживает цифровую подпись PDF с сервером временных меток или веб-службой.

Чтобы выполнить это требование, в пространство имен Aspose.PDF был добавлен класс [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings). Пожалуйста, посмотрите следующий фрагмент кода, который получает временную метку и добавляет ее к PDF-документу:

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

## Подписать PDF с X509Certificate2 в формате base64

Этот код подписывает PDF с использованием внешнего сертификата, возможно, взаимодействуя с сервером для получения подписанного хеша и встраивания подписи в PDF-документ.

Шаги для подписания PDF:

1. Создайте экземпляр PdfFileSignature.
1. Определите пользовательский хеш подписи.
1. Загрузка сертификата.
1. Подписание данных.
1. Привязка и подписание PDF.
1. Сохранение подписанного PDF.

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

## Подписать PDF с функцией подписи HASH

Используя пользовательскую функцию подписи хеша, орган, подписывающий, может реализовать конкретные криптографические стандарты или внутренние политики безопасности, которые выходят за рамки стандартных методов подписания, обеспечивая целостность документа.
Этот подход помогает проверить, что документ не был изменен с момента применения подписи и предоставляет юридически обязательную цифровую подпись с проверяемым доказательством личности подписанта с использованием сертификата PFX.

Этот фрагмент кода демонстрирует цифровую подпись PDF-документа с использованием сертификата PFX (PKCS#12) с пользовательской функцией подписи хеша на C#.

Давайте подробнее рассмотрим процесс подписания DPF:

1. Определите пути к файлам и информацию о сертификате:

- inputPdf: Путь к входному PDF-документу, который необходимо подписать.
- inputP12: Путь к файлу сертификата .p12 (PFX), используемому для подписания.
- inputPfxPassword: Пароль для сертификата PFX.
- outputPdf: Путь, по которому будет сохранен подписанный PDF.

2. Процесс подписи:

- Объект `PdfFileSignature` создается и привязывается к входному PDF.
- Объект `PKCS7` инициализируется с использованием сертификата PFX и его пароля. Метод 'CustomSignHash' назначается как пользовательская функция подписи хеша.
- Вызывается метод `Sign`, указывая номер страницы (1 в данном случае), детали подписи (причина, контент, местоположение) и позицию (прямоугольник с координатами (0, 0, 500, 500)) для подписи.
- Подписанный PDF затем сохраняется по указанному выходному пути.

3. Пользовательская подпись хеша:

- Метод `CustomSignHash` принимает массив байтов signableHash (хеш для подписи).
- Он загружает тот же сертификат PFX и получает его закрытый ключ.
- Закрытый ключ используется для подписи хеша с использованием `RSACryptoServiceProvider` и алгоритма SHA-1.
- Подписанные данные (массив байтов) возвращаются для применения к подписи PDF.

Алгоритм дайджеста можно указать в конструкторе PKCS7Detached. В делегате CustomSignHash можно вызвать стороннюю службу. Алгоритм подписи, используемый в CustomSignHash, должен соответствовать алгоритму ключа в сертификате, переданном в PKCS7/PKCS7Detached.

Пример ниже создает недетачированную подпись с алгоритмом RSA и алгоритмом дайджеста SHA-1.
Если вы используете PKCS7Detached вместо PKCS7, вы можете использовать ECDCA и установить желаемый алгоритм дайджеста.

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

Чтобы создать подпись, требуется предварительная оценка длины будущей цифровой подписи.
Если вы используете SignHash для создания цифровой подписи, вы можете обнаружить, что делегат вызывается дважды в процессе сохранения документа.
Если по какой-то причине вы не можете позволить себе два вызова, например, если во время вызова происходит запрос PIN-кода, вы можете использовать опцию `AvoidEstimatingSignatureLength` для классов PKCS1, PKCS7, PKCS7Detached и ExternalSignature.
Установка этой опции избегает этапа оценки длины подписи, устанавливая фиксированное значение в качестве ожидаемой длины - `DefaultSignatureLength`. Значение по умолчанию для свойства DefaultSignatureLength составляет 3000 байт.
Опция AvoidEstimatingSignatureLength работает только в том случае, если делегат SignHash установлен в свойстве CustomSignHash.
Если фактическая длина полученной подписи превышает ожидаемую длину, указанную свойством DefaultSignatureLength, вы получите `SignatureLengthMismatchException`, указывающий на фактическую длину.
Вы можете настроить значение параметра DefaultSignatureLength по своему усмотрению.

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

## Подписание PDF-документов с использованием ECDSA

Подписание PDF-документов с использованием ECDSA (Алгоритм цифровой подписи на основе эллиптической кривой) включает в себя использование эллиптической кривой криптографии для генерации цифровых подписей. Это обеспечивает высокую безопасность и эффективность, особенно для мобильных и ограниченных по ресурсам сред. Этот подход гарантирует, что ваши PDF-документы подписаны с использованием преимуществ безопасности эллиптической кривой криптографии.

Aspose.PDF поддерживает создание и проверку цифровых подписей на основе ECDSA.
Следующие эллиптические кривые поддерживаются для создания и проверки цифровых подписей:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

Алгоритм дайджеста по умолчанию - SHA2 с длиной, зависящей от размера ключа ECDSA.
Вы можете указать алгоритм дайджеста в конструкторе `PKCS7Detached`.

ECDSA цифровые подписи с следующими алгоритмами дайджеста могут быть подписаны: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.
ECDSA цифровые подписи с следующими алгоритмами дайджеста могут быть проверены: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

Вы можете проверить подпись и верификацию, создав сертификат PFX(output.pfx) в OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Доступные имена кривых для подписи и проверки в Aspose.PDF (список кривых в OpenSSL можно получить с помощью команды 'openssl ecparam -list_curves'): prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

Чтобы подписать PDF-документ с использованием ECDSA, общие шаги на C# будут следующими:

1. Вам понадобится сертификат ECDSA в формате PFX или P12. Эти сертификаты содержат как открытые, так и закрытые ключи, необходимые для подписания.
1. Используя библиотеку Aspose.PDF, вы связываете документ с обработчиком подписи.
1. Используйте закрытый ключ ECDSA для подписи хеша содержимого документа.
1. Поместите сгенерированную подпись внутри PDF-файла вместе с метаданными, такими как причина подписания, местоположение и контактные данные.

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