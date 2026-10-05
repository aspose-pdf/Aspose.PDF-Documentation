---
title: 名前と値でフィールドを埋める
linktitle: 名前と値でフィールドを埋める
type: docs
weight: 60
url: /ja/java/fill-fields-by-name-and-value/
description: Javaで動的な名前‑値フォームの更新のために、Formファサードのフィールド入力APIの適用方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Javaで名前と値のペアから複数のPDFフォームフィールドを埋める
Abstract: 現在のJavaサンプルセットは、繰り返し `fillField(...)` 呼び出しで個々のフィールドを埋めます。この記事では、リポジトリの例に存在しない別個のファサード機能を作り出すことなく、同じAPIパターンを自分の名前‑値コレクションに適用する方法を示します。
---
そのJava `FormExamples` クラスは個々のフィールドを直接埋めます:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

アプリケーションですでに動的なフィールド名と値のセットがある場合、同じものを適用してください。 `fillField(...)` 自分のループ内で呼び出す:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

これは、同じ Java API を使用して導出されたアプリケーションレベルのパターンです。 `FormExamples.fillTextFields(...)`; 現在のリポジトリには、マップベースの入力用の別個の専用ヘルパーメソッドが含まれていません。
