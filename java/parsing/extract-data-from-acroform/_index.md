---
title:  Extract data from AcroForm using Java
linktitle:  Extract data from AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: AcroForms exists in many PDF documents. This article aims to help you understand how to extract data from AcroForms  using Java and the Aspose.PDF.
lastmod: "2021-02-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract form fields from PDF document

Aspose.PDF for Java not only lets you create and fill in form fields, but also makes it easy to extract form field data or form field information from PDF files.

Suppose we don't know the names of the form fields in advance. Then we should iterate over each page in PDF to extract information about all AcroForms in PDF as well as the values of the form fields.

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

If you do know the name of the form fields that you wish to extract values from then you can use indexer in Documents.Form collection to quickly retrieve this data. Look at the bottom of this article for a sample code on how to use that function.

## Retrieve form field value by title

The form field's Value property allows you to get the value of a particular field. To get the value, get the form field from the Document object’s Form collection. This example selects a TextBoxField and retrieves its value using the Value property.

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
        // Create xml file.
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

Form class allows you to export data to an FDF file from the PDF file using ExportFdf method. In order to export data to FDF, you need to create an object of Form class and then call the ExportFdf method using the FileStream object. Finally, you can save the PDF file using Save method of the Form class. The following code snippet shows you how to export data to FDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Open Document
form.BindPdf(dataDir + "input.pdf");

// Create fdf file.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Export data
form.ExportFdf(fdfOutputStream);

// Close file stream
fdfOutputStream.Close();

// Save updated document
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```

## Export Data to XFDF from a PDF File

Form class allows you to export data to an XFDF file from the PDF file using ExportXfdf method. In order to export data to XFDF, you need to create an object of Form class and then call the ExportXfdf method using the FileStream object. Finally, you can save the PDF file using Save method of the Form class. The following code snippet shows you how to export data to XFDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Open Document
form.BindPdf(dataDir + "input.pdf");

// Create xfdf file.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Export data
form.ExportXfdf(xfdfOutputStream);

// Close file stream
xfdfOutputStream.Close();

// Save updated document
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```
