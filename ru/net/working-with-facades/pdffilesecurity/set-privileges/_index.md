---
title: Установка прав доступа к PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/set-privileges/
description: Узнайте, как изменять права пользователей в файлах PDF, ограничивая определённые действия с помощью Aspose.PDF в .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "Представляем новую возможность устанавливать права доступа к существующим файлам PDF с помощью класса PdfFileSecurity, что позволяет пользователям указывать разрешения на такие действия, как печать и копирование. Кроме того, теперь пользователи могут легко удалять расширенные права из документов PDF, обеспечивая больший контроль над изменениями документов и безопасностью. Эта функция упрощает управление PDF-файлами и повышает уровень соответствия требованиям безопасности",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Установка прав доступа к существующему файлу PDF

Чтобы установить права доступа к файлу PDF, создайте объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и вызовите метод SetPrivilege. Вы можете указать права доступа с помощью объекта DocumentPrivilege, а затем передать этот объект методу SetPrivilege. В следующем фрагменте кода показано, как установить права доступа к файлу PDF.

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

См. следующий метод с указанием пароля:

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

## Удаление функции расширенных прав из PDF

PDF-документы поддерживают функцию расширенных прав, позволяющую конечному пользователю вводить данные в поля форм с помощью Adobe Acrobat Reader, а затем сохранять копию заполненной формы. Однако это гарантирует, что PDF-файл не будет изменён, и если в структуру PDF будут внесены какие-либо изменения, функция расширенных прав будет потеряна. При просмотре такого документа отображается сообщение об ошибке, указывающее на то, что расширенные права были удалены, поскольку документ был изменён. Недавно мы получили требование удалить расширенные права из PDF-документа.

Для удаления расширенных прав из файла PDF в класс PdfFileSignature был добавлен новый метод под названием RemoveUsageRights(). Другой метод под названием ContainsUsageRights() добавлен для определения, содержит ли исходный PDF расширенные права.

{{% alert color="primary" %}}
Начиная с версии Aspose.PDF for .NET 9.5.0, названия следующих методов обновлены. Обратите внимание, что предыдущие методы всё ещё находятся в API, но они помечены как устаревшие и будут удалены. Поэтому рекомендуется попробовать использовать обновлённые методы.

- Метод IsContainSignature(.) был переименован в ContainsSignature(..).
- Метод IsCoversWholeDocument(..) был переименован в CoversWholeDocument(..).
{{% /alert %}}

Следующий код показывает, как удалить права использования из документа:

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