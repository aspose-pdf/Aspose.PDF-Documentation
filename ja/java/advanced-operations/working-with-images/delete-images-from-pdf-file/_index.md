---
title: "Java を使用した PDF ファイルから画像の削除"
linktitle: "画像の削除"
type: docs
weight: 20
url: /ja/java/delete-images-from-pdf-file/
description: Java で PDF ファイルから埋め込み画像を削除する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF ファイルから埋め込み画像の削除"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントから画像を削除する方法を示します。この例では、ページ画像コレクション内のインデックスに基づいて最初のページから画像リソースを削除し、変更されたドキュメントを保存します。
---
PDF ページから埋め込み画像を削除する必要がある場合は、ページ画像リソースコレクションを使用してください。

## インデックスで埋め込み画像の削除

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットの画像リソースに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) からアクセスしてください。
1. インデックスを使用して、ページ画像リソースコレクションから対象の画像を削除してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
