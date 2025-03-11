---
title: Copiar Campo Interno e Externo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /pt/net/copy-inner-and-outer-field/
description: Esta seção explica como copiar Campo Interno e Externo com Aspose.PDF Facades usando a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "A funcionalidade Copiar Campo Interno e Externo em Aspose.PDF for .NET aprimora a edição de formulários ao permitir que os usuários dupliquem campos dentro do mesmo PDF ou os transfiram de um arquivo PDF externo. Com os métodos fáceis de usar CopyInnerField e CopyOuterField fornecidos pela classe FormEditor, os usuários podem gerenciar campos de formulários de forma eficiente, garantindo consistência e economizando tempo na preparação de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) método permite que você copie um campo no mesmo arquivo, nas mesmas coordenadas, na página especificada. Este método requer o nome do campo que você deseja copiar, o novo nome do campo e o número da página na qual o campo precisa ser copiado. A classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) fornece este método. O seguinte trecho de código mostra como copiar o campo na mesma localização no mesmo arquivo.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## Copiar Campo Externo em um Arquivo PDF Existente

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) método permite que você copie um campo de formulário de um arquivo PDF externo e, em seguida, o adicione ao arquivo PDF de entrada na mesma localização e no número da página especificado. Este método requer o arquivo PDF do qual o campo precisa ser copiado, o nome do campo e o número da página na qual o campo precisa ser copiado. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). O seguinte trecho de código mostra como copiar um campo de um arquivo PDF externo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```