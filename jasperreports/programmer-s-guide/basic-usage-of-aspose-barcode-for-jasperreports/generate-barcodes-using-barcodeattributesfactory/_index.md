---
title: Generate Barcodes using BarCodeAttributesFactory
type: docs
weight: 50
url: /jasperreports/generate-barcodes-using-barcodeattributesfactory/
---

{{% alert color="primary" %}} 

The BarCodeAttributesFactory class is also included in the com.aspose.barcode.jr package. This class provides the static overloaded method Create() which accepts arguments like codetext, symbology type, and so on. Choose the overloaded method that suites the task at hand. 

{{% /alert %}} 
### **Generate BarCodes using the BarCodeAttributesFactory**
The BarCodeAttributesFactory.Create() method can be called directly in a JRCML file for generating barcodes. It’s used in the <image> tag, as shown below:

{{< highlight csharp >}}

 <image hAlign="Center">

  <reportElement x="0" y="100" width="500" height="250" />

    <imageExpression class="net.sf.jasperreports.engine.JRRenderable">

<![CDATA[new com.aspose.barcode.jr.BarCodeRenderer(com.aspose.barcode.jr.BarCodeAttributesFactory.Create("codetext","DataMatrix",java.awt.Color.RED))]]>

</imageExpression>

</image>



{{< /highlight >}}

The above code sample comes from a JRXML file that renders a DataMatrix barcode image with the codetext “codetext” and red foreground colour.
#### **Creating a Custom Class**
Generating barcodes using the BarCodeAttributesFactory.Create() method is feasible in those cases when you only need to pass codetext, symbology type and forecolor as parameters. If you want to change other properties, say the border color, background color, bar height, caption, xDimension, or yDimension, do it using a custom class. 

Create a static method in the custom class and create an instance of BarCodeAttributes. You may further call any available setxxx() methods from the BarCodeAttributes class to generate barcodes according to your specific requirements. 

Below is sample code required in the JRXML file for using the custom class.

{{< highlight csharp >}}

 <image>

  <reportElement x="0" y="600"  width="500" height="250" />

  <imageExpression class="net.sf.jasperreports.engine.JRRenderable">

<![CDATA[new com.aspose.barcode.jr.BarCodeRenderer(MyAttributesFactory.Create("test-123","qr",java.awt.Color.RED, "caption above", "caption below"))]]>

</imageExpression>

</image>



{{< /highlight >}}

In the above JRXML code snippet, we used a new class, MyAttributesFactory (will be created later). It’s Create() method takes five arguments:

1. Codetext
1. Symbology type
1. Foreground color
1. Caption above the barcode
1. Caption below the barcode

Next, we will create the **MyAttributesFactory.java** file to create the new class. Below is the code for the MyAttributesFactory class. 

{{< highlight csharp >}}

 import com.aspose.barcode.jr.BarCodeAttributes;

import java.awt.*;

/**

 * A sample factory class to create BarCodeAttributes instances for reports

 */

public class MyAttributesFactory {

    public static BarCodeAttributes Create(String text, String symbology, Color foreColor, String captionAbove, String captionBelow) {

        BarCodeAttributes b = new BarCodeAttributes();

        b.setCodeText(text);

        b.setSymbology(symbology);

        b.setForeColor(foreColor);

        b.setCodeTextVisible(false);

        b.setCaptionAbove(new Caption(captionAbove));

        b.setCaptionBelow(new Caption(captionBelow));

        b.setAutoSize(true);

        return b;

    }

}



{{< /highlight >}}

The Create method in the above class returns an instance of type BarCodeAttributes. Since we are creating the instance ourselves, we can call any available method of the BarCodeAttributes class to customize the barcode image. 
