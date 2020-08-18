---
title: Set Start and Stop Symbols of Codabar Barcode
type: docs
weight: 60
url: /jasperreports/set-start-and-stop-symbols-of-codabar-barcode/
---

{{% alert color="primary" %}} 

The Codabar barcode has the following structure:

1. Start Symbol at the beginning (A, B, C or D)
1. Data to be encoded
1. End symbol (A, B, C or D)

You can customize the start and stop symbols according to your requirements, using BarCodeAttributes.setCodabarStartSymbol() and BarCodeAttributes.setCodabarStopSymbol() methods.

{{% /alert %}} 
### **Programming Sample**
In the code below, we set A as the start symbol and D as the stop symbol for the Codabar barcode. 

**Java**

{{< highlight csharp >}}

 public class MyAttributes

{

    public static BarCodeAttributes Create(String text, String symbology)

    {

        BarCodeAttributes b = new BarCodeAttributes();

        b.setCodeText(text);

        b.setSymbology(symbology);

        b.setCodabarStartSymbol(CodabarSymbol.A);

        b.setCodabarStopSymbol(CodabarSymbol.D);

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

      "12345678", "CODABAR")

   )]]>

</imageExpression>

</image>



{{< /highlight >}}
