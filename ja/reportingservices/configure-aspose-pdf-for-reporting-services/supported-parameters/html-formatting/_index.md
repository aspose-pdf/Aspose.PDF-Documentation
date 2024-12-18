---
title: HTML Formatting
type: docs
weight: 20
url: /ja/reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

時々、書式付きでテキストボックスのテキストをエクスポートしたいことがあります。残念ながら、Reporting Servicesはこれをサポートしていません。しかし、Aspose.PDF for Reporting Servicesを使用して実装することは可能です。すべてのテキストボックス内のテキストをHTMLとして扱い、出力ドキュメント内のテキストをフォーマットするために必要なHTMLタグを挿入する特別なモードを有効にしてください。たとえば、同じテキストボックス内に通常、太字、斜体のテキストを持たせるには、次のテキストボックスの値を入力します：

Some of this text is ```<b>bold</b>``` and other text is ```<i>italic</i>```.

エクスポートされると、テキストは一部が **bold** で他の部分が *italic* のように見えます。

このアプローチにはいくつかの制限があることに注意してください

{{% /alert %}}

{{% alert color="primary" %}}

- 書式設定はデザイン時に表示されません（レポートビルダー、Reporting Servicesウェブポータルなど）。 HTML タグの形式のプレーンテキストを代わりに表示します。
- Aspose.PDF for Reporting Services のレンダリング拡張機能は、テキストボックス内の HTML コードを認識し、適切にフォーマットします。Reporting Services のデフォルトの PDF レンダラーは、このマークアップをプレーンテキストとしてエクスポートします。

**パラメーター名**: IsHtmlTagSupported  
**データ型**: Boolean  
**サポートされる値**: True, False (デフォルト)   

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

このパラメーターをレポートデザイナーに追加したい場合は、'Boolean' データ型を使用してください。

現在、Aspose.Pdf for Reporting Services はすべての HTML タグのサブセットをサポートしています。詳細は Aspose.PDF [ドキュメント](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) でご覧いただけます。

{{% /alert %}}