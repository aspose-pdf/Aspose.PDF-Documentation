---
title: Button Fields and Images
type: docs
weight: 40
url: /java/button-fields-and-images/
description: Learn how to add an image appearance to a button field in a PDF form using the Form facade in Aspose.PDF for Java.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Add an image appearance to a PDF button field in Java
Abstract: This article shows how to use the Form facade in Aspose.PDF for Java to bind a PDF form, load an image as a stream, fill an image button field, and save the updated document.
---
The Java example in `FormExamples.addImageAppearanceToButtonField(...)` shows how to update a button field appearance with an image stream.

The workflow is straightforward:

- bind the input PDF with `form.bindPdf(...)`
- open the image file with `Files.newInputStream(...)`
- call `form.fillImageField(...)` for the button field
- save the updated PDF

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
