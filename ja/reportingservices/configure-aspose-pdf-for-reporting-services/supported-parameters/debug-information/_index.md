---
title: デバッグ情報
linktitle: デバッグ情報
type: docs
weight: 90
url: /ja/reportingservices/debug-information/
description: Aspose.PDF for Reporting Services の PDF レンダリングに関するデバッグ情報にアクセスし、分析して、問題を効果的にトラブルシュートします。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

レンダリングやレンダリング結果に何らかの問題があることは避けられません。機密性やプライバシーなどの理由で、ユーザーのレポートで使用されたデータソースを取得できず、レポート内のエラーを再現できないことがあります。お客様と開発者間のやり取りをより容易かつ円滑にするために、このパラメータを追加しました。Aspose.PDF for Reporting Services でレポートのレンダリング時に問題が発生した場合は、このレポート パラメータを設定してください。そうすれば、XML 形式のレンダリング済みドキュメントが取得できます。その後、製品フォーラムに XML ファイルを投稿してください。

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
<SavingXmlFormat > 真 </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
