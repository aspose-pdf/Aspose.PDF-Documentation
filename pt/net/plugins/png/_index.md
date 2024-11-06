---
title: Conversor de PNG
type: docs
weight: 110
url: pt/net/plugins/png/
description: Converta documentos PDF em imagens PNG com o Plugin Aspose.PDF PNG
lastmod: "2024-01-24"
---

Se você está procurando [converter documentos PDF em imagens PNG](https://products.aspose.org/pdf/net/png-converter/) usando .NET, o Aspose.PDF para .NET oferece uma solução robusta. Neste artigo, vamos passar pelos passos essenciais para criar um objeto, adicionar uma fonte de dados e executar o método de processo usando a biblioteca Aspose.PDF.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de exemplo

## Explicação do Código

O código abaixo demonstra uma demonstração de conversão de PNG usando o Plugin Aspose.PDF PNG:

```csharp
using Aspose.Pdf.Plugins;

//....

// Crie uma nova instância da classe PngOptions.
var convertorOptions = new PngOptions();

// Adicione os caminhos de entrada e saída ao PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// Defina a resolução de saída para 300 DPI.
convertorOptions.OutputResolution = 300;

// Crie uma nova instância da classe Png.
Png converter = new ();

// Processe a conversão de PNG e obtenha o recipiente de resultado.
ResultContainer resultContainer = converter.Process(convertorOptions);

// Imprima o resultado no console.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
Vamos detalhar os passos principais:

1. **Criar um Objeto (PngOptions e Png)**

   O código começa criando uma instância da classe `PngOptions` para configurar a conversão para PNG. Adicionalmente, uma instância da classe `Png` é criada para processamento posterior.

2. **Adicionar Fonte de Dados**

   O caminho do arquivo PDF de entrada é adicionado ao `PngOptions` usando o método `AddInput`. Da mesma forma, o caminho de saída para as imagens PNG é adicionado usando o método `AddOutput`.

3. **Definir Resolução de Saída**

   O código define a resolução de saída para 300 DPI usando a propriedade `OutputResolution` da classe `PngOptions`.

4. **Executar Método Process**

   A conversão para PNG é iniciada chamando o método `Process` na classe `Png`, passando o `PngOptions` configurado. O resultado é armazenado no `resultContainer`.

5. **Manipular Resultado**

   O código imprime o resultado no console, mostrando o(s) caminho(s) do arquivo convertido.
