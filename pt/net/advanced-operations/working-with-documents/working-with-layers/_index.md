---
title: Trabalhar com camadas PDF usando C#
linktitle: Trabalhar com camadas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/work-with-pdf-layers/
description: A próxima tarefa explica como bloquear uma camada PDF, extrair elementos da camada PDF, achatar um PDF em camadas e mesclar todas as camadas dentro do PDF em uma só.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "Experimente uma gestão aprimorada de documentos PDF com o novo recurso Aspose.PDF for .NET que permite aos usuários trabalhar efetivamente com camadas PDF. Essa funcionalidade permite bloquear e desbloquear camadas, extrair elementos em arquivos separados, achatar conteúdo em camadas e mesclar várias camadas em uma, proporcionando maior controle sobre a visibilidade e organização do documento. Desbloqueie o potencial dos seus documentos PDF e otimize seus fluxos de trabalho com essas ferramentas poderosas",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

As camadas PDF permitem que um documento PDF contenha diferentes conjuntos de conteúdo que podem ser visualizados ou ocultados seletivamente. Cada camada em um PDF pode incluir texto, imagens ou gráficos, e os usuários podem alternar essas camadas, dependendo de suas necessidades. As camadas são frequentemente usadas em documentos complexos onde diferentes conteúdos precisam ser organizados ou separados.

## Bloquear uma camada PDF

Com Aspose.PDF for .NET você pode abrir um PDF, bloquear uma camada específica na primeira página e salvar o documento com as alterações.

Desde o lançamento 24.5, esse recurso foi implementado.

Foram adicionados dois novos métodos e uma propriedade:

- Layer.Lock(); - Bloqueia a camada.
- Layer.Unlock(); - Desbloqueia a camada.
- Layer.Locked; - Propriedade que indica o estado de bloqueio da camada.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## Extrair elementos da camada PDF

A biblioteca Aspose.PDF for .NET permite extrair cada camada da primeira página e salvar cada camada em um arquivo separado.

Para criar um novo PDF a partir de uma camada, o seguinte trecho de código pode ser usado:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

O lançamento 24.9 resultou em uma atualização para esse recurso.

É possível extrair elementos da camada PDF e salvá-los em um novo fluxo de arquivo PDF:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## Achatar um PDF em camadas

A biblioteca Aspose.PDF for .NET abre um PDF, itera por cada camada na primeira página e achata cada camada, tornando-a permanente na página.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

O método 'Layer.Flatten(bool cleanupContentStream)' aceita o parâmetro booleano que especifica se deve remover marcadores de grupo de conteúdo opcional do fluxo de conteúdo. Definir o parâmetro cleanupContentStream como falso acelera o processo de achatamento.

## Mesclar todas as camadas dentro do PDF em uma

A biblioteca Aspose.PDF for .NET permite mesclar todas as camadas PDF ou uma camada específica na primeira página em uma nova camada e salvar o documento atualizado.

Dois métodos foram adicionados para mesclar todas as camadas na página:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

O segundo parâmetro permite renomear o marcador de grupo de conteúdo opcional. O valor padrão é "oc1" (/OC /oc1 BDC).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```