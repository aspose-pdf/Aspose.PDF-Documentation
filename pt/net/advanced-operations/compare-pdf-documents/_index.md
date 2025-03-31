---
title: Comparar documentos PDF
linktitle: Comparar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /pt/net/compare-pdf-documents/
description: Desde o lançamento 24.7, é possível comparar o conteúdo de documentos PDF com marcas de anotação e saída lado a lado
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "O novo recurso de comparação de PDF em Aspose.PDF for .NET permite que os usuários identifiquem eficientemente as diferenças entre dois documentos PDF, seja por páginas específicas ou pelo conteúdo total. Com saídas lado a lado e opções personalizáveis, como marcadores de mudança adicionais e vários modos de comparação, esta poderosa ferramenta melhora a colaboração ao tornar as revisões fáceis de rastrear e revisar",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1180",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Observe que todas as ferramentas de comparação estão disponíveis na biblioteca [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/).

## Formas de comparar documentos PDF

Ao trabalhar com documentos PDF, há momentos em que você precisa comparar o conteúdo de dois documentos para identificar diferenças. A biblioteca Aspose.PDF for .NET fornece um conjunto de ferramentas poderoso para esse propósito. Neste artigo, exploraremos como comparar documentos PDF usando alguns trechos de código simples.

A funcionalidade de comparação no Aspose.PDF permite que você compare dois documentos PDF página por página. Você pode escolher comparar páginas específicas ou documentos inteiros. O documento de comparação resultante destaca as diferenças, facilitando a identificação de alterações entre os dois arquivos.

Aqui está uma lista de possíveis maneiras de comparar documentos PDF usando Aspose.PDF para a biblioteca .NET:

1. **Comparando Páginas Específicas** - Compare as primeiras páginas de dois documentos PDF.

1. **Comparando Documentos Inteiros** - Compare todo o conteúdo de dois documentos PDF.

1. **Comparar documentos PDF graficamente**:

- Compare PDF com o método GetDifference - imagens individuais onde as mudanças são marcadas.

- Compare PDF com o método CompareDocumentsToPdf - documento PDF com imagens onde as mudanças são marcadas.

## Comparando Páginas Específicas

O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF.

Passos:

1. Inicialização do Documento.
O código começa inicializando dois documentos PDF usando seus respectivos caminhos de arquivo (documentPath1 e documentPath2). Os caminhos são especificados como strings vazias por enquanto, mas na prática, você substituiria isso pelos caminhos reais dos arquivos.

2. Processo de Comparação.

- Seleção de Página - a comparação é limitada à primeira página de cada documento ('Pages[1]').
- Opções de Comparação:

'AdditionalChangeMarks = true' - esta opção garante que marcadores de mudança adicionais sejam exibidos. Esses marcadores destacam diferenças que podem estar presentes em outras páginas, mesmo que não estejam na página atual sendo comparada.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - este modo diz ao comparador para ignorar espaços no texto, focando apenas nas mudanças dentro das palavras.

3. O documento de comparação resultante, que destaca as diferenças entre as duas páginas, é salvo no caminho de arquivo especificado em 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## Comparando Documentos Inteiros

O segundo trecho de código amplia o escopo para comparar todo o conteúdo de dois documentos PDF.

Passos:

1. Inicialização do Documento.
Assim como no primeiro exemplo, dois documentos PDF são inicializados com seus caminhos de arquivo.

2. Processo de Comparação.

- Comparação de Documento Inteiro - ao contrário do primeiro trecho, este código compara todo o conteúdo dos dois documentos.

- Opções de Comparação - as opções são as mesmas do primeiro trecho, garantindo que os espaços sejam ignorados e que marcadores de mudança adicionais sejam exibidos.

3. O resultado da comparação, que destaca as diferenças em todas as páginas dos dois documentos, é salvo no arquivo especificado por 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Os resultados da comparação gerados por esses trechos são documentos PDF que você pode abrir em um visualizador como o Adobe Acrobat. Se você usar a visualização de duas páginas no Adobe Acrobat, verá as mudanças lado a lado:

- Exclusões - estas são anotadas na página da esquerda.
- Inserções - estas são anotadas na página da direita.

Ao definir 'AdditionalChangeMarks' como 'true', você também pode ver marcadores para mudanças que podem ocorrer em outras páginas, mesmo que essas mudanças não estejam na página atual sendo visualizada.

**Aspose.PDF for .NET** fornece ferramentas robustas para comparar documentos PDF, seja para comparar páginas específicas ou documentos inteiros. Ao usar opções como 'AdditionalChangeMarks' e diferentes configurações de 'ComparisonMode', você pode adaptar o processo de comparação às suas necessidades específicas. O documento resultante fornece uma visão clara, lado a lado, das mudanças, facilitando o rastreamento de revisões e garantindo a precisão do documento.

## Compare documentos PDF usando GraphicalPdfComparer

Ao colaborar em documentos, especialmente em ambientes profissionais, você frequentemente acaba com várias versões do mesmo arquivo.

Você pode usar a classe [GraphicalPdfComparer](https://reference.aspose.com/pdf/pt/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) para comparar documentos e páginas PDF. A classe é adequada para comparar mudanças no conteúdo gráfico de uma página.

Com Aspose.PDF for .NET, é possível comparar documentos e páginas e gerar o resultado da comparação em um documento PDF ou arquivo de imagem.

Você pode definir as seguintes propriedades da classe:

- Resolução - resolução em unidades DPI para imagens de saída, bem como para imagens geradas durante a comparação.
- Cor - a cor dos marcadores de mudança.
- Limite - limite de mudança em porcentagem. O valor padrão é zero. Definir um valor diferente de zero permite ignorar mudanças gráficas que são insignificantes para você.

A classe possui um método que permite obter diferenças de imagem de página em uma forma adequada para processamento posterior: **ImagesDifference GetDifference(Page page1, Page page2)**.

Este método retorna um objeto da classe [ImagesDifference](https://reference.aspose.com/pdf/pt/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) que contém uma imagem da primeira página sendo comparada e um array de diferenças. O array de diferenças e a imagem original têm o formato de pixel **RGB24bpp**.

ImagesDifference permite que você gere uma imagem diferente e obtenha uma imagem da segunda página sendo comparada, adicionando um array de diferenças à imagem original. Para fazer isso, use os métodos **ImagesDifference.GetDestinationImage e ImagesDifference.DifferenceToImage**.

### Compare PDF com o método GetDifference

O código fornecido define um método [GetDifference](https://reference.aspose.com/pdf/pt/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) que compara dois documentos PDF e gera representações visuais das diferenças entre eles.

Este método compara as primeiras páginas de dois arquivos PDF e gera duas imagens PNG:

- Uma imagem (diffPngFilePath) destaca as diferenças entre as páginas em vermelho.
- A outra imagem (destPngFilePath) é uma representação visual da página PDF de destino (segunda).

Esse processo pode ser útil para comparar visualmente mudanças ou diferenças entre duas versões de um documento.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### Compare PDF com o método CompareDocumentsToPdf

O trecho de código fornecido usou o método [CompareDocumentsToPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) que compara dois documentos e gera um relatório PDF dos resultados da comparação.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```