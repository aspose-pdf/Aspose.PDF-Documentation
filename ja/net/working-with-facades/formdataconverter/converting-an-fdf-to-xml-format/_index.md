---
title: FDFをXML形式に変換する
type: docs
weight: 10
url: /ja/net/converting-an-fdf-to-xml-format/
description: このセクションでは、FormDataConverterクラスを使用してFDFをXML形式に変換する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/ja/net/)の[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)名前空間は、AcroFormsを非常によくサポートしています。また、FDF、XFDF、XMLなどの異なるファイル形式へのフォームデータのインポートとエクスポートもサポートしています。しかし、開発者は時々、一つの形式を別の形式に変換する必要があるかもしれません。この記事では、FDFをXMLに変換する機能について説明します。

{{% /alert %}}

## 詳細

FDFはForms Data Formatの略で、FDFファイルにはキー/値のペアでフォームの値が含まれています。 私たちはまた、XMLファイルが値をタグとして含んでいることを知っています。ここで、主にキーはタグ名として表され、値はそのタグ内の値として表されます。現在、[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)はFDFファイル形式をXML形式に変換する柔軟性を提供しています。

この目的のために[FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter)クラスを使用することができます。このクラスは、一つのデータ形式を別の形式に変換するためのさまざまなメソッドを提供します。本記事では、[ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml)という名前のメソッドを1つだけ使用します。このメソッドは、FDFファイルを入力またはソースストリームとして受け取り、それをXML形式で保存します。

次のコードスニペットは、FDFファイルをXMLファイルに変換する方法を示しています:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConvertPdfToXML-ConvertPdfToXML.cs" >}}