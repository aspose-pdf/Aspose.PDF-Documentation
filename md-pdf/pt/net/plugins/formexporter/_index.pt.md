---
title: Form Exporter
type: docs
weight: 50
url: /net/plugins/formexpoter/
description: Como exportar valores de campos de formulário para arquivos CSV usando o Plugin Aspose.PDF Form Exporter
lastmod: "2024-01-24"
draft: false
---

Neste artigo, vamos mostrar como usar o [plugin Form Exporter](https://products.aspose.org/pdf/net/form-exporter/), que pode exportar valores de campos de formulário de arquivos PDF para arquivos CSV.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 21.1 ou posterior
* Um arquivo PDF de exemplo que contém alguns campos de formulário

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Etapas

As etapas básicas para exportar valores de campos de formulário para arquivos CSV usando o plugin FormExporter são:

1. Crie um objeto da classe `FormExporter`
1. Crie um objeto da classe `FormExporterValuesToCsvOptions` e especifique o predicado e o delimitador
1.
1.
1. Execute o método `Process` do objeto `FormExporter`

Vamos ver como implementar esses passos no código C#.

### Passo 1: Criar um objeto da classe FormExporter

A classe FormExporter é a classe principal que fornece a funcionalidade de exportar valores de campos de formulários para arquivos CSV. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```cs
// Criar uma instância do plugin FormExporter
var plugin = new FormExporter();
```

### Passo 2: Criar um objeto da classe FormExporterValuesToCsvOptions e especificar o predicado e o delimitador

A classe FormExporterValuesToCsvOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de exportação, como o predicado e o delimitador.
A classe FormExporterValuesToCsvOptions é uma classe auxiliar que permite especificar várias opções e parâmetros para o processo de exportação, como o predicado e o delimitador.

```cs
// Criar opções para exportar valores de campos de formulário para CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Etapa 3: Adicionar as fontes de dados de entrada e saída ao objeto de opções

As fontes de dados de entrada e saída são os arquivos PDF dos quais você deseja exportar e o arquivo CSV que você deseja salvar.
As fontes de dados de entrada e saída são os arquivos PDF dos quais você deseja exportar e o arquivo CSV que você deseja salvar.

```cs
// Adicionar arquivos de entrada e saída às opções
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### Passo 4: Executar o método Process da objeto FormExporter

O último passo é executar o método Process do objeto FormExporter, passando o objeto de opções como parâmetro.
O último passo é executar o método Process do objeto FormExporter, passando o objeto de opções como parâmetro.

```cs
// Processa os valores dos campos do formulário usando o plugin
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

O resultado conterá informações como os caminhos dos arquivos de entrada e saída.
