---
title: Using Barcode and Barcode Expression Tags in Report (JRXML) Files
type: docs
weight: 40
url: /jasperreports/using-barcode-and-barcode-expression-tags-in-report-jrxml-files/
---

{{% alert color="primary" %}} 

<bc:asposebarcode> and <bc:barCodeAttributesExpression> are special tags used in JasperReport files (JRXML) for rendering barcode images in reports with Aspose.BarCode for JasperReports library.

These tags can be used in two ways:

1. Print barcodes based on [parameter values](/barcode/jasperreports/using-barcode-and-barcode-expression-tags-in-report-28jrxml-29-files-html/), or
1. print barcodes based on [field values](/barcode/jasperreports/using-barcode-and-barcode-expression-tags-in-report-28jrxml-29-files-html/) (using a data source).

This article explains how to use them.

{{% /alert %}} 
### **Print Barcodes Based on Parameter Values**
The code example below is an example of how bacodes can be rendered based on parameter values.

[**XML**](/pages/createpage.action?spaceKey=barcodejasperreports&title=XML&linkCreation=true&fromPageId=14221351)

{{< highlight csharp >}}

 <componentElement>

   <reportElement x="0" y="70" width="400" height="150"/>

     <bc:asposebarcode

             xmlns:bc="http://jasperreports.sourceforge.net/jasperreports/asposebarcode"

                        xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/asposebarcode

							http://jasperreports.sourceforge.net/xsd/barcode.xsd">

                    <bc:barCodeAttributesExpression>$P{barCodeAttributes1}</bc:barCodeAttributesExpression>

    </bc:asposebarcode>

</componentElement>



{{< /highlight >}}

$P(barCodeAttributes1) is the text inside the <bc:barCodeAttributesExpression> tag. It specifies that it expects a parameter whose name is “barCodeAttributes1” of the parameter type “BarCodeAttributes”, defined in the **com.aspose.barcode.jr** package. 

Before using the parameter, degine it. It can be defined in a JRXML file as shown below.

{{< highlight csharp >}}

 <parameter name="barCodeAttributes1" class="com.aspose.barcode.jr.BarCodeAttributes"/> 

{{< /highlight >}}

JRXML files define the report. Pass the barCodeAttributes1 parameter from the Java source file. 
Below is sample code for passing a parameter.

{{< highlight csharp >}}

 Map<String, BarCodeAttributes> parameters = new HashMap<String, BarCodeAttributes>();

parameters.put("barCodeAttributes1", new BarCodeAttributes("123456", "code11"));

{{< /highlight >}}

In the above Java source file, we created an instance of type Map<key, value>. String type is used as the key and the BarCodeAttributes type is used as the value. 

After declaration, we added one element to the map. The key given is “barCodeAttributes1” and its value is of type “BarCodeAttributes”. Its constructor takes the codetext and symbology type as arguments. Both codetext and the symbology type are passed as string values. Based on the code snippets above, then, this code will create a Code11 barcode image in the report with the codetext “123456”. 
### **Print BarCodes Based on Field Values (Using a Data Source)**
Below is code snippet from a JRXML file which renders barcode images from a data source. The ID field is used as codetext.

[**XML**](/pages/createpage.action?spaceKey=barcodejasperreports&title=XML&linkCreation=true&fromPageId=14221351)

{{< highlight csharp >}}

 <componentElement>

    <reportElement x="0" y="4" width="315" height="150"/>

    <bc:asposebarcode

            xmlns:bc="http://jasperreports.sourceforge.net/jasperreports/asposebarcode"

            xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/asposebarcode

	http://jasperreports.sourceforge.net/xsd/barcode.xsd">

        <bc:barCodeAttributesExpression>$F{id}</bc:barCodeAttributesExpression>

    </bc:asposebarcode>

</componentElement>



{{< /highlight >}}

$F(id) means that a field called is “id” is required. The id field's type should be “BarCodeAttributes”. Below, the "id" field is defined in the JRXML file.

{{< highlight csharp >}}

 <field name="id" class="com.aspose.barcode.jr.BarCodeAttributes"/>  

{{< /highlight >}}

In the Java source file, pass a data source to the JRXML file. For this example, we use a custom class inherited from JRDataSource. And in the getFieldValue() method, return an instance of type “BarCodeAttributes”, which will be used by the <bc> tags in JRXML files for rendering barcodes. 

For more details about using a data source in JasperReports, please read [Printing Barcodes in a Report that uses a Data Source](/barcode/jasperreports/printing-barcodes-in-a-report-that-uses-a-data-source-html/). 
