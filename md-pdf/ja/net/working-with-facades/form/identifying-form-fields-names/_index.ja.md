---
title: フォームフィールド名の識別
type: docs
weight: 10
url: /net/identifying-form-fields-names/
description: Aspose.PDF.Facadesは、Formクラスを使用してフォームフィールド名を識別することを可能にします。
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/net/)は、既に作成されたPdfフォームを作成、編集、記入する機能を提供します。[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)名前空間には[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスが含まれており、[FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)という名前の関数が含まれています。この関数は、フィールド名とフィールド値の2つの引数を取ります。したがって、フォームフィールドを記入するためには、正確なフォームフィールド名を知っている必要があります。

## 実装の詳細

よくあるシナリオとして、あるツールで作成されたフォームに記入する必要がある場合があります。 Adobe Designer、そしてフォームフィールドの名前については確信がありません。したがって、フォームフィールドを記入するためには、まずすべてのPDFフォームフィールドの名前を読み取る必要があります。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスは、[FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)というプロパティを提供しており、これはフィールドの全名前を返し、PDFにフィールドが含まれていない場合はnullを返します。ただし、このプロパティを使用すると、PDFフォーム内のフィールド全体の名前を取得できますが、どの名前がフォーム上のどのフィールドに対応しているかを確信できない場合があります。

この問題の解決策として、各フィールドの外観属性を使用します。 Formクラスには、位置、色、境界線スタイル、フォント、リストアイテムなどの属性を返す[GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade)という関数があります。これらの値を保存するには、フィールドの視覚的属性を記録するために使用される[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade)クラスを使用する必要があります。これらの属性を取得したら、フィールド名を表示するフィールドの下にテキストフィールドを追加できます。

{{% alert color="primary" %}}
この時点で、「テキストフィールドを追加する場所をどのように決定するのか？」という疑問が生じます。
{{% /alert %}}

{{% alert color="primary" %}}
この問題の解決策は、フィールドの位置を保持する[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade)クラスのBoxプロパティです。 これらの値を矩形型の配列に保存し、新しいテキストフィールドを追加する位置を特定するためにこれらの値を使用する必要があります。

{{% /alert %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 名前空間には、PDFフォームを操作する機能を提供する [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) というクラスがあります。PDFフォームを開き、既存のすべてのフォームフィールドの下にテキストフィールドを追加し、新しい名前でPDFフォームを保存します。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-IdentifyFormFields-IdentifyFormFields.cs" >}}