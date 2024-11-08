---
title: DOC Converter
type: docs
weight: 10
url: /pt/net/plugins/doc/
description: Converter PDF para Word de forma simples com o Plugin PdfDoc
lastmod: "2024-01-24"
---

Este artigo orienta você sobre como usar o [Conversor Aspose.Pdf DOC para .NET](https://products.aspose.org/pdf/net/doc-converter/) para converter um documento PDF para o formato Microsoft Word (.doc / .docx).

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de amostra que contém alguns campos de formulário

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Etapas

### 1. Configurando Sua Conversão (captura de tela da classe FileDataSource)

O processo de conversão envolve três passos principais: definir os arquivos de entrada e saída, criar um objeto `PdfDoc` e especificar as opções de conversão.

#### 1.1. Definindo Fontes de Dados

* **Arquivo de Entrada:** Usaremos a classe `FileDataSource` para especificar o local do arquivo PDF que você deseja converter.
* **Arquivo de Entrada:** Usaremos a classe `FileDataSource` para especificar a localização do arquivo PDF que você deseja converter.

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * Substitua `"C:\Samples\sample.pdf"` pelo caminho real para o seu arquivo PDF.

* **Arquivo de Saída:** Da mesma forma, use outro objeto `FileDataSource` para definir a localização e o nome do arquivo para o documento Word resultante.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* Substitua `"C:\Samples\sample.docx"` pelo caminho de saída e nome do arquivo desejado.

### 2. Criando o Objeto Plugin PdfDoc (captura de tela da classe PdfDoc)

Em seguida, criamos uma instância da classe `PdfDoc` para realizar a conversão.

```csharp
  var plugin = new PdfDoc();
```

Este objeto serve como o motor para o processo de conversão.

### 3. Configurando Opções de Conversão

A classe `PdfToDocOptions` permite ajustar o processo de conversão.
A classe `PdfToDocOptions` permite que você refine o processo de conversão.

* **Formato de Salvamento:** Especifique o formato de saída desejado para o documento Word. Neste caso, usamos `SaveFormat.DocX` para gerar um documento compatível com Microsoft Word 2007 ou posterior (.docx).

* **Modo de Conversão:** Defina como o plugin interpreta a estrutura do PDF durante a conversão. Usaremos `ConversionMode.EnhancedFlow` para otimizar o documento Word resultante em termos de layout e formatação.

Aqui está o trecho de código para configurar as opções:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**Adicionando Entrada e Saída:**

Finalmente, associamos as fontes de dados previamente definidas com as opções de conversão usando os métodos `AddInput` e `AddOutput`:

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

Isso conecta o PDF de entrada e o documento Word desejado como saída ao processo de conversão.

### 4.
### 4.

Com tudo configurado, vamos iniciar a conversão chamando o método `Process` do plugin `PdfDoc` e passando as opções configuradas:

```csharp
  var resultContainer = plugin.Process(options);
```

Este método executa a conversão e retorna um objeto `ResultContainer` contendo detalhes sobre o processo.

**Recuperando Resultados:**

Embora não seja essencial para a conversão básica, você pode acessar os resultados através da propriedade `ResultCollection` do objeto `ResultContainer`. Isso pode ser útil para depuração ou acompanhamento de detalhes específicos da conversão.

```csharp
  var result = resultContainer.ResultCollection[0];

  // Imprimir o resultado (opcional para fins de demonstração)
  Console.WriteLine(result);
```

Com este passo final, seu documento PDF será convertido para o formato Word especificado e salvo no local de saída definido.

