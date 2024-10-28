---
title: Editor de Formulários
type: docs
weight: 40
url: /net/plugins/formeditor/
description: Como Adicionar, Atualizar e Remover Campos de Formulários em Arquivos PDF usando os Plugins do Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Neste artigo, vamos mostrar como usar o [plugin Editor de Formulários](https://products.aspose.org/pdf/net/form-editor/), que pode adicionar, atualizar e remover campos de formulários em arquivos PDF.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de exemplo que contém alguns campos de formulário

Você pode baixar a biblioteca Aspose.PDF para .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Passos

Os passos básicos para adicionar, atualizar e remover campos de formulários em arquivos PDF usando o plugin FormEditor são:

1. Criar um objeto da classe FormEditor
1. Criar um objeto da classe FormEditorAddOptions, FormEditorSetOptions ou FormRemoveSelectedFieldsOptions, dependendo da operação que você deseja realizar
1.
1. Execute o método Process da classe FormEditor

Vamos ver como implementar esses passos em código C# para cada operação.

### Passo 1: Criar um objeto da classe FormEditor

A classe FormEditor é a classe principal que fornece a funcionalidade de adicionar, atualizar e remover campos de formulário em arquivos PDF. Para usá-la, você precisa criar uma instância dela usando o construtor padrão:

```cs
// Criar uma instância do plugin FormEditor
var plugin = new FormEditor();
```

### Passo 2: Criar um objeto da classe FormEditorAddOptions, FormEditorSetOptions ou FormRemoveSelectedFieldsOptions, dependendo da operação que você deseja realizar

As classes `FormEditorAddOptions`, `FormEditorSetOptions` e `FormRemoveSelectedFieldsOptions` são classes auxiliares que permitem especificar várias opções e parâmetros para as operações de edição de formulário, como os tipos de campos de formulário, valores, propriedades, predicados, etc.
As classes `FormEditorAddOptions`, `FormEditorSetOptions` e `FormRemoveSelectedFieldsOptions` são classes auxiliares que permitem especificar várias opções e parâmetros para as operações de edição de formulários, como os tipos de campos de formulário, valores, propriedades, predicados, etc.

```cs
    // Cria opções para adicionar campos de formulário.
    var options = new FormEditorAddOptions(
        [
            // Cria um campo de formulário do tipo checkbox.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // Cria um campo de formulário do tipo combo box.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // Cria um campo de formulário do tipo textbox.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
Para atualizar os valores dos campos do formulário cujos valores são "a value" ou "an another value" para "new value", você pode usar o seguinte código:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

Para remover os campos do formulário cuja coordenada x do canto inferior esquerdo é maior que 300, você pode usar o seguinte código:

```cs
// Cria opções para remover campos do formulário
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Etapa 3: Adicione as fontes de dados de entrada e saída ao objeto de opções

As fontes de dados de entrada e saída são os arquivos PDF que você deseja editar e salvar.
As fontes de dados de entrada e saída são os arquivos PDF que você deseja editar e salvar.

```cs
// Especifique os caminhos dos arquivos de entrada e saída
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// Crie uma nova instância da classe FileDataSource para os arquivos de entrada e saída
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// Adicione as fontes de dados de entrada e saída às opções
options.AddInput(inputData);
options.AddOutput(outputData);
```

### Etapa 4: Execute o método Process do objeto FormEditor

A etapa final é executar o método Process do objeto FormEditor, passando o objeto de opções como parâmetro.
O último passo é executar o método Process do objeto FormEditor, passando o objeto de opções como parâmetro.

```cs
// Processa a operação de edição do formulário usando o plugin e as opções
ResultContainer result = plugin.Process(options);

// Obtém o primeiro resultado da coleção de resultados
var result = resultContainer.ResultCollection[0];

// Imprime o resultado
Console.WriteLine(result);
```

O resultado conterá informações como caminhos de arquivos de saída.
