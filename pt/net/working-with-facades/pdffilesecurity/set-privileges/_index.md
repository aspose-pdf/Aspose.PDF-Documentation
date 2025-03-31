---
title: Definir Privilégios em PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/set-privileges/
description: Descubra como modificar os privilégios do usuário em arquivos PDF, restringindo certas ações usando Aspose.PDF em .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "Apresentando a nova capacidade de definir privilégios em arquivos PDF existentes usando a classe PdfFileSecurity, permitindo que os usuários especifiquem permissões para ações como impressão e cópia. Além disso, os usuários agora podem facilmente remover direitos estendidos de documentos PDF, garantindo maior controle sobre modificações e segurança do documento. Essa funcionalidade simplifica a gestão de PDFs enquanto melhora a conformidade de segurança.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Definir Privilégios em um Arquivo PDF Existente

Para definir os privilégios de um arquivo PDF, crie um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesecurity) e chame o método SetPrivilege. Você pode especificar os privilégios usando o objeto DocumentPrivilege e, em seguida, passar esse objeto para o método SetPrivilege. O seguinte trecho de código mostra como definir os privilégios de um arquivo PDF.

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

Veja o seguinte método especificando uma senha:

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

## Remover o Recurso de Direitos Estendidos do PDF

Documentos PDF suportam o recurso de direitos estendidos para permitir que o usuário final preencha dados em campos de formulário usando o Adobe Acrobat Reader e, em seguida, salve uma cópia do formulário preenchido. No entanto, isso garante que o arquivo PDF não seja modificado e, se qualquer modificação na estrutura do PDF for feita, o recurso de direitos estendidos é perdido. Ao visualizar tal documento, uma mensagem de erro é exibida, informando que os direitos estendidos foram removidos porque o documento foi modificado. Recentemente, recebemos uma solicitação para remover direitos estendidos de documentos PDF.

Para remover os direitos estendidos de um arquivo PDF, um novo método chamado RemoveUsageRights() foi adicionado à classe PdfFileSignature. Outro método chamado ContainsUsageRights() foi adicionado para determinar se o PDF de origem contém direitos estendidos.

{{% alert color="primary" %}}
A partir da versão Aspose.PDF for .NET 9.5.0, os nomes dos seguintes métodos foram atualizados. Observe que os métodos anteriores ainda estão na API, mas foram marcados como obsoletos e serão removidos. Portanto, é recomendável tentar usar os métodos atualizados.

- O método IsContainSignature(.) foi renomeado para ContainsSignature(..).
- O método IsCoversWholeDocument(..) foi renomeado para CoversWholeDocument(..).
{{% /alert %}}

O seguinte código mostra como remover direitos de uso do documento:

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