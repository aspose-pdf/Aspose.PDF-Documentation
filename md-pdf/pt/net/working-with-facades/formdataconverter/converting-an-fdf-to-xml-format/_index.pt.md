---
title: Convertendo um FDF para o formato XML
type: docs
weight: 10
url: /net/converting-an-fdf-to-xml-format/
description: Esta seção explica como você pode converter um FDF para o formato XML com a Classe FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

O namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) no [Aspose.PDF para .NET](/pdf/net/) suporta muito bem os AcroForms. Ele também suporta a importação e exportação de dados de formulário para diferentes formatos de arquivo, como FDF, XFDF e XML. No entanto, às vezes, os desenvolvedores podem precisar converter um formato em outro. Este artigo examina o recurso que converte FDF em XML.

{{% /alert %}}

## Detalhes

FDF significa Formato de Dados de Formulário, e um arquivo FDF contém os valores do formulário em um par chave/valor. Nós também sabemos que o arquivo XML contém os valores como tags. Onde, na maioria das vezes, a chave é representada como o nome da tag e o valor é representado como o valor dentro dessa tag. Agora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nos fornece a flexibilidade de converter um formato de arquivo FDF em um formato XML.

Podemos usar a classe [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) para este propósito. Esta classe nos fornece diferentes métodos para converter um formato de dados em outro formato. Neste artigo, usaremos apenas um método chamado [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Este método leva um arquivo FDF como entrada ou fluxo de origem e o salva no formato XML.

O trecho de código a seguir mostra como converter um arquivo FDF em um arquivo XML: