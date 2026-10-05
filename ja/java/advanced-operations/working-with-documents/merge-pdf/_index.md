---
title: JavaでPDFファイルをマージする
linktitle: PDFファイルをマージする
type: docs
weight: 50
url: /ja/java/merge-pdf-documents/
description: Javaで複数のPDFファイルを単一のドキュメントに結合する方法を学びましょう。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで全体の文書、選択した範囲、および交互のページを結合します。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを結合する方法を説明します。2 つのファイルの結合、複数ドキュメントのマージ、ページ範囲の選択、特定の位置に別のドキュメントを挿入、ページを交互に配置、セクションブックマーク付きの結合出力の作成についてカバーしています。
---
Aspose.PDF for Javaは、出力の組み立て方法に応じて、いくつかのマージ戦略をサポートしています。

## 2つの PDF ドキュメントの結合

最もシンプルなマージフローが必要で、1つの完全なドキュメントを別のドキュメントに追加したい場合にこのアプローチを使用します。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクト。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 2番目の文書から1番目の文書へのコレクション。
1. 更新された PDF を保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

このヘルパーメソッドはページ範囲のマージロジックを一箇所にまとめ、他のサンプルが同じ検証済みコピー手順を再利用できるようにします。

1. ソースと宛先の PDF を開くまたは受け取る [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクト。
1. 要求されたページ範囲を正規化し、利用可能な範囲内に収めます。 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクション。
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

## 複数のPDFドキュメントを1つのファイルに結合する

入力ファイルのリストを順番に単一の出力ドキュメントに結合する必要がある場合は、このパターンを使用してください。

1. 空の出力 PDF を作成する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 各入力ファイルを1つずつ開き、その全体をコピーしてください [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲を出力ドキュメントに入れる。
1. すべてのソースファイルが処理された後、マージされた結果を保存してください。

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

## 2つのドキュメントから選択したページ範囲をマージする

この例では、各ソースドキュメントから特定のページ範囲のみを取得して、カスタム出力ファイルを作成します。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトと新しい出力ドキュメントを作成してください。
1. 必要なものだけ追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 各ソースドキュメントからの範囲です。
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

## あるPDF文書を別のPDFの特定の位置に挿入する

ある文書が別の文書の前後だけでなく、その中に表示されるべき場合にこのアプローチを使用します。

1. ベースと挿入された PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトと新しい出力ドキュメントを作成してください。
1. ベース文書の最初の部分をコピーし、次に挿入された文書全体を追加し、最後に残りのベース文書を追加します。 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲。
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

## ページを交互にして2つのPDF文書の結合

この例は2つのドキュメントからページを交互に差し込むもので、両方の入力がページ単位で最終出力に貢献すべき場合に便利です。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトと新しい出力ドキュメントを作成してください。
1. 利用可能な最大ページ数までループし、各利用可能ページを追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 最初と2番目の文書を順に。
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

## 区切りページとブックマークでドキュメントの結合

結合されたファイルがナビゲートしやすく、各ソースドキュメントの開始位置が明確に示されている必要がある場合に、このパターンを使用してください。

1. 空の出力 PDF を作成する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そして各ソースファイルを順に開いてください。
1. 区切り線を追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 見出しを付けてから、作成します [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) そのセクションのブックマーク。
1. ソースページを追加し、オプションで最初のコンテンツページを指すブックマークを追加し、最終的に結合されたドキュメントを保存してください。

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
