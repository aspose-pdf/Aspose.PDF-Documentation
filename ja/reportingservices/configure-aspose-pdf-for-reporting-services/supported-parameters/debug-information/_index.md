---
title: デバッグ情報
linktitle: デバッグ情報
type: docs
weight: 90
url: /ja/reportingservices/debug-information/
description: Aspose.PDF for Reporting Services の PDF レンダリングに関するデバッグ情報にアクセスし、分析して、問題を効果的にトラブルシューティングします。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

レンダリングやレンダリング結果に何らかの問題があることは避けられません。機密性やプライバシーなどの理由で、ユーザーのレポートで使用されたデータソースを取得できず、レポートのエラーを再現できないことがあります。顧客と開発者間のやり取りをより簡単かつ円滑にするために、このパラメータを追加します。Aspose.PDF for Reporting Services でレポートのレンダリングに問題が発生した場合は、このレポート パラメータを設定してください。すると、XML 形式のレンダリングされたドキュメントが取得できます。その後、XML ファイルを製品フォーラムに投稿してください。

{{% /alert %}}

{{% alert color="primary" %}}
**パラメータ名**: SavingXmlFormat  
**日付型**: Boolean  
**サポートされる値**: True, False (default)  

**例**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

