---
title: Decorate Form Field in PDF
type: docs
weight: 20
url: /net/decorate-form-field/
description: This section explains how to decorate Form Field in PDF using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Decorate a Particular Form Field in an Existing PDF File

[DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method present in [FormEditor](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/formeditor) class allows you to decorate a particular form field in a PDF file. If you want to decorate a particular field then you need to pass the field name to this method. However, before calling this method, you need to create objects of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. You also need to assign the [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://apireference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method and finally save the updated PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class.
The following code snippet shows you how to decorate a particular form field.

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

[DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method allows you to decorate all the form fields of a particular type in a PDF file at once. If you want to decorate all fields of a particular type then you need to pass the field type to this method. However, before calling this method, you need to create objects of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. You also need to assign the [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://apireference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method and finally save the updated PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to decorate all the fields of a particular type.


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




