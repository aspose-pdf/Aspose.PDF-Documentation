---
title: 使用 Java 从 PDF 文件中删除图像
linktitle: 删除图像
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: 了解如何使用 Java 从 PDF 文件中删除嵌入图像。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 删除 PDF 文件中嵌入的图像
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文档中删除图像。该示例通过页面图像集合中的索引从第一页中删除图像资源，然后保存修改后的文档。
---
当您需要从 PDF 页面中删除嵌入的图像时，请使用页面图像资源集合。

## 按索引删除嵌入图像

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)上的图片资源。
1. 通过索引从页面资源集合中删除目标图像。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
