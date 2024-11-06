---
title: Form Exporter
type: docs
weight: 60
url: pt/net/plugins/formflattener/
description: Como achatar campos de formulários em arquivos PDF usando o Plugin FormFlattener da Aspose.PDF
lastmod: "2024-01-24"
---

Neste artigo, mostraremos como usar o [plugin FormFlattener](https://products.aspose.org/pdf/net/form-flattener/), que pode achatar campos de formulários em arquivos PDF.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 21.1 ou posterior
* Um arquivo PDF de amostra que contém alguns campos de formulário

Você pode baixar a biblioteca Aspose.PDF para .NET no site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Etapas

Os passos básicos para achatar campos de formulários em arquivos PDF usando o plugin FormFlattener são:

1. Crie um objeto da classe FormFlattener
1. Crie um objeto da classe FormFlattenAllFieldsOptions ou FormFlattenSelectedFieldsOptions, dependendo se você deseja achatar todos ou alguns campos
1. Execute o método Process do objeto FormFlattener

Vamos ver como implementar esses passos em código C#.

### Passo 1: Criar um objeto da classe FormFlattener

A classe FormFlattener é a classe principal que fornece a funcionalidade de achatamento dos campos de formulários em arquivos PDF. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```cs
// Cria uma instância do plugin FormFlattener
var plugin = new FormFlattener();
```

### Passo 2: Criar um objeto da classe FormFlattenAllFieldsOptions ou FormFlattenSelectedFieldsOptions, dependendo se você deseja achatar todos ou alguns campos

As classes FormFlattenAllFieldsOptions e FormFlattenSelectedFieldsOptions são classes auxiliares que permitem especificar várias opções e parâmetros para o processo de achatamento.
As classes FormFlattenAllFieldsOptions e FormFlattenSelectedFieldsOptions são classes auxiliares que permitem especificar várias opções e parâmetros para o processo de achatamento.

```cs
// Criar opções para achatar todos os campos
var options = new FormFlattenAllFieldsOptions();
```

Para achatar apenas os campos de formulário cujo canto inferior esquerdo x-coordinate é maior que 300, você pode usar o seguinte código:

```cs
// Criar opções para achatar campos selecionados
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Passo 3: Adicionar as fontes de dados de entrada e saída ao objeto de opções

As fontes de dados de entrada e saída são os arquivos PDF que você deseja achatar e salvar.
As fontes de dados de entrada e saída são os arquivos PDF que você deseja achatar e salvar.

```cs
// Adiciona fontes de dados de entrada e saída às opções
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### Etapa 4: Execute o método Process do objeto FormFlattener

A etapa final é executar o método Process do objeto FormFlattener, passando o objeto de opções como parâmetro. Este método realizará o processo de achatamento e retornará um objeto ResultContainer, que contém os resultados do processo, como o status, as mensagens, as fontes de dados de saída, etc. Você pode acessar os resultados usando as propriedades e métodos da classe ResultContainer. Por exemplo, para obter o primeiro resultado da coleção de resultados e imprimi-lo no console, você pode usar o seguinte código:

```cs
// Processa as opções e obtém o contêiner de resultados
var resultContainer = plugin.Process(options);

// Obtém o primeiro resultado do contêiner de resultados
var result = resultContainer.ResultCollection[0];

// Imprime o resultado
Console.WriteLine(result);
```
Aqui está o documento traduzido para o português, mantendo a formatação original em markdown e respeitando as suas instruções:

```
O resultado conterá informações como caminhos de arquivos de saída.
```
