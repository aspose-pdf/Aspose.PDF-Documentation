---
title: Extract Data AcroForms
linktitle: Extract Data AcroForms
type: docs
weight: 30
url: /php-java/extract-form/
description: This section explains how to extract forms from your PDF document with Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Value from an Individual Field of PDF Document

The form field's [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) allows you to get the value of a particular field.

To get the value, get the form field from the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Form collection.

This example selects a [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) and retrieves its value using the [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Open a document
    $document = new Document($inputFile);

    // Get a field
    $textBoxField = $document->getForm()->get("textbox1");

    // Get the field name
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // Get the field value
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```

