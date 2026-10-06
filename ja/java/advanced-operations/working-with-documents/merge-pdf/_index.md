---
title: "Java での PDF ファイルの結合"
linktitle: "PDF ファイルの結合"
type: docs
weight: 50
url: /ja/java/merge-pdf-documents/
description: Javaで複数のPDFファイルを単一のドキュメントに結合する方法を学びましょう。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java でのドキュメント全体、選択した範囲、および交互のページの結合"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを結合する方法を説明します。2 つのファイルの結合、複数ドキュメントのマージ、ページ範囲の選択、特定の位置に別のドキュメントを挿入、ページを交互に配置、セクションブックマーク付きの結合出力の作成についてカバーしています。
---
Aspose.PDF for Java は、出力の組み立て方法に応じて、複数のマージ戦略をサポートしています。

## 2 つの PDF ドキュメントの結合

最もシンプルなマージフローが必要で、1つの完全なドキュメントを別のドキュメントに追加したい場合に、このアプローチを使用してください。

1. 両方のソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトとして開いてください。
1. 2 番目のドキュメントの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクションを 1 番目のドキュメントに追加してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## 文書間で選択したページ範囲のコピー

このヘルパーメソッドは、ページ範囲のマージロジックを一か所にまとめ、他のサンプルが同じ検証済みのコピー手順を再利用できるようにします。

1. ソースと宛先の PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを開くか、既存のオブジェクトを受け取ってください。
1. 要求されたページ範囲を正規化し、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクションの有効な範囲内に収めてください。
1. 検証済みの範囲から各ページを宛先ドキュメントに追加してください。

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

## 複数の PDF ドキュメントの 1 つのファイルへの結合

入力ファイルのリストを順番に単一の出力ドキュメントに結合する必要がある場合は、このパターンを使用してください。

1. 出力用の空の PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを作成してください。
1. 各入力ファイルを 1 つずつ開き、その全 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲を出力ドキュメントにコピーしてください。
1. すべてのソースファイルの処理が完了した後、マージされた結果を保存してください。

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

## 2 つのドキュメントから選択したページ範囲の結合

この例では、各ソースドキュメントから特定のページ範囲のみを取得して、カスタム出力ファイルを作成します。

1. 両方のソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトとして開き、新しい出力ドキュメントを作成してください。
1. 各ソースドキュメントから必要な [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲のみを追加してください。
1. 組み立てられた出力ドキュメントを保存してください。

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

## 別の PDF の指定位置への PDF ドキュメントの挿入

ある文書が別の文書の前後だけでなく、その中に挿入される必要がある場合に、このアプローチを使用してください。

1. 挿入先と挿入する PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトとして開き、新しい出力ドキュメントを作成してください。
1. ベース文書の最初の部分をコピーし、次に挿入された文書全体を追加し、最後に残りのベース文書の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲を追加してください。
1. 再配置された結果を新しいファイルに保存してください。

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

## ページを交互に配置した 2 つの PDF ドキュメントの結合

この例では、2つのドキュメントからページを交互に差し込みます。両方の入力がページ単位で最終出力に貢献すべき場合に便利です。

1. 両方のソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトとして開き、新しい出力ドキュメントを作成してください。
1. 利用可能な最大ページ数までループし、各利用可能ページを [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトとして、最初の文書と2番目の文書から交互に追加してください。
1. インタリーブされた出力ドキュメントを保存してください。

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

## 区切りページとブックマークを使用したドキュメントの結合

結合されたファイルがナビゲートしやすく、各ソースドキュメントの開始位置が明確に示されている必要がある場合に、このパターンを使用してください。

1. 出力用の空の PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを作成し、各ソースファイルを順に開いてください。
1. 見出し付きの区切り用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、そのセクションの [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) ブックマークを作成してください。
1. ソースページを追加し、オプションで最初のコンテンツページを指すブックマークを追加した後、結合されたドキュメントを保存してください。

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
