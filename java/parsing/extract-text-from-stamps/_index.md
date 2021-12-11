---
title: Extract Text From Stamps
type: docs
weight: 60
url: /java/extract-text-from-stamps/
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
