---
title: FDF、XML、XFDF形式の違いとは
type: docs
weight: 30
url: ja/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: このセクションでは、Aspose.PDF Facadesを使用したXML、FDF、およびXFDFフォームの違いについて説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

FDF、XML、XFDFのような多くの異なる用語を混在させました。これらの用語はどれも何らかの形で関連しています。この記事では、これらの概念とそれらの相互関係について探ります。

{{% /alert %}}

## フォームの解明

Aspose.PDF for .NETは、Adobeにより標準化されたPDFドキュメントを操作するために使用されます。そして、PDFドキュメントにはAcroFormsと呼ばれるインタラクティブなフォームが含まれています。これらのインタラクティブなフォームには、コンボ、テキストボックス、ラジオボタンなどの多くのフォームフィールドがあります。Adobeのインタラクティブフォームとフォームフィールドは、HTMLフォームとそのフォームフィールドと同じように機能します。

フォームフィールドの値を別のファイルに保存することが可能です：FDF（Forms Data Format）ファイルです。
``` このドキュメントには、キー/ペア形式でのフォームフィールドの値が含まれています。FDFファイルはこの目的のためにまだ使用されています。しかし、AdobeはXFDFと呼ばれるXMLエンコードされたタイプのFDFも提供しています。XFDFファイルは、XMLタグを使用してフォームフィールドの値を階層的に保存します。

Aspose.PDFを使用すると、開発者はPDFフォームフィールドの値をFDFまたはXFDFファイルにエクスポートするだけでなく、XMLファイルにもエクスポートできます。これらのファイルはすべて、PDFフォームフィールドの値を保存するために異なる構文を使用します。以下の例は、その違いを説明しています。

PDFフォームフィールドの値をFDF、XML、XFDF形式で提示する必要があると仮定します。これらの仮定されたフォームフィールドのフィールド名と値は以下の通りです：

|**Field Name**|**Field Value**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Additional Address Line|

これらの値をFDF、XML、XFDF形式でどのように表現するか見てみましょう。

### FDF形式とは？

FDFファイルはキー/ペア形式でデータを保存し、/Tがキーを表し、/Vが値を表し、括弧（）内のデータがキーまたは値の内容を表すことを私たちは知っています。 /T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(追加の住所行)

### XML形式とは何ですか？

開発者は、各PDFフォームフィールドをフィールドタグ`<field>`の形式で表現できます。各フィールドタグには、フィールド名を示す属性名と、フィールド値を表すサブタグ`<value>`があります。以下に示します:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>追加の住所行</value>
  </field>
 </fields>
```

### XFDF形式とは何ですか？

上記のデータをXFDF形式で表現することは、XML形式と似ていますが、いくつかの違いがあります。 XFDFファイルでは、XML Namespaceを追加します。これは<http://ns.adpbe.com/xfdf/>であり、これらのPDFフォームフィールドを含むPDFドキュメントを指すために使用される追加のタグ`<f>`があります。XMLのように、XFDFも以下に示すように、フィールドタグ`<field>`の形式でフィールドを含みます:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### フォームフィールド名の識別

Aspose.PDF for .NETは、既に作成されたPDFフォームを作成、編集、および入力する機能を提供します。 それは [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) クラスを含んでおり、[FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) という名前の関数があり、2つのパラメータ、すなわち入力する必要があるフィールド名とフィールド値を取ります。したがって、フォームフィールドを入力するためには、正確なフォームフィールド名を把握している必要があります。私たちはよく、あるツールで作成されたフォームを入力する必要があるシナリオに遭遇します。 Adobe Designer、そしてフォームフィールド名について確信が持てません。要求を達成するためには、すべてのPDFフォームフィールドの名前を読み取る必要があります。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) クラスは、[FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) というプロパティを提供しており、これによりすべてのフィールド名が返され、PDFにフィールドがない場合はnullを返します。しかし、このプロパティはすべてのPDFフォームフィールドの名前を返し、どの名前がフォーム上のどのフィールドに対応しているかは不明です。

この問題の解決策として、各フィールドの外観属性が必要になります。 [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) クラスには、位置、色、境界スタイル、フォント、リストアイテムなどの属性を返す GetFieldFacade という名前の関数があります。これらの値を保存するために、フィールドの視覚的属性を記録するために使用される [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) クラスを使用します。これらの属性を取得したら、すべてのフィールドの下にフィールド名を表示するテキストフィールドを追加できます。ここで、テキストフィールドを追加する場所をどのように決定するかという問題が生じます。この問題の解決策は、フィールドの位置を保持する [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) クラスの Box プロパティです。これらの値を矩形タイプの配列に保存し、これらの値を使用して新しいテキストフィールドを追加する位置を特定します。  
Aspose.Pdf.Facades 名前空間には、PDF フォームを操作する機能を提供する [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) という名前のクラスがあります。 Open a PDFフォームを開き、既存のすべてのフォームフィールドの下にテキストフィールドを追加し、新しい名前でPDFフォームを保存します。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}