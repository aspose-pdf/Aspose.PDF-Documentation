---
title: HTML 書式設定
linktitle: HTML 書式設定
type: docs
weight: 20
url: /ja/reportingservices/html-formatting/
description: Aspose.PDF for Reporting Services を使用して PDF レポートで HTML 書式設定を有効にします。スタイルと構造を簡単に追加できます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

テキストボックス内のテキストを書式付きでエクスポートしたくなることがありますが、残念ながら Reporting Services はこれをサポートしていません。しかし、Aspose.PDF for Reporting Services を使用すれば実装可能です。テキストボックス内のすべてのテキストを HTML として扱う特別なモードを有効にし、出力ドキュメントでテキストを書式設定するために必要な HTML タグを配置します。例えば、同じテキストボックス内で普通、太字、斜体のテキストを使用したい場合、以下のテキストボックスの値を入力します：

このテキストの一部は ```<b>bold</b>``` そして他のテキストは ```<i>italic</i>```.

エクスポートすると、テキストは **bold** の一部と *italic* の他の部分のように表示されます。

このアプローチにはいくつかの制限があることにご注意ください

{{% /alert %}}

{{% alert color="primary" %}}

- 書式はデザイン時（Report Builder、Reporting Services の Web ポータルなど）に表示されません。代わりに、タグ付きのプレーンテキストとして HTML テキストが表示されます。
- Aspose.PDF for Reporting Services のレンダリング拡張機能は、テキストボックス内の HTML コードを認識し、適切にフォーマットします。Reporting Services のデフォルト PDF レンダラは、このマークアップをプレーンテキストとしてエクスポートします。

**パラメータ名**: IsHtmlTagSupported  
**データ型**: Boolean  
**サポートされる値**: True, False (default)   

**例**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Report Designerでこのパラメータを追加したい場合は、'Boolean' データ型を使用してください。

 
現在 Aspose.Pdf for Reporting Services はすべての HTML タグのサブセットをサポートしています。詳細は Aspose.PDF のドキュメントでご確認いただけます。 [ドキュメント](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

