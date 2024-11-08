---
title: パラメーターを設定する
type: docs
weight: 10
url: /ja/reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.Pdf for Reporting Services がドキュメントを生成する方法に影響を与える特定の構成パラメーターを指定できます。このセクションでは、このプロセスについて説明します。

{{% /alert %}}

Aspose.Pdf for Reporting Services を構成するには、C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config ファイルを編集する必要があります。これは XML ファイルであり、Aspose.PDF レンダラーに対応する ```<Extension>``` 要素の中にレンダラー構成があります。

**例**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--ここに PDF へのエクスポート用の構成要素を挿入します。以下は例です
ページの向きのために -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}


{{% alert color="primary" %}}

If you want to set parameters for specific report file but not for every report on the server, you can add a report parameter for the specific report in the Report Builder as the following steps (for example, we’ll add an 'IsLandscape' parameter shown earlier):

特定のレポートファイルに対してパラメータを設定したいが、サーバー上のすべてのレポートには設定したくない場合、次の手順でレポートビルダーに特定のレポートのパラメータを追加できます（例えば、前述の 'IsLandscape' パラメータを追加します）。

1. Open the report in the Report Designer, right-click on the 'Parameters' folder in the 'Report Data' pane, and select 'Add Parameter…' (or, alternately, pull down the 'New' list and select 'Parameter…').

   レポートデザイナーでレポートを開き、「レポートデータ」ペインの「パラメータ」フォルダーを右クリックし、「パラメータの追加...」を選択します（または、代わりに「新規」リストをプルダウンして「パラメータ...」を選択します）。

![todo:image_alt_text](setting-parameters_1.png)

1. In the 'Report Parameter Properties' dialog, create the parameter named 'IsLandscape', with the data type of Boolean, and add the value True in the 'Default Values' tab.

   「レポートパラメータプロパティ」ダイアログで、データ型をブール型とし、名前を 'IsLandscape' とするパラメータを作成し、「既定値」タブに値 True を追加します。

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}