---
title: Remove PDF Bates Numbering in Java
linktitle: Remove Bates Numbering
type: docs
weight: 100
url: /java/remove-bates-numbering/
description: Remove Bates numbering from all pages of a PDF in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Bates Numbering in Java
Abstract: Remove Bates numbering from all pages of a PDF in Java.
---
Remove Bates numbering from all pages of a PDF in Java.

## Delete Bates numbering

Use this approach when existing Bates numbering artifacts should be removed from the document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Call the page collection helper that deletes Bates numbering.
1. Save the cleaned output file.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## Related artifact topics

- [Add Bates Numbering](/pdf/java/add-bates-numbering/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
