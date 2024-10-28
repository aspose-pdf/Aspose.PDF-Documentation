---
title: XMLをFDF形式に変換する
type: docs
weight: 20
url: /net/converting-an-xml-to-fdf-format/
description: このセクションでは、FormDataConverterを使用してXMLをFDF形式に変換する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 名前空間は、[Aspose.PDF for .NET](/pdf/net/)においてAcroFormsを非常によくサポートしています。また、FDF、XFDF、XMLなどの異なるファイル形式へのフォームデータのインポートとエクスポートもサポートしています。しかし、時にはある形式を別の形式に変換する必要がある場合があります。この記事では、FDF形式をXMLに変換する機能について詳しく見ていきます。

{{% /alert %}}

## 詳細

FDFはForms Data Formatの略で、FDFファイルにはキー/バリューのペアでフォームの値が含まれています。 私たちはまた、XMLファイルがタグとして値を含んでいることを知っています。ここで、主にキーはタグ名として表され、値はそのタグ内の値として表されます。現在、[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)は、XMLファイル形式をFDF形式に変換する柔軟性を提供しています。

この目的のために[FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter)クラスを使用します。このクラスは、あるデータ形式を別のデータ形式に変換するためのさまざまなメソッドを提供します。この記事では、ConvertXmlToFdf(..)という1つのメソッドの使用方法を示します。このメソッドは、FDFファイルを入力またはソースストリームとして受け取り、それをXML形式に保存します。次のコードスニペットは、FDFファイルをXMLファイルに変換する方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-XMLToPdf-XMLToPdf.cs" >}}