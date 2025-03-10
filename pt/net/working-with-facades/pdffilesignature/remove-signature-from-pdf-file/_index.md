---
title: Remover Assinatura de Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/remove-signature-from-pdf/
description: Esta seção explica como remover a assinatura de um arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "A funcionalidade permite que os usuários removam eficientemente assinaturas digitais de arquivos PDF usando a classe PdfFileSignature. Este recurso oferece flexibilidade, permitindo a remoção de assinaturas específicas enquanto opcionalmente mantém os campos de assinatura para uso futuro, aprimorando as capacidades de gerenciamento de documentos.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Remover Assinatura Digital do Arquivo PDF

Quando uma assinatura é adicionada a um arquivo PDF, é possível removê-la. Você pode remover uma assinatura específica ou todas as assinaturas em um arquivo. O método mais rápido para remover a assinatura também remove o campo de assinatura, mas é possível apenas remover a assinatura, mantendo o campo de assinatura para que o arquivo possa ser assinado novamente.

O método RemoveSignature da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) permite que você remova uma assinatura de um arquivo PDF. Este método recebe o nome da assinatura como entrada. Especifique o nome da assinatura diretamente para remover todas as assinaturas ou obtenha os nomes das assinaturas usando o método [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

O seguinte trecho de código mostra como remover a assinatura digital do arquivo PDF.

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

### Remover Assinatura, mas Manter o Campo de Assinatura

Como mostrado acima, o método [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) permite que você remova campos de assinatura de arquivos PDF. Ao usar este método com versões anteriores a 9.3.0, tanto a assinatura quanto o campo de assinatura são removidos. Alguns desenvolvedores desejam remover apenas a assinatura e manter o campo de assinatura para que ele possa ser usado para resignar o documento. Para manter o campo de assinatura e remover apenas a assinatura, utilize o seguinte trecho de código.

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

O seguinte exemplo mostra como remover todas as assinaturas dos campos.

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