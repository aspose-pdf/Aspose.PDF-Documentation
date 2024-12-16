---
title: Identificación de nombres de campos de formulario
type: docs
weight: 10
url: /es/net/identifying-form-fields-names/
description: Aspose.PDF.Facades te permite identificar nombres de campos de formulario usando la clase Form.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF para .NET](/pdf/es/net/) proporciona la capacidad de crear, editar y completar formularios PDF ya creados. El espacio de nombres [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) contiene la clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), que contiene la función llamada [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) y toma dos argumentos, es decir, nombre del campo y valor del campo. Por lo tanto, para completar los campos del formulario, debes conocer el nombre exacto del campo del formulario.

## Detalles de implementación

A menudo nos encontramos con un escenario donde necesitamos llenar el formulario que se ha creado en alguna herramienta, es decir, Adobe Designer, y no estamos seguros sobre los nombres de los campos del formulario. Entonces, para completar los campos del formulario, primero necesitamos leer los nombres de todos los campos del formulario en PDF. La clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) proporciona la propiedad llamada [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) que devuelve todos los nombres de los campos y devuelve null si el PDF no contiene ningún campo. Sin embargo, al usar esta propiedad, obtenemos los nombres de todos los campos en el formulario PDF y podríamos no estar seguros de qué nombre corresponde a qué campo en el formulario.

Como solución a este problema, utilizaremos los atributos de apariencia de cada campo. Form class tiene una función llamada [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) que devuelve atributos, incluyendo ubicación, color, estilo de borde, fuente, elemento de lista y así sucesivamente. Para guardar estos valores necesitamos usar la clase [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), que se utiliza para registrar los atributos visuales de los campos. Una vez que tenemos estos atributos, podemos añadir un campo de texto debajo de cada campo que mostraría el nombre del campo.

{{% alert color="primary" %}}
En este punto, surge la pregunta "¿cómo determinaríamos la ubicación donde agregar el campo de texto?"
{{% /alert %}}

{{% alert color="primary" %}}
La solución a este problema es la propiedad Box en la clase [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), que contiene la ubicación del campo. Necesitamos guardar estos valores en un array de tipo rectángulo y usar estos valores para identificar la posición donde agregar los nuevos campos de texto.

{{% /alert %}}

En el espacio de nombres [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) tenemos una clase llamada [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) que proporciona la capacidad de manipular formularios PDF. Abra un formulario PDF; agregue un campo de texto debajo de cada campo de formulario existente y guarde el formulario PDF con un nuevo nombre.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-IdentifyFormFields-IdentifyFormFields.cs" >}}