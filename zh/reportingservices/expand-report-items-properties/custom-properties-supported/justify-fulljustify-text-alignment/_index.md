---
title: Justify FullJustify 文本对齐
linktitle: Justify FullJustify 文本对齐
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: 使用 Aspose.PDF for Reporting Services 在 PDF 报告中实现完美的文本对齐。支持对齐和完全对齐选项。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报表生成器不支持为文本框指定文本对齐方式的功能 `Justify` 和 `FullJustify`。借助 Aspose.PDF for Reporting Services，您可以通过添加自定义属性轻松实现这一点。

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

报告中的代码应如下所示：

## 例子

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
