---
title: Delete Annotations (facades)
type: docs
weight: 10
url: /java/delete-annotations/
description: This section explains how to delete annotations with Aspose.PDF Facades using PdfAnnotationEditor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

You can use [PdfAnnotationEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor) class to delete  annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a [PdfAnnotationEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor) object and bind input PDF file using bindPdf method. After that, call [deleteAnnotations](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use save method to save the updated PDF file.

The following code snippet shows you how to delete annotation by specified annotation type.

```java
public static void DeleteAnnotation() {
        // Open document
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("Please enter number:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // Save updated PDF
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
    
  [PdfAnnotationEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) allows you delete all the annotations from the existing PDF file.
  
  First off, create a [PdfAnnotationEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor)  and bind input PDF file using BindPdf method. 
  
  After that, call [deleteAnnotations](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) method, to delete all the annotations from the file, and then use Save method to save the updated PDF file. The following code snippet shows you how to delete all the annotations from the PDF file.

    ```java
 public static void DeleteAllAnnotations() {
        // Open document
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        // Delete all annoations
        annotationEditor.deleteAnnotations();
        // Save updated PDF
        annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
    }
    ```
