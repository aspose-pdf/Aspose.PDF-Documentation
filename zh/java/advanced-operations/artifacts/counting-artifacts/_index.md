---
title: 使用 Java 统计 PDF 工件
linktitle: 统计工件
type: docs
weight: 40
url: /zh/java/counting-artifacts/
description: 学习如何使用 Java 与 Aspose.PDF 检查并统计 PDF 文档中的分页工件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 统计 PDF 中的工件
Abstract: 本文解释了如何使用 Aspose.PDF for Java 检查并统计 PDF 文档中的分页工件。它展示了如何遍历页面工件并统计水印、背景、页眉和页脚子类型。
---
## 统计页面上的分页工件

当您需要快速统计页面上主要分页工件子类型时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 读取 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 从目标的集合 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 遍历页面 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 收集并统计您需要报告的每种分页子类型。

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
