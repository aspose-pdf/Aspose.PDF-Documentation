---
title: Extract Text From Stamps
type: docs
weight: 60
url: /php-java/extract-text-from-stamps/
description: Discover how to extract text from stamps in PDFs using Aspose.PDF for PHP Java. Achieve accurate text retrieval effortlessly.
---

## Extract Text from Stamp Annotations

Aspose.PDF for PHP via Java lets you extract text from stamp annotations. In order to extract text from Stamp Annotations in a PDF, the following steps can be used.

1. Load the PDF document
1. Get the desired page of the document
1. Create a new instance of the StampAnnotation class
1. Create a new instance of the AnnotationSelector class and pass the stamp annotation to it
1. Accept the annotation selector on the page
1. Get the selected stamp annotations
1. Create a new instance of the TextAbsorber class
1. Get the first stamp annotation
1. Get the normal appearance of the stamp annotation
1. Visit the appearance using the text absorber
1. Get the extracted text from the text absorber
1. Close the document

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```
