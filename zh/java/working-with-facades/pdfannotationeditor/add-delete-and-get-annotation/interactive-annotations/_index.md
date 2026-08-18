---
title: 使用 Java 的交互式注释
linktitle: 交互式注释
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: 了解如何使用 Java 在 PDF 文档中添加、检查和删除链接注释。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中使用交互式 PDF 注释
Abstract: 本文介绍如何使用 Java 处理 PDF 文件中的交互式链接注释。它包括定位文本、在匹配的文本区域上创建链接注释、读取现有链接注释以及删除它们。
---
## 添加链接注释

1. 加载源 PDF 文档并在第一页中搜索目标文本。
2. 使用匹配的文本矩形创建 `LinkAnnotation` 并分配目标 URI。
3. 将注释添加到页面并保存更新的 PDF。

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
