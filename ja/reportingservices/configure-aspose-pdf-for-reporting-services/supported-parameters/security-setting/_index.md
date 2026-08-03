---
title: セキュリティ設定
linktitle: セキュリティ設定
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

ネットワークや PDF ドキュメントの保護など、セキュリティはあらゆる分野で常に最も重要な問題です。ドキュメントはさまざまな理由で安全に保たれます。ドキュメントの作成者はドキュメントの内容を安全に保ちたい、他の人に変更を許可したくない、などです。

Aspose.PDF for Reporting Services は、PDF ドキュメントの保護に役立つ機能を開発者に提供することで、このようなセキュリティ面に細心の注意を払っています。したがって、開発者が PDF ドキュメントにさまざまなセキュリティ対策を適用できるようにする多数のパラメータが含まれています。

これらの対策の 1 つは、暗号化中に PDF ドキュメントをパスワードで保護することです。また、コンテンツの変更、コンテンツのコピー、ドキュメントの印刷を制限または許可したり、フォーム入力を許可/無効にしたりすることもできます。現時点では、これらの機能はデフォルトの SQL Reporting Services PDF エクスポーターではサポートされていませんが、Aspose.PDF for Reporting Services を使用してこれらの機能を実装できます。対応するセキュリティ パラメーターをレポートまたはレポート サーバー構成ファイルに追加するだけで、権限が制限された安全な PDF ドキュメントを作成できるようになります。

現在、Aspose.PDF for Reporting Services レンダラーは次のセキュリティ属性をサポートしています。

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## 例

```xml
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
```

