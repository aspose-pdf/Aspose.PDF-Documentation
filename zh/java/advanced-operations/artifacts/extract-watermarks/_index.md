---
title: 在 Java 中提取 PDF 水印详细信息
linktitle: 提取水印详细信息
type: docs
weight: 50
url: /zh/java/extract-watermarks/
description: 在 Java 中读取 PDF 首页上水印工件的文本和边界矩形。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中提取水印详细信息
Abstract: 在 Java 中读取 PDF 首页上水印工件的文本和边界矩形。
---
在 Java 中读取 PDF 首页上水印工件的文本和边界矩形。

## 从 PDF 中提取水印工件

当您需要检查现有水印工件并读取其文本或位置时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 遍历目标页面的 artifact 集合。
1. 筛选水印分页工件，并输出其文本和边界矩形。

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

## 相关主题

- [添加水印](/pdf/zh/java/add-watermarks/)
- [删除水印](/pdf/zh/java/remove-watermarks/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
