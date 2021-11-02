---
title: Changing field appearance and attributes
type: docs
weight: 20
url: /net/changing-field-appearance-and-attributes/
description: This section explains how you can change field appearance and attributes with FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) class of [Aspose.Pdf.Facades namespace](https://apireference.aspose.com/pdf/net/aspose.pdf.facades) allows you to not only change the look and feel of the form field, but also the behavior of the field. In this article, we will see how we can use FormEditor class to change the field appearance, field attributes, and the field limit as well.

{{% /alert %}}

## Implementation details

[SetFieldAppearance](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) method is used to the change the appearance of a form field. It takes AnnotationFlag as a parameter. AnnotationFlag is an enumeration which has different members like Hidden or NoRotate etc.

[SetFieldAttributes](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) method is used to change the attribute of a form field. A parameter passed to this method is PropertyFlag enumeration which contains members like ReadOnly or Required etc.

[FormEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) class also provides a method to set the field limit. It tells the field that how much characters it can be filled with. The bellow code snippet shows you how all of these methods can be used.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}
