---
title: "ボタンフィールドと画像"
linktitle: "ボタンフィールドと画像"
type: docs
weight: 40
url: /ja/java/button-fields-and-images/
description: Aspose.PDF for Java の Form ファサードを使用して、PDF フォームのボタンフィールドに画像の外観を追加する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF のボタンフィールドに画像の外観の追加"
Abstract: この記事では、Aspose.PDF for Java の Form ファサードを使用して PDF フォームをバインドし、画像をストリームとして読み込み、画像ボタンフィールドに入力し、更新されたドキュメントを保存する方法を示します。
---
Java の例 `FormExamples.addImageAppearanceToButtonField(...)` では、画像ストリームを使用してボタンフィールドの外観を更新する方法を示しています。

ワークフローは以下の通りです。

- 入力 PDF を `form.bindPdf(...)` でバインドしてください。
- 画像ファイルを `Files.newInputStream(...)` で開いてください。
- ボタンフィールドに対して `form.fillImageField(...)` を呼び出してください。
- 更新された PDF を保存してください。

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
