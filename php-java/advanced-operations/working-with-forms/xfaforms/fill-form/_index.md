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

    // Load XFA form
    $document = new Document($inputFile);
    
    // Get names of XFA form fields
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Set field values        
    $document->getForm()->getXFA()->set_Item($names[0],"Field 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Field 1");
        
    // Save the updated document
    $document->save($outputFile);
    
    // Save modified PDF    
    $document->close();
```
