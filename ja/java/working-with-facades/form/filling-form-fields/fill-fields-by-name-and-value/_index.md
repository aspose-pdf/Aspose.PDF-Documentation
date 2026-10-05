---
title: 名前と値でフィールドを埋める
linktitle: 名前と値でフィールドを埋める
type: docs
weight: 60
url: /ja/java/fill-fields-by-name-and-value/
description: "Java で動的な名前‑値フォームを更新する場合、Form ファサードのフィールド入力 API の適用方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java で名前と値のペアから複数の PDF フォームフィールドを埋める"
Abstract: "現在の Java サンプルセットでは、繰り返し `fillField(...)` を呼び出すことで個々のフィールドを埋めています。本記事では、リポジトリの例に存在しない別個のファサード機能を作成することなく、同じ API パターンを独自の名前‑値コレクションに適用する方法を示します。"
---
Java の `FormExamples` クラスは、個々のフィールドを直接埋めます。

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

アプリケーションですでに動的なフィールド名と値のセットを持っている場合は、同じ `fillField(...)` を独自のループ内で呼び出してください。

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

これは、`FormExamples.fillTextFields(...)` で使用されている同じ Java API から導出されたアプリケーションレベルのパターンです。現在のリポジトリには、マップベースの入力用の別個の専用ヘルパーメソッドは含まれていません。
