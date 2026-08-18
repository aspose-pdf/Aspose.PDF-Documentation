---
title: 用 Java 分割 PDF 文件
linktitle: 分割 PDF 文件
type: docs
weight: 60
url: /java/split-pdf-document/
description: 了解如何使用 Java 将 PDF 页面拆分为单独的 PDF 文件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 按页面、范围、组和文件名模式拆分 PDF 文档
Abstract: 本文介绍如何使用 Aspose.PDF for Java 分割 PDF 文档。它涵盖拆分为单页、两部分或三部分、奇数页和偶数页、固定大小块、自定义范围、第一页或最后一页加上其余部分、自定义页面组和稳定的文件名生成。
---
Aspose.PDF for Java 支持除每个文件一页输出之外的多种分割模式。

## 将 PDF 拆分为单页文件

当每个源页面应成为单独的输出文档时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为要导出的每个[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将选定的[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到新文档中。
1. 保存每个输出的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## 将 PDF 拆分为两部分

此示例根据中点将源文档分为两个连续的输出文件。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 计算可用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 集合的中点。
1. 将前半页复制到一个输出文档中，将其余页面复制到另一个输出文档中。
1. 保存两个结果文档。

```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## 将 PDF 拆分为固定大小的页面组

当每个输出文件应包含相同数量的页面（可能除了最后一部分）时，请使用此模式。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 以 `pagesPerPart` 为组循环遍历 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 集合。
1. 为每个组创建一个新的输出文档，并将计算出的页面范围复制到其中。
1. 使用生成的文件名保存每个部分。

```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## 按自定义页面范围拆分 PDF

此示例允许您为每个输出文档定义明确的起始页和结束页。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 在数组或其他集合中定义所需的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 范围。
1. 根据源页数验证每个范围并将匹配的页面复制到新文档中。
1. 保存每个基于范围的输出文件。

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## 拆分第一页和其余页面

当封面页应与文档的其余部分分开导出时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并确认它包含页面。
1. 为第一个[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 创建一个输出文档。
1. 当有多个页面可用时，为剩余页面范围创建另一个文档。
1. 保存两个结果。

```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## 拆分最后一页和前面几页

此示例将最后一页与文档的其余部分分开，这对于提取摘要或签名页非常有用。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并检查它是否为空。
1. 将最后一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 复制到新的输出文档中。
1. 当较早的页面仍然存在时，从原始文档中删除该页面。
1. 将最后一页和其余页面保存为单独的文件。

```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## 将 PDF 拆分为三个部分

当文档应分为三个大小大致相等的连续部分时，请使用此模式。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并确定总页数。
1. 计算每个输出部分的大致大小。
1. 创建最多三个文档并复制匹配的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 范围。
1. 保存每个生成的部分。

```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## 将 PDF 拆分为自定义页面组

此示例演示如何从非连续页面集而不是连续范围构建输出文件。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 定义 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 数字的自定义组。
1. 为每个组创建一个新的输出文档，并仅添加该组中的有效页面。
1. 保存每个非空组文档。

```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## 将 PDF 拆分为具有稳定文件名的单页

当输出名称应保持词法可排序时（例如在自动化管道中），请使用此版本。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为每个[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 创建一个输出文档。
1. 使用零填充页码保存每个文件。

```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## 将 PDF 拆分为奇数页和偶数页

此示例通过根据页码奇偶性分隔页面来创建两个输出。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为奇数 [页](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 编号创建一个输出文档，为偶数页编号创建另一个输出文档。
1. 使用每个输出文档所需的增量迭代源页面。
1. 分别保存奇数页和偶数页结果。

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```
