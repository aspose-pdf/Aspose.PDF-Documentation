---
title: Apariencia y atributos del campo
type: docs
weight: 20
url: /net/changing-field-appearance-and-attributes/
description: Esta sección explica cómo puede cambiar la apariencia y los atributos del campo con la clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

La clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) del [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) le permite no solo cambiar el aspecto y la sensación del campo del formulario, sino también el comportamiento del campo. En este artículo, veremos cómo podemos usar la clase FormEditor para cambiar la apariencia del campo, los atributos del campo y también el límite del campo.

{{% /alert %}}

## Detalles de implementación

El método [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) se utiliza para cambiar la apariencia de un campo de formulario. Toma AnnotationFlag como un parámetro. AnnotationFlag es una enumeración que tiene diferentes miembros como Hidden o NoRotate, etc.

El método [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) se utiliza para cambiar el atributo de un campo de formulario. Un parámetro pasado a este método es la enumeración PropertyFlag que contiene miembros como ReadOnly o Required, etc.

La clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) también proporciona un método para establecer el límite del campo. Le indica al campo cuántos caracteres se pueden completar. El siguiente fragmento de código muestra cómo se pueden utilizar todos estos métodos.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}