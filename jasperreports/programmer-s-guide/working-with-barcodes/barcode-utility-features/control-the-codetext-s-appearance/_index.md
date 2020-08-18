---
title: Control the Codetext's Appearance
type: docs
weight: 30
url: /jasperreports/control-the-codetext-s-appearance/
---

{{% alert color="primary" %}} 

Aspose.BarCode for JasperReports provides complete control over the appearance of the codetext in the barcode image. There are many settings that can be applied to the codetext to customize its appearance. These are discussed below.

{{% /alert %}} 
### **Foreground Color**
Developers who want to add colors to their barcodes can change the color of the codetext. The color can be specified in the JRXML file.

**JRXML**

{{< highlight csharp >}}

 <image hAlign="Center">

    <reportElement x="0" y="100" width="500" height="250" />

    <imageExpression class="net.sf.jasperreports.engine.JRRenderable"><![CDATA[new com.aspose.barcode.jr.BarCodeRenderer(com.aspose.barcode.jr.BarCodeAttributesFactory.Create("codetext","DataMatrix",java.awt.Color.BLACK))]]></imageExpression>

</image>

{{< /highlight >}}
