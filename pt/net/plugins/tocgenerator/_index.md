---
title: Gerador de TdC
type: docs
weight: 150
url: pt/net/plugins/tocgenerator/
description: Cria tabela de conteúdo com Aspose.PDF Gerador de TdC para .NET
lastmod: "2024-01-24"
draft: false
---

Você deseja aprimorar seus documentos PDF [adicionando um Índice (TdC)](https://products.aspose.org/pdf/net/toc-generator/) dinamicamente? Aspose.PDF para .NET oferece uma classe poderosa `TocGenerator` que permite gerar TdCs com facilidade. Neste guia, vamos percorrer os passos básicos para criar um TdC em um documento PDF usando Aspose.PDF, cobrindo a criação de um objeto `TocGenerator`, adicionando caminhos de entrada/saída e executando o processo de geração do TdC.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de exemplo

Além disso, familiarize-se com a classe `TocOptions` e suas funcionalidades. Informações detalhadas podem ser encontradas na [Referência API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

Agora, vamos mergulhar no código e explorar como gerar um Índice para o seu documento PDF.
Agora, vamos mergulhar no código e explorar como gerar um Sumário para o seu documento PDF.

## Passo a passo do Código

Usaremos a classe `TocGeneratorDemo` com um método `Run` para demonstrar como criar um Sumário. Vamos detalhar os passos principais:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // Executa a demonstração de geração do TOC.
        internal static void Run()
        {
            // Cria uma nova instância da classe TocGenerator.
            TocGenerator generator = new();

            // Cria uma nova instância da classe TocOptions.
            TocOptions options = new();
            // Adiciona os caminhos de entrada e saída ao TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // Processa a geração do TOC e obtém o recipiente de resultado.
            var resultContainer = generator.Process(options);

            // Obtém o resultado do recipiente de resultados.
            var result = resultContainer.ResultCollection[0];

            // Imprime o resultado no console.
            Console.WriteLine(result);
        }
    }
}
```
### 1. Criar um Objeto TocGenerator

O código começa criando uma nova instância da classe `TocGenerator`. Esta classe oferece métodos para gerar TOCs para documentos PDF.

```csharp
TocGenerator generator = new();
```

### 2. Criar TocOptions

Em seguida, uma nova instância da classe `TocOptions` é criada para configurar o processo de geração do TOC. Os caminhos dos arquivos de entrada e saída são adicionados às opções.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. Executar o Processo de Geração de TOC

O método `Process` é então chamado no objeto `TocGenerator`, passando as opções configuradas. O contêiner de resultado contém o TOC gerado, e ele é impresso no console.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
