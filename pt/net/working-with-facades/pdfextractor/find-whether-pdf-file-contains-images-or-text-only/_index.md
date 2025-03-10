---
title: Descubra se o PDF contém imagens ou texto
linktitle: Verifique a presença de texto e imagens
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/find-whether-pdf-file-contains-images-or-text-only/
description: Este tópico explica como descobrir se um arquivo PDF contém apenas imagens ou texto com a classe PdfExtractor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Find whether PDF contains images or text",
    "alternativeHeadline": "Determine PDF Content: Text, Images, or Both",
    "abstract": "Descubra a funcionalidade que permite aos usuários determinar de forma eficiente se um arquivo PDF contém texto, imagens ou ambos, usando a classe PdfExtractor. Este recurso simplifica o processo de análise do conteúdo do PDF, fornecendo uma saída clara sobre a presença de texto e imagens dentro do arquivo. Com apenas algumas linhas de código, os usuários podem classificar efetivamente seus documentos PDF com base no tipo de conteúdo",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "265",
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
    "url": "/net/find-whether-pdf-file-contains-images-or-text-only/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/find-whether-pdf-file-contains-images-or-text-only/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Verifique a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Contexto

Um arquivo PDF pode conter tanto texto quanto imagens. Às vezes, um usuário pode precisar descobrir se um arquivo PDF contém apenas texto ou se contém apenas imagens. Também podemos descobrir se contém ambos ou nenhum.

{{% alert color="primary" %}}

O trecho de código a seguir mostra como atender a esse requisito.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Instantiate a memoryStream object to hold the extracted text from Document
    using (var ms = new MemoryStream())
    {
        // Create the PdfExtractor
        using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
        {
            // Bind PDF document
            extractor.BindPdf(dataDir + "FilledForm.pdf");
            // Extract text from the input PDF document
            extractor.ExtractText();
            // Save the extracted text to a text file
            extractor.GetText(ms);
            // Check if the MemoryStream length is greater than or equal to 1

            bool containsText = ms.Length >= 1;

            // Extract images from the input PDF document
            extractor.ExtractImage();

            // Calling HasNextImage method in while loop. When images will finish, loop will exit
            bool containsImage = extractor.HasNextImage();

            // Now find out whether this PDF is text only or image only

            if (containsText && !containsImage)
            {
                Console.WriteLine("PDF contains text only");
            }
            else if (!containsText && containsImage)
            {
                Console.WriteLine("PDF contains image only");
            }
            else if (containsText && containsImage)
            {
                Console.WriteLine("PDF contains both text and image");
            }
            else if (!containsText && !containsImage)
            {
                Console.WriteLine("PDF contains neither text or nor image");
            }
        }
    }
}
```