---
title: Remove PDF Backgrounds in Java
linktitle: Remove Backgrounds
type: docs
weight: 80
url: /java/remove-backgrounds/
description: Remove background artifacts from the first page of a PDF in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Backgrounds in Java
Abstract: Remove background artifacts from the first page of a PDF in Java.
---
Remove background artifacts from the first page of a PDF in Java.

## Remove background artifacts

Use this approach when existing background artifacts should be deleted from the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the page artifact collection in reverse order.
1. Delete artifacts whose type is pagination and subtype is background, then save the document.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Related artifact topics

- [Add Backgrounds](/pdf/java/add-backgrounds/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
