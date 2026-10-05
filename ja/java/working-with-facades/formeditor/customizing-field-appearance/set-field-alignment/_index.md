---
title: "フィールドの配置の設定"
linktitle: "フィールドの配置の設定"
type: docs
weight: 20
url: /ja/java/set-field-alignment/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF フォームフィールドの水平テキスト配置を設定する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォームフィールドの配置を設定する
Abstract: この記事では、既存の PDF をバインドし、水平フィールド配置を設定し、更新されたドキュメントを Aspose.PDF for Java の FormEditor ファサードを使用して保存する方法を示します。
---
## 水平フィールド配置の設定

1. ソースPDFを...にバインドする `FormEditor` ファサード。
2. 呼び出す `setFieldAlignment(...)` 対象フィールドと希望する配置定数のために。
3. 更新されたドキュメントを保存してください。

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
