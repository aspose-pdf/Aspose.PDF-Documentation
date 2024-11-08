```
---
title: 両端揃え（Justify FullJustify）テキスト配置
type: docs
weight: 40
url: /ja/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポートビルダーは、テキストボックスの「Justify」と「FullJustify」のテキスト配置を指定する機能をサポートしていません。Aspose.Pdf for Reporting Servicesを使用することで、カスタムプロパティを追加することで簡単にそれを行うことができます。

{{% /alert %}}

{{% alert color="primary" %}}
**カスタムプロパティ名** : TextAlignment  
**カスタムプロパティタイプ** : String  
**カスタムプロパティ値** : Justify, FullJustify  

レポートでのコードは次のようになります：

**例**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}
```