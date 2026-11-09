---
title: Remove PDF Headers and Footers in Java
linktitle: Remove Headers and Footers
type: docs
weight: 110
url: /java/remove-headers-footers/
description: Remove header and footer artifacts from the first page of a PDF in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Headers and Footers in Java
Abstract: Remove header and footer artifacts from the first page of a PDF in Java.
---
Remove header and footer artifacts from the first page of a PDF in Java.

## Delete header and footer artifacts

Use this approach when existing header and footer artifacts should be removed from the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the page artifact collection in reverse order.
1. Delete pagination artifacts whose subtype is header or footer, then save the document.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Related artifact topics

- [Add Headers and Footers](/pdf/java/artifacts-header-footer/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
