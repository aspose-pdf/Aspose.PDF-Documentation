---
title: Converter outros formatos de arquivo para PDF em .NET
linktitle: Converter outros formatos de arquivo para PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /pt/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: Este tópico mostra como o Aspose.PDF permite converter outros formatos de arquivo, como EPUB, MD, PCL, XPS, PS, XML e LaTeX para documentos PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert other file formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple File Formats to PDF in C#",
    "abstract": "Aspose.PDF for .NET introduz um recurso versátil que permite aos usuários converter perfeitamente uma variedade de formatos de arquivo, incluindo EPUB, Markdown, PCL, XPS, PS, XML e LaTeX, em documentos PDF de alta qualidade. Essa funcionalidade melhora o gerenciamento de documentos, garantindo compatibilidade e acessibilidade em várias plataformas, mantendo a integridade do conteúdo original.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "4894",
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
    "url": "/net/convert-other-files-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-other-files-to-pdf/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como **converter vários outros tipos de formatos de arquivo para PDF usando C#**. Ele cobre os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

- [Converter EPUB para PDF](#csharp-convert-epub-to-pdf)
- [Converter Markdown para PDF](#csharp-convert-markdown-to-pdf)
- [Converter PCL para PDF](#csharp-convert-pcl-to-pdf)
- [Converter Texto para PDF](#csharp-convert-text-to-pdf)
- [Converter Texto pré-formatado para PDF](#csharp-convert-pre-formatted-text-to-pdf)
- [Converter XPS para PDF](#csharp-convert-xps-to-pdf)
- [Converter PostScript para PDF](#csharp-convert-ps-to-pdf)
- [Converter XML para PDF](#csharp-convert-xml-to-pdf)
- [Converter XLS-FO para PDF](#csharp-convert-xlsfo-to-pdf)
- [Converter LaTeX/TeX para PDF](#csharp-convert-latex-to-pdf)
- [Converter OFD para PDF](#csharp-convert-ofd-to-pdf)

## Converter EPUB para PDF

**Aspose.PDF for .NET** permite que você converta arquivos EPUB para o formato PDF de forma simples.

<abbr title="publicação eletrônica">EPUB</abbr> (abreviação de publicação eletrônica) é um padrão de e-book livre e aberto do Fórum Internacional de Publicação Digital (IDPF). Os arquivos têm a extensão .epub. O EPUB é projetado para conteúdo refluível, o que significa que um leitor EPUB pode otimizar o texto para um dispositivo de exibição específico.

O EPUB também suporta conteúdo de layout fixo. O formato é destinado a ser um formato único que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook. A versão EPUB 3 também é endossada pelo Grupo de Estudo da Indústria do Livro (BISG), uma associação comercial líder para melhores práticas padronizadas, pesquisa, informações e eventos, para embalagem de conteúdo.

{{% alert color="success" %}}
**Tente converter EPUB para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["EPUB para PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão EPUB para PDF com Aplicativo Gratuito](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong>Converter EPUB para PDF</strong></a>

1. Crie uma instância da classe [EpubLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/epubloadoptions).
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document) mencionando o nome do arquivo de origem e as opções.
3. Salve o documento com o nome de arquivo desejado.

O próximo trecho de código mostra como converter arquivos EPUB para o formato PDF com C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEPUBtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.EpubLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EPUBToPDF.epub", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertEPUBtoPDF_out.pdf");
    }
}
```

Você também pode definir o tamanho da página para conversão. Para definir um novo tamanho de página, você usa o objeto `SizeF` e o passa para o construtor [EpubLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/epubloadoptions/constructors/main).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEPUBtoPDFAdv()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.EpubLoadOptions(new SizeF(1190, 1684));

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EPUBToPDF.epub", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertEPUBtoPDFAdv_out.pdf");
    }
}
```

## Converter Markdown para PDF

**Esse recurso é suportado pela versão 19.6 ou superior.**

{{% alert color="success" %}}
**Tente converter Markdown para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["Markdown para PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão Markdown para PDF com Aplicativo Gratuito](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET fornece a funcionalidade para criar um documento PDF com base no arquivo de dados de entrada [Markdown](https://daringfireball.net/projects/markdown/syntax). Para converter o Markdown para PDF, você precisa inicializar o [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document) usando [MdLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/mdloadoptions).

O seguinte trecho de código mostra como usar essa funcionalidade com a biblioteca Aspose.PDF:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong>Converter Markdown para PDF</strong></a>

1. Crie uma instância da classe [MdLoadOptions ](https://reference.aspose.com/pdf/pt/net/aspose.pdf/mdloadoptions/) .
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document) mencionando o nome do arquivo de origem e as opções.
3. Salve o documento com o nome de arquivo desejado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMarkdownToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.MdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.md", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertMarkdownToPDF_out.pdf");
    }
}
```

## Converter PCL para PDF

<abbr title="Linguagem de Comando da Impressora">PCL</abbr> (Linguagem de Comando da Impressora) é uma linguagem de impressora da Hewlett-Packard desenvolvida para acessar recursos padrão da impressora. Os níveis PCL 1 a 5e/5c são linguagens baseadas em comandos que usam sequências de controle que são processadas e interpretadas na ordem em que são recebidas. Em um nível de consumidor, os fluxos de dados PCL são gerados por um driver de impressão. A saída PCL também pode ser facilmente gerada por aplicativos personalizados.

{{% alert color="success" %}}
**Tente converter PCL para PDF online**

Aspose.PDF para .NET apresenta a você um aplicativo online gratuito ["PCL para PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PCL para PDF com Aplicativo Gratuito](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Atualmente, apenas PCL5 e versões anteriores são suportadas**

<table>
    <thead>
        <tr>
            <th>
                Conjuntos de Comandos
            </th>
            <th>
                Suporte
            </th>
            <th>
                Exceções
            </th>
            <th>
                Descrição
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Comandos de controle de trabalho
            </td>
            <td>
                +
            </td>
            <td>
                Modo de impressão duplex
            </td>
            <td>
                Controle do processo de impressão: número de cópias, bandeja de saída, impressão simplex/duplex, deslocamentos à esquerda e superior, etc.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de controle de página
            </td>
            <td>
                +
            </td>
            <td>
                Comando de pular perfuração
            </td>
            <td>
                Especificar um tamanho de página, margens, orientação da página, distâncias entre linhas e caracteres, etc.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de posicionamento do cursor
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Especificar a posição do cursor e, portanto, as origens de texto, imagens raster ou vetoriais e detalhes.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de seleção de fonte
            </td>
            <td>
                +
            </td>
            <td>
                <ol>
                    <li>Comando de Dados de Impressão Transparente.</li>
                    <li>Fontes suaves incorporadas. Na versão atual, em vez de criar uma fonte suave, nossa biblioteca seleciona uma fonte adequada entre as fontes TrueType "duras" existentes instaladas na máquina de destino. <br/>
                        A adequação é definida pela razão largura/altura.<br/>
                        Esse recurso funciona apenas para fontes Bitmap e TrueType e não garante que o texto impresso com a fonte suave será relevante ao que está no arquivo de origem.<br/>
                        Porque os códigos de caracteres na fonte suave podem não corresponder aos padrões padrão.
                    </li>
                    <li>Conjuntos de Símbolos Definidos pelo Usuário.</li>
                </ol>
            </td>
            <td>
                Permitir o carregamento de fontes suaves (incorporadas) do arquivo PCL e gerenciá-las na memória.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de gráficos raster
            </td>
            <td>
                +
            </td>
            <td>
                Apenas preto e branco
            </td>
            <td>
                Permitir o carregamento de imagens raster do arquivo PCL para a memória, especificar parâmetros raster. <br
                    > como largura, altura, tipo de compressão, resolução, etc.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de cor
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permitir coloração para todos os objetos imprimíveis.
            </td>
        </tr>
        <tr>
            <td>
                Comandos do modelo de impressão
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permitir preenchimento de texto, imagens raster e áreas retangulares com padrões raster predefinidos e <br>
                definidos pelo usuário, especificar o modo de transparência para padrões e
                imagem raster de origem. <br> Padrões predefinidos são hachuras, hachura cruzada
                e sombreamento.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de preenchimento de área retangular
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permitir a criação e preenchimento de áreas retangulares com padrões.
            </td>
        </tr>
        <tr>
            <td>
                Comandos de Gráficos Vetoriais HP-GL/2
            </td>
            <td>
                +
            </td>
            <td>
                Comando Vetorial Telado (SV), Comando de Modo de Transparência (TR), Comando de Dados Transparentes (TD), RO
                (Rotacionar Sistema de Coordenadas), Comando de Fontes Escaláveis ou Bitmap (SB), Comando de Inclinação de Caracteres (SL) e
                Espaço Extra (ES) não estão implementados e comandos DV (Definir Caminho de Texto Variável) são realizados em
                versão beta.
            </td>
            <td>
                Permitir o carregamento de imagens vetoriais HP-GL/2 do arquivo PCL para a memória. A imagem vetorial tem uma origem no canto inferior
                esquerdo da área imprimível, pode ser escalada, traduzida, rotacionada e recortada. <br>
                A imagem vetorial pode conter texto, como rótulos, e figuras geométricas como
                retângulo, círculo, elipse, linha, arco, curva bezier e figuras complexas compostas por figuras simples. <br> Figuras fechadas, incluindo letras de rótulos, podem ser preenchidas com
                preenchimento sólido ou padrão vetorial. <br> O padrão pode ser
                hachuras, hachura cruzada, sombreamento, raster definido pelo usuário, hachura PCL ou hachura cruzada e PCL
                definido pelo usuário. Os padrões PCL são raster. Os rótulos podem ser rotacionados, escalados e direcionados individualmente em
                quatro direções: para cima, para baixo, para a esquerda e para a direita. As direções Esquerda e Direita envolvem a disposição de letras uma após a outra. As direções Para Cima e Para Baixo envolvem a disposição de letras uma sob a outra.
            </td>
        </tr>
        <tr>
            <td>
                Macros
            </td>
            <td>
                ―
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permitir o carregamento de uma sequência de comandos PCL na memória e usar essa sequência muitas vezes, por exemplo,
                para imprimir cabeçalho de página ou definir uma formatação para um conjunto de páginas.
            </td>
        </tr>
        <tr>
            <td>
                Texto Unicode
            </td>
            <td>
                ―
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Permitir a impressão de caracteres não ASCII. Não implementado devido à falta de arquivos de amostra com <br
                    > texto Unicode.
            </td>
        </tr>
        <tr>
            <td>
                PCL6 (PCL-XL)
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Realizado apenas na versão Beta devido à falta de arquivos de teste. Fontes incorporadas também não são
                suportadas.<br> A extensão JetReady não é suportada porque é
                impossível ter a especificação JetReady.
            </td>
            <td>
                Formato de arquivo binário.
            </td>
        </tr>
    </tbody>
</table>

### Convertendo um arquivo PCL para o formato PDF

Para permitir a conversão de PCL para PDF, o Aspose.PDF possui a classe [`PclLoadOptions`](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pclloadoptions) que é usada para inicializar o objeto LoadOptions. Posteriormente, esse objeto é passado como um argumento durante a inicialização do objeto Document e ajuda o mecanismo de renderização PDF a determinar o formato de entrada do documento de origem.

O seguinte trecho de código mostra o processo de conversão de um arquivo PCL para o formato PDF.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong>Converter PCL para PDF</strong></a>

1. Crie uma instância da classe [PclLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pclloadoptions/) .
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/) mencionando o nome do arquivo de origem e as opções.
3. Salve o documento com o nome de arquivo desejado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPCLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.PclLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPCLtoPDF.pcl", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertPCLtoPDF_out.pdf");
    }
}
```

Você também pode monitorar a detecção de erros durante o processo de conversão. Para isso, você precisa configurar o objeto PclLoadOptions: definir ou desmarcar SupressErrors.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPCLtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.PclLoadOptions { SupressErrors = true };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPCLtoPDFAdvanced.pcl", options))
    {
        if (options.Exceptions != null)
        {
            foreach (var ex in options.Exceptions)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // Save PDF document
        document.Save(dataDir + "ConvertPCLtoPDFAdvanced_out.pdf");
    }
}
```

### Problemas Conhecidos

1. A origem de strings de texto e imagens pode diferir ligeiramente daquelas no arquivo PCL de origem se a direção de impressão não for 0°. O mesmo se aplica a imagens vetoriais se o sistema de coordenadas do gráfico vetorial estiver rotacionado (comando RO precedido).
2. A origem de rótulos em imagens vetoriais pode diferir daquelas no arquivo PCL de origem se os rótulos forem influenciados por uma sequência de comandos: Origem do Rótulo (LO), Definir Caminho de Texto Variável (DV), Direção Absoluta (DI) ou Direção Relativa (DR).
3. Um texto pode ser lido incorretamente se deve ser renderizado com fonte suave (incorporada) Bitmap ou TrueType, porque atualmente essas fontes são apenas parcialmente suportadas (veja as exceções na "tabela de recursos suportados"). Nessa situação, o texto pode ser lido corretamente apenas se os códigos de caracteres em uma fonte suave corresponderem aos padrões padrão. O estilo do texto lido também pode diferir do que está no arquivo PCL de origem, pois não é necessário definir o estilo no cabeçalho da fonte suave.
4. Se o arquivo PCL analisado contiver fontes suaves Intellifont ou Universal, uma exceção será lançada, pois fontes Intellifont e Universal não são suportadas.
5. Se o arquivo PCL analisado contiver comandos de macros, o resultado da análise diferirá fortemente do arquivo de origem, pois comandos de macros não são suportados.

## Converter Texto para PDF

**Aspose.PDF for .NET** suporta o recurso de conversão de texto simples e arquivo de texto pré-formatado para o formato PDF.

Converter texto para PDF significa adicionar fragmentos de texto à página PDF. No caso de arquivos de texto, lidamos com 2 tipos de texto: pré-formatado (por exemplo, 25 linhas com 80 caracteres por linha) e texto não formatado (texto simples). Dependendo de nossas necessidades, podemos controlar essa adição nós mesmos ou confiar nos algoritmos da biblioteca.

{{% alert color="success" %}}
**Tente converter TEXTO para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["Texto para PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão TEXTO para PDF com Aplicativo Gratuito](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Converter arquivo de texto simples para PDF

No caso do arquivo de texto simples, podemos usar a seguinte técnica:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong>Converter Texto para PDF</strong></a>

1. Use um _TextReader_ para ler todo o texto.
2. Instancie o objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/) e adicione uma nova página na coleção Pages.
3. Crie um novo objeto de [TextFragment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/textfragment/) e passe o objeto _TextReader_ para seu construtor.
4. Adicione o objeto _TextFragment_ como parágrafo na coleção _Paragraphs_. Se a quantidade de texto for maior que a página, o algoritmo da biblioteca adiciona automaticamente páginas extras.
5. Use o método **Save** da classe [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPlainTextFileToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Read the source text file
    using (var streamReader = new StreamReader(dataDir + "TextToPDFInput.txt"))
    {
        // // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            // Create an instance of TextFragment and pass the text from reader object to its constructor as argument
            var text = new Aspose.Pdf.Text.TextFragment(streamReader.ReadToEnd());
            // Add a new text paragraph in paragraphs collection and pass the TextFragment object
            page.Paragraphs.Add(text);
            // Save PDF document
            document.Save(dataDir + "TextToPDF_out.pdf");
        }
    }
}
```

### Converter arquivo de texto pré-formatado para PDF

Converter texto pré-formatado é semelhante ao texto simples, mas você precisa fazer algumas ações adicionais, como definir margens, tipo e tamanho da fonte. Obviamente, a fonte deve ser monoespaçada (por exemplo, Courier New).

Siga estas etapas para converter texto pré-formatado para PDF com C#:

<a name="csharp-convert-pre-formatted-text-to-pdf" id="csharp-convert-pre-formatted-text-to-pdf"><strong>Converter TXT Pré-formatado para PDF</strong></a>

1. Leia todo o texto como um array de strings.
2. Instancie o objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/) e adicione uma nova página na coleção [Pages](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/pages/).
3. Execute um loop através de um array de strings e adicione cada string como um parágrafo na coleção [Paragraphs](https://reference.aspose.com/pdf/pt/net/aspose.pdf/paragraphs/).

Nesse caso, o algoritmo da biblioteca também adiciona páginas extras, mas podemos controlar esse processo nós mesmos. O exemplo a seguir mostra como converter um arquivo de texto pré-formatado para um documento PDF com tamanho de página A4.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPreFormattedTextToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Read the text file as array of string
    var lines = File.ReadAllLines(dataDir + "ConvertPreFormattedTextToPdf.txt");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set left and right margins for better presentation
        page.PageInfo.Margin.Left = 20;
        page.PageInfo.Margin.Right = 10;
        page.PageInfo.DefaultTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier New");
        page.PageInfo.DefaultTextState.FontSize = 12;

        foreach (var line in lines)
        {
            // check if line contains "form feed" character
            // see https://en.wikipedia.org/wiki/Page_break
            if (line.StartsWith("\x0c"))
            {
                page = document.Pages.Add();
                page.PageInfo.Margin.Left = 20;
                page.PageInfo.Margin.Right = 10;
                page.PageInfo.DefaultTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier New");
                page.PageInfo.DefaultTextState.FontSize = 12;
            }
            else
            {
                // Create an instance of TextFragment and pass the line to its constructor as argument
                var text = new Aspose.Pdf.Text.TextFragment(line);
                // Add a new text paragraph in paragraphs collection and pass the TextFragment object
                page.Paragraphs.Add(text);
            }
        }
        // Save PDF document
        document.Save(dataDir + "PreFormattedTextToPDF_out.pdf");
    }
}
```

## Converter XPS para PDF

**Aspose.PDF for .NET** suporta o recurso de conversão de arquivos <abbr title="Especificação de Papel XML">XPS</abbr> para o formato PDF. Confira este artigo para resolver suas tarefas.

O tipo de arquivo XPS está associado principalmente à Especificação de Papel XML da Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente codinome Metro e subsumindo o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos em seu sistema operacional Windows.

{{% alert color="primary" %}}

O formato de arquivo é basicamente um arquivo XML compactado que é usado principalmente para distribuição e armazenamento. É muito difícil de editar e é implementado principalmente pela Microsoft.

{{% /alert %}}

Para converter XPS para PDF com Aspose.PDF for .NET, introduzimos uma classe chamada [XpsLoadOption](https://reference.aspose.com/pdf/pt/net/aspose.pdf/xpsloadoptions) que é usada para inicializar um objeto [LoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/loadoptions). Posteriormente, esse objeto é passado como um argumento durante a inicialização do objeto Document e ajuda o mecanismo de renderização PDF a determinar o formato de entrada do documento de origem.

{{% alert color="primary" %}}

Em ambos XP e Windows 7, você deve encontrar uma Impressora XPS pré-instalada se olhar no Painel de Controle e depois em Impressoras. Para criar esses arquivos, você pode usar essa impressora como dispositivo de saída. No Windows 7, você deve ser capaz de apenas clicar duas vezes no arquivo para abri-lo em um visualizador XPS. Você também pode baixar o visualizador XPS do site da Microsoft.

{{% /alert %}}

O seguinte trecho de código mostra o processo de conversão de um arquivo XPS para o formato PDF com C#.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong>Converter XPS para PDF</strong></a>

1. Crie uma instância da classe [XpsLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/xpsloadoptions/) .
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/) mencionando o nome do arquivo de origem e as opções.
3. Salve o documento no formato PDF com o nome de arquivo desejado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertXPSToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Instantiate Options object
    var options = new Aspose.Pdf.XpsLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertXPSToPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter o formato XPS para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["XPS para PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão XPS para PDF com Aplicativo Gratuito](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Converter PostScript para PDF

<a name="csharp-convert-ps-to-pdf" id="csharp-convert-ps-to-pdf"><strong>Converter PostScript para PDF</strong></a>

**Aspose.PDF for .NET** suporta recursos de conversão de arquivos PostScript para o formato PDF. Um dos recursos do Aspose.PDF é que você pode definir um conjunto de pastas de fontes a serem usadas durante a conversão.

Para converter um arquivo PostScript para o formato PDF, Aspose.PDF for .NET oferece a classe [PsLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/psloadoptions) que é usada para inicializar o objeto LoadOptions. Posteriormente, esse objeto pode ser passado como um argumento para o construtor do objeto Document, que ajudará o mecanismo de Renderização PDF a determinar o formato do documento de origem.

O seguinte trecho de código pode ser usado para converter um arquivo PostScript para o formato PDF com Aspose.PDF for .NET:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPostScriptToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new PsLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPostscriptInput.ps", options))
    {
        // Save PDF document
        document.Save(dataDir + "PSToPDF_out.pdf");
    }
}
```

Além disso, você pode definir um conjunto de pastas de fontes que serão usadas durante a conversão:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPostscriptToPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options with custom font folders
    var options = new Aspose.Pdf.PsLoadOptions
    {
        FontsFolders = new[] { dataDir + @"\fonts1", dataDir + @"\fonts2" }
    };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPostscriptInput.ps", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertPostscriptToPDFAdvanced_out.pdf");
    }
}
```

## Converter XML para PDF

<a name="csharp-convert-xml-to-pdf" id="csharp-convert-xml-to-pdf"><strong>Converter XML para PDF</strong></a>

O formato XML é usado para armazenar dados estruturados. Existem várias maneiras de converter <abbr title="Linguagem de Marcação Extensível">XML</abbr> para PDF no Aspose.PDF:

1. Transformar qualquer dado XML em HTML usando XSLT e converter HTML para PDF conforme descrito abaixo.
2. Gerar documento XML usando o esquema XSD do Aspose.PDF.
3. Usar documento XML baseado no padrão XSL-FO.

{{% alert color="success" %}}
**Tente converter XML para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["XML para PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão XML para PDF com Aplicativo Gratuito](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

## Converter XSL-FO para PDF

<a name="csharp-convert-xslfo-to-pdf" id="csharp-convert-xslfo-to-pdf"><strong>Converter XSL-FO para PDF</strong></a>

A conversão de arquivos XSL-FO para PDF pode ser implementada usando a técnica tradicional do Aspose.PDF - instanciar o objeto [Document](https://reference.aspose.com/page/net/aspose.page/document) com [XslFoLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/xslfoloadoptions). Mas às vezes você pode encontrar uma estrutura de arquivo incorreta. Para esse caso, o conversor XSL-FO permite definir a estratégia de tratamento de erros. Você pode escolher `ThrowExceptionImmediately`, `TryIgnore` ou `InvokeCustomHandler`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Convert_XSLFO_to_PDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");
    // Set error handling strategy
    options.ParsingErrorsHandlingType = Aspose.Pdf.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFOToPdf_out.pdf");
    }
}
```

## Converter LaTeX/TeX para PDF

<a name="csharp-convert-latex-to-pdf" id="csharp-convert-latext-to-pdf"><strong>Converter LaTeX/TeX para PDF</strong></a>

O formato de arquivo LaTeX é um formato de arquivo de texto com marcação na derivação LaTeX da família de linguagens TeX e LaTeX é um formato derivado do sistema TeX. LaTeX (ˈleɪtɛk/lay-tek ou lah-tek) é um sistema de preparação de documentos e linguagem de marcação de documentos. É amplamente utilizado para a comunicação e publicação de documentos científicos em muitos campos, incluindo matemática, física e ciência da computação. Também desempenha um papel importante na preparação e publicação de livros e artigos que contêm materiais multilíngues complexos, como sânscrito e árabe, incluindo edições críticas. O LaTeX usa o programa de composição TeX para formatar sua saída e é escrito na linguagem de macro TeX.

{{% alert color="success" %}}
**Tente converter LaTeX/TeX para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["LaTex para PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão LaTeX/TeX para PDF com Aplicativo Gratuito](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET suporta o recurso de converter arquivos TeX para o formato PDF e, para atender a essa necessidade, o namespace Aspose.Pdf possui uma classe chamada [LatexLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/latexloadoptions) que fornece as capacidades para carregar arquivos LaTex e renderizar a saída no formato PDF usando a [classe Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).
O seguinte trecho de código mostra o processo de conversão de um arquivo LaTex para o formato PDF com C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTeXtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.TeXLoadOptions();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "samplefile.tex", options))
    {
        // Save PDF document
        document.Save(dataDir + "TeXToPDF_out.pdf");
    }
}
```

## Converter OFD para PDF

<a name="csharp-convert-ofd-to-pdf" id="csharp-convert-ofd-to-pdf"><strong>Converter OFD para PDF</strong></a>

O formato OFD refere-se a "Documento de Layout Fixo Aberto", estabelecido como o padrão nacional da China para armazenamento de arquivos eletrônicos, usado como uma alternativa ao popular formato PDF. Ele suporta documentos de layout fixo, garantindo exibição consistente em diferentes plataformas. Arquivos OFD são utilizados para diversos fins, incluindo documentos digitais e aplicações comerciais.

Aspose.PDF for .NET suporta o recurso de converter arquivos OFD para o formato PDF e, para atender a essa necessidade, o namespace Aspose.Pdf possui uma classe chamada [OfdLoadOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/ofdloadoptions/) que fornece as capacidades para carregar arquivos OFD e renderizar a saída no formato PDF usando a [classe Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).

O seguinte trecho de código mostra o processo de conversão de um arquivo OFD para o formato PDF com C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```