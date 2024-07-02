---
title: Extract XFA Form
linktitle: Extract XFA Form
type: docs
weight: 30
url: /php-java/extract-form/
description: This section explains how to extract forms from your PDF document with Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Value from an Form Field of PDF Document

The form field's [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) allows you to get the value of a particular field.

To get the value, get the form field from the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Form collection.

This example selects a [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) and retrieves its value using the [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Load XFA form
    $document = new Document($inputFile);
    
    // Get names of XFA form fields
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Get field values
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // Save modified PDF    
    $document->close();
```

