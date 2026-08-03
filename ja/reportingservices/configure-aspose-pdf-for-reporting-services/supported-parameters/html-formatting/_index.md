---
title: HTMLのフォーマット
linktitle: HTMLのフォーマット
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Aspose.PDF for Reporting Services を使用して PDF レポートで HTML 書式設定を有効にします。スタイルと構造を簡単に追加します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

場合によっては、テキストボックス内のテキストを書式付きでエクスポートしたい場合があります。残念ながら、Reporting Services はこれをサポートしていません。ただし、Aspose.PDF for Reporting Services を使用して実装することはできます。テキストボックス内のすべてのテキストが HTML として扱われる特別なモードを有効にし、出力ドキュメント内のテキストの書式設定に必要な HTML タグを追加するだけです。たとえば、同じテキストボックスに標準、太字、斜体のテキストを含めるには、次のテキストボックス値を入力します。

このテキストの一部は `<b>bold</b>` であり、他のテキストは `<i>italic</i>` です。

エクスポートすると、テキストの一部は **太字**、他のテキストは *斜体* のように表示されます。

このアプローチにはいくつかの制限があることに注意してください

{{% /alert %}}

{{% alert color="primary" %}}

- 書式設定は、設計時 (レポート ビルダー、Reporting Services Web ポータルなど) には表示されません。代わりに、HTML テキストがタグ付きのプレーン テキストの形式で表示されます。
- Aspose.PDF for Reporting Services レンダリング拡張機能は、テキスト ボックス内の HTML コードを認識し、適切にフォーマットします。 Reporting Services の既定の PDF レンダラーは、このマークアップをプレーン テキストとしてエクスポートします。

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## 例

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

このパラメータをレポート デザイナーに追加する場合は、`Boolean` データ型を使用します。

現在、Aspose.Pdf for Reporting Services は、すべての HTML タグのサブセットをサポートしています。詳細については、Aspose.PDF [ドキュメント](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) を参照してください。

{{% /alert %}}
