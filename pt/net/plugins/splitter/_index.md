---
title: Splitter
type: docs
weight: 120
url: /pt/net/plugins/splitter/
description: Divide documentos PDF em páginas separadas
lastmod: "2024-01-24"
draft: false
---

Você tem um documento PDF grande que gostaria de dividir em arquivos menores e mais gerenciáveis? Com o [Aspose.PDF Splitter for .NET](https://products.aspose.org/pdf/net/splitter/), você pode facilmente realizar essa tarefa. Neste artigo, exploraremos o processo de dividir um documento PDF em vários arquivos usando o plugin Aspose.PDF. Vamos mergulhar no código e passar pelos passos.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de exemplo

Além disso, familiarize-se com a classe `SplitOptions` e suas propriedades. Você pode encontrar informações detalhadas sobre essa classe na [Referência da API](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). Observe que cada `FileDataSource` de saída representa uma única página nos arquivos PDF divididos.

Agora, vamos explorar o código fornecido e entender como dividir um documento PDF.
Agora, vamos explorar o código fornecido e entender como dividir um documento PDF.

## Visão Geral do Código

O código abaixo demonstra uma demonstração de divisão de PDF usando o Aspose.PDF.Plugins:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// Define o caminho de entrada do documento PDF a ser dividido.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Cria uma nova instância de Splitter.
var splitter = new Splitter();

// Cria opções para a divisão do documento.
var options = new SplitOptions();

// Adiciona fontes de dados de entrada e saída às opções.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// Processa as opções para dividir o documento.
var result = splitter.Process(options);
Console.WriteLine(result);
```

Vamos detalhar os passos principais:
Vamos detalhar os passos principais:

1. **Definir o PDF de Entrada**

   O código começa especificando o caminho do documento PDF de entrada a ser dividido. Isso é feito usando o método `File.OpenRead`.

2. **Criar um Objeto (Divisor e Opções de Divisão)**

   O código cria uma instância da classe `Splitter` para gerenciar o processo de divisão. Além disso, uma instância da classe `SplitOptions` é criada para configurar a operação de divisão.

3. **Adicionar Fonte de Dados (Entrada e Saída)**

   O documento PDF de entrada é adicionado ao `SplitOptions` como uma fonte de dados de entrada usando o método `AddInput`. Para cada página do documento, um caminho de arquivo de saída é adicionado como uma fonte de dados de saída usando o método `AddOutput`.

4. **Executar Método de Processo**

   O processo de divisão é iniciado chamando o método `Process` na classe `Splitter`, passando as `SplitOptions` configuradas. O resultado da operação é armazenado na variável `result`.

5. **Manipular Resultado**

   O código imprime o resultado no console, fornecendo informações sobre o processo de divisão.

O código imprime o resultado no console, fornecendo informações sobre o processo de divisão.
```
