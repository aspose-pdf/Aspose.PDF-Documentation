---
title: 使用 Java 删除 PDF 文件中的图像
linktitle: 删除图像
type: docs
weight: 20
url: /zh/java/delete-images-from-pdf-file/
description: 了解如何在 Java 中删除 PDF 文件中的嵌入图像。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 删除 PDF 文件中的嵌入图像
Abstract: 本文展示了如何使用 Aspose.PDF for Java 删除 PDF 文档中的图像。示例通过在页面图像集合中的索引，从第一页移除图像资源，然后保存修改后的文档。
---
当需要从 PDF 页面中删除嵌入图像时，请使用页面图像资源集合。

## 通过索引删除嵌入的图像

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 访问目标上的图像资源 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 通过索引从页面资源集合中删除目标图像。
1. 保存已更新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
