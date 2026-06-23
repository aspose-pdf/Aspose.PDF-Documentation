---
title: Justify FullJustify テキスト配置
linktitle: Justify FullJustify テキスト配置
type: docs
weight: 40
url: /ja/reportingservices/justify-fulljustify-text-alignment/
description: Aspose.PDF for Reporting Services を使用して、PDF レポートで完璧なテキスト配置を実現します。justify と full justify のオプションをサポートします。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

レポート ビルダーはテキストボックス「Justify」および「FullJustify」のテキスト配置を指定する機能をサポートしていません。Aspose.Pdf for Reporting Services を使用すれば、カスタム プロパティを追加するだけで簡単に実現できます。

{{% /alert %}}

{{% alert color="primary" %}}
**カスタム プロパティ名** : TextAlignment  
**カスタム プロパティ タイプ** : String  
**カスタム プロパティ 値** : Justify, FullJustify  

レポートでは、コードは次のようにする必要があります:

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

