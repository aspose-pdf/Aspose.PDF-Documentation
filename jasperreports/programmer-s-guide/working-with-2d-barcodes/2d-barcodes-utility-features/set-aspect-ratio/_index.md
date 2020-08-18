---
title: Set Aspect Ratio
type: docs
weight: 30
url: /jasperreports/set-aspect-ratio/
---

{{% alert color="primary" %}} 

A barcode's aspect ratio is the width:height ratio. We can control how tall or wide a barcode is by controlling its aspect ratio. 

{{% /alert %}} 
### **Setting Aspect Ratio**
An aspect ratio of 3:2 means that the barcode is 1.5 or 3/2 times wider than it is tall. In other words, the width of the barcode is 1.5 times larger than the height. Below is a Pdf417 barcode with an aspect ration of 1.5

**PDF417 barcode with an aspect ratio of 1.5** 

![todo:image_alt_text](set-aspect-ratio_1.png)

An aspect ratio of 2 means that the barcode's width is twice its height. Below is a Pdf417 barcode with an aspect ratio of 2. 

**PDF417 barcode with an aspect ratio of 2** 

![todo:image_alt_text](set-aspect-ratio_2.png)

The code below shows how to set the aspect ratio in Java.

**Java**

{{< highlight csharp >}}

 public class MyAttributes

{

    public static BarCodeAttributes Create(String text, String symbology)

    {

        BarCodeAttributes b = new BarCodeAttributes();

        b.setCodeText(text);

        b.setSymbology(symbology);

        // Set Aspect Ratio to 3:2 or 1.5

        b.setPDF417AspectRatio(1.5f);

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

      "1234567890", "PDF417")

   )]]>

</imageExpression>

</image>



{{< /highlight >}}
