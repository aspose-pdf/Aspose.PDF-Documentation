---
title: Extract Text From Stamps
type: docs
weight: 60
url: /java/extract-text-from-stamps/
description: Learn how to extract text from stamps in PDF files using Aspose.PDF for Java. Follow this guide for precise text retrieval.
TechArticle: true 
AlternativeHeadline: How to Extract Text From Stamps with Aspose.PDF for Java 
Abstract: The article provides a guide on using Aspose.PDF for Java to extract text from stamp annotations in a PDF document. The process involves creating a `Document` class object to access the PDF, retrieving the desired annotation from a specific page, and using a `TextAbsorber` class to capture the text. The article includes a Java code snippet demonstrating these steps, where a `StampAnnotation` is identified and its normal appearance is visited to extract and print the text content. This method enables efficient text extraction from specific annotations within a PDF using Aspose.PDF for Java.
SoftwareApplication: java
---

## Extract Text from Stamp Annotations

Aspose.PDF for Java lets you extract text from stamp annotations. In order to extract text from Stamp Annotations in a PDF, the following steps can be used.

1. Create a Document class object
1. Get the desired Annotation from list of annotations of a page
1. Define a new object of TextAbsorber class
1. Use the TextAbsorber's visit method to get the Text

```java
Document doc = new Document(dataDir+"test.pdf");
Annotation item = doc.getPages().get_Item(1).getAnnotations().get_Item(3);
if (item instanceof StampAnnotation ) {
   StampAnnotation annot = (StampAnnotation) item;
   TextAbsorber ta = new TextAbsorber();
   XForm ap = annot.getNormalAppearance();
   ta.visit(ap);
   System.out.println(ta.getText());
}
```
