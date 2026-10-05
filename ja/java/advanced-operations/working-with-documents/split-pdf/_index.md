---
title: "Java での PDF ファイルの分割"
linktitle: "PDF ファイルの分割"
type: docs
weight: 60
url: /ja/java/split-pdf-document/
description: "Java で PDF ページを個別の PDF ファイルに分割する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF 文書の分割：ページ、範囲、グループ、ファイル名パターンによる分割"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF 文書を分割する方法を説明します。単一ページへの分割、2 部または 3 部への分割、奇数ページと偶数ページへの分割、固定サイズのチャンクへの分割、カスタム範囲の指定、最初または最後のページと残りのページへの分割、カスタムページグループの指定、および安定したファイル名の生成について取り上げます。"
---
Aspose.PDF for Java は、1 ページごとのファイル出力以外にも、いくつかの分割パターンをサポートしています。

## PDF の単一ページのファイルへの分割

各ソースページを別々の出力ドキュメントにする必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. エクスポートしたい各 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に対して、新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 選択した [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を新しい文書に追加してください。
1. 各出力 PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

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

## PDF の2つの部分への分割

この例では、ソースドキュメントを中点に基づいて2つの連続した出力ファイルに分割します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 利用可能な [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクションの中点を計算してください。
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

## PDF の固定サイズのページグループへの分割

すべての出力ファイルが同じページ数を含むべき場合（ただし最後の部分は例外になることがあります）にこのパターンを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ループ処理 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクションを `pagesPerPart` ごとのグループで行ってください。
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

## PDF のカスタムページ範囲による分割

この例では、各出力ドキュメントの開始ページと終了ページを明示的に定義できます。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 範囲を配列または他のコレクションで定義してください。
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
1. 最初の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) の出力ドキュメントを 1 つ作成してください。
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
1. 最後の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を新しい出力ドキュメントへコピーしてください。
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

## PDF の3つの部分への分割

文書をほぼ同じサイズの3つの連続したセクションに分割する必要がある場合は、このパターンを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、総ページ数を取得してください。
1. 各出力パートの概算サイズを計算してください。
1. 最大3つのドキュメントを作成し、対応する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) の範囲をコピーしてください。
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

## PDF のカスタムページ グループへの分割

この例では、連続する範囲ではなく、非連続のページセットから出力ファイルを作成する方法を示しています。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. カスタム グループを定義する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) の番号を指定してください。
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

## PDF を単一ページに分割し、安定したファイル名で保存

出力名が辞書順にソート可能なままである必要がある場合、たとえば自動化パイプラインで使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ごとに出力ドキュメントを 1 つ作成してください。
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

## PDF の奇数ページと偶数ページへの分割

この例では、ページ番号の奇数・偶数に基づいてページを分割し、2 つの出力を生成します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) のページ番号が奇数のページと偶数のページに対して、それぞれ出力ドキュメントを 1 つ作成してください。
1. 各出力ドキュメントに対して必要な増分でソースページを繰り返し処理してください。
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
