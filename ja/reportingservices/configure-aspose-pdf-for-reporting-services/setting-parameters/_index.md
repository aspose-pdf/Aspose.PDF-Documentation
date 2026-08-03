---
title: パラメータの設定
linktitle: パラメータの設定
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Aspose.PDF for Reporting Services で PDF レンダリングのパラメーターを設定する方法を確認してください。出力の正確な制御を実現します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services がドキュメントを生成する方法に影響を与える特定の構成パラメーターを指定できます。このセクションでは、このプロセスについて説明します。

{{% /alert %}}

Reporting Services 用に Aspose.Pdf を構成するには、`C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config` ファイルを編集する必要があります。これは XML ファイルであり、レンダラー構成は Aspose.PDF レンダラーに対応する `<Extension>` 要素内にあります。

## 例

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

サーバー上のすべてのレポートではなく、特定のレポート ファイルにパラメーターを設定したい場合は、次の手順でレポート ビルダーで特定のレポートにレポート パラメーターを追加できます (たとえば、前に示した 'IsLandscape' パラメーターを追加します)。

1. レポート デザイナーでレポートを開き、[レポート データ] ペインの [パラメーター] フォルダーを右クリックして、[パラメーターの追加…] を選択します (または、[新規] リストをプルダウンして [パラメーター…] を選択します)。

![Parameters set up. Step 1](setting-parameters_1.png)

1. [レポート パラメーター プロパティ] ダイアログで、ブール型のデータ型で「IsLandscape」という名前のパラメーターを作成し、[デフォルト値] タブに値 True を追加します。

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
