---
title: Obter Valor da Opção de Botão
type: docs
weight: 40
url: pt/net/get-button-option-value/
description: Esta seção explica como obter o Valor da Opção de Botão com Aspose.PDF Facades usando a Classe Form.
lastmod: "2021-06-05"
draft: false
---

## Obter Valores de Opção de Botão de um Arquivo PDF Existente

Os botões de rádio oferecem uma maneira de mostrar diferentes opções. A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) permite que você obtenha todos os valores de opção de botão para um determinado botão de rádio. Você pode obter esses valores usando o método [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Este método requer o nome do botão de rádio como parâmetro de entrada e retorna uma Hashtable. Você pode iterar através desta Hashtable para obter os valores das opções. O snippet de código a seguir mostra como obter os valores de opção de botão de um arquivo PDF existente.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## Obter Valor da Opção Atual do Botão de um Arquivo PDF Existente

Os botões de rádio fornecem uma maneira de definir valores de opção, no entanto, apenas um deles pode ser selecionado por vez. Se você deseja obter o valor da opção atualmente selecionada, pode usar o método [GetButtonOptionCurrentValue**. A classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fornece este método. O método [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) requer o nome do botão de rádio como parâmetro de entrada e retorna o valor como string. O seguinte trecho de código mostra como obter o valor da opção atual do botão de um arquivo PDF existente.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}