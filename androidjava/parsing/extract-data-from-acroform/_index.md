---
title:  Extract data from AcroForm 
linktitle:  Extract data from AcroForm
type: docs
weight: 50
url: /androidjava/extract-data-from-acroform/
description: AcroForms exists in many PDF documents. This article aims to help you understand how to extract data from AcroForms with the Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract form fields from PDF document

Aspose.PDF for Android via Java not only lets you create and fill in form fields, but also makes it easy to extract form field data or form field information from PDF files.

Suppose we don't know the names of the form fields in advance. Then we should iterate over each page in PDF to extract information about all AcroForms in PDF as well as the values of the form fields. To get access to the form we need to use [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) method.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

If you do know the name of the form fields that you wish to extract values from then you can use indexer in Documents.Form collection to quickly retrieve this data.

## Retrieve form field value by title

The form field's Value property allows you to get the value of a particular field. To get the value, get the form field from the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [form field collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). This example selects a [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) and retrieves its value using the [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) method.

```java

    public void extractFormDataByName () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```

## Extract Data to XML from a PDF File

Form class allows you to export data to an XML file from the PDF file using ExportXml method. In order to export data to XML, you need to create an object of Form class and then call the ExportXml method using the FileStream object. Finally, you can close FileStream object and dispose Form object. The following code snippet shows you how to export data to XML file.

```java
public void extractFormFieldsToXML () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## Export Data to FDF from a PDF File

To export PDF forms data to XFDF file, we can use the [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) method in the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) class.

Please note, that it's a class from `com.aspose.pdf.facades`. Despite the similar name, this class has a slightly different purpose.

In order to export data to FDF, you need to create an object of `Form` class and then call the `exportXfdf` method using the `OutputStream` object. The following code snippet shows you how to export data to XFDF file.

```java
public void extractFormExportFDF () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Export Data to XFDF from a PDF File

To export PDF forms data to XFDF file, we can use the [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) method in the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) class.

In order to export data to XFDF, you need to create an object of `Form` class and then call the `exportXfdf` method using the `OutputStream` object. 
The following code snippet shows you how to export data to XFDF file.

```java
    public void extractFormExportXFDF () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
