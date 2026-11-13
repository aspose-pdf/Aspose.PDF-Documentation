---
title: Extract PDF Watermark Details in Java
linktitle: Extract Watermark Details
type: docs
weight: 50
url: /java/extract-watermarks/
description: Read the text and bounding rectangle of watermark artifacts on the first page of a PDF in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract Watermark Details in Java
Abstract: Read the text and bounding rectangle of watermark artifacts on the first page of a PDF in Java.
---
Read the text and bounding rectangle of watermark artifacts on the first page of a PDF in Java.

## Extract watermark artifacts from a PDF

Use this example when you need to inspect existing watermark artifacts and read their text or position.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the artifact collection of the target page.
1. Filter watermark pagination artifacts and print their text and rectangles.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Related artifact topics

- [Add Watermarks](/pdf/java/add-watermarks/)
- [Remove Watermarks](/pdf/java/remove-watermarks/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
