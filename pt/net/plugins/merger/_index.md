---
title: Merger
type: docs
weight: 100
url: /pt/net/plugins/merger/
description: Como mesclar múltiplos arquivos PDF em um usando o Plugin Merger do Aspose.PDF
lastmod: "2024-01-24"
---

Neste artigo, vamos mostrar como usar o [plugin Merger](https://products.aspose.org/pdf/net/merger/), que pode mesclar vários arquivos PDF em um e salvar como um novo arquivo.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 21.1 ou posterior
* Três arquivos PDF de amostra que você deseja mesclar

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Etapas

As etapas básicas para mesclar múltiplos arquivos PDF em um usando o plugin Merger são:

1. Criar um objeto da classe Merger
2. Criar um objeto da classe MergeOptions e adicionar os caminhos dos arquivos de entrada e saída
3. Executar o método Process do objeto Merger

Vamos ver como implementar essas etapas em código C#.

### Etapa 1: Criar um objeto da classe Merger
### Etapa 1: Criar um objeto da classe Merger

A classe Merger é a principal classe que fornece a funcionalidade de mesclar vários arquivos PDF em um único. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```cs
// Criar uma nova instância de Merger
var pdfMerger = new Merger();
```

### Etapa 2: Criar um objeto da classe MergeOptions e adicionar os caminhos dos arquivos de entrada e saída

A classe MergeOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de mesclagem, como o intervalo de páginas, a ordem, a segurança, etc.
A classe MergeOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de mesclagem, como o intervalo de páginas, a ordem, a segurança, etc.

```cs
// Especifique os caminhos dos arquivos de entrada e saída
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// Crie uma instância da classe MergeOptions
var mergeOptions = new MergeOptions();

// Adicione os caminhos dos arquivos de entrada e saída às opções
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Etapa 3: Execute o método Process do objeto Merger

A etapa final é executar o método Process do objeto Merger, passando o objeto mergeOptions como parâmetro.
O passo final é executar o método Process do objeto Merger, passando o objeto mergeOptions como parâmetro.

```cs
// Processar a fusão e salvar o arquivo mesclado
pdfMerger.Process(mergeOptions);

// Imprimir uma mensagem de confirmação
Console.WriteLine("Os arquivos PDF foram mesclados com sucesso.");
```
