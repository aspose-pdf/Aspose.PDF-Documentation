---
title: Gerador de Tabelas
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: Permite adicionar/inserir uma tabela na página especificada do documento PDF.
lastmod: "2024-01-24"
draft: false
---

Você precisa criar tabelas dinâmicas e visualmente atraentes em seus documentos PDF usando .NET? Aspose.PDF para .NET oferece uma classe poderosa chamada TableGenerator que simplifica o processo. Neste capítulo, vamos passar pelos passos para gerar tabelas em um documento PDF usando [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/), desde criar um documento de demonstração até gerar tabelas com a classe TableGenerator.
Vamos mergulhar e aprender como gerar tabelas passo a passo.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.3 ou posterior
* Um arquivo PDF de amostra

## Criando um Documento de Demonstração

Antes de começarmos a gerar tabelas, vamos criar um documento de demonstração com páginas vazias onde nossas tabelas serão inseridas.
Antes de começarmos a gerar tabelas, vamos criar um documento de demonstração com páginas vazias onde nossas tabelas serão inseridas.

* Crie um novo documento PDF.
* Adicione páginas vazias ao documento.
* Salve o documento no arquivo especificado.

```cs
// <summary>
// Cria um documento de demonstração com páginas vazias.
//
// Parâmetros:
// - fileName: O caminho e nome do arquivo de saída.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // Crie um novo documento PDF.
    var document = new Aspose.Pdf.Document();

    // Adicione quatro páginas vazias ao documento.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // Salve o documento no arquivo especificado.
    document.Save(fileName);
}
```

## Gerando Tabelas

Uma vez que temos nosso documento de demonstração pronto, podemos começar a gerar tabelas usando a classe `TableGenerator`. O seguinte trecho demonstra como gerar tabelas com vários tipos de conteúdo e opções de formatação. Veja como gerar tabelas:

* Crie uma nova instância da classe `TableGenerator`.
* Crie uma nova instância da classe `TableGenerator`.
* Crie opções de tabela e especifique fontes de dados de arquivos de entrada e saída.
* Adicione tabelas com linhas e células às opções, especificando conteúdo e formatação.
* Processe a geração da tabela usando o método `Process` e obtenha o recipiente de resultado.

### Criando Tabelas

Para criar uma tabela usando Aspose.PDF, siga estas etapas:

```cs
// Crie uma nova instância da classe TableGenerator.
var generator = new TableGenerator();

// Crie opções de tabela e adicione tabelas de demonstração.
var options = new TableOptions();

// Adicione fontes de dados de arquivos de entrada e saída às opções.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// Adicione a primeira tabela às opções.
options
    .InsertPageAfter(1)
    .AddTable()
```

No código acima, criamos uma instância de `TableOptions` e especificamos fontes de dados de arquivos de entrada e saída para o documento PDF.
No código acima, criamos uma instância de `TableOptions` e especificamos fontes de dados de arquivo de entrada e saída para o documento PDF.

### Adicionando Conteúdo às Tabelas

Uma vez que a tabela é criada, você pode populá-la com linhas e células contendo vários tipos de conteúdo, como texto, HTML, imagens, etc. Veja como adicionar conteúdo a uma tabela:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Cabeçalho 1</h1>")) // Adiciona conteúdo HTML à célula.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Cabeçalho 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Cabeçalho 3</h3>"));
```

Neste exemplo, adicionamos uma linha à tabela e a populamos com células contendo fragmentos HTML representando cabeçalhos.

Métodos úteis:

* **InsertPageAfter**: Insere uma página após o número de página especificado.
* **InsertPageBefore**: Insere uma página antes do número de página especificado.
* **AddTable**: Adiciona uma tabela ao documento.
* **AddTable**: Adiciona uma tabela ao documento.
* **AddRow**: Adiciona uma linha à tabela.
* **AddCell**: Adiciona células à linha.
* **AddParagraph**: Adiciona conteúdo à célula.

Você pode adicionar os seguintes tipos de conteúdo como parágrafo:

* **HtmlFragment** - um conteúdo baseado em marcação HTML
* **TeXFragment** - um conteúdo baseado em marcação TeX/LaTeX
* **TextFragment** - um conteúdo de texto simples
* **Image** - gráficos

## Realizar geração de tabela

Após adicionar o conteúdo, podemos começar a criar a tabela.

```cs
// Processa a geração da tabela e obtém o contêiner de resultados.
var resultContainer = generator.Process(options);

// Imprime o número de resultados na coleção de resultados.
Console.WriteLine(resultContainer.ResultCollection.Count);
```

O método `Process` realiza a geração da tabela. Este método também pode ser envolto em try-catch para lidar com erros.

Abaixo você pode ver o código completo do exemplo:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Representa uma classe que demonstra o uso de geração de tabela em Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // Executa a demonstração de geração de tabela.
        // </summary>
        internal static void Run()
        {
            // Cria um documento de demonstração e gera tabelas.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // Cria um documento de demonstração com quatro páginas vazias.
        //
        // Parâmetros:
        // - fileName: O caminho e nome do arquivo de saída.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // Cria um novo documento PDF.
            var document = new Aspose.Pdf.Document();

            // Adiciona quatro páginas vazias ao documento.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // Salva o documento no arquivo especificado.
            document.Save(fileName);
        }

        // <summary>
        // Gera tabelas usando a classe TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // Cria uma nova instância da classe TableGenerator.
            var generator = new TableGenerator();

            // Cria opções de tabela e adiciona tabelas de demonstração.
            var options = new TableOptions();

            // Adiciona fontes de dados de arquivos de entrada e saída às opções.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // Adiciona a primeira tabela às opções.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Cabeçalho 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Cabeçalho 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Cabeçalho 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small A equação $E=mc^2$, descoberta em 1905 por Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Célula 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Célula 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Célula 3 1a"))
                            .AddParagraph(new TextFragment("Célula 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Célula 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Célula 3 3"));

            // Adiciona a segunda tabela às opções.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Cabeçalho 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cabeçalho 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cabeçalho 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // Processa a geração da tabela e obtém o contêiner de resultados.
            var resultContainer = generator.Process(options);

            // Imprime o número de resultados na coleção de resultados.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

