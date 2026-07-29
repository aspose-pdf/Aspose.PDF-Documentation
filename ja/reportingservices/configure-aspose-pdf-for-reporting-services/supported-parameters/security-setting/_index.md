---
title: セキュリティ設定
linktitle: セキュリティ設定
type: docs
weight: 30
url: /ja/reportingservices/security-setting/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

セキュリティは、ネットワークの保護であれ PDF ドキュメントの保護であれ、あらゆる分野において常に最も重要な問題です。ドキュメントが安全に保護される理由はさまざまあります。たとえば、ドキュメントの作成者が内容を安全に保ち、他者が変更できないようにしたい、というようなケースです。

Aspose.PDF for Reporting Services は、PDF ドキュメントの保護に役立つ機能を開発者に提供することで、これらのセキュリティ面に十分配慮しています。そのため、開発者が PDF ドキュメントにさまざまなセキュリティ対策を適用できるように、複数のパラメータが用意されています。

これらの対策のひとつは、暗号化時に PDF ドキュメントにパスワード保護を施すことです。また、コンテンツの変更やコピー、文書の印刷、フォームの入力を許可または無効にすることもできます。これらの機能は現在、デフォルトの SQL Reporting Services PDF エクスポーターではサポートされていませんが、Aspose.PDF for Reporting Services を使用すれば実装可能です。レポートまたはレポートサーバーの構成ファイルに該当するセキュリティ パラメータを追加するだけで、権限が限定された安全な PDF ドキュメントを作成できます。

現在、Aspose.PDF for Reporting Services レンダラーは以下のセキュリティ属性をサポートしています：

{{% /alert %}}

{{% alert color="primary" %}}

**パラメータ名**: ユーザーパスワード  
**データ型**: 文字列  
**サポートされる値**: 任意のプレーンテキスト

**パラメータ名**: マスターパスワード  
**データ型**: 文字列  
**サポートされる値**: 任意のプレーンテキスト 

**パラメータ名**: IsCopyingAllowed  
**データ型**: Boolean  
**サポートされる値**: True, False (default)  

**パラメータ名**: IsPrintingAllowed  
**データ型**: Boolean  
**サポートされる値**: True, False (default)  

**パラメータ名**: IsContentsModifyingAllowed  
**データ型**: Boolean  
**サポートされる値**: True, False (default)  

**パラメータ名**: IsFormFillingAllowed  
**データ型**: Boolean  
**サポートされる値**: True, False (default)  

**例**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>偽</IsCopyingAllowed>
    <IsPrintingAllowed>偽</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
