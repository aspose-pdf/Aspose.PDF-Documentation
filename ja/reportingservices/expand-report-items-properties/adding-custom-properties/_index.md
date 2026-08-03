---
title: カスタムプロパティの追加
linktitle: カスタムプロパティの追加
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: Aspose.PDF for Reporting Services を使用して PDF レポートにカスタム プロパティを追加する方法を学びます。ドキュメントを効率的にカスタマイズします。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

一部のレポート アイテムにカスタム プロパティを追加して、目次、線の矢印などの使用方法を拡張できます。このセクションでは、このプロセスについて説明します。

{{% /alert %}}

一部のレポート アイテムにカスタム プロパティを追加して、目次、線の矢印などの用途を拡張できます。このセクションでは、このプロセスについて説明します。

カスタム プロパティを追加するには、次の手順で RDL ドキュメントのコード ファイルを編集する必要があります。

1. 次の図のように、プロジェクトを開いてソリューション エクスプローラーに移動し、選択したレポート ファイルを右クリックして、[コードの表示] メニュー項目を選択します。

![Add Custom Properties](adding-custom-properties_1.png)

2. XMLコードファイルを編集します。たとえば、グラフ レポート アイテムのカスタム プロパティを追加する場合は、次の例の赤いテキストのようなコードを追加する必要があります。

## 例

```xml
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
```

このコード例では、カスタム プロパティ名は IsInList、値は `True` です。

