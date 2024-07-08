---
title:  Extract data from AcroForm 
linktitle:  Extract data from AcroForm
type: docs
weight: 50
url: /php-java/extract-data-from-acroform/
description: AcroForms exists in many PDF documents. This article aims to help you understand how to extract data from AcroForms using PHP and the Aspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract form fields from PDF document

Aspose.PDF for PHP not only lets you create and fill in form fields, but also makes it easy to extract form field data or form field information from PDF files.

Suppose we don't know the names of the form fields in advance. Then we should iterate over each page in PDF to extract information about all AcroForms in PDF as well as the values of the form fields. To get access to the form we need to use [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) method.

```php

    // Create a new instance of the License class and set the license file
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Set the path to the directory containing the PDF document
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // Set the path to the input PDF file
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // Set the response header to indicate that the response will be in JSON format
    header('Content-Type: application/json; charset=utf-8');

    // Initialize the response data variable
    $responseData = "";

    try {
        // Create a new instance of the Document class and load the input PDF file
        $document = new Document($inputFile);

        // Get the form fields from the document and convert them to PHP values
        $fields = java_values($document->getForm()->getFields());

        // Loop through each form field and extract the field name and value
        foreach ($fields as $formField) {
            // Concatenate the field name and value to the response data
            $responseData = $responseData . "(Field Name: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Value: " . $formField->getValue() . "),";
        }

        // Close the document
        $document->close();
    }
```

If you do know the name of the form fields that you wish to extract values from then you can use indexer in Documents.Form collection to quickly retrieve this data.

## Extract Data to XML from a PDF File

Form class allows you to export data to an XML file from the PDF file using ExportXml method. In order to export data to XML, you need to create an object of Form class and then call the ExportXml method using the FileStream object. Finally, you can close FileStream object and dispose Form object. The following code snippet shows you how to export data to XML file.

```php

    // Open document
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Create a FileOutputStream object to write the font file.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // Export data
    $form->exportXml($xmlOutputStream);

    // Close file stream
    $xmlOutputStream->close();

    // Close the document
    $form->close();
```

## Export Data to FDF from a PDF File

To export PDF forms data to XFDF file, we can use the [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) method in the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) class.

Please note, that it's a class from `com.aspose.pdf.facades`. Despite the similar name, this class has a slightly different purpose.

In order to export data to FDF, you need to create an object of `Form` class and then call the `exportXfdf` method using the `OutputStream` object. The following code snippet shows you how to export data to XFDF file.

```php

    // Open document
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Create a FileOutputStream object to write the font file.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // Export data
    $form->exportFdf($xmlOutputStream);

    // Close file stream
    $xmlOutputStream->close();

    // Close the document
    $form->close();
```

## Export Data to XFDF from a PDF File

To export PDF forms data to XFDF file, we can use the [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) method in the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) class.

In order to export data to XFDF, you need to create an object of `Form` class and then call the `exportXfdf` method using the `OutputStream` object. 
The following code snippet shows you how to export data to XFDF file.

```php

    // Open document
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Create a FileOutputStream object to write the font file.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // Export data
    $form->exportXfdf($xmlOutputStream);

    // Close file stream
    $xmlOutputStream->close();

    // Close the document
    $form->close();
```
