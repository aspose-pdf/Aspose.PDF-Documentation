---
title: Delete Images from PDF File using Java
linktitle: Delete Images
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Learn how to delete embedded images from PDF files in Java.
lastmod: "2026-05-27"
TechArticle: true
AlternativeHeadline: Delete embedded images from PDF files with Java
Abstract: This article shows how to delete images from PDF documents using Aspose.PDF for Java. The example removes an image resource from the first page by its index in the page image collection and then saves the modified document.
---
Use the page image resource collection when you need to remove embedded images from a PDF page.

## Delete an embedded image by index

1. Open the source PDF document and select the page that contains the image resource.
2. Delete the target image from the page resource collection by its index.
3. Save the updated PDF document after the image is removed.

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```

This removes the first image resource from page 1 of the document.
