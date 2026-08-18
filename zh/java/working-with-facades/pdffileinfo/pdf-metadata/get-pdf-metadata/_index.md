---
title: 获取 PDF 元数据
linktitle: 获取 PDF 元数据
type: docs
weight: 20
url: /java/get-pdf-metadata/
description: 了解如何使用 PdfFileInfo 外观在 Java 中读取 PDF 元数据。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 检索 PDF 元数据。
Abstract: 了解如何使用 Aspose.PDF for Java 检索 PDF 元数据。 Java 示例读取标准字段，例如主题、标题、关键字、创建者、创建日期和修改日期，以及文件状态标志和自定义 `Reviewer` 元数据条目。
---
## 获取 PDF 元数据

此示例读取标准文档信息、文件状态标志和自定义元数据键。

### 步骤

1. 为源 PDF 创建一个 `PdfFileInfo` 对象。
2. 阅读标准元数据字段，例如主题、标题、关键字和创建者。
3. 检查文件状态标志，例如文件是否有效、已加密、受密码保护或组合。
4. 使用`getMetaInfo` 读取自定义元数据值。
5. 关闭`PdfFileInfo`实例。

### Java示例

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
