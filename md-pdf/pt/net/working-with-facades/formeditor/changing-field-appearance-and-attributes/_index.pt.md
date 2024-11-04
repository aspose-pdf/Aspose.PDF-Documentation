---
title: Aparência e atributos do campo
type: docs
weight: 20
url: /net/changing-field-appearance-and-attributes/
description: Esta seção explica como você pode alterar a aparência e os atributos do campo com a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

A classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) permite não apenas mudar a aparência do campo do formulário, mas também o comportamento do campo. Neste artigo, veremos como podemos usar a classe FormEditor para mudar a aparência do campo, os atributos do campo e também o limite do campo.

{{% /alert %}}

## Detalhes de implementação

O método [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) é usado para mudar a aparência de um campo de formulário. Ele leva AnnotationFlag como um parâmetro. AnnotationFlag é uma enumeração que possui diferentes membros como Hidden ou NoRotate etc.

O método [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) é usado para mudar o atributo de um campo de formulário. Um parâmetro passado para este método é a enumeração PropertyFlag que contém membros como ReadOnly ou Required etc.

A classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) também fornece um método para definir o limite do campo. Ele informa ao campo quantos caracteres ele pode ser preenchido. O trecho de código abaixo mostra como todos esses métodos podem ser usados.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}