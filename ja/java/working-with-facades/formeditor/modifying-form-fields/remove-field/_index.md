---
title: "フィールドの削除"
linktitle: "フィールドの削除"
type: docs
weight: 40
url: /ja/java/remove-field/
description: JavaでAspose.PDFのFormEditorファサードを使用して、PDFドキュメントから既存のフォームフィールドを削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: JavaでPDFフォームフィールドを削除する
Abstract: この記事では、既存のPDFをバインドし、指定されたフィールドを削除し、Aspose.PDF for JavaのFormEditorファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## フィールドの削除

1. ソースPDFをバインドする `FormEditor` ファサード。
2. 呼び出し `removeField(...)` 対象フィールド名の場合。
3. 更新されたドキュメントを保存してください。

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
