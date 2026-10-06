---
title: "Java での PDF ページサイズの変更"
linktitle: ページサイズの変更
type: docs
weight: 40
url: /ja/java/change-page-size/
description: "Java で PDF ページの寸法を読み取り、変更する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用してページ寸法とボックスを読み取り、更新"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ページの寸法を読み取り、変更する方法を示します。ページサイズの取得、回転を考慮したページサイズの測定、および変更前後のボックス寸法を出力しながら最初のページを新しいサイズに更新する方法をカバーしています。"
---
Aspose.PDF for Java は、ページ寸法の取得だけでなく、更新も可能です。

## ページサイズの変更

既存のページのサイズを変更し、変更前後のページボックスを検査する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを取得し、現在のボックス値を出力してください。
1. 新しいページサイズを設定し、ドキュメントを保存してください。

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## ページサイズの取得

ページの表示寸法を読み取る必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 回転処理を有効にしてページの矩形を取得してください。
1. ページの幅と高さを出力してください。

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## 回転を適用したページサイズの取得

回転を考慮する前後のページ寸法を比較する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象の[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)を回転してください。
1. ページの矩形を回転あり・なしで読み取り、両方の値を出力してください。

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
