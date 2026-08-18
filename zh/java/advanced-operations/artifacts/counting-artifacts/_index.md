---
title: 在 Java 中计算 PDF 工件数
linktitle: 计算文物
type: docs
weight: 40
url: /java/counting-artifacts/
description: 了解如何使用 Java 和 Aspose.PDF 检查和计算 PDF 文档中的分页工件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 计算 PDF 中的伪影
Abstract: 本文介绍如何使用 Aspose.PDF for Java 检查和计算 PDF 文档中的分页工件。它展示了如何迭代页面工件并计算水印、背景、页眉和页脚子类型。
---
## 计算页面上的分页工件数

当您需要快速计算页面上的主要分页工件子类型时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从目标 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 读取 [工件](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 集合。
1. 迭代页面 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 集合并计算需要报告的每个分页子类型。

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
