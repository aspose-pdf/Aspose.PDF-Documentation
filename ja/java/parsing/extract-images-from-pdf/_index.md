---
title: "Java を使用した PDF からの画像抽出"
linktitle: "PDF からの画像抽出"
type: docs
weight: 20
url: /ja/java/extract-images-from-the-pdf-file/
description: Aspose.PDF for Java を使用して PDF ファイルから埋め込み画像を抽出する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を介した PDF からの画像抽出"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントから埋め込み画像を抽出する方法を解説します。ソース PDF を開き、ページリソースコレクションから画像にアクセスし、抽出した XImage を外部ファイルに保存する手順を示します。
---
埋め込みグラフィックを再利用したり、ドキュメント資産を検査したり、下流処理のために画像をエクスポートしたりする必要がある場合に、PDF ページから画像を抽出します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開き、抽出された画像ファイル用の出力ストリームを開いてください。
1. 対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) をドキュメントから取得し、その `Resources.Images` コレクションにアクセスしてください。
1. 必要な [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) オブジェクトを、その画像コレクションからインデックスで取得してください。
1. `image.save(outputImage)` を呼び出して、抽出された画像バイトをターゲットストリームに書き込んでください。

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
