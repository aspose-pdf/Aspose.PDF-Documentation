---
title: ライン矢印
linktitle: ライン矢印
type: docs
weight: 20
url: /ja/reportingservices/line-arrows/
description: Aspose.PDF for Reporting Services を使用して PDF レポートにライン矢印を追加する方法を学びましょう。レポートのビジュアルを手軽に強化できます。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

RDL 仕様ではライン要素に関する矢印が規定されていないため、Report Builder はラインの矢印設定をサポートしていません。Aspose.PDF for Reporting Services を使用すれば、簡単に実現できます。

{{% /alert %}}

{{% alert color="primary" %}}

現在、Aspose.PDF レンダラーはカスタム プロパティを追加することで、ラインの開始点または終了点に矢印を追加することをサポートしています。

ラインに開始矢印を追加  
**カスタム プロパティ** **名前**: HasArrowAtStart  
**カスタム プロパティ 値**: True  

ラインに終了矢印を追加  
**カスタム プロパティ** **名前**: HasArrowAtEnd  
**カスタム プロパティ 値**: True  

例えば、現在のレポートファイルに 'line1' と 'line2' という名前の 2 本の線があり、line1 は開始矢印が、line2 は開始矢印と終了矢印が設定されています。これらの要件を満たすには、以下のコードフラグメントのようにカスタム プロパティを追加できます。

**例**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>開始に矢印がある</Name>
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
        <Name>開始に矢印がある</Name>
        <Value>True</Value>
      </CustomProperty>
<CustomProperty>
        <Name>終端に矢印がある</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
