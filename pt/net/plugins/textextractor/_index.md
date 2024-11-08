---
title: Extrator de Texto
type: docs
weight: 140
url: /pt/net/plugins/textextractor/
description: Extrai o conteúdo de texto do documento PDF.
lastmod: "2024-01-24"
---

Você possui um documento PDF do qual precisa [extrair texto programaticamente](https://products.aspose.org/pdf/net/text-extractor/)? Com o Aspose.PDF para .NET, você pode facilmente realizar essa tarefa usando a classe TextExtractor. Neste artigo, vamos percorrer os passos básicos para criar uma aplicação de extração de texto em .NET, cobrindo a criação de um objeto TextExtractor, adicionando uma fonte de dados e executando o processo de extração de texto.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de exemplo

Além disso, familiarize-se com a classe `TextExtractorOptions` e suas funcionalidades. Informações detalhadas podem ser encontradas na [Referência da API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

Agora, vamos mergulhar no código e explorar como extrair texto de um documento PDF.
Agora, vamos mergulhar no código e explorar como extrair texto de um documento PDF.

## Explicação do Código

O código a seguir demonstra as capacidades de extração de texto. Vamos detalhar as etapas principais:

### 1. Criar um Objeto TextExtractor

O código começa criando uma nova instância da classe `TextExtractor`. Esta classe fornece métodos para extrair texto de documentos PDF.

```csharp
using TextExtractor extractor = new();
```

### 2. Adicionar uma Fonte de Dados

Em seguida, é criado um `FileDataSource` para o arquivo PDF de entrada. Este é o arquivo do qual o texto será extraído.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. Criar TextExtractorOptions

Um objeto `TextExtractorOptions` é criado para configurar o processo de extração de texto. A fonte de arquivo de entrada é adicionada às opções.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. Executar o Processo de Extração de Texto

O método `Process` é então chamado no objeto `TextExtractor`, passando as opções configuradas.
O método `Process` é então chamado no objeto `TextExtractor`, passando as opções configuradas.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

Você pode ver o código completo abaixo:

``````cs
using Aspose.Pdf.Plugins;
// ...

// Crie uma nova instância de TextExtractor.
using TextExtractor extractor = new();

// Crie um FileDataSource para o arquivo PDF de entrada.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Crie TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// Processa a extração de texto.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// Imprime o texto extraído.
Console.WriteLine(results[0]);

```

