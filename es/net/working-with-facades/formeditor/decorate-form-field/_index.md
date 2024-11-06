---
title: Decorar Campo de Formulario en PDF
type: docs
weight: 20
url: es/net/decorate-form-field/
description: Esta sección explica cómo decorar un campo de formulario en PDF usando la clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Decorar un Campo de Formulario Particular en un Archivo PDF Existente

El método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) presente en la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) permite decorar un campo de formulario particular en un archivo PDF. Si desea decorar un campo en particular, entonces necesita pasar el nombre del campo a este método. Sin embargo, antes de llamar a este método, necesita crear objetos de las clases [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) y [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Necesita asignar el objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) a la propiedad [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) del objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Después de eso, puede establecer cualquier atributo proporcionado por el objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Una vez que haya establecido los atributos, puede llamar al método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) y finalmente guardar el PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).
El siguiente fragmento de código le muestra cómo decorar un campo de formulario en particular.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## Decorate All Fields of a Particular Type in an Existing PDF File

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) el método le permite decorar todos los campos de formulario de un tipo particular en un archivo PDF de una vez. If you want to decorate all fields of a particular type then you need to pass the field type to this method.  
Si deseas decorar todos los campos de un tipo particular, entonces necesitas pasar el tipo de campo a este método. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes.

Sin embargo, antes de llamar a este método, necesita crear objetos de las clases [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) y [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Necesitas asignar el objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) a la propiedad [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) del objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Después de eso, puedes establecer cualquier atributo proporcionado por el objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Una vez que hayas configurado los atributos, puedes llamar al método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) y finalmente guardar el PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). El siguiente fragmento de código te muestra cómo decorar todos los campos de un tipo particular.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```