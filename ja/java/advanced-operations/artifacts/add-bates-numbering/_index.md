---
title: "Java での PDF への Bates 番号付けの追加"
linktitle: "Bates 番号付けの追加"
type: docs
weight: 10
url: /ja/java/add-bates-numbering/
description: "Aspose.PDF を使用した Java で、PDF ドキュメントにベーツ番号を追加および削除する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を介したベーツ番号の追加"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメント内にベーツ番号アーティファクトを作成および削除する方法を説明します。`BatesNArtifact` の設定、ベーツ番号ヘルパーまたは汎用ページ付けヘルパーによる適用、およびドキュメントからのベーツ番号の削除方法をカバーしています。"
---
ベーツ番号アーティファクトは、法務、アーカイブ、文書管理ワークフローにおいて、各ページに永続的なページレベルの識別子が必要な場合に役立ちます。

## 専用ヘルパーを使用したベーツ番号の追加

専用ページコレクションヘルパーを使用してベーツ番号を適用したい場合は、この例を使用してください。

1. ソース PDF を開き、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) サンプルで必要とされる余分なページを追加してください。
1. [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) の設定を作成してください。
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

## ページネーションアーティファクトを使用したベーツ番号の追加

この例では、汎用ページネーション API を使用して、ベーツアーティファクトを渡すことでベーツ番号付けを適用します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で開き、必要なページを追加してください。
1. [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) を作成し、それをページネーションアーティファクトのリストに追加してください。
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

既存の Bates 番号付けアーティファクトをドキュメントから削除する必要がある場合に、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. Bates 番号付けを削除するページコレクションヘルパーを呼び出してください。
1. クリーンアップされた出力ファイルを保存してください。

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
