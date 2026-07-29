---
title: カスタム プロパティの追加
linktitle: カスタム プロパティの追加
type: docs
weight: 10
url: /ja/reportingservices/adding-custom-properties/
description: Aspose.PDF for Reporting Services を使用して PDF レポートにカスタム プロパティを追加する方法を学びます。ドキュメントを効率的にカスタマイズできます。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

ToC や線矢印など、一部のレポート アイテムの使用範囲を拡大するためにカスタム プロパティを追加できます。このセクションではそのプロセスについて説明します。

{{% /alert %}}

{{% alert color="primary" %}}

目次、線矢印など、一部のレポート アイテムの使用範囲を拡大するためにカスタム プロパティを追加できます。このセクションではそのプロセスについて説明します。

カスタムプロパティを追加するには、次の手順で RDL ドキュメントのコードファイルを編集する必要があります。

1. 以下の図のように、プロジェクトを開き、ソリューション エクスプローラーへ移動し、選択したレポート ファイルを右クリックして、\u0027View Code\u0027 メニュー項目を選択します。

![todo:image_alt_text](adding-custom-properties_1.png)

2. XML コード ファイルを編集します。たとえば、チャート レポート アイテムにカスタム プロパティを追加したい場合は、以下の例の赤いテキストに似たコードを追加する必要があります。

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
        <Name>リスト内か</Name>
        <Value>真</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

このコードフラグメント例では、カスタムプロパティ名は IsInList で、値は 'True' です。

{{% /alert %}}
