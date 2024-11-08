---
title: デバッグ情報
type: docs
weight: 90
url: /ja/reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レンダリングやレンダリング結果に問題があるのは避けられません。秘密やプライバシーなどの理由から、ユーザーのレポートで使用されているデータソースを取得できず、レポートのエラーを再現できません。顧客と開発者のコミュニケーションをより簡単かつ円滑にするために、このパラメーターを追加しました。Aspose.PDF for Reporting Servicesでレポートのレンダリングに問題が発生した場合は、このレポートパラメーターを設定してください。そうすると、XML形式でレンダリングされたドキュメントを取得できます。その後、製品フォーラムにXMLファイルを投稿してください。

{{% /alert %}}

{{% alert color="primary" %}}
**パラメーター名**: SavingXmlFormat  
**データ型**: Boolean  
**サポートされる値**: True, False (デフォルト)  

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