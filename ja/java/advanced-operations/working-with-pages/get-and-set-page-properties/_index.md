---
title: "Java での PDF ページプロパティの取得および設定"
linktitle: ページプロパティの取得と設定
type: docs
weight: 90
url: /ja/java/get-and-set-page-properties/
description: "Java で、ページ数、ボックス、回転、色情報などの PDF ページプロパティを検査する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイルのページ数、ボックス、色タイプの検査"
Abstract: "この記事では、Aspose.PDF for Java を使用してページプロパティを検査する方法を説明します。ページ数の取得、段落の生成と保存前の結果カウントの確認、主要なページボックス値のすべての出力、各ページのカラータイプの識別を取り上げています。"
---
Aspose.PDF for Java は、ページ数、ページボックス、回転、およびページのカラータイプを検査できます。

## ページ数の取得

PDF の総ページ数を読み取る必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ コレクションのサイズを読み取ってください。
1. 合計ページ数を出力してください。

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## 保存する前のページ数の取得

ファイルを書き込む前に、生成されたコンテンツが何ページになるかを知りたい場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページにコンテンツを追加してください。
1. 段落を処理して、レイアウト計算を強制してください。
1. 結果として得られたページ数を読み取り、出力してください。

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## ページ ボックスのプロパティの取得

主要なボックス寸法およびページ回転値をすべて検査する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いて、対象ページにアクセスしてください。
1. ページボックスの値をマップに収集してください。
1. サイズとページ回転情報を出力してください。

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## 各ページの色タイプの取得

ページが白黒、グレースケール、または RGB かを判別する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. すべてのページを反復処理して、各ページの [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) を読み取ってください。
1. 列挙型の値を読みやすいテキストに変換して、結果を出力してください。

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
