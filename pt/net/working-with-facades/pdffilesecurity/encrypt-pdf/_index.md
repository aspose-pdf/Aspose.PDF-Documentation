---
title: Criptografar Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/encrypt-pdf-file/
description: Este tópico explica como criptografar um arquivo PDF usando a classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "Descubra como melhorar a segurança de seus documentos sensíveis com o novo recurso de criptografia de PDF usando a classe PdfFileSecurity. Essa funcionalidade permite que você proteja seus arquivos PDF com senha, garantindo que apenas usuários autorizados possam acessá-los. Explore vários tipos e algoritmos de criptografia, incluindo AES com um comprimento de chave de até 256 bits, para proteção robusta durante o compartilhamento e arquivamento de arquivos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Criptografar um documento PDF protege seu conteúdo contra acesso não autorizado de fora, especialmente durante o compartilhamento ou arquivamento de arquivos.

Documentos PDF confidenciais podem ser criptografados e protegidos por senha. Apenas usuários que conhecem a senha poderão descriptografar, abrir e visualizar esses documentos.

Vamos dar uma olhada em como a criptografia de PDF funciona com a biblioteca Aspose.PDF.

## Criptografar Arquivo PDF usando Diferentes Tipos e Algoritmos de Criptografia

Para criptografar um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesecurity) e, em seguida, chamar o método [EncryptFile](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Você pode passar a senha do usuário, a senha do proprietário e privilégios para o método [EncryptFile](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Você também precisa passar os valores KeySize e Algorithm para este método.

Revise uma lista possível de [CryptoAlgorithm](https://reference.aspose.com/pdf/pt/net/aspose.pdf/cryptoalgorithm):

|**Nome do membro**|**Valor**|**Descrição**|
| :- | :- | :- |
|RC4x40|0|RC4 com comprimento de chave 40.|
|RC4x128|1|RC4 com comprimento de chave 128.|
|AESx128|2|AES com comprimento de chave 128.|
|AESx256|3|AES com comprimento de chave 256.|

O seguinte trecho de código mostra como criptografar um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```