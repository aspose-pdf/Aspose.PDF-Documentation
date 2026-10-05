---
title: フィールド名の変更
linktitle: フィールド名の変更
type: docs
weight: 50
url: /ja/java/rename-field/
description: Java で Aspose.PDF の FormEditor ファサードを使用して、PDF ドキュメント内の既存のフォームフィールドの名前を変更する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォームフィールドの名前を変更する
Abstract: この記事では、既存の PDF をバインドし、指定されたフィールドの名前を変更し、更新されたドキュメントを Aspose.PDF for Java の FormEditor ファサードを使用して保存する方法を示します。
---
## フィールドの名前の変更

1. ソース PDF をバインドする `FormEditor` ファサード。
2. 呼び出し `renameField(...)` 現在のフィールド名と新しいフィールド名で
3. 更新されたドキュメントを保存してください。

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
