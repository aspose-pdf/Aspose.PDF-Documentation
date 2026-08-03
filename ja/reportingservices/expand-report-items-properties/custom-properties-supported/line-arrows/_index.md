---
title: 線の矢印
linktitle: 線の矢印
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Aspose.PDF for Reporting Services を使用して PDF レポートに線の矢印を追加する方法を学習します。レポートのビジュアルを簡単に強化します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL 仕様では線要素に関する矢印が指定されていないため、レポート ビルダーは線の矢印の設定をサポートしていません。 Aspose.PDF for Reporting Services を使用すると、それを簡単に行うことができます。

{{% /alert %}}

現在、Aspose.PDF レンダラーは、カスタム プロパティを追加することで、行の先頭または末尾に矢印を追加することをサポートしています。

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

たとえば、次の 2 つの行があります。 `line1` そして `line2` 現在のレポート ファイルで、行 1 に開始矢印、行 2 に開始矢印と終了矢印がある場合、これらの要件を満たすために、次のコード フラグメントのようにカスタム プロパティを追加できます。

## 例

```xml
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
```

