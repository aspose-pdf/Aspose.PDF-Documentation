---
title: Fill AcroForms
linktitle: Fill AcroForms
type: docs
weight: 20
url: /php-java/fill-form/
description: This section explains how to fill form field in a PDF document with Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF documents are wonderful, and really the preferred file type, for creating Forms.

Aspose.PDF for PHP via Java allows you to fill a form field, get the field from the Document object’s Form collection.

Let's look at the following example how to resolve this task:

```php

    // Open document
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // Get a field    
    $textBoxField = $document->getForm()->get("textbox1");

    // Modify field value
    $textBoxField->setValue("Value to be filled in the field");
        
    // Save updated document
    $document->save($outputFile);
    $document->close();
```
