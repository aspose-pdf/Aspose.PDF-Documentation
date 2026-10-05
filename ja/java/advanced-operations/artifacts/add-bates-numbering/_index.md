---
title: "Java での PDFにBates Numberingの追加"
linktitle: Bates Numberingの追加
type: docs
weight: 10
url: /ja/java/add-bates-numbering/
description: Aspose.PDFを使用したJavaで、PDFドキュメントにBates numberingを追加および削除する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを介してBates Numberingを追加
Abstract: この記事では、Aspose.PDF for Java を使用して PDF 文書内でベーツ番号アーティファクトを作成および削除する方法を説明します。`BatesNArtifact` の構成、ベーツ番号ヘルパーまたは汎用ページ付けヘルパーを通じた適用、そして文書からベーツ番号を削除する方法をカバーしています。
---
ベーツ番号アーティファクトは、各ページに永続的なページレベルの識別子が必要な法務、アーカイブ、文書管理ワークフローで役立ちます。

## 専用ヘルパーを使用したベーツ番号の追加

専用ページコレクションヘルパーを使用してベーツ番号を適用したい場合は、この例を使用してください。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) サンプルで必要とされる余分なページを追加してください。
1. 作成してください [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 設定。
1. ページコレクションにベーツ番号を適用し、出力ファイルを保存してください。

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## ページネーションアーティファクトを使用したベーツ番号付与の追加

この例では、汎用ページネーション API にベーツアーティファクトを渡すことでベーツ番号付けを適用します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 必要なページを追加してください。
1. 作成してください [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) それをページネーションアーティファクトリストに追加してください。
1. ページコレクションにページネーションアーティファクトを適用し、ドキュメントを保存してください。

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Bates番号付けの削除

既存のBates番号付けアーティファクトを文書から削除する必要がある場合に、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. Bates番号付けを削除するページコレクションヘルパーを呼び出してください。
1. クリーンアップされた出力ファイルを保存してください。

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
