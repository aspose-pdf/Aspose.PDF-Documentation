---
title: Remove PDF Watermarks in Java
linktitle: Remove Watermarks
type: docs
weight: 90
url: /java/remove-watermarks/
description: Remove watermark artifacts from the first page of a PDF in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Watermarks in Java
Abstract: Remove watermark artifacts from the first page of a PDF in Java.
---
Remove watermark artifacts from the first page of a PDF in Java.

## Delete watermark artifacts

The example removes only artifacts of type `Pagination` and subtype `Watermark` from the first page. Visible watermarks stored as regular page text, images, or annotations remain in the PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the page artifact collection in reverse order.
1. Delete pagination artifacts whose subtype is watermark, then save the document.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Related artifact topics

- [Add Watermarks](/pdf/java/add-watermarks/)
- [Extract Watermark Details](/pdf/java/extract-watermarks/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
