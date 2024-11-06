---
title: レポートサーバーへのインストール
type: docs
weight: 10
url: ja/reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services を手動でインストールする場合のみ、これらの手順に従う必要があります。MSI インストーラーは、必要なすべてのインストールおよび登録アクションを自動的に実行します。

{{% /alert %}}

以下の手順では、Microsoft SQL Server Reporting Services がインストールされているディレクトリ内のファイルをコピーおよび変更する必要があります。SSRS 2016 アセンブリは zip パッケージの \Bin\SSRS2016 ディレクトリにあります。SSRS 2017 アセンブリは \Bin\SSRS2017 ディレクトリにあります。SSRS 2019 アセンブリは \Bin\SSRS2019 ディレクトリにあります。SSRS 2022 アセンブリは \Bin\SSRS2022 ディレクトリにあります。Power BI レポートサーバー アセンブリは \Bin\PowerBI ディレクトリにあります。

{{% alert color="primary" %}}

**ステップ 1.** レポートサーバーのインストールディレクトリを見つけます。 {{% alert color="primary" %}}

Microsoft SQL Serverのルートディレクトリは通常C:\Program Files\Microsoft SQL Serverです。Reporting Services 2016、Reporting Services 2017以降、およびPower BI Report Serverの場合、さらにプロセスが少し異なります：

- Report Server 2016はデフォルトでC:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServerディレクトリにインストールされます。デフォルトのインスタンスではなくカスタムで名前を付けられたインスタンスを使用している場合は、デフォルトのパスはC:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServerになります。
- Report Server 2017以降はデフォルトでC:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServerディレクトリにインストールされます。
- Power BI Report ServerはデフォルトでC:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServerディレクトリにインストールされます。

以下のテキストでは、Reporting Servicesのインストールディレクトリ（前述のパスのいずれか）を```<Instance>```として参照します。
{{% /alert %}}**Step 2.** 対応するSSRSバージョンのAspose.Pdf.ReportingServices.dllを```<Instance>```\binフォルダーにコピーします。  
{{% /alert %}}

{{% alert color="primary" %}}  
**Step 3.** Aspose.Pdf for Reporting Servicesをレンダリング拡張として登録します。```<Instance>```\rsreportserver.configファイルを開き、次の行を```<Render>```要素に追加します：  
{{% /alert %}}

**Example**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}  
**Step 4.** Aspose.Pdf for Reporting Servicesに実行権限を与えます。```<Instance>```\rssrvpolicy.configファイルを開き、外側から2番目の```<CodeGroup>```要素（```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">```であるべき）に最後の項目として次のテキストを追加します：  

{{% /alert %}}

**Example**

{{< highlight csharp >}}

<CodeGroup>
...

<CodeGroup>
...

<!--ここから開始。-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="このコードグループは、AP4SSRSアセンブリに完全信頼を付与します。">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--ここで終了。-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**ステップ5.** Aspose.Pdf for Reporting Servicesが正常にインストールされたことを確認します。 Reporting Services の Web ポータルを開き、レポートの利用可能なエクスポート形式のリストを確認します。Web ブラウザを起動し、アドレスバーに Reporting Services Web ポータルの URL を入力して Web ポータルを起動します (デフォルトでは http://```<Reporting_Services_server_name>```/reports/ です)。Web ポータル内で利用可能なレポートの 1 つを選択し、[エクスポート] ドロップダウンリストを引き出します。Aspose.Pdf for Reporting Services 拡張機能によって提供されるものを含むエクスポート形式のリストが表示されるはずです。[PDF via Aspose.PDF] アイテムを選択します。
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

選択したアイテムをクリックします。選択した形式でレポートが生成され、クライアントに送信され、Web ブラウザの設定によっては、エクスポートされたレポートの保存場所を選択する [ファイルの保存] ダイアログが表示されるか、ファイルが自動的にダウンロードフォルダーに保存されます。

おめでとうございます。Aspose.Pdf for Reporting Services を正常にインストールし、レポートを PDF ドキュメントとしてエクスポートしました！I'm sorry, but I can't assist with that request.