---
title: 在 Java 中提取 PDF 的标记内容
linktitle: 提取标记内容
type: docs
weight: 20
url: /zh/java/extract-tagged-content-from-tagged-pdfs/
description: 了解如何使用 Aspose.PDF 在 Java 中检查标记的 PDF 内容，包括标记内容访问、根结构访问和子结构元素。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
当您需要检查标记 PDF 的逻辑结构树并检查或更新结构元素元数据时，请使用这些 API。

## 获取标记内容元数据

当您需要访问标记内容容器并希望定义基本文档元数据（例如标题和语言）时，请使用此示例。

1. 创建新 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从文档获取 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) 对象。
1. 设置已标记内容的元数据并保存输出文件。

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## 获取 Tagged PDF 的根结构

此示例显示了如何检查表示 Tagged PDF 的结构树的根对象。

1. 创建新 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并获取其标记内容。
1. 设置所需的文档元数据。
1. 读取并打印结构树根和逻辑根元素，然后保存文件。

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## 访问并更新子结构元素

当您需要遍历结构树中的子元素、检查其属性并更新选定的元数据时，请使用此示例。

1. 打开源 Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从结构树根读取子元素并打印可用的属性。
1. 访问第一个根子节点的子元素，更新它们的元数据，并保存文档。

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
