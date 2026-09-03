---
title: Justify FullJustify Text Alignment
linktitle: Justify FullJustify Text Alignment
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Achieve perfect text alignment in PDF reports with Aspose.PDF for Reporting Services. Support for justify and full justify options.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Report builder does not support the capability to specify text alignment for textbox `Justify` and `FullJustify`. With Aspose.PDF for Reporting Services, you can do that easily by adding custom properties.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

In report the code should be like the following:

## Example

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
