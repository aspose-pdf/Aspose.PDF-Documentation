---
title: Generate AustraliaPost Barcode with Different Format Control Code Options
type: docs
weight: 50
url: /jasperreports/generate-australiapost-barcode-with-different-format-control-code-options/
---

{{% alert color="primary" %}} 

AustraliaPost barcode can be generated using following format control code options:

1. Standard
1. ReplyPaid
1. Customer2
1. Customer3
1. Routing
1. Redirection

These control code can be applied using the BarCodeAttributes.setAustraliaPostFormatControlCode() method. 

{{% /alert %}} 
### **Programming Sample**
The following code snippet generates a AustraliaPost barcode with standard format control code.

**Java**

{{< highlight csharp >}}

 public class MyAttributes

{

    public static BarCodeAttributes Create(String text, String symbology)

    {

        BarCodeAttributes b = new BarCodeAttributes();

        b.setCodeText(text);

        b.setSymbology(symbology);

        b.setAustraliaPostFormatControlCode(AustraliaPostFormatControlCode.Standard);

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

      "12345678", "AustraliaPost")

   )]]>

</imageExpression>

</image>



{{< /highlight >}}

The above code generates the following image using the standard format control code.

![todo:image_alt_text](generate-australiapost-barcode-with-different-format-control-code-options_1.png)




Image samples using the other format control codes are shown below.

**Customer2** 

![todo:image_alt_text](generate-australiapost-barcode-with-different-format-control-code-options_2.png)

**Customer3** 

![todo:image_alt_text](generate-australiapost-barcode-with-different-format-control-code-options_3.png)

**Redirection** 

![todo:image_alt_text](generate-australiapost-barcode-with-different-format-control-code-options_4.png)

**ReplyPaid** 

![todo:image_alt_text](generate-australiapost-barcode-with-different-format-control-code-options_5.png)

**Routing** 

![todo:image_alt_text](generate-australiapost-barcode-with-different-format-control-code-options_6.png)
