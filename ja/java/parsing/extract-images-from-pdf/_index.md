---
title: "Java を使用した PDF から画像の抽出"
linktitle: "PDF から画像の抽出"
type: docs
weight: 20
url: /ja/java/extract-images-from-the-pdf-file/
description: Aspose.PDF for Java を使用して PDF ファイルから埋め込み画像を抽出する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を介して PDF から画像を抽出する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントから埋め込み画像を抽出する方法を解説します。ソース PDF を開き、ページリソースコレクションから画像にアクセスし、抽出した XImage を外部ファイルに保存する手順を示します。
---
埋め込みグラフィックを再利用したり、ドキュメント資産を検査したり、下流処理のために画像をエクスポートしたりする必要がある場合に、PDF ページから画像を抽出します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスを取得し、抽出された画像ファイル用の出力ストリームを開いてください。
1. 対象を取得 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 文書から取得し、それにアクセスする `Resources.Images` コレクション。
1. 必要なものを取得 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) インデックスでその画像コレクションからオブジェクト。
1. 呼び出す `image.save(outputImage)` 抽出された画像バイトをターゲットストリームに書き込む

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
