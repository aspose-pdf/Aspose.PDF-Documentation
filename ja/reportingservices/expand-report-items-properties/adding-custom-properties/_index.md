---
title: カスタムプロパティの追加
linktitle: カスタムプロパティの追加
type: docs
weight: 10
url: /ja/reportingservices/adding-custom-properties/
description: Aspose.PDF for Reporting Services を使用して PDF レポートにカスタムプロパティを追加する方法を学びましょう。ドキュメントを効率的にカスタマイズできます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

目次やライン矢印など、一部のレポート項目にカスタムプロパティを追加して使用範囲を拡大できます。このセクションではこの手順について説明します。

{{% /alert %}}

{{% alert color="primary" %}}

目次やライン矢印など、一部のレポート項目にカスタムプロパティを追加して使用範囲を拡大できます。このセクションではこの手順について説明します。

カスタム プロパティを追加するには、以下の手順で RDL ドキュメントのコード ファイルを編集する必要があります。

1. 以下の図のように、プロジェクトを開き、ソリューション エクスプローラーへ移動し、対象のレポート ファイルを右クリックして、'View Code' メニュー項目を選択します。

![todo:image_alt_text](adding-custom-properties_1.png)

2. XML コード ファイルを編集します。たとえば、チャート レポート アイテムにカスタム プロパティを追加したい場合は、以下の例の赤いテキストと同様のコードを追加する必要があります。

**例**

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

このコードフラグメント例では、カスタムプロパティ名は IsInList で、値は 'True' です。

{{% /alert %}}

