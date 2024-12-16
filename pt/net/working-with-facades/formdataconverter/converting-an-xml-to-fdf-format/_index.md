---
title: Convertendo um XML para o formato FDF
type: docs
weight: 20
url: /pt/net/converting-an-xml-to-fdf-format/
description: Esta seção explica como você pode converter um XML para o formato FDF com FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

O namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) no [Aspose.PDF for .NET](/pdf/pt/net/) suporta muito bem AcroForms. Ele também suporta a importação e exportação de dados de formulário para diferentes formatos de arquivo como FDF, XFDF, e XML. No entanto, às vezes um desenvolvedor precisa converter um formato para outro. Neste artigo, vamos examinar o recurso que nos permite converter um formato FDF em XML.

{{% /alert %}}

## Detalhes

FDF significa Forms Data Format, e um arquivo FDF contém os valores do formulário em um par chave/valor. Sabemos também que o arquivo XML contém os valores como tags. Onde, na maioria das vezes, a chave é representada como o nome da tag e o valor é representado como o valor dentro dessa tag. Agora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) fornece a flexibilidade para converter um formato de arquivo XML em formato FDF.

Use a classe [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) para esse propósito. Esta classe fornece diferentes métodos para converter um formato de dados em outro. Este artigo mostra como usar um método, ConvertXmlToFdf(..), que recebe um arquivo FDF como uma entrada ou fluxo de origem e o salva no formato XML. O trecho de código a seguir mostra como converter um arquivo FDF em um arquivo XML.