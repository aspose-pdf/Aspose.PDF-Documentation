---
title: Report Server にインストール
linktitle: Report Server にインストール
type: docs
weight: 10
url: /ja/reportingservices/install-to-report-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

MSI インストーラを使用せずに Aspose.PDF for Reporting Services を手動でインストールする場合にのみ、以下の手順を実行する必要があります。MSI インストーラは、必要なインストールおよび登録アクションをすべて自動的に実行します。

{{% /alert %}}

以下の手順では、Microsoft SQL Server Reporting Services がインストールされているディレクトリ内のファイルをコピーおよび変更する必要があります。SSRS 2016 アセンブリは zip パッケージの \Bin\SSRS2016 ディレクトリにあります；SSRS 2017 アセンブリは \Bin\SSRS2017 ディレクトリにあります；SSRS 2019 アセンブリは \Bin\SSRS2019 ディレクトリにあります；SSRS 2022 アセンブリは \Bin\SSRS2022 ディレクトリにあります；Power BI Report Server アセンブリは \Bin\PowerBI ディレクトリにあります。 

{{% alert color="primary" %}}

**Step 1.** Report Server のインストールディレクトリを見つけます。Microsoft SQL Server のルートディレクトリは通常 C:\Program Files\Microsoft SQL Server です。以降の手順は、Reporting Services 2016、Reporting Services 2017 以降、および Power BI Report Server で若干異なります。

- Report Server 2016 はデフォルトで C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer ディレクトリにインストールされます。デフォルト以外のカスタム名インスタンスを使用している場合、デフォルトのパスは C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer になります。
- Report Server 2017 以降はデフォルトで C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer ディレクトリにインストールされます。
- Power BI Report Server はデフォルトで C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer ディレクトリにインストールされます。

以下のテキストでは、Reporting Services のインストールディレクトリ（前述のパスのうちの1つ）を次のように参照します ```<Instance>```.
{{% /alert %}}

{{% alert color="primary" %}}
**Step 2.** 対応する SSRS バージョン用の Aspose.Pdf.ReportingServices.dll をコピーします ```<Instance>```\bin フォルダー。
{{% /alert %}}

{{% alert color="primary" %}}
**Step 3.** Aspose.Pdf for Reporting Services をレンダリング拡張機能として登録します。開く ```<Instance>```\rsreportserver.config ファイルに、次の行を追加してください ```<Render>``` 要素:
{{% /alert %}}

**例**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Step 4.** Aspose.Pdf for Reporting Services に実行権限を付与してください。```<Instance>```\rssrvpolicy.config ファイルを開き、次のテキストを 2 番目から外側の ```<CodeGroup>``` 要素の最後の項目として追加します（この要素は ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):``` である必要があります）。
{{% /alert %}}

**例**

{{< highlight csharp >}}

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**Step 5.** Aspose.Pdf for Reporting Services が正常にインストールされたことを確認します。Reporting Services の Web ポータルを開き、レポートの利用可能なエクスポート形式の一覧を確認します。Web ブラウザーを起動し、アドレスバーに Reporting Services の Web ポータル URL を入力することでポータルを起動できます（既定では http://```<Reporting_Services_server_name>```/reports/). 利用可能なレポートの1つをWebポータルで選択し、エクスポートのドロップダウンリストを開きます。Aspose.Pdf for Reporting Services拡張機能が提供する形式を含むエクスポート形式のリストが表示されるはずです。Aspose.PDFを使用したPDF項目を選択します。

 
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

選択した項目をクリックしてください。選択した形式でレポートが生成され、クライアントに送信されます。そして、Web ブラウザーの設定に応じて、エクスポートされたレポートを保存する場所を選択するための Save File ダイアログを表示するか、または自動的にファイルをダウンロード フォルダーに保存します。

{{% alert color="primary" %}}
おめでとうございます。Aspose.Pdf for Reporting Services のインストールに成功し、レポートを PDF 文書としてエクスポートしました！
{{% /alert %}}







