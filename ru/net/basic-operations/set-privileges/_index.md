---
title: Установить привилегии, зашифровать и расшифровать PDF
linktitle: Зашифровать и расшифровать PDF файл
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Зашифровать PDF файл с помощью C# с использованием различных типов и алгоритмов шифрования. Также расшифровать PDF файлы с использованием пароля владельца.
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
    "abstract": "Новая функция позволяет пользователям эффективно шифровать и расшифровывать PDF файлы с помощью C# с использованием различных типов и алгоритмов шифрования. Используя пароли пользователя и владельца, она обеспечивает надежный контроль доступа к документам и разрешения, гарантируя конфиденциальность и целостность содержимого PDF, упрощая управление безопасностью для разработчиков.",
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
    "description": "Зашифровать PDF файл с помощью C# с использованием различных типов и алгоритмов шифрования. Также расшифровать PDF файлы с использованием пароля владельца."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Установить привилегии на существующий PDF файл

Чтобы установить привилегии на PDF файл, создайте объект класса [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) и укажите права, которые вы хотите применить к документу. После определения привилегий передайте этот объект в качестве аргумента методу [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Следующий фрагмент кода показывает, как установить привилегии PDF файла.

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

## Зашифровать PDF файл с использованием различных типов и алгоритмов шифрования

Вы можете использовать метод [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) для шифрования PDF файла. Вы можете передать пароль пользователя, пароль владельца и разрешения в метод [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). Кроме того, вы можете передать любое значение перечисления [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Это перечисление предоставляет различные комбинации алгоритмов шифрования и размеров ключей. Вы можете передать значение по вашему выбору. Наконец, сохраните зашифрованный PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

> Пожалуйста, укажите разные пароли пользователя и владельца при шифровании PDF файла.

- **Пароль пользователя**, если установлен, это то, что вам нужно предоставить для открытия PDF. Acrobat/Reader предложит пользователю ввести пароль пользователя. Если он неверный, документ не откроется.
- **Пароль владельца**, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader запретит эти действия в зависимости от настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Следующий фрагмент кода показывает, как зашифровать PDF файлы.

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

## Расшифровать PDF файл с использованием пароля владельца

Все чаще пользователи обмениваются PDF файлами с шифрованием, чтобы предотвратить несанкционированный доступ к документам, таким как печать/копирование/обмен/извлечение информации о содержимом PDF файла. Сегодня это лучший выбор для шифрования PDF файла, поскольку он сохраняет конфиденциальность и целостность содержимого. В этом отношении существует необходимость доступа к зашифрованному PDF файлу, поскольку такой доступ может быть получен только авторизованным пользователем. Также люди ищут различные решения для расшифровки PDF файлов в Интернете.

Лучше решить эту проблему один раз, используя библиотеку Aspose.PDF.

Чтобы расшифровать PDF файл, вам сначала нужно создать объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и открыть PDF с использованием пароля владельца. После этого вам нужно вызвать метод [Decrypt](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Наконец, сохраните обновленный PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Следующий фрагмент кода показывает, как расшифровать PDF файл.

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

## Изменить пароль PDF файла

Если вы хотите изменить пароль PDF файла, вам сначала нужно открыть PDF файл с использованием пароля владельца с помощью объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). После этого вам нужно вызвать метод [ChangePasswords](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Вам нужно передать текущий пароль владельца вместе с новым паролем пользователя и новым паролем владельца в этот метод. Наконец, сохраните обновленный PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- Пароль пользователя, если установлен, это то, что вам нужно предоставить для открытия PDF. Acrobat/Reader предложит пользователю ввести пароль пользователя. Если он неверный, документ не откроется.
>- Пароль владельца, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader запретит эти действия в зависимости от настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Следующий фрагмент кода показывает, как изменить пароль PDF файла.

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

## Как - определить, защищен ли исходный PDF паролем

**Aspose.PDF for .NET** предоставляет отличные возможности работы с PDF документами. При использовании класса Document пространства имен Aspose.PDF для открытия PDF документа, который защищен паролем, нам нужно предоставить информацию о пароле в качестве аргумента конструктору Document, и в случае, если эта информация не предоставлена, генерируется сообщение об ошибке. На самом деле, при попытке открыть PDF файл с помощью объекта Document, конструктор пытается прочитать содержимое PDF файла, и в случае, если правильный пароль не предоставлен, генерируется сообщение об ошибке (это происходит для предотвращения несанкционированного доступа к документу).

При работе с зашифрованными PDF файлами вы можете столкнуться со сценарием, когда вам будет интересно определить, есть ли у PDF открытый пароль и/или пароль для редактирования. Иногда есть документы, которые не требуют информации о пароле при их открытии, но требуют информации для редактирования содержимого файла. Поэтому, чтобы удовлетворить вышеуказанные требования, класс PdfFileInfo, представленный в Aspose.PDF.Facades, предоставляет свойства, которые могут помочь в определении необходимой информации.

### Получить информацию о безопасности PDF документа

PdfFileInfo содержит три свойства для получения информации о безопасности PDF документа.

1. свойство PasswordType возвращает значение перечисления PasswordType:
    - PasswordType.None - документ не защищен паролем.
    - PasswordType.User - документ был открыт с паролем пользователя (или паролем открытия документа).
    - PasswordType.Owner - документ был открыт с паролем владельца (или паролем разрешений, редактирования).
    - PasswordType.Inaccessible - документ защищен паролем, но для его открытия требуется пароль, в то время как был предоставлен неверный пароль (или не был предоставлен пароль).
2. логическое свойство HasOpenPassword - используется для определения, требует ли входной файл пароль при его открытии.
3. логическое свойство HasEditPassword - используется для определения, требует ли входной файл пароль для редактирования его содержимого.

### Определить правильный пароль из массива

Иногда возникает необходимость определить правильный пароль из массива паролей и открыть документ с правильным паролем. Следующий фрагмент кода демонстрирует шаги для перебора массива паролей и попытки открыть документ с правильным паролем.

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