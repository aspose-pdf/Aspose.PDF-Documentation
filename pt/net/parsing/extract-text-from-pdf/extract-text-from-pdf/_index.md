---
title: Extrair Texto de PDF C#
linktitle: Extrair Texto de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF em C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "Descubra a poderosa nova funcionalidade em Aspose.PDF for .NET que permite aos desenvolvedores extrair texto de documentos PDF sem esforço. Este recurso suporta extração de todas as páginas ou regiões específicas, acomoda layouts de múltiplas colunas e até permite a recuperação de texto destacado com apenas algumas linhas de código. Aprimore suas capacidades de processamento de documentos e simplifique a extração de conteúdo com esta ferramenta versátil.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é uma necessidade comum. Neste exemplo, você verá como Aspose.PDF for .NET permite extrair texto de todas as páginas de um documento PDF. Você precisa criar um objeto da classe **TextAbsorber**. Depois disso, abra o PDF usando a classe **Document** e chame o método **Accept** da coleção **Pages**. A classe **TextAbsorber** absorve o texto do documento e retorna na propriedade **Text**. O seguinte trecho de código mostra como extrair texto de todas as páginas de um documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Chame o método **Accept** em uma página específica do objeto Document. O Índice é o número da página específica de onde o texto precisa ser extraído.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Extrair Texto de Páginas Usando o Dispositivo de Texto

Você pode usar a classe **TextDevice** para extrair texto de um arquivo PDF. O TextDevice usa o TextAbsorber em sua implementação, portanto, na verdade, eles fazem a mesma coisa, mas o TextDevice foi apenas implementado para unificar a abordagem "Device" para extrair qualquer coisa da página, como ImageDevice, PageDevice, etc. O TextAbsorber pode extrair texto de Página, PDF inteiro ou XForm, este TextAbsorber é mais universal.

### Extrair texto de todas as páginas

Os seguintes passos e o trecho de código mostram como extrair texto de um PDF usando o dispositivo de texto.

1. Crie um objeto da classe Document com o arquivo PDF de entrada especificado.
1. Crie um objeto da classe TextDevice.
1. Use o objeto da classe TextExtractOptions para especificar as opções de extração.
1. Use o método Process da classe TextDevice para converter o conteúdo em texto.
1. Salve o texto no arquivo de saída.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## Extrair Texto de uma Região Específica da Página

A classe **TextAbsorber** fornece a capacidade de extrair texto de uma página específica ou de todas as páginas de um documento PDF. Esta classe retorna o texto extraído na propriedade **Text**. No entanto, se tivermos a necessidade de extrair texto de uma região específica da página, podemos usar a propriedade **Rectangle** de **TextSearchOptions**. A propriedade Rectangle aceita um objeto Rectangle como valor e, usando esta propriedade, podemos especificar a região da página da qual precisamos extrair o texto.

O método **Accept** de uma página é chamado para extrair o texto. Crie objetos das classes **Document** e **TextAbsorber**. Chame o método **Accept** na página individual, como Índice da **Page**, do objeto **Document**. O **Índice** é o número da página específica de onde o texto precisa ser extraído. Você pode obter o texto da propriedade **Text** da classe **TextAbsorber**. O seguinte trecho de código mostra como extrair texto de uma página individual.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Extrair texto com base em colunas

Um arquivo PDF pode ser composto por elementos como Texto, Imagem, Anotações, Anexos, Gráficos, etc., e Aspose.PDF for .NET oferece o recurso de adicionar e manipular todos esses elementos. Esta API é notável quando se trata de adição e extração de texto de documentos PDF e podemos nos deparar com um cenário onde um documento PDF é composto por mais de uma coluna (documento de múltiplas colunas) e precisamos extrair o conteúdo da página respeitando o mesmo layout, então Aspose.PDF for .NET é a escolha certa para cumprir essa exigência. Uma abordagem é reduzir o tamanho da fonte do conteúdo dentro do documento PDF e, em seguida, realizar a extração de texto. O seguinte trecho de código mostra os passos para reduzir o tamanho do texto e, em seguida, tentar extrair texto do documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### Segunda abordagem - Usando ScaleFactor

Nesta nova versão, também introduzimos várias melhorias no TextAbsorber e no mecanismo interno de formatação de texto. Agora, durante a extração de texto usando o modo 'Puro', você pode especificar a opção ScaleFactor e pode ser outra abordagem para extrair texto de um documento PDF de múltiplas colunas além da abordagem mencionada acima. Este fator de escala pode ser ajustado para ajustar a grade que é usada para o mecanismo interno de formatação de texto durante a extração de texto. Especificar os valores de ScaleFactor entre 1 e 0.1 (incluindo 0.1) tem o mesmo efeito que a redução da fonte.

Especificar os valores de ScaleFactor entre 0.1 e -0.1 é tratado como valor zero, mas faz com que o algoritmo calcule automaticamente o fator de escala necessário durante a extração de texto. O cálculo é baseado na largura média do glifo da fonte mais popular na página, mas não podemos garantir que no texto extraído nenhuma string de coluna alcance o início da próxima coluna. Observe que, se o valor do ScaleFactor não for especificado, o valor padrão de 1.0 será usado. Isso significa que nenhuma escala será realizada. Se o valor especificado do ScaleFactor for maior que 10 ou menor que -0.1, o valor padrão de 1.0 será usado.

Propomos o uso de autoescala (ScaleFactor = 0) ao processar um grande número de arquivos PDF para extração de conteúdo de texto. Ou definir manualmente uma redução redundante da largura da grade (cerca de ScaleFactor = 0.5). No entanto, você não deve determinar se a escala é necessária para documentos concretos ou não. Se você definir uma redução redundante da largura da grade para o documento (que não precisa disso), o conteúdo de texto extraído permanecerá totalmente adequado. Por favor, dê uma olhada no seguinte trecho de código.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

Observe que não há correspondência direta entre o novo ScaleFactor e o antigo coeficiente de redução manual da fonte. No entanto, por padrão, o algoritmo leva em conta o valor do tamanho da fonte que já foi reduzido devido a algumas razões internas. Por exemplo, reduzir o tamanho da fonte de 10 para 7 tem o mesmo efeito que definir um fator de escala para 5/8 (= 0.625).

{{% /alert %}}

## Extrair Texto Destacado de Documento PDF

Em vários cenários de extração de texto de um documento PDF, você pode se deparar com a necessidade de extrair apenas o texto destacado do documento PDF. Para implementar essa funcionalidade, adicionamos os métodos TextMarkupAnnotation.GetMarkedText() e TextMarkupAnnotation.GetMarkedTextFragments() na API. Você pode extrair texto destacado de um documento PDF filtrando TextMarkupAnnotation e usando os métodos mencionados. O seguinte trecho de código mostra como você pode extrair texto destacado de um documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## Acessar Fragmento de Texto e Elementos de Segmento do XML

Às vezes, precisamos acessar itens TextFragment ou TextSegment ao processar documentos PDF gerados a partir de XML. Aspose.PDF for .NET fornece acesso a tais itens pelo nome. O trecho de código abaixo mostra como usar essa funcionalidade.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```