---
title: Optimizer
type: docs
weight: 80
url: /pt/net/plugins/optimizer/
description: Como Otimizar e Manipular Arquivos PDF com o Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

Neste capítulo, exploraremos como utilizar o [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) para otimizar, redimensionar e rotacionar arquivos PDF em suas aplicações C#. 
Vamos mergulhar e aprender como realizar essas tarefas passo a passo.

## Pré-requisitos

Você precisará do seguinte:

* Visual Studio 2019 ou posterior
* Aspose.PDF para .NET 24.1 ou posterior
* Um arquivo PDF de amostra que contém alguns campos de formulário

## Otimizando Arquivos PDF

Otimizar um arquivo PDF envolve reduzir seu tamanho e melhorar o desempenho. Os seguintes trechos mostram como realizar essa tarefa. Veja como você pode otimizar um arquivo PDF:

* Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
* Crie uma nova fonte de dados de arquivo para o arquivo PDF de saída otimizado.
* Crie uma instância de `OptimizeOptions`.
* Adicione as fontes de dados de entrada e saída às opções de otimização.
* Adicione as fontes de dados de entrada e saída às opções de otimização.
* Crie uma instância de `Optimizer` e processe a otimização usando as opções de otimização.

```cs
// Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
var inputDataSource = new FileDataSource(inputPath);

// Crie uma nova fonte de dados de arquivo para o arquivo PDF otimizado de saída.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Crie uma nova instância de OptimizeOptions.
var options = new OptimizeOptions();

// Adicione as fontes de dados de entrada e saída às opções de otimização.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);

// Crie uma nova instância de Optimizer.
var optimizer = new Optimizer();

// Processe a otimização usando as opções de otimização.
optimizer.Process(options);
```

## Redimensionando Arquivos PDF

Redimensionar um arquivo PDF envolve alterar o tamanho de sua página. O seguinte código mostra como realizar essa tarefa. Siga estes passos para redimensionar um arquivo PDF:

* Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
* Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
* Crie uma nova fonte de dados de arquivo para o arquivo PDF de saída redimensionado.
* Crie uma instância de `ResizeOptions` e defina o tamanho de página desejado.
* Adicione as fontes de dados de entrada e saída às opções de redimensionamento.
* Crie uma instância de `Optimizer` e processe o redimensionamento usando as opções de redimensionamento.

```cs
// Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
var inputDataSource = new FileDataSource("sample.pdf");

// Crie uma nova fonte de dados de arquivo para o arquivo PDF de saída redimensionado.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// Crie uma nova instância de ResizeOptions e defina o tamanho de página desejado.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// Adicione as fontes de dados de entrada e saída às opções de redimensionamento.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Crie uma nova instância de Optimizer.
var optimizer = new Optimizer();

// Processe o redimensionamento usando as opções de redimensionamento.
optimizer.Process(opt);
```

## Rotating PDF Pages
## Rotacionando Páginas de PDF

Rotacionar páginas de PDF permite que você altere a orientação das páginas dentro de um documento PDF. Veja como você pode rotacionar páginas de PDF:

* Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
* Crie uma nova fonte de dados de arquivo para o arquivo PDF de saída.
* Crie uma instância de `RotateOptions` e defina o valor de rotação.
* Adicione as fontes de dados de entrada e saída às opções de rotação.
* Crie uma instância de `Optimizer` e processe a rotação usando as opções de rotação.

```cs
// Crie uma nova fonte de dados de arquivo para o arquivo PDF de entrada.
var inputDataSource = new FileDataSource(inputPath);

// Crie uma nova fonte de dados de arquivo para o arquivo PDF otimizado de saída.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Crie uma nova instância de RotateOptions.
var opt = new RotateOptions();

// Adicione as fontes de dados de entrada e saída às opções de rotação.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Defina o valor de rotação
opt.Rotation = Rotation.on180;

// Crie uma nova instância de Optimizer.
var optimizer = new Optimizer();

// Processe a otimização usando as opções de rotação.
optimizer.Process(opt)
```
## Conclusão

Você aprendeu como otimizar, redimensionar e rotacionar arquivos PDF usando o Plugin Aspose.PDF Optimizer em C#. Incorpore essas técnicas em suas aplicações para manipular documentos PDF de forma eficiente de acordo com suas necessidades.
