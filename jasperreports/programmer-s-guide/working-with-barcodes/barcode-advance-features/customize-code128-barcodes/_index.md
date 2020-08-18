---
title: Customize Code128 Barcodes
type: docs
weight: 70
url: /jasperreports/customize-code128-barcodes/
---

{{% alert color="primary" %}} 

Code128 barcode can be generated using 3 different code/character sets. 

1. Code A
1. Code B
1. Code C

These code sets can be specified using BarCodeAttributes.setCode128Set() method. Aspose.BarCode also provides the option to set the codeset as Auto, to choose the best possible code set internally. 

{{% /alert %}} 
### **Programming Sample**
In the below code snippet, we set the Code128 code set to Auto and generate a Code128 barcode.

**Java**

{{< highlight csharp >}}

 public class MyAttributes

{

    public static BarCodeAttributes Create(String text, String symbology)

    {

        BarCodeAttributes b = new BarCodeAttributes();

        b.setCodeText(text);

        b.setSymbology(symbology);

        b.setCode128Set(Code128Set.AUTO);

        return b;

    }

}



{{< /highlight >}}

**JRXML**

{{< highlight csharp >}}

 <image hAlign="Center">

<reportElement x="0" y="600"  width="500" height="250" />                

<imageExpression class="net.sf.jasperreports.engine.JRRenderable">

   <![CDATA[new com.aspose.barcode.jr.BarCodeRenderer(MyAttributes.Create(

      "12345678", "Code128")

   )]]>

</imageExpression>

</image>



{{< /highlight >}}
