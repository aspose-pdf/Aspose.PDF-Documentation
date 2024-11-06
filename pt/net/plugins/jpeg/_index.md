---
title: Conversor JPEG
type: docs
weight: 90
url: pt/net/plugins/jpeg/
description: Como converter páginas PDF em imagens JPEG usando o Conversor JPEG da Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Neste artigo, mostraremos como usar o [Conversor JPEG](https://products.aspose.org/pdf/net/jpeg-converter/), que pode converter páginas PDF em imagens JPEG e salvar como arquivos separados.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de amostra que contém algumas páginas

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Passos

Os passos básicos para converter páginas PDF em imagens JPEG usando o Conversor JPEG são:

1. Criar um objeto da classe Jpeg
1. Criar um objeto da classe JpegOptions e adicionar os caminhos dos arquivos de entrada e saída
1. Executar o método Process do objeto Jpeg e obter o recipiente de resultado
1.
1.

Vamos ver como implementar esses passos em código C#.

### Passo 1: Criar um objeto da classe Jpeg

A classe Jpeg é a classe principal que fornece a funcionalidade de converter páginas PDF em imagens JPEG. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```cs
// Criar uma nova instância de Jpeg
var converter = new Jpeg();
```

### Passo 2: Criar um objeto da classe JpegOptions e adicionar os caminhos dos arquivos de entrada e saída

A classe JpegOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de conversão, como a resolução de saída, o intervalo de páginas, a qualidade da imagem, etc.
A classe JpegOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de conversão, como a resolução de saída, o intervalo de páginas, a qualidade da imagem, etc.

```cs
// Especifique os caminhos dos arquivos de entrada e saída
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// Crie uma instância da classe JpegOptions
var converterOptions = new JpegOptions();

// Adicione os caminhos dos arquivos de entrada e saída às opções
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

Você também pode definir outras opções, como a resolução de saída, o intervalo de páginas, a qualidade da imagem, etc. usando as propriedades da classe JpegOptions. Por exemplo, para converter apenas a primeira página do arquivo PDF para uma imagem JPEG com resolução de 300 dpi, você pode usar o seguinte código:

```cs
// Defina a resolução de saída para 300 dpi
converterOptions.OutputResolution = 300;

// Defina o intervalo de páginas para a primeira página
converterOptions.PageRange = new PageRange(1);
```
### Etapa 3: Execute o método Process do objeto Jpeg e obtenha o recipiente de resultado

A etapa final é executar o método Process do objeto Jpeg, passando o objeto converterOptions como parâmetro. Este método realizará a conversão e retornará um objeto ResultContainer, que contém os resultados da conversão, como o status, as mensagens, os caminhos dos arquivos de saída, etc. Você pode acessar os resultados usando as propriedades e métodos da classe ResultContainer. Por exemplo, para obter o recipiente de resultado e imprimir o status da conversão, você pode usar o seguinte código:

```cs
// Processa a conversão e obtém o recipiente de resultado
ResultContainer resultContainer = converter.Process(converterOptions);

// Imprime o status da conversão
Console.WriteLine(resultContainer.Status);
```

O status da conversão pode ser Sucesso ou Falha, dependendo de se a conversão foi concluída com sucesso ou não.

### Etapa 4: Imprima os caminhos das imagens JPEG convertidas

O recipiente de resultado contém uma coleção de resultados, um para cada caminho de arquivo de saída.
O contêiner de resultados contém uma coleção de resultados, um para cada caminho de arquivo de saída.

```cs
// Imprime os caminhos das imagens JPEG convertidas
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

Os caminhos dos arquivos de saída terão o formato {outputPath}{pageNumber}.jpg, onde {outputPath} é o diretório de saída e {pageNumber} é o número da página do arquivo PDF. Por exemplo, se o diretório de saída é C:\Samples\images e o arquivo PDF tem três páginas, os caminhos dos arquivos de saída serão:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
