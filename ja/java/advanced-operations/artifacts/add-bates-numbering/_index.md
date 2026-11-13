---
title: JavaでPDFにBates番号付けを追加する
linktitle: Bates番号付けを追加する
type: docs
weight: 10
url: /ja/java/add-bates-numbering/
description: 専用のBates番号付けヘルパーまたは汎用ページ付けAPIを使用して、JavaでPDFページに連続したBates識別子を追加します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでBates番号付けを追加する
Abstract: 専用のBates番号付けヘルパーまたは汎用ページ付けAPIを使用して、JavaでPDFページに連続したBates識別子を追加します。
---
Bates番号付けのアーティファクトは、各ページに永続的なページレベルの識別子が必要な法的、アーカイブ、文書管理のワークフローで役立ちます。

## 専用ヘルパーでBates番号付けを追加する

専用のページコレクションヘルパーを使用してベーツ番号付けを適用したい場合は、この例を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開き、例に必要なページを追加してください。
1. [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) オブジェクトを設定してください。
1. ページコレクションにベーツ番号付与を適用し、出力ファイルを保存してください。

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

## ページネーション アーティファクトを使用してBates番号付けを追加する

この例では、汎用ページネーション API にBatesアーティファクトを渡すことでBates番号付けを適用します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開き、例に必要なページを追加してください。
1. [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) オブジェクトを作成し、ページネーションアーティファクトのリストに追加してください。
1. ページコレクションにページネーション アーティファクトを適用し、ドキュメントを保存してください。

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

## 関連トピック

- [ベーツ番号付与を削除](/pdf/ja/java/remove-bates-numbering/)
- [JavaでPDFアーティファクトを操作する](/pdf/ja/java/artifacts/)
