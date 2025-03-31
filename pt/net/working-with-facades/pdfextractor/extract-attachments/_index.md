---
title: Extrair Anexos de Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/extract-attachments/
description: Descubra como extrair e gerenciar anexos em documentos PDF no .NET usando Aspose.PDF para melhor manuseio de documentos.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "A nova funcionalidade de extração de anexos em Aspose.PDF for .NET permite que os desenvolvedores recuperem e gerenciem facilmente anexos de arquivos dentro de documentos PDF. Ao utilizar a classe PdfExtractor, os usuários podem extrair anexos e obter informações essenciais, como nomes e detalhes dos anexos, aprimorando as capacidades de processamento de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Uma das principais categorias sob as capacidades de extração do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) é a extração de anexos. Esta categoria fornece um conjunto de métodos, que não apenas ajudam a extrair os anexos, mas também fornecem métodos que podem lhe dar informações relacionadas ao anexo, ou seja, os métodos [GetAttachmentInfo](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) e [GetAttachName](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) fornecem informações sobre o anexo e o nome do anexo, respectivamente. Para extrair e, em seguida, obter anexos, usamos os métodos [ExtractAttachment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) e [GetAttachment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

O seguinte trecho de código mostra como usar os métodos PdfExtractor:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```