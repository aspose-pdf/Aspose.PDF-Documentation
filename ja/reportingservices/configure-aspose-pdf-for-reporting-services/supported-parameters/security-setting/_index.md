---
title: Security Setting
type: docs
weight: 30
url: ja/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

セキュリティは、ネットワークやPDFドキュメントの保護など、あらゆる分野で最も重要な問題であり続けています。ドキュメントは、さまざまな理由で安全に作成されます。たとえば、ドキュメントの作成者がその内容を安全に保ち、他者に変更を許可したくない場合などです。

Aspose.Pdf for Reporting Servicesは、開発者がPDFドキュメントを保護するのに役立つこれらの機能を提供することにより、このようなセキュリティの側面に非常に注意を払っています。したがって、開発者がPDFドキュメントに対してさまざまなセキュリティ対策を適用できるようにする多くのパラメータが含まれています。

これらの対策の1つは、暗号化中にPDFドキュメントをパスワードで保護することです。 あなたは、コンテンツの修正を制限したり許可したり、コンテンツのコピー、文書の印刷、またはフォームの記入を許可/無効にすることもできます。これらの機能は現在、デフォルトのSQL Reporting Services PDFエクスポーターではサポートされていませんが、Aspose.Pdf for Reporting Servicesを使用してこれらの機能を実装することができます。対応するセキュリティパラメータをレポートまたはレポートサーバーの構成ファイルに追加するだけで、制限された特権を持つ安全なPDFドキュメントを作成することができます。

現在、Aspose.Pdf for Reporting Servicesレンダラーは以下のセキュリティ属性をサポートしています:

{{% /alert %}}

{{% alert color="primary" %}}

**パラメータ名**: ユーザーパスワード  
**データ型**: 文字列  
**サポートされる値**: 任意のプレーンテキスト

**パラメータ名**: マスターパスワード  
**データ型**: 文字列  
**サポートされる値**: 任意のプレーンテキスト

**パラメータ名**: コピー許可  
**データ型**: ブール値  
**サポートされる値**: True, False (デフォルト)

**パラメータ名**: 印刷許可  
**データ型**: ブール値  

**サポートされる値**: True, False (デフォルト)
**パラメーター名**: IsContentsModifyingAllowed  
**データ型**: Boolean  
**サポートされる値**: True, False (default)  

**パラメーター名**: IsFormFillingAllowed  
**データ型**: Boolean  
**サポートされる値**: True, False (default)  

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