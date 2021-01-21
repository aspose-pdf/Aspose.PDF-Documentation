---
title: Working with Annotations - Facades
type: docs
weight: 30
url: /net/working-with-annotations-facades/
description: This section explains how to work with with Annotations - Facades using PdfAnnotationEditor Class.
lastmod: "2021-01-19"
draft: false
---

## Add Annotation in an Existing PDF File

[PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) allows you to add annotations of different types in an existing PDF file. You can use the respective method to add a particular annotation. For example, in the following code snippet, we have used [CreateFreeText](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method add [FreeText](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) type annotation. Any type of annotations can be added to the PDF file in the same way. First of all, you need to create an object of type [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)  and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Secondly, you have to create a Rectangle object to specify the area of the annotatation. After that, you can call [CreateFreeText](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method to add [FreeText](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) annotation, and then use [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file.

### Add FreeText Annotation

The following code snippet shows you how to add an annotation in a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-AddFreeTextAnnotation-AddFreeTextAnnotation.cs" >}}

### Create File Annotation without Icon

When adding a file annotation to PDF file, the createFileAttachment(..) method takes an argument to specify the icon that will be displayed for annotation. The values for Icon can be: "Graph", "PushPin", "Paperclip", "Tag". However if we need to add an annotation without an annotation, we can specify the opacity value for this icon (0 is complete transparent). Please try using the following code snippet to add a file annotation without any icon (in fact Icon is there but its transparent).



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-CreateFileAnnotation-CreateFileAnnotation.cs" >}}

## Delete All Annotations from an Existing PDF File

[PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) allows you delete all the annotations from the existing PDF file. First off, create a [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method to delete all the annotations from the file, and then use [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all the annotations from the PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-DeleteAllAnnotations-DeleteAllAnnotations.cs" >}}

## Delete All Annotations by Specified Type

You can use [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class to delete all the annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all annotations by specified annotation type.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-DeleteSpecificAnnotations-DeleteSpecificAnnotations.cs" >}}

## Update Annotations in an Existing PDF File

[PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class allows you to update annotation in an existing PDF file. First of all, create an object of [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class and bind PDF file. After that, create an object of particular annotation type; for example, in the following code snippet, we have used [FreeTextAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) object. The type of annotation object will depend upon the fact that which annotation type you want to update. Once you have created an object of a specific annotation type, you need to call [ModifyAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) method. Finally, save the updated document using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class. The following code snippet shows you how to update annotation in an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-UpdateAnnotations-UpdateAnnotations.cs" >}}

## Import Annotations from XFDF into PDF File

ImportAnnotationFromXfdf method allows you to import annotations to a PDF file. In order to import annotations, you need to create [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to create an enumeration of annotation types which you want to import to PDF file. You can then use ImportAnnotationFromXfdf method to import the annotations. And finally, save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object. The following code snippet shows you how to import annotations from XFDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-ImportAnnotations-ImportAnnotations.cs" >}}

## Export Annotations from PDF File to XFDF

The ExportAnnotationXfdf method allows you to export annotations from a PDF file. In order to export annotations, you need to create [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to create an enumeration of annotation types which you want to export from PDF file. You can then use ExportAnnotationXfdf method to import the annotations. And finally, save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object. The following code snippet shows you how to export annotations to XFDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-ExportAnnotations-ExportAnnotations.cs" >}}

## Extract Annotations from an Existing PDF File

[ExtractAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) method allows you to extract annotations from a PDF file. In order to extract annotations, you need to create [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to create an enumeration of annotation types which you want to extract from PDF file. You can then use [ExtractAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) method to extract the annotations to an ArrayList. After that, you can loop through this list and get individual annotations. And finally, save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object. The following code snippet shows you how to extract annotations from PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Annotations-ExtractAnnotations-ExtractAnnotations.cs" >}}



