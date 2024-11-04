---
title: Justificar Texto en un Campo de Cuadro de Texto
type: docs
weight: 20
url: /net/justify-text-in-a-textbox-field/
description: Este artículo te muestra cómo justificar texto en un campo de cuadro de texto usando la clase Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

En este artículo, te mostraremos cómo justificar texto en un campo de cuadro de texto en un archivo PDF.

{{% /alert %}}

## Detalles de implementación

La clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) en el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ofrece la capacidad de decorar un campo de formulario PDF. Ahora, si su requisito es justificar el texto en un campo de cuadro de texto, puede lograrlo fácilmente usando el valor [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) de la enumeración [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) y llamando al método [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). En el siguiente ejemplo, primero llenaremos un campo de cuadro de texto utilizando el método [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) de la clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). Después de eso, utilizaremos la clase FormEditor para justificar el texto en el campo del cuadro de texto. El siguiente fragmento de código le muestra cómo justificar texto en un campo de cuadro de texto.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
Por favor, tenga en cuenta que la alineación justificada no es compatible con PDF, por eso el texto se alineará a la izquierda cuando ingrese el texto en el Campo de Texto. Pero cuando el campo no está activo, el texto está justificado.