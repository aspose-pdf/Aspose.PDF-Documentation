---
title: Adicionar assinatura digital ou assinar digitalmente PDF em C#
linktitle: Assinar digitalmente PDF
type: docs
weight: 10
url: /net/digitally-sign-pdf-file/
description: Assinar digitalmente documentos PDF usando C# ou VB.NET. Verificar ou validar os PDFs assinados digitalmente usando C# ou VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Como assinar digitalmente PDF",
    "alternativeHeadline": "Trabalhando com PDF assinado digitalmente",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, assinatura digital PDF",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "dateModified": "2022-02-04",
    "description": "Assinar digitalmente documentos PDF usando C# ou VB.NET. Verificar ou validar os PDFs assinados digitalmente usando C# ou VB.NET."
}
</script>

Aspose.PDF para .NET suporta a funcionalidade de assinar digitalmente os arquivos PDF usando a classe SignatureField. Você também pode certificar um arquivo PDF com um Certificado PKCS12. Algo semelhante a [Adicionando Assinaturas e Segurança no Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Ao assinar um documento PDF usando uma assinatura, você basicamente confirma seu conteúdo "como está". Consequentemente, quaisquer outras alterações feitas posteriormente invalidam a assinatura e, assim, você saberia se o documento foi alterado. Por outro lado, certificar um documento primeiro permite especificar as alterações que um usuário pode fazer ao documento sem invalidar a certificação.

Em outras palavras, o documento ainda seria considerado como mantendo sua integridade e o destinatário ainda poderia confiar no documento. Para mais detalhes, por favor visite Certificar e assinar um PDF. Em geral, certificar um documento pode ser comparado a assinar um executável .NET com código.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Aspose.PDF para recursos de assinatura .NET

Podemos usar as seguintes classes e método para assinatura de PDF

- Classe [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- Enumeração [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- Propriedade [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) na classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)

## Assinar PDF com assinaturas digitais

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // Use objetos PKCS7/PKCS7Detached
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Salvar o arquivo PDF de saída
            signature.Save(outFile);
        }
    }
}
```
## Adicionar carimbo de data/hora à assinatura digital

### Como assinar digitalmente um PDF com carimbo de data/hora

Aspose.PDF para .NET suporta a assinatura digital do PDF com um servidor de carimbo de data/hora ou serviço Web.

Para realizar essa exigência, a classe [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) foi adicionada ao namespace Aspose.PDF. Por favor, veja o seguinte trecho de código que obtém o carimbo de data/hora e o adiciona ao documento PDF:

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // Usuário/Senha podem ser omitidos
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Criar qualquer um dos três tipos de assinatura
            signature.Sign(1, "Razão da Assinatura", "Contato", "Localização", true, rect, pkcs);
            // Salvar o arquivo PDF de saída
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destacado",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/criar-documento-pdf/captura-de-tela.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

