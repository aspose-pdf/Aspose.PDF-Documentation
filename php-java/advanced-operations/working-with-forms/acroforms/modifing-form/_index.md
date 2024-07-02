---
title: Modifying AcroForms
linktitle: Modifying AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: This section explains how to modifying forms in your PDF document with Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Set Custom Form Field Font

Form fields in Adobe PDF files can be configured to use specific default fonts. Aspose.PDF allows developers to apply any font as a field default font, whether one of the 14 core fonts or a custom font.
To set and update the default font used for form fields, Aspose.PDF has the DefaultAppearance (Font font, double size, Color color) class. This class can be accessed using com.aspose.pdf.DefaultAppearance. To use this object, use the Field class' setDefaultAppearance(..) method.

The following code snippet shows you how to set the default font for PDF form field.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");

    // Create font object
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // Set the font information for form field
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // Save updated document
    $document->save($outputFile);
    $document->close();        

    $document->close();
```

## Get/Set FieldLimit

The FormEditor class SetFieldLimit method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // Getting maximum field limit using DOM
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

You can also get the same value using the Aspose.PDF.Facades namespace using the following code snippet.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");

    // Getting maximum field limit using DOM
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");

    // Delete field
    $field->delete();
    
    $document->close();
```
## Delete a Particular Form Field from a PDF Document

All the form fields are contained in the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Form collection. This collection provides different methods that manage form fields, including the delete method. If you want to delete a particular field, pass the field name as a parameter to the delete method and then save the updated PDF document.

The following code snippet shows how to delete a named field from a PDF document.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");

    // Delete field
    $field->delete();
    
    $document->close();
```

## Modify Form Field in a PDF Document

The [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Form collection allows you to manage form fields in a PDF document.

To modify a form field, get the field from the Form collection and set its properties. Then save the updated PDF document.

The following code snippet shows how to modify an existing form field in a PDF document.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");

    // Modify the field value
    $field->setValue("Updated Value");

    // Set the field as read only
    $field->setReadOnly(true);

    // Save the updated document
    $document->save($outputFile);        
    $document->close();
```

### Move Form Field to a New Location in a PDF File

If you want to move a form field to a new location on a PDF page, first get the field object and then specify a new value for its setRect method. A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) object with new coordinates is assigned to the setRect(..) method. Then save the updated PDF using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's save method.

The following code snippet shows you how to move a form field to a new location.

```php

    // Open a document
    $document = new Document($inputFile);

    // Get particular form field from document
    $field = $document->getForm()->get("textbox1");

    // Modify the field location
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // Save the updated document
    $document->save($outputFile);        
    $document->close();
```
