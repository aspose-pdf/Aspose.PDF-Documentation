---
title: "Java を使用した既存の PDF ファイルの画像の置換"
linktitle: "画像の置換"
type: docs
weight: 70
url: /ja/java/replace-image-in-existing-pdf-file/
description: "Java で既存の PDF ファイルに埋め込まれた画像を置換する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用して既存の PDF ファイルの画像の置換"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメント内の画像を置換する方法を示します。リソースインデックスによる画像の置換と、ImagePlacementAbsorber を使用して見つかった最初の一致する画像配置の置換について説明します。"
---
画像の対象範囲をどの程度正確に指定するかに応じて、ページ画像コレクションまたは配置ベースの検索のいずれかを使用してください。

## リソースインデックスで画像を置き換える

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットの画像リソースにアクセスする [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを取得してください。
1. ターゲットの画像リソースを新しい画像ファイルで置き換えてください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## 画像の置き換え：`ImagePlacementAbsorber`

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) を作成し、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を訪問してください。
1. 対象の [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) を取得し、新しい画像ストリームに置き換えてください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
