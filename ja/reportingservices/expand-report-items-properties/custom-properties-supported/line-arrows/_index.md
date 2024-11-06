---
title: 線の矢印
type: docs
weight: 20
url: ja/reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL仕様は線要素についての矢印を指定していないため、レポートビルダーでは線の矢印の設定をサポートしていません。しかし、Aspose.Pdf for Reporting Servicesを使用すると、それを簡単に行うことができます。

{{% /alert %}}

{{% alert color="primary" %}}

現在、Aspose.PDFレンダラーは、カスタムプロパティを追加することにより、線の始点または終点に矢印を追加することをサポートしています。

線の始点に矢印を追加  
**カスタムプロパティ** **名前**: HasArrowAtStart  
**カスタムプロパティ値**: True  

線の終点に矢印を追加  
**カスタムプロパティ** **名前**: HasArrowAtEnd  
**カスタムプロパティ値**: True  

例えば、現在のレポートファイルには 'line1' と 'line2' という名前の2本の線があり、line1には始点の矢印があり、line2には始点と終点の矢印があります。これらの要件を満たすために、以下のコードフラグメントのようにカスタムプロパティを追加することができます。

**例**

{{< highlight csharp >}}

 <Line Name="line1">
```

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
```