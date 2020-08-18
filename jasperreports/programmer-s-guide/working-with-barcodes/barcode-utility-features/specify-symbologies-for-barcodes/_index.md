---
title: Specify Symbologies for Barcodes
type: docs
weight: 10
url: /jasperreports/specify-symbologies-for-barcodes/
---

### **What are Barcodes?**
Barcode is a system for automatic identification of items, such as books in a library, by means of printed bars of different widths, which represent numbers. Barcodes are used for many reasons among them are, to speed up checkout, to track sales and to help with inventory. The first set of numbers in a barcode is the manufacturer code. The second set of numbers in the barcode is the product code. The barcode was introduced in the early 80s and is often printed on the record sleeve only, sometimes also on the center record paper label.
### **What are Barcode Symbologies?**
Barcode Symbology is the protocol that defines a standard for arranging the bars and spaces (between the bars) that comprise a particular type of barcode, such as UPCA, EAN, Code128, etc.
#### **Barcode Symbologies Supported in Aspose.BarCode**
Aspose.BarCode supports nearly all popular barcode symbologies. The symbology can be set either using the JRXML file or a custom barcode attributes factory.

A list of all pre-defined symbologies in Symbology enumeration are listed below.

|**Symbologies**|**Description**|
| :- | :- |
|Codabar|Specifies that the data should be encoded with Codabar barcode specification.|
|Code11|Specifies that the data should be encoded with Code11 barcode specification.|
|Code128|Specifies that the data should be encoded with Code128 barcode specification.|
|Code39Standard|Specifies that the data should be encoded with Standard Code39 barcode specification.|
|Code39Extended|Specifies that the data should be encoded with Extended Code39 barcode specification.|
|Code93Standard|Specifies that the data should be encoded with Standard Code93 barcode specification.|
|Code93Extended|Specifies that the data should be encoded with Extended Code93 barcode specification.|
|EAN13|Specifies that the data should be encoded with EAN-13 barcode specification.|
|EAN8|Specifies that the data should be encoded with EAN-8 barcode specification.|
|BooklandEAN|Specifies that the data should be encoded with [BooklandEAN](http://www.aspose.com/wiki/wikiedit.aspx?topic=Aspose.BarCode.BooklandEAN&return=Aspose.BarCode.SpecifySymbologies) barcode specification.|
|Interleaved2of5|Specifies that the data should be encoded with Interleaved 2 of 5 barcode specification.|
|MSI|Specifies that the data should be encoded with MSI Plessey barcode specification.|
|Standard2of5|Specifies that the data should be encoded with Standard 2 of 5 barcode specification.|
|UPCA|Specifies that the data should be encoded with UPC-A barcode specification.|
|UPCE|Specifies that the data should be encoded with UPC-E barcode specification.|
|Postnet|Specifies that the data should be encoded with Postnet barcode specification.|
|Planet|Specifies that the data should be encoded with Planet barcode specification.|
|Pdf417|Specifies that the data should be encoded with Pdf417 barcode specification.|
|Datamatrix|Specifies that the data should be encoded with Datamatrix barcode specification.|
|QR|Specifies that the data should be encoded with QR barcode specification.|
|Aztec|Specifies that the data should be encoded with Aztec barcode specification.|
|SwissPostParcel|Specifies that the data should be encoded with Swiss Post Parcel barcode specification.|
|IATA|Specifies that the data should be encoded with IATA barcode specification.|
|RM4SCC|Specifies that the data should be encoded with RM4SCC barcode specification.|
|Matrix|Specifies that the data should be encoded with Matrix barcode specification.|
|Italian Post 25|Specifies that the data should be encoded with Italian Post 25 barcode specification.|
|Code32|Specifies that the data should be encoded with Code32 barcode specification.|
|DataLogic|Specifies that the data should be encoded with Data Logic barcode specification.|
|DutchKIX|Specifies that the data should be encoded with Dutch KIX barcode specification.|
|UpcaGs1Code128Coupon|Specifies that the data should be encoded with UpcaGs1Code128 Coupon barcode specification.|
|UpcaGs1DatabarCoupon|Specifies that the data should be encoded with UpcaGs1Databar Coupon barcode specification.|
#### **Code Sample**
**JRXML**

{{< highlight csharp >}}

 <image hAlign="Center">

    <reportElement x="0" y="100" width="500" height="250" />

    <imageExpression class="net.sf.jasperreports.engine.JRRenderable"><![CDATA[new com.aspose.barcode.jr.BarCodeRenderer(com.aspose.barcode.jr.BarCodeAttributesFactory.Create("codetext","DataMatrix",java.awt.Color.BLACK))]]></imageExpression>

</image>



{{< /highlight >}}
