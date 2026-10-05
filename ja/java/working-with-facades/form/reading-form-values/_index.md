---
title: Form の値を読み取る
linktitle: Form の値を読み取る
type: docs
weight: 60
url: /ja/java/reading-form-values/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォーム フィールドの名前と値を検査する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォーム フィールドの名前と値を読み取る
Abstract: このセクションでは、Aspose.PDF for Java 用の現在の Form facade サンプルセットで実装されている Java のフォーム読み取りワークフローを取り上げます。リポジトリは、一般的なフィールド検査のサンプルを提供し、まだ一致する Java サンプルがない専門ページ向けに明示的なスコープノートを使用しています。
---
そのJava `FormExamples` クラスは、Facades API によって公開されている主要なフォーム処理ワークフローを示します。

## フィールド値の取得

使用 `FormExamples.inspectFormFields(...)` フィールド名とその現在の値を検査する。

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
