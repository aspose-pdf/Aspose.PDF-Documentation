---
title: Convert XFA Form to AcroForm
linktitle: Convert XFA Form
type: docs
weight: 10
url: /php-java/convert-form/
description: This section explains how to convert XFA Form to AcroForm with Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convert Dynamic XFA Form to Standard AcroForm

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. It can also convert dynamic XFA form to standard Acroform. The information about the form (as far as PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering. The objects of XFA form are drawn at the time loading the document.

Currently PDF supports two different methods for integrating data and PDF forms:

- AcroForms (also known as Acrobat forms), introduced and included in the PDF 1.2 format specification.

- Adobe XML Forms Architecture (XFA) forms, introduced in the PDF 1.5 format specification as an optional feature. (The XFA specification is not included in the PDF specification, it is only referenced.)

It's not possible to extract or manipulate pages of XFA Forms, because the form content is generated at runtime (during XFA form viewing) within the application trying to display or render the XFA form. Aspose.PDF has a feature that allows developers to convert XFA forms to standard AcroForms.

```php

        // Load XFA form
        $document = new Document($inputFile);
        
        // Set the form fields type as standard AcroForm
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // Save the updated document
        $document->save($outputFile);
        
        // Save modified PDF    
        $document->close();
```