---
title: "Java での PDFファイルの分割"
linktitle: "PDFファイルの分割"
type: docs
weight: 60
url: /ja/java/split-pdf-document/
description: JavaでPDFページを個別のPDFファイルに分割する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用して、ページ、範囲、グループ、ファイル名パターンでPDF文書を分割します
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを分割する方法を説明します。単一ページへの分割、2 部または 3 部への分割、奇数ページと偶数ページ、固定サイズのチャンク、カスタム範囲、最初または最後のページと残り、カスタムページグループ、および安定したファイル名生成について取り上げます。
---
Aspose.PDF for Java は、1 ページごとのファイル出力以外にも、いくつかの分割パターンをサポートしています。

## PDF を単一ページのファイルに分割する

各ソースページを別々の出力ドキュメントにする必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 新しい PDF を作成する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) それぞれ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) エクスポートしたいです。
1. 選択した項目を追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 新しい文書へ。
1. 各出力PDFを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

## PDF を2つの部分に分割する

この例では、ソースドキュメントを中点に基づいて2つの連続した出力ファイルに分割します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 利用可能なものの中点を計算する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクション。
1. ページの前半を1つの出力ドキュメントにコピーし、残りのページを別のドキュメントにコピーしてください。
1. 両方の結果ドキュメントを保存してください。

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

## PDF を固定サイズのページグループに分割する

すべての出力ファイルが同じページ数を含むべき場合（ただし最後の部分は例外になることがあります）にこのパターンを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ループ処理 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) グループごとのコレクション `pagesPerPart`。
1. 各グループごとに新しい出力ドキュメントを作成し、計算されたページ範囲をそれにコピーしてください。
1. 各パーツを生成されたファイル名で保存してください。

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

## PDF をカスタムページ範囲で分割する

この例では、各出力ドキュメントの開始ページと終了ページを明示的に定義できます。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なものを定義する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 配列や他のコレクション内の範囲。
1. 各範囲をソースページ数と照合し、一致するページを新しいドキュメントにコピーしてください。
1. 各範囲ベースの出力ファイルを保存してください。

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

## 最初のページと残りのページの分割

カバーページを文書の残りの部分から別々にエクスポートする必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、ページが含まれていることを確認してください。
1. 最初のものの出力ドキュメントを1つ作成してください [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 複数ページが利用可能な場合、残りのページ範囲について別のドキュメントを作成してください。
1. 両方の結果を保存してください。

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

## 最後のページと前のページの分割

この例では、文書の最後のページを他のページから分離します。これは、要約ページや署名ページを抽出するのに便利です。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、空でないことを確認してください。
1. 最後をコピー [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 新しい出力ドキュメントへ。
1. 前のページがまだ残っている場合は、そのページを元のドキュメントから削除してください。
1. 最後のページと残りのページを別々のファイルとして保存してください。

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

## PDF を3つの部分に分割する

文書をほぼ同じサイズの3つの連続したセクションに分割する必要がある場合は、このパターンを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、総ページ数を決定してください。
1. 各出力パートの概算サイズを計算してください。
1. 最大3つのドキュメントを作成し、一致するものをコピーします [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲。
1. 生成された各パートを保存してください。

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

## PDF をカスタムページ グループに分割する

この例では、連続する範囲ではなく、非連続のページセットから出力ファイルを作成する方法を示しています。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. カスタム グループを定義する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 数字。
1. 各グループごとに新しい出力ドキュメントを作成し、そのグループの有効なページのみを追加してください。
1. 空でない各グループ文書を保存してください。

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

## PDF を単一ページに分割し、安定したファイル名で保存する

出力名が辞書順にソート可能なままである必要がある場合、例えば自動化パイプラインで使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 各項目について1つの出力ドキュメントを作成します [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 各ファイルをゼロ埋めしたページ番号で保存してください。

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

## PDFを奇数ページと偶数ページに分割する

この例では、ページ番号の奇数・偶数に基づいてページを分割し、2つの出力を作成します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 奇数用に出力ドキュメントを1つ作成する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 番号と偶数ページ用の別のもの。
1. 各出力ドキュメントごとに必要な増分を使用して、ソースページを繰り返し処理してください。
1. 奇数ページと偶数ページの結果を別々に保存してください。

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
