---
title: Working with Form Fields
type: docs
weight: 60
url: /net/working-with-form-fields/
description: This topic explains how to work with Form Fields with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-01-19"
draft: false
---

In order to fill the form fields in an existing PDF file, you need to use [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/form) class. This class provides [FillField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) method which allows you to fill different fields. For example, you can either fill a text field using this method or set check box and combo box values. First of all, you need to create an object of Form class with input and output PDF file parameters, and then call the [FillField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) method. You can use [FillImageField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillimagefield) method to fill image fields. After that, you need to call [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save) method to save the output PDF file. The following code snippet shows you how to fill form fields in an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-FillFormFieldF-FillFormFieldF.cs" >}}

## Get Form Field Facade Values from Existing PDF File

[FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) represents a class to record visual attributes of a field, including the following information: border style, width, border color, background color, font, font size, caption, text color, text alignment, and text rotation. If you want to get the visual attributes of a field, you can use [GetFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) method of [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/form) class. This method returns an object of [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) class. You can use this object to get all the visual attributes of the form field. The following code snippet shows you how to get form field facade values from existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetFormFieldValue-GetFormFieldValue.cs" >}}

## Add Form Field in an Existing PDF file

In order to add a form field in an existing PDF file, you need to use [AddField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. This method requires you to specify the type of the field you want to add along with the name and location of the field. You need to create an object of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class, use [AddField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) method to add a new field in the PDF, and finally use [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method to save the updated PDF file. The following code snippet shows you how to add form field in an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-AddFormField-AddFormField.cs" >}}

## Delete Form Field from an Existing PDF File

In order to delete a form field from an existing PDF file, you can use [RemoveField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. This method takes only one argument: field name. You need to create an object of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class, call [RemoveField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) method to remove a particular field from the PDF and then call the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method to save the updated PDF file. The following code snippet shows you how to delete form fields from an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-DeleteField-DeleteField.cs" >}}

## Move Form Field to a New Location in Existing PDF File

If you want to move a form field to a new location then you can use [MoveField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. You only need to provide the field name and new location of this field to the [MoveField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) method. You also need to save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to move a form field in a new location in a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-MoveField-MoveField.cs" >}}

## Get Value of a Form Field from a PDF Document

In order to get value of a form field, you need to create object of [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/form) class and call [GetField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfield) method. [GetField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfield) method takes field name as input and returns its value as string.
The following code snippet shows you how to get value of a form field.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetFieldValue-GetFieldValue.cs" >}}

## Flatten All Fields in an Existing PDF File

[FlattenAllFields](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/flattenallfields) method of the [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/form) class allows you to flatten all the fields of the PDF form. You first need to create [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form) object with input and output PDF files and then call the [FlattenAllFields](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/flattenallfields) method and finally save the updated PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method. The following code snippet shows you how to flatten all the fields of the PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-FlattenAllFields-FlattenAllFields.cs" >}}

## Fill Form fields using DataTable

Aspose.PDF for .NET provides great capabilities for create/manipulating form fields inside PDF document. Using this API, you can programmatically fill form fields inside PDF file, fill form fields by [Import Data from FDF into a PDF File ](/pdf/net/import-and-export-data/), [Import Data from XFDF into a PDF File](/pdf/net/import-and-export-data/), [Import Data from XML into a PDF File](/pdf/net/import-and-export-data/) or even you can import data from [System.Data.DataTable](https://apireference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) object. If we have a requirement to fill forms fields using data from database/data-source, we can export the data to DataTable and then use [ImportDataTable(..)](https://apireference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) method of [Aspose.Pdf.Facades.AutoFiller](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) class.

## Decorate a Particular Form Field in an Existing PDF File

[DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method present in [FormEditor](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/formeditor) class allows you to decorate a particular form field in a PDF file. If you want to decorate a particular field then you need to pass the field name to this method. However, before calling this method, you need to create objects of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. You also need to assign the [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://apireference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method and finally save the updated PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class.
The following code snippet shows you how to decorate a particular form field.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-DecorateParticularField-DecorateParticularField.cs" >}}

### Set Form Field Font other than 14 core PDF fonts

In order to set the font, a new property [CustomFont](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/properties/customfont) is added in [FormFieldFacade](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/formfieldfacade) class.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-DecorateParticularField-SetFont.cs" >}}

## Decorate All Fields of a Particular Type in an Existing PDF File

[DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method allows you to decorate all the form fields of a particular type in a PDF file at once. If you want to decorate all fields of a particular type then you need to pass the field type to this method. However, before calling this method, you need to create objects of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. You also need to assign the [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://apireference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method and finally save the updated PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to decorate all the fields of a particular type.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-DecorateFields-DecorateFields.cs" >}}
