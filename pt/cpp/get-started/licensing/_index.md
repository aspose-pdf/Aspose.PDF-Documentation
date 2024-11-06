---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: pt/cpp/licensing/
description: Aspose. PDF para C++ convida seus clientes a obter uma licença Clássica e Licença Contabilizada. Assim como usar uma licença limitada para explorar melhor o produto.
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitações da Versão de Avaliação

Queremos que nossos clientes testem nossos componentes completamente antes de comprar, então a versão de avaliação permite que você a use normalmente. No entanto, haveria as seguintes limitações ao usar uma versão de avaliação da API:

**PDF criado com uma marca d'água de avaliação**  
A versão de avaliação do Aspose.PDF para C++ fornece funcionalidade completa do produto, mas todas as páginas nos documentos PDF gerados são marcadas com "Apenas para Avaliação. Criado com Aspose.PDF. Copyright 2002-2017 Aspose Pty Ltd" no topo.

**Limite do Número de Itens de Coleção que podem ser Processados**

Na versão de avaliação, apenas quatro itens podem ser processados de qualquer coleção (por exemplo, apenas quatro páginas, quatro campos de formulário, etc.).

## Aplicar Licença usando Arquivo ou Objeto de Stream

A licença pode ser carregada de um arquivo ou objeto de stream. Aspose.PDF para C++ tentará encontrar a licença nos seguintes locais:

1. Caminho explícito.
1. A pasta que contém Aspose.PDF.dll.
1. A pasta que contém o assembly que chamou Aspose.PDF.dll.
1. A pasta que contém o assembly de entrada (seu .exe).
1. Um recurso incorporado no assembly que chamou Aspose.PDF.dll.

A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo, sem um caminho, como mostrado no exemplo abaixo.

### Carregando uma Licença de Arquivo

A maneira mais fácil de aplicar uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar apenas o nome do arquivo sem um caminho.

{{% alert color="primary" %}}

Quando você chama o método SetLicense, o nome da licença que você passa deve ser o do arquivo de licença. Por exemplo, se você mudar o nome do arquivo de licença para "Aspose.PDF.lic.xml", passe esse nome de arquivo para o método Pdf->SetLicense(…).

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### Carregando uma Licença de um Objeto de Stream

O exemplo a seguir mostra como carregar uma licença a partir de um stream.

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## Licença Medida

Aspose.PDF permite que os desenvolvedores apliquem uma chave medida. É um novo mecanismo de licenciamento. O novo mecanismo de licenciamento será usado junto com o método de licenciamento existente. Aqueles clientes que desejam ser cobrados com base no uso das funcionalidades da API podem usar o licenciamento medido. Para mais detalhes, por favor, consulte a seção FAQ de Licenciamento Medido.

Uma nova classe Metered foi introduzida para aplicar a chave medida. Following is the sample code demonstrating how to set metered public and private keys.

A seguir está o exemplo de código demonstrando como definir chaves públicas e privadas medidas.

For more details, please refer to the [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) section.

Para mais detalhes, por favor, consulte a seção [Perguntas Frequentes sobre Licenciamento Medido](https://purchase.aspose.com/faqs/licensing/metered).