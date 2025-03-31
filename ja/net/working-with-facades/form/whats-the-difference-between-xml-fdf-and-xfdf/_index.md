---
title: FDF、XML、およびXFDF形式の違い
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: このセクションでは、Aspose.PDF Facadesを使用して、XML、FDF、およびXFDFフォームの違いについて説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NETを通じてPDFフォームデータ操作におけるFDF、XML、およびXFDF形式の違いを発見してください。この機能により、開発者は各形式の独自の構文を持つさまざまな形式でインタラクティブなフォームフィールドの値をシームレスにエクスポートでき、PDF処理におけるこれらの重要なファイルタイプの理解と使用を向上させます。異なるデータ形式でフォームフィールドを表現する方法に関する詳細な洞察を得て、PDFフォームの取り扱いを最適化してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

FDF、XML、XFDFなどのさまざまな用語が混在しています。これらの用語は、何らかの形で互いに関連しています。この記事では、これらの概念とそれらの相互関係を探ります。

{{% /alert %}}

## フォームの解明

Aspose.PDF for .NETは、Adobeによって標準化されたPDF文書を操作するために使用されます。PDF文書には、AcroFormsと呼ばれるインタラクティブなフォームが含まれています。これらのインタラクティブなフォームには、コンボ、テキストボックス、ラジオボタンなどの多くのフォームフィールドがあります。Adobeのインタラクティブフォームとフォームフィールドは、HTMLフォームとそのフォームフィールドと同様に機能します。

フォームフィールドの値を別のファイルに保存することが可能です：FDF（Forms Data Format）ファイルです。これは、キー/ペア形式でフォームフィールドの値を含みます。FDFファイルは、今でもこの目的で使用されています。しかし、AdobeはXFDFと呼ばれるFDFのXMLエンコードタイプも提供しています。XFDFファイルは、XMLタグを使用して階層的にフォームフィールドの値を保存します。

Aspose.PDFを使用すると、開発者はPDFフォームフィールドの値をFDFまたはXFDFファイルだけでなく、XMLファイルにもエクスポートできます。これらのファイルはすべて、PDFフォームフィールドの値を保存するために異なる構文を使用します。以下の例では、違いを説明します。

PDFフォームフィールドの値をFDF、XML、およびXFDF形式で表示する必要があると仮定しましょう。これらの仮定されたフォームフィールドのフィールド名と値は以下の通りです：

|**フィールド名**|**フィールド値**|
| :- | :- |
|会社|Aspose.com|
|住所.1|オーストラリア、シドニー|
|住所.2|追加の住所行|
これらの値をFDF、XML、およびXFDF形式で表現する方法を見てみましょう。

### FDF形式とは？

FDFファイルは、キー/ペア形式でデータを保存します。ここで、/Tはキーを表し、/Vは値を表し、括弧内のデータはキーまたは値のいずれかの内容を表します。たとえば、/T(Company)はCompanyがフィールドキーであり、/V(Aspose.com)はフィールド値を意味します。

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### XML形式とは？

開発者は、各PDFフォームフィールドをフィールドタグ`<field>`の形式で表現できます。各フィールドタグには、フィールド名を示す属性nameと、フィールド値を表すサブタグ`<value>`があります。以下に示します：

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
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### XFDF形式とは？

上記のデータをXFDF形式で表現することは、XML形式と似ていますが、いくつかの違いがあります。XFDFファイルでは、XML名前空間`<http://ns.adpbe.com/xfdf/>`を追加し、PDF文書を指すために使用される追加のタグ`<f>`があります。XMLと同様に、XFDFもフィールドタグ`<field>`の形式でフィールドを含みます。以下に示します：

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

### フォームフィールド名の特定

Aspose.PDF for .NETは、PDFフォームを作成、編集、既に作成されたPDFフォームに記入する機能を提供します。これは、[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスを含み、[FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)という関数を持ち、記入する必要があるフィールド名とフィールド値の2つのパラメータを取ります。したがって、フォームフィールドを記入するには、正確なフォームフィールド名を知っている必要があります。
私たちはしばしば、Adobe Designerなどのツールで作成されたフォームを記入する必要があるシナリオに直面しますが、フォームフィールド名がわからないことがあります。この要件を達成するためには、すべてのPDFフォームフィールドの名前を読み取る必要があります。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスは、すべてのフィールド名を返し、PDFにフィールドがない場合はnullを返す[FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)というプロパティを提供します。しかし、このプロパティはすべてのPDFフォームフィールドの名前を返し、どの名前がどのフィールドに対応しているかはわかりません。

この問題の解決策として、各フィールドの外観属性が必要です。[Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html)クラスには、位置、色、境界スタイル、フォント、リスト項目などの属性を返すGetFieldFacadeという関数があります。これらの値を保存するために、フィールドの視覚的属性を記録するために使用される[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)クラスを使用します。これらの属性を取得したら、各フィールドの下にフィールド名を表示するテキストフィールドを追加できます。ここで、テキストフィールドを追加する位置をどのように決定するかという問題が生じます。この問題の解決策は、フィールドの位置を保持する[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)クラスのBoxプロパティです。これらの値を矩形型の配列に保存し、新しいテキストフィールドを追加する位置を特定するためにこれらの値を使用します。
Aspose.Pdf.Facades名前空間には、PDFフォームを操作する機能を提供する[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)というクラスがあります。PDFフォームを開き、既存の各フォームフィールドの下にテキストフィールドを追加し、新しい名前でPDFフォームを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```