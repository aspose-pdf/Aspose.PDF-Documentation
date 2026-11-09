---
title: 在 Java 中统计 PDF 工件
linktitle: 计数工件
type: docs
weight: 40
url: /zh/java/counting-artifacts/
description: 了解如何使用 Java 与 Aspose.PDF 检查并计数 PDF 文档中的分页工件。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 计数 PDF 工件
Abstract: 本文解释了如何使用 Aspose.PDF for Java 检查并计数 PDF 文档中的分页工件。它展示了如何遍历页面工件并计数水印、背景、页眉和页脚子类型。
---
## 在页面上计数分页工件

当您需要快速统计页面上主要分页工件子类型时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 读取目标页面 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 的 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 集合。
1. 遍历页面的 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 集合，并按需要报告的分页子类型统计工件数量。

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

## 相关主题

- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
- [提取水印详情](/pdf/zh/java/extract-watermarks/)
- [移除背景](/pdf/zh/java/remove-backgrounds/)
- [移除水印](/pdf/zh/java/remove-watermarks/)
- [移除 Bates 编号](/pdf/zh/java/remove-bates-numbering/)
- [删除页眉和页脚](/pdf/zh/java/remove-headers-footers/)
