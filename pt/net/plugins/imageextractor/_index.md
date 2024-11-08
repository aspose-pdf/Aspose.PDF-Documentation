---
title: Extrator de Imagens
type: docs
weight: 80
url: /pt/net/plugins/imageextractor/
description: Extração de Imagens de PDFs de forma fácil com o Plugin ImageExtractor
lastmod: "2024-01-24"
draft: false
---

Se você já precisou extrair imagens de um arquivo PDF usando .NET, o Aspose.PDF para .NET oferece uma solução poderosa e simples. Neste guia, vamos passar pelos passos básicos para criar um objeto, adicionar uma fonte de dados e executar o método process usando o [Extrator de Imagens Aspose.PDF](https://products.aspose.org/pdf/net/image-extractor/).

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 21.1 ou posterior
* Um arquivo PDF de exemplo

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.
Agora, vamos mergulhar no código e aprender como usar o plugin ImageExtractor.

## Passos

O código fornecido demonstra o uso do plugin `ImageExtractor` para extrair imagens de um arquivo PDF.
O código fornecido demonstra o uso do plugin `ImageExtractor` para extrair imagens de um arquivo PDF.

### 1. Criar um Objeto (ImageExtractor)

O primeiro passo envolve criar uma instância do plugin `ImageExtractor`. Isso é realizado usando o seguinte código:

```csharp
using var plugin = new ImageExtractor();
```

Aqui, a instrução `using` garante a correta disposição dos recursos quando a operação é concluída.

### 2. Adicionar Fonte de Dados

Em seguida, uma instância da classe `ImageExtractorOptions` é criada para configurar o processo de extração de imagens. O caminho do arquivo de entrada é adicionado às opções usando o método `AddInput`:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

Certifique-se de substituir `"C:\Samples\"` e `"sample.pdf"` pelo caminho e nome do arquivo PDF apropriados.

### 3. Executar Método Process

O passo final é processar a extração de imagens usando o plugin e as opções:

```csharp
O resultado é armazenado no `resultContainer`, que contém a(s) imagem(ns) extraída(s).

### 4. Manipular Imagem(ns) Extraída(s)

Após executar o processo, você pode recuperar a(s) imagem(ns) extraída(s) do contêiner de resultados. O código abaixo demonstra como salvar a primeira imagem extraída em um local temporário:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

Certifique-se de personalizar o caminho de destino e o nome do arquivo de acordo com suas preferências.

Você pode copiar o exemplo completo abaixo:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // Demonstra o uso do plugin ImageExtractor para extrair imagens de um arquivo PDF.
    // </summary>
    internal static void Run()
    {
        // Cria uma instância do plugin ImageExtractor.
        using var plugin = new ImageExtractor();

        // Cria uma instância da classe ImageExtractorOptions.
        var imageExtractorOptions = new ImageExtractorOptions();

        // Adiciona o caminho do arquivo de entrada às opções.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // Processa a extração de imagem usando o plugin e as opções.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // Obtém a imagem extraída do contêiner de resultados.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

