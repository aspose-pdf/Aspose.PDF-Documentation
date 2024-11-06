---
title: フィールドの外観と属性
type: docs
weight: 20
url: ja/net/changing-field-appearance-and-attributes/
description: このセクションでは、FormEditorクラスを使用してフィールドの外観と属性を変更する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) クラスは、[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) に属しており、フォームフィールドの外観や感触だけでなく、フィールドの動作も変更することができます。この記事では、FormEditorクラスを使用してフィールドの外観、属性、およびフィールドの制限を変更する方法を見ていきます。

{{% /alert %}}

## 実装の詳細

[SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) メソッドは、フォームフィールドの外観を変更するために使用されます。 パラメーターとしてAnnotationFlagを取ります。AnnotationFlagは、HiddenやNoRotateなどの異なるメンバーを持つ列挙型です。

[SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute)メソッドは、フォームフィールドの属性を変更するために使用されます。このメソッドに渡されるパラメーターは、ReadOnlyやRequiredなどのメンバーを含むPropertyFlag列挙型です。

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor)クラスは、フィールドの制限を設定するためのメソッドも提供します。フィールドがどれだけの文字を埋めることができるかを伝えます。以下のコードスニペットは、これらすべてのメソッドをどのように使用できるかを示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}