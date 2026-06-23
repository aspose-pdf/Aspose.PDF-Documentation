---
title: 設定パラメータ
linktitle: 設定パラメータ
type: docs
weight: 10
url: /ja/reportingservices/setting-parameters/
description: Aspose.PDF for Reporting Services における PDF レンダリングのパラメータ設定方法をご確認ください。出力を正確に制御できます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.Pdf for Reporting Services がドキュメントを生成する際に影響する特定の構成パラメータを指定できます。このセクションではその手順を説明します。

{{% /alert %}}

Aspose.Pdf for Reporting Services を構成するには、C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config ファイルを編集する必要があります。このファイルは XML ファイルで、レンダラー構成は内部にあります。 ```<Extension>``` Aspose.PDF レンダラに対応する要素。

**例**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}

サーバー上のすべてのレポートではなく、特定のレポート ファイルに対してだけパラメータを設定したい場合は、Report Builder で特定のレポートにレポート パラメータを追加できます。以下の手順に従ってください（例として、前述の ‘IsLandscape’ パラメータを追加します）。

1. Report Designer でレポートを開き、‘Report Data’ ペインの ‘Parameters’ フォルダーを右クリックし、‘Add Parameter…’ を選択します（または、‘New’ リストを下に展開して ‘Parameter…’ を選択することもできます）。
 
![todo:image_alt_text](setting-parameters_1.png)

1. ‘Report Parameter Properties’ ダイアログで、名前を ‘IsLandscape’ とするパラメータを作成し、データ型を Boolean に設定し、‘Default Values’ タブで値 True を追加します。

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

