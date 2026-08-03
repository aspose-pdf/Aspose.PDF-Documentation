---
title: デバッグ情報
linktitle: デバッグ情報
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Aspose.PDF for Reporting Services の PDF レンダリングのデバッグ情報にアクセスして分析し、問題を効果的にトラブルシューティングします。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レンダリングまたはレンダリング結果に問題があることは避けられません。秘密やプライバシーなどの理由により、ユーザーのレポートで使用されたデータ ソースを取得できなかったため、レポートでエラーを再現できませんでした。顧客と開発者間のコミュニケーションをより簡単かつスムーズにするために、このパラメーターを追加します。 Aspose.PDF for Reporting Services を使用してレポートをレンダリングするときに問題が発生した場合は、このレポート パラメーターを設定してください。そうすれば、XML 形式でレンダリングされたドキュメントが得られます。その後、XML ファイルを製品フォーラムに投稿してください。

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## 例

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
