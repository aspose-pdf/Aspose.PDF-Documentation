---
title: ボタン フィールドと画像
linktitle: ボタン フィールドと画像
type: docs
weight: 40
url: /ja/java/button-fields-and-images/
description: Aspose.PDF for Java の Form ファサードを使用して、PDF フォームのボタンフィールドに画像の外観を追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF のボタンフィールドに画像の外観を追加する
Abstract: この記事では、Aspose.PDF for Java の Form ファサードを使用して PDF フォームをバインドし、画像をストリームとして読み込み、画像ボタンフィールドに入力し、更新されたドキュメントを保存する方法を示します。
---
Javaの例は `FormExamples.addImageAppearanceToButtonField(...)` 画像ストリームを使用してボタンフィールドの外観を更新する方法を示します。

ワークフローは簡単です:

- 入力PDFをバインドする `form.bindPdf(...)`
- 画像ファイルを開くには `Files.newInputStream(...)`
- 呼び出す `form.fillImageField(...)` ボタン フィールド用
- 更新された PDF を保存する

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
