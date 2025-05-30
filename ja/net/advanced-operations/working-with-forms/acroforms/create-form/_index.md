---
title: AcroFormの作成 - C#で入力可能なPDFを作成
linktitle: AcroFormの作成
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/create-form/
description: Aspose.PDF for .NETを使用して、PDFファイルにフォームをゼロから作成できます
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create AcroForm - Create Fillable PDF in C#",
    "alternativeHeadline": "Create Interactive Forms in PDF with C#",
    "abstract": "Aspose.PDF for .NETは、ゼロから入力可能なPDFフォームを作成する機能を提供し、開発者がテキストボックス、ラジオボタン、コンボボックスなどのカスタマイズ可能なフォームフィールドをPDFにシームレスに統合できるようにします。この機能により、ユーザーはドキュメントのインタラクティビティを向上させ、アプリケーション内でのデータ収集を改善できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create AcroForm, fillable PDF, C#, Aspose.PDF, form fields, TextBoxField, RadioButtonField, ComboBoxField, add tooltip, PDF document generation",
    "wordcount": "3828",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2025-04-01",
    "description": "Aspose.PDF for .NETを使用して、PDFファイルにフォームをゼロから作成できます"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## ゼロからフォームを作成

### PDFドキュメントにフォームフィールドを追加

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスは、PDFドキュメント内のフォームフィールドを管理するための[Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form)というコレクションを提供します。

フォームフィールドを追加するには：

1. 追加したいフォームフィールドを作成します。
1. [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form)コレクションのAddメソッドを呼び出します。

### TextBoxFieldの追加

以下の例は、[TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)を追加する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBoxFieldToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create a field
        var textBoxField = new Aspose.Pdf.Forms.TextBoxField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
        textBoxField.PartialName = "textbox1";
        textBoxField.Value = "Text Box";

        // Configure border
        var border = new Aspose.Pdf.Annotations.Border(textBoxField);
        border.Width = 5;
        border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
        textBoxField.Border = border;

        // Set color
        textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

        // Add field to the document
        document.Form.Add(textBoxField, 1);

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBoxFieldToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf");

    // Create a field
    var textBoxField = new Aspose.Pdf.Forms.TextBoxField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
    textBoxField.PartialName = "textbox1";
    textBoxField.Value = "Text Box";

    // Configure border
    var border = new Aspose.Pdf.Annotations.Border(textBoxField);
    border.Width = 5;
    border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
    textBoxField.Border = border;

    // Set color
    textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

    // Add field to the document
    document.Form.Add(textBoxField, 1);

    // Save PDF document
    document.Save(dataDir + "TextBox_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### RadioButtonFieldの追加

以下のコードスニペットは、PDFドキュメントに[RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield)を追加する方法を示しています。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRadioButtonToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        document.Pages.Add();

        // Instantiate RadioButtonField object with page number as argument
        var radio = new Aspose.Pdf.Forms.RadioButtonField(document.Pages[1]);

        // Add first radio button option and also specify its origin using Rectangle object
        radio.AddOption("Test", new Aspose.Pdf.Rectangle(0, 0, 20, 20));

        // Add second radio button option
        radio.AddOption("Test1", new Aspose.Pdf.Rectangle(20, 20, 40, 40));

        // Add radio button to form object of Document object
        document.Form.Add(radio);

        // Save PDF document
        document.Save(dataDir + "RadioButton_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRadioButtonToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    document.Pages.Add();

    // Instantiate RadioButtonField object with page number as argument
    var radio = new Aspose.Pdf.Forms.RadioButtonField(document.Pages[1]);

    // Add first radio button option and also specify its origin using Rectangle object
    radio.AddOption("Test", new Aspose.Pdf.Rectangle(0, 0, 20, 20));

    // Add second radio button option
    radio.AddOption("Test1", new Aspose.Pdf.Rectangle(20, 20, 40, 40));

    // Add radio button to form object of Document object
    document.Form.Add(radio);

    // Save PDF document
    document.Save(dataDir + "RadioButton_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

[TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)は、いくつかのウィジェット注釈と共に追加できます。
{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, please visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBoxFieldToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        var page = document.Pages.Add();

        // Defining an array with rectangle data for widget annotations. 
        // The number of elements in the array determines the number of widget annotations to add.
        var rects = new Aspose.Pdf.Rectangle[]
        {
            new Aspose.Pdf.Rectangle(10, 600, 110, 620),
            new Aspose.Pdf.Rectangle(10, 630, 110, 650),
            new Aspose.Pdf.Rectangle(10, 660, 110, 680)
        };

        // Defining an array with DefaultAppearance used to specify how widget annotations are displayed in the added field.
        var defaultAppearances = new Aspose.Pdf.Annotations.DefaultAppearance[]
        {
            new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 10, System.Drawing.Color.DarkBlue),
            new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 12, System.Drawing.Color.DarkGreen),
            new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 14, System.Drawing.Color.DarkMagenta)
        };

        // Create a field
        var textBoxField = new Aspose.Pdf.Forms.TextBoxField(page, rects);

        // Setting the appearances of widget annotations
        short i = 0;
        foreach (Aspose.Pdf.Annotations.WidgetAnnotation wa in textBoxField)
        {
            wa.DefaultAppearance = defaultAppearances[i++];
        }
        textBoxField.Value = "Text";

        // Add field to the document
        document.Form.Add(textBoxField);

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, please visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBoxFieldToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    var page = document.Pages.Add();

    // Defining an array with rectangle data for widget annotations. 
    // The number of elements in the array determines the number of widget annotations to add.
    var rects = new Aspose.Pdf.Rectangle[]
    {
        new Aspose.Pdf.Rectangle(10, 600, 110, 620),
        new Aspose.Pdf.Rectangle(10, 630, 110, 650),
        new Aspose.Pdf.Rectangle(10, 660, 110, 680)
    };

    // Defining an array with DefaultAppearance used to specify how widget annotations are displayed in the added field.
    var defaultAppearances = new Aspose.Pdf.Annotations.DefaultAppearance[]
    {
        new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 10, System.Drawing.Color.DarkBlue),
        new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 12, System.Drawing.Color.DarkGreen),
        new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 14, System.Drawing.Color.DarkMagenta)
    };

    // Create a field
    var textBoxField = new Aspose.Pdf.Forms.TextBoxField(page, rects);

    // Setting the appearances of widget annotations
    short i = 0;
    foreach (Aspose.Pdf.Annotations.WidgetAnnotation wa in textBoxField)
    {
        wa.DefaultAppearance = defaultAppearances[i++];
    }
    textBoxField.Value = "Text";

    // Add field to the document
    document.Form.Add(textBoxField);

    // Save PDF document
    document.Save(dataDir + "TextBox_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

以下のコードスニペットは、3つのオプションを持つRadioButtonFieldを追加し、それをテーブルセル内に配置する手順を示しています。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRadioButtonWithOptionsToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        var page = document.Pages.Add();

        // Create a table
        var table = new Aspose.Pdf.Table();
        table.ColumnWidths = "120 120 120";
        page.Paragraphs.Add(table);

        // Add a row to the table
        var r1 = table.Rows.Add();

        // Add cells to the row
        var c1 = r1.Cells.Add();
        var c2 = r1.Cells.Add();
        var c3 = r1.Cells.Add();

        // Create a RadioButtonField
        var rf = new Aspose.Pdf.Forms.RadioButtonField(page);
        rf.PartialName = "radio";
        document.Form.Add(rf, 1);

        // Create RadioButtonOptionField options
        var opt1 = new Aspose.Pdf.Forms.RadioButtonOptionField();
        var opt2 = new Aspose.Pdf.Forms.RadioButtonOptionField();
        var opt3 = new Aspose.Pdf.Forms.RadioButtonOptionField();

        opt1.OptionName = "Item1";
        opt2.OptionName = "Item2";
        opt3.OptionName = "Item3";

        opt1.Width = 15;
        opt1.Height = 15;
        opt2.Width = 15;
        opt2.Height = 15;
        opt3.Width = 15;
        opt3.Height = 15;

        rf.Add(opt1);
        rf.Add(opt2);
        rf.Add(opt3);

        // Configure borders and captions for options
        opt1.Border = new Aspose.Pdf.Annotations.Border(opt1);
        opt1.Border.Width = 1;
        opt1.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
        opt1.Characteristics.Border = System.Drawing.Color.Black;
        opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
        opt1.Caption = new Aspose.Pdf.Text.TextFragment("Item1");

        opt2.Border = new Aspose.Pdf.Annotations.Border(opt2);
        opt2.Border.Width = 1;
        opt2.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
        opt2.Characteristics.Border = System.Drawing.Color.Black;
        opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
        opt2.Caption = new Aspose.Pdf.Text.TextFragment("Item2");

        opt3.Border = new Aspose.Pdf.Annotations.Border(opt3);
        opt3.Border.Width = 1;
        opt3.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
        opt3.Characteristics.Border = System.Drawing.Color.Black;
        opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
        opt3.Caption = new Aspose.Pdf.Text.TextFragment("Item3");

        // Add options to the cells
        c1.Paragraphs.Add(opt1);
        c2.Paragraphs.Add(opt2);
        c3.Paragraphs.Add(opt3);

        // Save PDF document
        document.Save(dataDir + "RadioButtonWithOptions_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRadioButtonWithOptionsToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    var page = document.Pages.Add();

    // Create a table
    var table = new Aspose.Pdf.Table();
    table.ColumnWidths = "120 120 120";
    page.Paragraphs.Add(table);

    // Add a row to the table
    var r1 = table.Rows.Add();

    // Add cells to the row
    var c1 = r1.Cells.Add();
    var c2 = r1.Cells.Add();
    var c3 = r1.Cells.Add();

    // Create a RadioButtonField
    var rf = new Aspose.Pdf.Forms.RadioButtonField(page);
    rf.PartialName = "radio";
    document.Form.Add(rf, 1);

    // Create RadioButtonOptionField options
    var opt1 = new Aspose.Pdf.Forms.RadioButtonOptionField();
    var opt2 = new Aspose.Pdf.Forms.RadioButtonOptionField();
    var opt3 = new Aspose.Pdf.Forms.RadioButtonOptionField();

    opt1.OptionName = "Item1";
    opt2.OptionName = "Item2";
    opt3.OptionName = "Item3";

    opt1.Width = 15;
    opt1.Height = 15;
    opt2.Width = 15;
    opt2.Height = 15;
    opt3.Width = 15;
    opt3.Height = 15;

    rf.Add(opt1);
    rf.Add(opt2);
    rf.Add(opt3);

    // Configure borders and captions for options
    opt1.Border = new Aspose.Pdf.Annotations.Border(opt1);
    opt1.Border.Width = 1;
    opt1.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
    opt1.Characteristics.Border = System.Drawing.Color.Black;
    opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
    opt1.Caption = new Aspose.Pdf.Text.TextFragment("Item1");

    opt2.Border = new Aspose.Pdf.Annotations.Border(opt2);
    opt2.Border.Width = 1;
    opt2.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
    opt2.Characteristics.Border = System.Drawing.Color.Black;
    opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
    opt2.Caption = new Aspose.Pdf.Text.TextFragment("Item2");

    opt3.Border = new Aspose.Pdf.Annotations.Border(opt3);
    opt3.Border.Width = 1;
    opt3.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
    opt3.Characteristics.Border = System.Drawing.Color.Black;
    opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
    opt3.Caption = new Aspose.Pdf.Text.TextFragment("Item3");

    // Add options to the cells
    c1.Paragraphs.Add(opt1);
    c2.Paragraphs.Add(opt2);
    c3.Paragraphs.Add(opt3);

    // Save PDF document
    document.Save(dataDir + "RadioButtonWithOptions_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### RadioButtonFieldにキャプションを追加

以下のコードスニペットは、RadioButtonFieldに関連付けられるキャプションを追加する方法を示しています：

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingCaptionToRadioButtonField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf"))
    {
        using (var document = new Aspose.Pdf.Document(dataDir + "RadioButtonField.pdf"))
        {
            foreach (var item in form.FieldNames)
            {
                Console.WriteLine(item.ToString());
                var radioOptions = form.GetButtonOptionValues(item);

                if (item.Contains("radio1"))
                {
                    var field1 = document.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
                    var fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
                    fieldoption.OptionName = "Yes";
                    fieldoption.PartialName = "Yesname";

                    var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
                    updatedFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
                    updatedFragment.TextState.FontSize = 10;
                    updatedFragment.TextState.LineSpacing = 6.32f;

                    // Create TextParagraph object
                    var par = new Aspose.Pdf.Text.TextParagraph();

                    // Set paragraph position
                    par.Position = new Aspose.Pdf.Text.Position(field1.Rect.LLX, field1.Rect.LLY + updatedFragment.TextState.FontSize);
                    // Specify word wraping mode
                    par.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;

                    // Add new TextFragment to paragraph
                    par.AppendLine(updatedFragment);

                    // Add the TextParagraph using TextBuilder
                    var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
                    textBuilder.AppendParagraph(par);

                    field1.DeleteOption("item1");
                }
            }

            // Save PDF document
            document.Save(dataDir + "RadioButtonField_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingCaptionToRadioButtonField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using var form = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
    using var document = new Aspose.Pdf.Document(dataDir + "RadioButtonField.pdf");

    foreach (var item in form.FieldNames)
    {
        Console.WriteLine(item.ToString());
        var radioOptions = form.GetButtonOptionValues(item);

        if (item.Contains("radio1"))
        {
            var field1 = document.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
            var fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
            fieldoption.OptionName = "Yes";
            fieldoption.PartialName = "Yesname";

            var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
            updatedFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            updatedFragment.TextState.FontSize = 10;
            updatedFragment.TextState.LineSpacing = 6.32f;

            // Create TextParagraph object
            var par = new Aspose.Pdf.Text.TextParagraph();

            // Set paragraph position
            par.Position = new Aspose.Pdf.Text.Position(field1.Rect.LLX, field1.Rect.LLY + updatedFragment.TextState.FontSize);
            // Specify word wraping mode
            par.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;

            // Add new TextFragment to paragraph
            par.AppendLine(updatedFragment);

            // Add the TextParagraph using TextBuilder
            var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
            textBuilder.AppendParagraph(par);

            field1.DeleteOption("item1");
        }
    }

    // Save PDF document
    document.Save(dataDir + "RadioButtonField_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### グループ化されたチェックボックスを追加する別の方法

以下のコードスニペットは、PDFドキュメントにグループ化されたチェックボックスフィールドを追加する方法を示しています。
{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddGroupedCheckBoxFieldsToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        var page = document.Pages.Add();

        var radioButtonField = new Aspose.Pdf.Forms.RadioButtonField(page);

        // Add radio button options and specify its position using Rectangle
        var opt1 = new Aspose.Pdf.Forms.RadioButtonOptionField(page, new Aspose.Pdf.Rectangle(50, 500, 70, 520));
        var opt2 = new Aspose.Pdf.Forms.RadioButtonOptionField(page, new Aspose.Pdf.Rectangle(100, 500, 120, 520));

        // Set option names for identification
        opt1.OptionName = "Option1";
        opt2.OptionName = "Option2";

        // Set the style of the radio buttons
        opt1.Style = Aspose.Pdf.Forms.BoxStyle.Square;
        opt2.Style = Aspose.Pdf.Forms.BoxStyle.Cross;

        // Configure the border of the first radio button
        opt1.Border = new Aspose.Pdf.Annotations.Border(opt1);
        opt1.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Dashed;
        opt1.Border.Width = 1;
        opt1.Characteristics.Border = System.Drawing.Color.Blue;

        // Configure the border of the second radio button
        opt2.Border = new Aspose.Pdf.Annotations.Border(opt2);
        opt2.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
        opt2.Border.Width = 1;
        opt2.Characteristics.Border = System.Drawing.Color.Black;

        radioButtonField.Add(opt1);
        radioButtonField.Add(opt2);

        // Add radio button field to the form object of the document
        document.Form.Add(radioButtonField);

        // Save PDF document
        document.Save(dataDir + "GroupedCheckboxFields_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddGroupedCheckBoxFieldsToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    var page = document.Pages.Add();

    var radioButtonField = new Aspose.Pdf.Forms.RadioButtonField(page);

    // Add radio button options and specify its position using Rectangle
    var opt1 = new Aspose.Pdf.Forms.RadioButtonOptionField(page, new Aspose.Pdf.Rectangle(50, 500, 70, 520));
    var opt2 = new Aspose.Pdf.Forms.RadioButtonOptionField(page, new Aspose.Pdf.Rectangle(100, 500, 120, 520));

    // Set option names for identification
    opt1.OptionName = "Option1";
    opt2.OptionName = "Option2";

    // Set the style of the radio buttons
    opt1.Style = Aspose.Pdf.Forms.BoxStyle.Square;
    opt2.Style = Aspose.Pdf.Forms.BoxStyle.Cross;

    // Configure the border of the first radio button
    opt1.Border = new Aspose.Pdf.Annotations.Border(opt1);
    opt1.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Dashed;
    opt1.Border.Width = 1;
    opt1.Characteristics.Border = System.Drawing.Color.Blue;

    // Configure the border of the second radio button
    opt2.Border = new Aspose.Pdf.Annotations.Border(opt2);
    opt2.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
    opt2.Border.Width = 1;
    opt2.Characteristics.Border = System.Drawing.Color.Black;

    radioButtonField.Add(opt1);
    radioButtonField.Add(opt2);

    // Add radio button field to the form object of the document
    document.Form.Add(radioButtonField);

    // Save PDF document
    document.Save(dataDir + "GroupedCheckboxFields_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### ComboBoxフィールドの追加

以下のコードスニペットは、PDFドキュメントにComboBoxフィールドを追加する方法を示しています。

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddComboBoxToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        document.Pages.Add();

        // Instantiate ComboBox Field object
        var combo = new Aspose.Pdf.Forms.ComboBoxField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

        // Add options to ComboBox
        combo.AddOption("Red");
        combo.AddOption("Yellow");
        combo.AddOption("Green");
        combo.AddOption("Blue");

        // Add combo box object to form fields collection of document object
        document.Form.Add(combo);

        // Save PDF document
        document.Save(dataDir + "ComboBox_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddComboBoxToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    document.Pages.Add();

    // Instantiate ComboBox Field object
    var combo = new Aspose.Pdf.Forms.ComboBoxField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

    // Add options to ComboBox
    combo.AddOption("Red");
    combo.AddOption("Yellow");
    combo.AddOption("Green");
    combo.AddOption("Blue");

    // Add combo box object to form fields collection of document object
    document.Form.Add(combo);

    // Save PDF document
    document.Save(dataDir + "ComboBox_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### CheckboxFieldの追加

以下のコードスニペットは、PDFドキュメントにCheckboxFieldを追加する方法を示しています。

{{< tabs tabID="8" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCheckBoxFieldToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        var page = document.Pages.Add();

        // Create a field
        var checkboxField = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 620, 100, 650));
        checkboxField.Characteristics.Background = System.Drawing.Color.Aqua;
        checkboxField.Style = Aspose.Pdf.Forms.BoxStyle.Circle;

        // Add field to the form
        document.Form.Add(checkboxField);

        // Save PDF document
        document.Save(dataDir + "CheckboxField_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCheckBoxFieldToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    var page = document.Pages.Add();

    // Create a field
    var checkboxField = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 620, 100, 650));
    checkboxField.Characteristics.Background = System.Drawing.Color.Aqua;
    checkboxField.Style = Aspose.Pdf.Forms.BoxStyle.Circle;

    // Add field to the form
    document.Form.Add(checkboxField);

    // Save PDF document
    document.Save(dataDir + "CheckboxField_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### ListBoxFieldの追加

以下のコードスニペットは、PDFドキュメントにListBoxFieldを追加する方法を示しています。

{{< tabs tabID="9" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddListBoxFieldToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF file
        var page = document.Pages.Add();

        // Create a field
        var listBoxField = new Aspose.Pdf.Forms.ListBoxField(page, new Aspose.Pdf.Rectangle(50, 650, 100, 700));
        listBoxField.PartialName = "list";
        listBoxField.AddOption("Red");
        listBoxField.AddOption("Green");
        listBoxField.AddOption("Blue");
        // Add field to the form
        document.Form.Add(listBoxField);

        // Save PDF document
        document.Save(dataDir + "ListBoxField_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddListBoxFieldToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page to PDF file
    var page = document.Pages.Add();

    // Create a field
    var listBoxField = new Aspose.Pdf.Forms.ListBoxField(page, new Aspose.Pdf.Rectangle(50, 650, 100, 700));
    listBoxField.PartialName = "list";
    listBoxField.AddOption("Red");
    listBoxField.AddOption("Green");
    listBoxField.AddOption("Blue");
    // Add field to the form
    document.Form.Add(listBoxField);

    // Save PDF document
    document.Save(dataDir + "ListBoxField_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### SignatureFieldの使用

以下のコードスニペットは、SignatureFieldを使用してPDFドキュメントに署名する方法を示しています。

{{< tabs tabID="10" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
private static void SignPdfBySignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Add page to PDF file	
        var page = document.Pages.Add();

        // Create a field
        var signatureField = new Aspose.Pdf.Forms.SignatureField(page, new Aspose.Pdf.Rectangle(100, 700, 200, 800));
        document.Form.Add(signatureField);

        var pkcs = new Aspose.Pdf.Forms.PKCS7("test1.pfx", "test1");
        pkcs.Date = new DateTime();
        pkcs.ContactInfo = "Test";
        pkcs.Location = "TestLocation";
        pkcs.Reason = "Verify";
        pkcs.ShowProperties = false;
        signatureField.Sign(pkcs);

        // Save PDF document
        document.Save(dataDir + "SignatureField_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
private static void SignPdfBySignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf");

    // Add page to PDF file
    var page = document.Pages.Add();

    // Create a field
    var signatureField = new Aspose.Pdf.Forms.SignatureField(page, new Aspose.Pdf.Rectangle(100, 700, 200, 800));
    document.Form.Add(signatureField);

    var pkcs = new Aspose.Pdf.Forms.PKCS7("test1.pfx", "test1");
    pkcs.Date = new DateTime();
    pkcs.ContactInfo = "Test";
    pkcs.Location = "TestLocation";
    pkcs.Reason = "Verify";
    pkcs.ShowProperties = false;
    signatureField.Sign(pkcs);

    // Save PDF document
    document.Save(dataDir + "SignatureField_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### フォームフィールドにツールチップを追加

Documentクラスは、PDFドキュメント内のフォームフィールドを管理するためのFormというコレクションを提供します。フォームフィールドにツールチップを追加するには、FieldクラスのAlternateNameを使用します。Adobe Acrobatは「代替名」をフィールドツールチップとして使用します。

以下のコードスニペットは、最初にC#を使用し、次にVisual Basicを使用してフォームフィールドにツールチップを追加する方法を示しています。

{{< tabs tabID="11" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTooltipToField.pdf"))
    {
        // Set the tooltip for textfield
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
        {
            field.AlternateName = "Text box tool tip";
        }

        // Save PDF document
        document.Save(dataDir + "AddTooltipToField_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddTooltipToField.pdf");

    // Set the tooltip for textfield
    if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
    {
        field.AlternateName = "Text box tool tip";
    }

    // Save PDF document
    document.Save(dataDir + "AddTooltipToField_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>