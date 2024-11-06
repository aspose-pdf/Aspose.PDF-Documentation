---
title: XLS Converter
type: docs
weight: 20
url: pt/net/plugins/xls/
description: Como converter arquivos PDF para planilhas Excel usando plugins Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

Neste artigo, vamos mostrar como usar o [plugin PdfXls](https://products.aspose.org/pdf/net/xls-converter/), que pode converter arquivos PDF para o formato Excel com alta fidelidade e precisão.

{{% /alert %}}

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF for .NET 24.1 ou posterior
* Um arquivo PDF de exemplo que você deseja converter para o formato Excel

Você pode baixar a biblioteca Aspose.PDF for .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Passos

Os passos básicos para converter um arquivo PDF para o formato Excel usando o plugin PdfXls são:

1. Criar um objeto da classe PdfXls
1. Adicionar as fontes de dados de entrada e saída ao objeto PdfToXlsOptions
1. Executar o método Process do objeto PdfXls

Vamos ver como implementar esses passos em código C#.
Vamos ver como implementar esses passos em código C#.

### Passo 1: Criar um objeto da classe PdfXls

A classe PdfXls é a classe principal que fornece a funcionalidade de converter PDF para Excel. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```csharp
// Criar uma instância do plugin PdfXls
var plugin = new PdfXls();
```

### Passo 2: Adicionar as fontes de dados de entrada e saída ao objeto PdfToXlsOptions

A classe PdfToXlsOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de conversão. Para usá-la, você precisa criar uma instância dela e adicionar as fontes de dados de entrada e saída usando os métodos `AddInput` e `AddOutput`. As fontes de dados podem ser tanto caminhos de arquivos quanto streams. Por exemplo, para converter um arquivo PDF chamado `sample.pdf` na pasta `C:\Samples` para um arquivo Excel chamado `sample.xlsx` na mesma pasta, você pode usar o seguinte código:

```csharp
// Especificar os caminhos dos arquivos de entrada e saída
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Criar uma instância da classe PdfToXlsOptions
var options = new PdfToXlsOptions();

// Adicionar os caminhos dos arquivos de entrada e saída às opções
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
Você também pode definir outras opções, como o formato de saída, o intervalo de páginas, o nome da planilha, etc., usando as propriedades da classe PdfToXlsOptions. Por exemplo, para converter o arquivo PDF para o formato XLSX, inserir uma coluna em branco na primeira posição e nomear a planilha como "MySheet", você pode usar o seguinte código:

```csharp
// Definir o formato de saída para XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// Inserir uma coluna em branco na primeira posição
options.InsertBlankColumnAtFirst = true;
```

### Etapa 3: Execute o método Process do objeto PdfXls

A etapa final é executar o método Process do objeto PdfXls, passando o objeto PdfToXlsOptions como parâmetro.
O passo final é executar o método Process do objeto PdfXls, passando o objeto PdfToXlsOptions como parâmetro.

```csharp
// Processa a conversão de PDF para Excel usando o plugin e as opções
var resultContainer = plugin.Process(options);

// Obtém o primeiro resultado da coleção de resultados
var result = resultContainer.ResultCollection[0];

// Imprime o resultado
Console.WriteLine(result);
```

O resultado conterá informações como os caminhos dos arquivos de saída.
