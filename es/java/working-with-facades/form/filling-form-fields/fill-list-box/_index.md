---
title: Fill List Box
linktitle: Fill List Box
type: docs
weight: 40
url: /java/fill-list-box/
description: Learn how to fill a list box field in a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Set a list box field value in a PDF form with Java
Abstract: This article shows how to bind a PDF form, set a list box field value, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Utilice `FormExamples.fillListBoxFields(...)` para completar un campo de cuadro de lista.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
