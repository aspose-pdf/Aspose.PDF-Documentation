---
title: Установка привилегий, шифрование и расшифровка PDF
linktitle: Шифрование и расшифровка PDF файлов
type: docs
weight: 20
url: ru/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Шифруйте PDF файлы с помощью C# используя различные типы и алгоритмы шифрования. Также расшифровывайте PDF файлы, используя пароль владельца.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Установка привилегий, шифрование и расшифровка PDF",
    "alternativeHeadline": "Как зашифровать и расшифровать PDF файл",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, encrypt pdf, decrypt pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "Шифруйте PDF файлы с помощью C# используя различные типы и алгоритмы шифрования. Также расшифровывайте PDF файлы, используя пароль владельца."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Установка привилегий на существующий PDF файл

Для установки привилегий на PDF файл, создайте объект класса [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) и укажите права, которые вы хотите применить к документу. После определения привилегий передайте этот объект в качестве аргумента методу [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Следующий фрагмент кода показывает, как установить привилегии для PDF файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Загрузка исходного PDF файла
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Создание объекта привилегий документа
    // Применение ограничений ко всем привилегиям
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Разрешить только чтение на экране
    documentPrivilege.AllowScreenReaders = true;
    // Шифрование файла с паролями пользователя и владельца.
    // Необходимо установить пароль, чтобы после просмотра файла с пользовательским паролем,
    // Была включена только опция чтения экрана
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Сохранение обновленного документа
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## Шифрование PDF-файла с использованием различных типов и алгоритмов шифрования

Вы можете использовать метод [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) для шифрования PDF-файла. Вы можете передать пользовательский пароль, пароль владельца и разрешения методу [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). Кроме того, вы можете передать любое значение перечисления [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Это перечисление предоставляет различные комбинации алгоритмов шифрования и размеров ключей. Вы можете передать выбранное вами значение. Наконец, сохраните зашифрованный PDF-файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>Пожалуйста, укажите разные пользовательские и владельческие пароли при шифровании PDF-файла.

- **Пользовательский пароль**, если установлен, это то, что вам необходимо предоставить для открытия PDF.
- **Пользовательский пароль**, если установлен, необходимо предоставить для открытия PDF.
- **Пароль владельца**, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader будет запрещать эти действия в соответствии с настройками разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Следующий фрагмент кода показывает, как зашифровать PDF файлы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Открыть документ
Document document = new Document(dataDir+ "Encrypt.pdf");
// Зашифровать PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// Сохранить обновленный PDF
document.Save(dataDir);
```

## Расшифровать PDF файл с использованием пароля владельца

Все чаще пользователи обмениваются PDF файлами с шифрованием, чтобы предотвратить несанкционированный доступ к документам, таким как печать/копирование/поделиться / извлечение информации о содержимом PDF файла.
Все чаще пользователи обмениваются зашифрованными PDF-файлами, чтобы предотвратить несанкционированный доступ к документам, таким как печать/копирование/распространение/извлечение информации о содержимом PDF-файла.
В связи с этим возникает необходимость доступа к зашифрованному PDF-файлу, так как такой доступ может быть получен только авторизованным пользователем. Также люди ищут различные решения для расшифровки PDF-файлов в Интернете.

Лучше всего решить эту проблему один раз, используя библиотеку Aspose.PDF.

Для расшифровки PDF-файла сначала необходимо создать объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и открыть PDF, используя пароль владельца.
Чтобы расшифровать PDF-файл, сначала необходимо создать объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и открыть PDF, используя пароль владельца.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Открыть документ
Document document = new Document(dataDir + "Decrypt.pdf", "password");
// Расшифровать PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// Сохранить обновленный PDF
document.Save(dataDir);
```

## Изменение пароля PDF-файла

Если вы хотите изменить пароль PDF-файла, сначала нужно открыть PDF-файл, используя пароль владельца с объектом [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Если вы хотите изменить пароль PDF-файла, сначала вам нужно открыть PDF-файл, используя пароль владельца с помощью объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- Пользовательский пароль, если установлен, необходимо предоставить для открытия PDF. Acrobat/Reader запросит у пользователя ввод пользовательского пароля. Если он не верен, документ не откроется.
>- Пароль владельца, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader будет запрещать эти действия на основе настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Следующий пример кода показывает, как изменить пароль PDF-файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Открыть документ
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// Изменить пароль
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// Сохранить обновленный PDF
document.Save(dataDir);
```
## Как определить, защищен ли исходный PDF паролем

**Aspose.PDF для .NET** предоставляет отличные возможности для работы с PDF документами. При использовании класса Document из пространства имен Aspose.PDF для открытия защищенного паролем PDF документа, необходимо предоставить информацию о пароле в качестве аргумента конструктору Document, и в случае, если эта информация не предоставлена, генерируется сообщение об ошибке. Фактически, при попытке открыть PDF файл с помощью объекта Document, конструктор пытается прочитать содержимое PDF файла, и в случае, если не предоставлен правильный пароль, генерируется сообщение об ошибке (это делается для предотвращения несанкционированного доступа к документу).

При работе с зашифрованными PDF файлами, вы можете столкнуться с ситуацией, когда вам будет интересно узнать, имеет ли PDF открытый пароль и/или пароль для редактирования.
### Получение информации о защите документа PDF

PdfFileInfo содержит три свойства для получения информации о защите документа PDF.

1. свойство PasswordType возвращает значение перечисления PasswordType:
    - PasswordType.None - документ не защищен паролем
    - PasswordType.User - документ был открыт с паролем пользователя (или паролем для открытия документа)
    - PasswordType.Owner - документ был открыт с паролем владельца (или паролем для прав, редактирования)
    - PasswordType.Inaccessible - документ защищен паролем, но для его открытия требуется пароль, при этом был введен неверный пароль (или пароль не был введен).
2. булево свойство HasOpenPassword - используется для определения, требуется ли пароль для открытия входного файла.
3. булево свойство HasEditPassword - используется для определения, требуется ли пароль для редактирования содержимого входного файла.

### Определение правильного пароля из массива
### Определение правильного пароля из массива

Иногда возникает необходимость определить правильный пароль из массива паролей и открыть документ с правильным паролем. Следующий фрагмент кода демонстрирует шаги по перебору массива паролей и попытке открыть документ с правильным паролем.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Загрузка исходного PDF файла
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Определение, зашифрован ли исходный PDF
Console.WriteLine("Файл защищен паролем " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Количество страниц в документе = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Пароль = " + passwords[passwordcount] + " не верен");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
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
```

