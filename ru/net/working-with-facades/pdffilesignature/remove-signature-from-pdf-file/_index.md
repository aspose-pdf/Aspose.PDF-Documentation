---
title: Удалить подпись из PDF файла
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/remove-signature-from-pdf/
description: Этот раздел объясняет, как удалить подпись из PDF файла с помощью класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "Функциональность позволяет пользователям эффективно удалять цифровые подписи из PDF файлов с помощью класса PdfFileSignature. Эта функция предоставляет гибкость, позволяя удалять конкретные подписи, при этом опционально сохраняя поля подписи для будущего использования, улучшая возможности управления документами.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "434",
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
    "url": "/net/remove-signature-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-signature-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Удалить цифровую подпись из PDF файла

Когда подпись была добавлена в PDF файл, ее можно удалить. Вы можете удалить либо конкретную подпись, либо все подписи в файле. Самый быстрый способ удаления подписи также удаляет поле подписи, но возможно просто удалить подпись, сохранив поле подписи, чтобы файл можно было подписать снова.

Метод RemoveSignature класса [PdfFileSignature](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilesignature) позволяет вам удалить подпись из PDF файла. Этот метод принимает имя подписи в качестве входных данных. Либо укажите имя подписи напрямую, чтобы удалить все подписи, получите имена подписей, используя метод [GetSignNames](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

Следующий фрагмент кода показывает, как удалить цифровую подпись из PDF файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignature()
{  
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdFileSignature.GetSignNames();
        // Remove all the signatures from the PDF file
        for (int index = 0; index < sigNames.Count; index++)
        {
            Console.WriteLine($"Removed {sigNames[index]}");
            pdFileSignature.RemoveSignature(sigNames[index]);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

### Удалить подпись, но сохранить поле подписи

Как показано выше, метод [RemoveSignature](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) класса [PdfFileSignature](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilesignature) позволяет вам удалять поля подписи из PDF файлов. При использовании этого метода с версиями до 9.3.0 как подпись, так и поле подписи удаляются. Некоторые разработчики хотят удалить только подпись и сохранить поле подписи, чтобы его можно было использовать для повторной подписи документа. Чтобы сохранить поле подписи и удалить только подпись, пожалуйста, используйте следующий фрагмент кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        pdFileSignature.RemoveSignature("Signature1", false);

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

Следующий пример показывает, как удалить все подписи из полей.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        var sigNames = pdFileSignature.GetSignatureNames();
        foreach (var sigName in sigNames)
        {
            pdFileSignature.RemoveSignature(sigName, false);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```