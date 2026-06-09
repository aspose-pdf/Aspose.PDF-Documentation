---
title: Count PDF Artifacts in Java
linktitle: Counting Artifacts
type: docs
weight: 40
url: /java/counting-artifacts/
description: Learn how to inspect and count pagination artifacts in PDF documents using Java with Aspose.PDF.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Counting Artifacts in PDF using Java
Abstract: This article explains how to inspect and count pagination artifacts in PDF documents using Aspose.PDF for Java. It shows how to iterate through page artifacts and count watermark, background, header, and footer subtypes.
---
## Count pagination artifacts on a page

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read the [Artifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/artifact/) collection from the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Iterate through the page [Artifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/artifact/) collection and count each pagination subtype you need to report.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
