---
title: セキュリティ設定
linktitle: セキュリティ設定
type: docs
weight: 30
url: /ja/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

セキュリティは常にあらゆる分野において最も重要な課題であり、ネットワークの保護であれ PDF ドキュメントの保護であれです。ドキュメントが安全に保たれる理由はさまざまあります。たとえば、ドキュメントの作成者が内容を安全に保ち、他者が変更できないようにしたい場合などです。

Aspose.Pdf for Reporting Services は、このようなセキュリティ面に十分配慮し、PDF ドキュメントを保護するために開発者が利用できる機能を提供しています。そのため、開発者が PDF ドキュメントにさまざまなセキュリティ対策を適用できるようにする多数のパラメータが含まれています。

これらの対策の一つは、暗号化時に PDF ドキュメントにパスワードを設定することです。コンテンツの変更、コンテンツのコピー、ドキュメントの印刷、フォーム入力の許可/無効化なども制限または許可できます。これらの機能は現在、デフォルトの SQL Reporting Services PDF Exporter ではサポートされていませんが、Aspose.Pdf for Reporting Services を使用すれば実装可能です。レポートまたはレポートサーバーの構成ファイルに対応するセキュリティパラメータを追加するだけで、限定された権限を持つ安全な PDF ドキュメントを作成できます。

現在、Aspose.Pdf for Reporting Services レンダラーは以下のセキュリティ属性をサポートしています:

{{% /alert %}}

{{% alert color="primary" %}}

**パラメータ名**: ユーザーパスワード  
**データ型**: 文字列  
**サポートされる値**: 任意のプレーンテキスト

**パラメータ名**: マスターパスワード  
**データ型**: 文字列  
**サポートされる値**: 任意のプレーンテキスト 

**パラメータ名**: IsCopyingAllowed  
**データ型**: ブール  
**サポートされる値**: True, False（デフォルト）  

**パラメータ名**: IsPrintingAllowed  
**データ型**: ブール  
**サポートされる値**: True, False（デフォルト）  

**パラメータ名**: IsContentsModifyingAllowed  
**データ型**: ブール  
**サポートされる値**: True, False（デフォルト）  

**パラメータ名**: IsFormFillingAllowed  
**データ型**: ブール  
**サポートされる値**: True, False（デフォルト）  

**例**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

