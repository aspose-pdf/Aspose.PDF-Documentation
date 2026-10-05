---
title: "AcroForm の抽出 - Java で PDF からフォームデータの抽出"
linktitle: "AcroForm の抽出"
type: docs
weight: 30
url: /ja/java/extract-form/
description: Aspose.PDF for Java を使用して PDF ドキュメントの AcroForm フィールドから値を抽出します。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF ファイルからフォームフィールドの値を抽出
Abstract: "この記事では、Aspose.PDF for Java を使用して AcroForm フィールドからデータを抽出する方法を示します。サンプルでは、Form ファサードを使用してフィールド名を反復処理し、各フィールドの現在値を読み取ってマップに保存し、後続の処理に利用します。"
---
使用する `Form` は、単純なフィールド名からフィールド値への抽出フローが必要な場合のファサードです。

## すべての AcroForm フィールドからの値の抽出

1. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを使用して PDF フォームドキュメントを開いてください。
1. フィールド名を取得元から反復処理し、各現在のフィールド値を [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードからマップに格納してください。

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
