---
title: ライン矢印
linktitle: ライン矢印
type: docs
weight: 20
url: /ja/reportingservices/line-arrows/
description: Aspose.PDF for Reporting Services を使用して、PDFレポートにライン矢印を追加する方法を学びましょう。レポートのビジュアルを手軽に強化できます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

RDL 仕様ではライン要素の矢印が規定されていないため、Report Builder はラインの矢印設定をサポートしていません。Aspose.Pdf for Reporting Services を使用すれば、簡単に実現できます。

{{% /alert %}}

{{% alert color="primary" %}}

現在、Aspose.PDF レンダラーはカスタムプロパティを追加することで、ラインの開始点または終了点に矢印を追加することをサポートしています。

線の開始矢印を追加  
**カスタム プロパティ** **名前**: HasArrowAtStart  
**カスタム プロパティ値**: True  

線の終了矢印を追加  
**カスタム プロパティ** **名前**: HasArrowAtEnd  
**カスタム プロパティ値**: True  

例えば、現在のレポート ファイルには 'line1' と 'line2' という名前の 2 本の線があり、line1 は開始矢印を持ち、line2 は開始矢印と終了矢印の両方を持ちます。これらの要件を満たすために、以下のコード フラグメントのようにカスタム プロパティを追加できます。

**例**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>
......
<Line Name="line2">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
<CustomProperty>
        <Name>HasArrowAtEnd</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}

