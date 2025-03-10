---
title:  Extract data from AcroForm 
linktitle:  Extract data from AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: AcroForms exists in many PDF documents. This article aims to help you understand how to extract data from AcroForms using Java and the Aspose.PDF.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extract data from AcroForms using the Aspose.PDF for Java
Abstract: The article provides a comprehensive guide on how to handle form fields within PDF documents using Aspose.PDF for Java. It describes methods to extract form field data, both when field names are known and unknown. For unknown field names, developers can iterate over each page to extract data, while known fields can be directly accessed using the indexer in the Document's Form collection. The article includes code snippets demonstrating how to retrieve form field values by title and export data to various formats, such as JSON, XML, FDF, and XFDF. It highlights the use of third-party libraries, like Gson, for JSON conversion, and explains how to use the `exportXml`, `exportFdf`, and `exportXfdf` methods for other formats, emphasizing the utility of the `com.aspose.pdf.facades.Form` class for these operations.
SoftwareApplication: java
---

## Extract form fields from PDF document

Aspose.PDF for Java not only lets you create and fill in form fields, but also makes it easy to extract form field data or form field information from PDF files.

Suppose we don't know the names of the form fields in advance. Then we should iterate over each page in PDF to extract information about all AcroForms in PDF as well as the values of the form fields. To get access to the form we need to use [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) method.

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // Get values from all fields
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Field Name :" + formField.getPartialName());
        System.out.println("Value : " + formField.getValue());
    }
}
```

If you do know the name of the form fields that you wish to extract values from then you can use indexer in Documents.Form collection to quickly retrieve this data.

## Retrieve form field value by title

The form field's Value property allows you to get the value of a particular field. To get the value, get the form field from the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [form field collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). This example selects a [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) and retrieves its value using the [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) method.

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```

## Extract form fields from PDF document to JSON

For export form data to JSON, we recommend using the 3rd party library like [Gson](https://github.com/google/gson).
Following snippets shows how to export `Name` and `Value` to JSON:

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

In this example we used an additional class

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```

## Extract Data to XML from a PDF File

Form class allows you to export data to an XML file from the PDF file using ExportXml method. In order to export data to XML, you need to create an object of Form class and then call the ExportXml method using the FileStream object. Finally, you can close FileStream object and dispose Form object. The following code snippet shows you how to export data to XML file.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // Open document
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // Create XML file.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // Export data
        form.exportXml(xmlOutputStream);

        // Close file stream
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // Close the document
    form.dispose();
    ;
}
```

## Export Data to FDF from a PDF File

To export PDF forms data to XFDF file, we can use the [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) method in the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) class.

Please note, that it's a class from `com.aspose.pdf.facades`. Despite the similar name, this class has a slightly different purpose.

In order to export data to FDF, you need to create an object of `Form` class and then call the `exportXfdf` method using the `OutputStream` object. The following code snippet shows you how to export data to XFDF file.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: handle exception
            e.printStackTrace();
        }

    }
```

## Export Data to XFDF from a PDF File

To export PDF forms data to XFDF file, we can use the [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) method in the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) class.

In order to export data to XFDF, you need to create an object of `Form` class and then call the `exportXfdf` method using the `OutputStream` object. 
The following code snippet shows you how to export data to XFDF file.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
```
