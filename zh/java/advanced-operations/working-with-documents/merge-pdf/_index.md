---
title: 在 Java 中合并 PDF 文件
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /zh/java/merge-pdf-documents/
description: 了解如何在 Java 中将多个 PDF 文件合并为单个文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 合并完整文档、选定范围和交错页面
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 合并 PDF 文档。内容包括合并两个文件、合并多个文档、选择页码范围、将一个文档插入到另一个文档的特定位置、交替页合并，以及使用章节书签构建合并输出。
---
Aspose.PDF for Java 支持多种合并策略，具体取决于应如何组装输出。

## 合并两个 PDF 文档

当您需要最简单的合并流程并希望将一个完整文档追加到另一个文档时，请使用此方法。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 添加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 从第二个文档收集到第一个文档。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## 在文档之间复制选定的页面范围

此辅助方法将页面范围合并逻辑集中在一个位置，以便其他示例可以复用相同的已验证复制例程。

1. 打开或接收源和目标 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 规范化请求的页码范围，使其保持在可用范围内 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 集合。
1. 将验证范围内的每一页添加到目标文档。

```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## 将多个 PDF 文档合并为一个文件

当您需要按顺序将一系列输入文件合并为单个输出文档时，请使用此模式。

1. 创建一个空的输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 一次打开一个输入文件并复制其完整内容 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 将范围写入输出文档。
1. 在处理完所有源文件后，保存合并结果。

```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## 合并两个文档中选定的页面范围

此示例通过仅从每个源文档中获取特定页范围来创建自定义输出文件。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象并创建一个新的输出文档。
1. 仅添加必需的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 每个源文档的范围。
1. 保存已组装的输出文档。

```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## 在特定位置将一个 PDF 文档插入到另一个 PDF 文档中

当一个文档应出现在另一个文档内部，而不是仅仅在其前后时，请使用此方法。

1. 打开基准 PDF 和插入的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象并创建一个新的输出文档。
1. 复制基础文档的第一部分，然后追加完整的插入文档，最后追加剩余的基础文档 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 范围。
1. 将重新排序的结果保存为新文件。

```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## 将两个 PDF 文档的页面交替合并

此示例交叉插入两个文档的页面，当两个输入都应逐页贡献到最终输出时，这非常有用。

1. 打开两个源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象并创建一个新的输出文档。
1. 遍历最大可用页数并添加每个可用的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 依次从第一个和第二个文档。
1. 保存交错输出文档。

```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## 合并文档，包含分隔页和书签

当合并文件需要保持易于导航，并清晰显示每个源文档的起始位置时，请使用此模式。

1. 创建一个空的输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并依次打开每个源文件。
1. 添加带有标题的分隔页 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)，然后创建一个 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) 作为该部分的书签。
1. 追加源页面，可选地添加指向第一个内容页面的书签，并保存最终合并的文档。

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```
