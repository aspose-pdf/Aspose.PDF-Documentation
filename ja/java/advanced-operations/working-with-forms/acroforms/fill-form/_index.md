---
title: AcroForm に入力 - Java で PDF フォームに入力
linktitle: AcroForm に入力
type: docs
weight: 20
url: /ja/java/fill-form/
description: AcroForm フィールドを PDF ドキュメントに入力する（Aspose.PDF for Java を使用）
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF ファイルの AcroForm フィールドに入力
Abstract: この記事では、Aspose.PDF for Java を使用して AcroForm フィールドに入力する方法を説明します。サンプルでは、Form ファサードを介して PDF をロードし、フィールド名を値マップと照合し、一致するフィールドを更新し、完成したドキュメントを保存します。
---
その `Form` facadeは、既存のAcroFormのフィールド入力を自動化するために使用できます。

## AcroForm フィールドに新しい値を入力する

1. PDF フォームドキュメントを開く [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade。
1. Form フィールドを反復処理し、提供された値で一致するエントリを更新してください。
1. 更新された PDF ドキュメントを保存してください。

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
