---
title: Get Button Option Value
type: docs
weight: 40
url: /net/get-button-option-value/
description: This section explains how to get Button Option Value with Aspose.PDF Facades using Form Class.
lastmod: "2021-06-05"
draft: false
---

## Get Button Option Values from an Existing PDF File

The radion buttons provide a way to show different options. The [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form) class allows you to get all the button option values for a particular radio button. You can get these values using [GetButtonOptionValues](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues) method. This method requires the name of the radio button as input parameter and returns a Hashtable. You can iterate through this Hashtable to get the option values. The following code snippet shows you how to get button option values from existing PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## Get Current Button Option Value from an Existing PDF File

Radio buttons provide a way to set option values, however one of them can be selected at a time. If you want to get the currently selected option value then you can use [GetButtonOptionCurrentValue** method. [Form](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form) class provides this method. The [GetButtonOptionCurrentValue](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) method requires radio button name as input parameter and returns the value as string. The following code snippet shows you how to get current button option value from an existing PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}
