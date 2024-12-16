---
title: Justificar Texto em um Campo de Caixa de Texto
type: docs
weight: 20
url: /pt/net/justify-text-in-a-textbox-field/
description: Este artigo mostra como Justificar Texto em um Campo de Caixa de Texto usando a Classe Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Neste artigo, mostraremos como justificar texto em um campo de caixa de texto em um arquivo PDF.

{{% /alert %}}

## Detalhes da implementação

A classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) no [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) oferece a capacidade de decorar um campo de formulário PDF. Agora, se o seu requisito é justificar o texto em um campo de caixa de texto, você pode facilmente conseguir isso usando o valor [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) da enumeração [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) e chamando o método [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). No exemplo abaixo, primeiro vamos preencher um Campo de Caixa de Texto usando o método [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) da classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). Depois disso, usaremos a classe FormEditor para justificar o Texto no Campo de Caixa de Texto. O trecho de código a seguir mostra como justificar texto em um Campo de Caixa de Texto.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
Please note that a justificação alinhada não é suportada por PDF, por isso o texto ficará alinhado à esquerda quando você inserir o texto no Campo de Texto. Mas quando o campo não está ativo, o texto é justificado.