---
title: 全行揃えテキストの配置
linktitle: 全行揃えテキストの配置
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Aspose.PDF for Reporting Services を使用して、PDF レポートで完璧なテキストの配置を実現します。両端揃えおよび完全両端揃えオプションのサポート。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート ビルダーは、テキストボックスのテキスト配置を指定する機能をサポートしていません。 `Justify` そして `FullJustify`。 Aspose.PDF for Reporting Services を使用すると、カスタム プロパティを追加することでこれを簡単に行うことができます。

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

レポートのコードは次のようになります。

## 例

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
