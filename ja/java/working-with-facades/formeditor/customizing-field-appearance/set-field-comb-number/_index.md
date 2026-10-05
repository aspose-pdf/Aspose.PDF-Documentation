---
title: "フィールドのコンブ番号の設定"
linktitle: "フィールドのコンブ番号の設定"
type: docs
weight: 60
url: /ja/java/set-field-comb-number/
description: JavaでAspose.PDFのFormEditorファサードを使用して、PDFフォームフィールドのコンブ番号を設定する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: JavaでPDFフォームフィールドのコンブ番号を設定する
Abstract: この記事では、既存のPDFをバインドし、フィールドのコンブ番号を設定し、Aspose.PDF for JavaのFormEditorファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## フィールドのコンブ番号の設定

1. ソースPDFをバインドする `FormEditor` ファサード。
2. 呼び出す `setFieldCombNumber(...)` 対象フィールドとコンブ値のために。
3. 更新されたドキュメントを保存してください。

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
