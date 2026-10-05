---
title: "フィールドの垂直配置の設定"
linktitle: "フィールドの垂直配置の設定"
type: docs
weight: 30
url: /ja/java/set-field-alignment-vertical/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF フォームフィールドの垂直配置を設定する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォームフィールドの垂直配置を設定する
Abstract: この記事では、既存の PDF をバインドし、垂直フィールド配置を設定し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## 垂直フィールド配置の設定

1. ソースPDFをにバインドする `FormEditor` ファサード。
2. 呼び出し `setFieldAlignmentV(...)` 対象フィールドと希望する垂直配置定数用に。
3. 更新されたドキュメントを保存してください。

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
