---
title: カスタムプロパティの追加
type: docs
weight: 10
url: ja/reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート項目の使用を拡張するために、カスタムプロパティを追加できます。たとえば、ToC、ライン矢印などです。このセクションでは、このプロセスについて説明します。

{{% /alert %}}

{{% alert color="primary" %}}

レポート項目の使用を拡張するために、カスタムプロパティを追加できます。たとえば、目次、ライン矢印などです。このセクションでは、このプロセスについて説明します。

カスタムプロパティを追加するには、以下の手順でRDLドキュメントのコードファイルを編集する必要があります。

1. 次の図のように、プロジェクトを開き、ソリューションエクスプローラに移動し、選択したレポートファイルを右クリックして、「コードの表示」メニュー項目を選択します。

![todo:image_alt_text](adding-custom-properties_1.png)

2. XMLコードファイルを編集します。たとえば、チャートレポート項目にカスタムプロパティを追加したい場合は、次の例の赤いテキストに似たコードを追加する必要があります。

**Example**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

このコード断片の例では、カスタムプロパティ名は IsInList で、値は 'True' です。

{{% /alert %}}