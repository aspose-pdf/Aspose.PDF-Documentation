---
title: JavaでPDFのベーツ番号付けを削除する
linktitle: ベーツ番号付けを削除する
type: docs
weight: 100
url: /ja/java/remove-bates-numbering/
description: JavaでPDFの全ページからベーツ番号付けを削除します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaでベーツ番号付けを削除する
Abstract: JavaでPDFの全ページからベーツ番号付けを削除します。
---
JavaでPDFの全ページからベーツ番号付けを削除します。

## ベーツ番号付けを削除する

既存のベーツ番号付けアーティファクトをドキュメントから削除する必要がある場合に、この方法を使用します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
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

## 関連トピック

- [ベーツ番号付けを追加](/pdf/ja/java/add-bates-numbering/)
- [JavaでPDFアーティファクトを操作する](/pdf/ja/java/artifacts/)
