---
title: フォームフィールド名の特定
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/identifying-form-fields-names/
description: Aspose.Pdf.Facadesを使用すると、Formクラスを利用してフォームフィールド名を特定できます。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "Aspose.PDF for .NETの機能は、PDFドキュメント内のフォームフィールド名を特定するプロセスを簡素化します。Formクラスとその属性を利用することで、ユーザーはフィールド名を簡単に取得し、対応するフィールドと共に表示でき、PDFフォームの記入と編集を効率化します。この機能は、Adobe Designerなどの外部ツールで作成されたフォームを扱う際に、正確なフィールド操作を保証することでユーザーエクスペリエンスを向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

[Aspose.PDF for .NET](/pdf/ja/net/)は、PDFフォームを作成、編集、既に作成されたPDFフォームに記入する機能を提供します。[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)名前空間には、[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスが含まれており、[FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)という名前の関数があり、フィールド名とフィールド値の2つの引数を取ります。したがって、フォームフィールドに記入するには、正確なフォームフィールド名を知っている必要があります。

## 実装の詳細

私たちはしばしば、Adobe Designerなどのツールで作成されたフォームに記入する必要があるシナリオに直面しますが、フォームフィールド名が不明な場合があります。したがって、フォームフィールドに記入するためには、まずすべてのPDFフォームフィールドの名前を読み取る必要があります。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスは、すべてのフィールド名を返す[FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)というプロパティを提供しており、PDFにフィールドが含まれていない場合はnullを返します。ただし、このプロパティを使用すると、PDFフォーム内のすべてのフィールド名が取得されますが、どの名前がどのフィールドに対応しているかは不明な場合があります。

この問題の解決策として、各フィールドの外観属性を使用します。Formクラスには、位置、色、境界スタイル、フォント、リスト項目などの属性を返す[GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade)という名前の関数があります。これらの値を保存するために、フィールドの視覚的属性を記録するために使用される[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade)クラスを使用する必要があります。これらの属性を取得したら、各フィールドの下にフィールド名を表示するテキストフィールドを追加できます。

{{% alert color="primary" %}}
この時点で、「テキストフィールドを追加する位置をどのように決定するか？」という疑問が生じます。
{{% /alert %}}

{{% alert color="primary" %}}
この問題の解決策は、フィールドの位置を保持する[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade)クラスのBoxプロパティです。これらの値を長方形型の配列に保存し、新しいテキストフィールドを追加する位置を特定するためにこれらの値を使用する必要があります。
{{% /alert %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)名前空間には、PDFフォームを操作する機能を提供する[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor)というクラスがあります。PDFフォームを開き、既存の各フォームフィールドの下にテキストフィールドを追加し、新しい名前でPDFフォームを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```