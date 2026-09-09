---
title: パラメータの設定
linktitle: パラメータの設定
type: docs
weight: 10
url: /ja/reportingservices/setting-parameters/
description: Aspose.PDF for Reporting Services で PDF レンダリング用のパラメータを設定し、出力を正確に制御する方法を説明します。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services がドキュメントを生成する方法に影響する特定の設定パラメータを指定できます。このセクションでは、その手順を説明します。

{{% /alert %}}

Aspose.PDF for Reporting Services を設定するには、`C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config` ファイルを編集する必要があります。これは XML ファイルで、レンダラーの設定は Aspose.PDF レンダラーに対応する ```<Extension>``` 要素の中にあります。

**例**

{{< highlight csharp >}}

<Render>
...
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

サーバー上のすべてのレポートではなく、特定のレポートファイルだけにパラメータを設定したい場合は、Report Builder でそのレポートにレポートパラメータを追加できます。以下の手順では、先ほど示した `IsLandscape` パラメータを追加する例を使用します。

1. Report Designer でレポートを開き、`Report Data` ペインの `Parameters` フォルダを右クリックして `Add Parameter...` を選択します。別の方法として、`New` リストを開いて `Parameter...` を選択してもかまいません。
 
![todo:image_alt_text](setting-parameters_1.png)

1. `Report Parameter Properties` ダイアログで `IsLandscape` という名前のパラメータを作成し、データ型を Boolean に設定したうえで、`Default Values` タブに True を追加します。

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

