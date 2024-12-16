---
title: Conversor HTML
type: docs
weight: 70
url: /pt/net/plugins/html/
description: Como converter arquivos PDF para e de arquivos HTML usando o plugin Aspose.PDF PdfHtml
lastmod: "2024-01-24"
draft: false
---

Neste artigo, mostraremos como usar o [plugin PdfHtml](https://products.aspose.org/pdf/net/html-converter/), que pode converter arquivos PDF para e de arquivos HTML.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 21.1 ou posterior
* Um arquivo PDF de exemplo e um arquivo HTML de exemplo

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Etapas

As etapas básicas para converter arquivos PDF para e de arquivos HTML usando o plugin PdfHtml são:

1. Criar um objeto da classe PdfHtml
2. Criar um objeto da classe PdfToHtmlOptions ou HtmlToPdfOptions, dependendo da direção da conversão
3. Adicionar as fontes de dados de entrada e saída ao objeto de opções
4.
Vamos ver como implementar esses passos em código C# para cada direção da conversão.

### Passo 1: Criar um objeto da classe PdfHtml

A classe PdfHtml é a classe principal que fornece a funcionalidade de converter arquivos PDF para e de arquivos HTML. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```cs
// Cria uma instância do plugin PdfHtml
var plugin = new PdfHtml();
```

### Passo 2: Criar um objeto da classe PdfToHtmlOptions ou HtmlToPdfOptions, dependendo da direção da conversão

As classes PdfToHtmlOptions e HtmlToPdfOptions são classes auxiliares que permitem especificar várias opções e parâmetros para o processo de conversão, como o formato de saída, o intervalo de páginas, a codificação, as fontes, etc. Para usar essas classes, você precisa criar uma instância da classe apropriada usando o construtor padrão ou passando alguns parâmetros. Por exemplo, para converter um arquivo PDF para um arquivo HTML com recursos embutidos, você pode usar o seguinte código:

```cs
Para converter um arquivo HTML em um arquivo PDF com as configurações padrão, você pode usar o seguinte código:

```cs
// Crie uma nova instância da classe HtmlToPdfOptions
var options = new HtmlToPdfOptions();
```

Você também pode definir outras opções, como o formato de saída, o intervalo de páginas, a codificação, as fontes, etc., usando as propriedades das classes de opções. Por exemplo, para converter um arquivo PDF em um arquivo HTML com codificação UTF-8 e fonte Arial, você pode usar o seguinte código:

```cs
// Crie uma nova instância da classe PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// Defina a codificação para UTF-8
options.Encoding = Encoding.UTF8;

// Defina a fonte para Arial
options.Font = "Arial";
```

### Etapa 3: Adicione as fontes de dados de entrada e saída ao objeto de opções

As fontes de dados de entrada e saída são os arquivos PDF ou HTML que você deseja converter e salvar.
As fontes de entrada e saída são os arquivos PDF ou HTML que você deseja converter e salvar.

```cs
// Especifique os caminhos dos arquivos de entrada e saída
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// Adicione os caminhos dos arquivos de entrada e saída às opções
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### Etapa 4: Execute o método Process da classe PdfHtml

A etapa final é executar o método Process do objeto PdfHtml, passando o objeto de opções como parâmetro. Este método realizará a conversão e retornará um objeto ResultContainer, que contém os resultados da conversão, como o status, as mensagens, as fontes de dados de saída, etc. Você pode acessar os resultados usando as propriedades e métodos da classe ResultContainer. Por exemplo, para obter o primeiro resultado da coleção de resultados e imprimi-lo no console, você pode usar o seguinte código:

```cs
// Processe a conversão e obtenha o contêiner de resultados
var resultContainer = plugin.Process(options);

// Obtenha o primeiro resultado da coleção de resultados
var result = resultContainer.ResultCollection[0];

// Imprima o resultado no console
Console.WriteLine(result);
```

O resultado conterá informações como caminhos de arquivos de saída.
```
