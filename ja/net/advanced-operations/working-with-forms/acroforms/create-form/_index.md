---
title: Create AcroForm - Create Fillable PDF in C#
linktitle: Create AcroForm
type: docs
weight: 10
url: /ja/net/create-form/
description: Aspose.PDF for .NETを使用して、PDFファイルでゼロからフォームを作成できます
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create AcroForm",
    "alternativeHeadline": "PDFでAcroFormを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, create acroform",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用して、PDFファイルでゼロからフォームを作成できます"
}
</script>

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## スクラッチからフォームを作成

### PDFドキュメントにフォームフィールドを追加

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスは [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) というコレクションを提供しており、PDFドキュメントのフォームフィールドを管理するのに役立ちます。

フォームフィールドを追加するには：

1. 追加したいフォームフィールドを作成します。
1. [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) コレクションのAddメソッドを呼び出します。

### TextBoxFieldの追加

以下の例は、[TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// フィールドを作成する
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "テキストボックス";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// ドキュメントにフィールドを追加
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// 変更したPDFを保存
pdfDocument.Save(dataDir);
```
### RadioButtonFieldの追加

次のコードスニペットは、PDFドキュメントに[RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield)を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Documentオブジェクトをインスタンス化します
Document pdfDocument = new Document();
// PDFファイルにページを追加します
pdfDocument.Pages.Add();
// ページ番号を引数に持つRadioButtonFieldオブジェクトをインスタンス化します
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// 最初のラジオボタンオプションを追加し、Rectangleオブジェクトを使用してその原点も指定します
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// 第二のラジオボタンオプションを追加します
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Documentオブジェクトのフォームオブジェクトにラジオボタンを追加します
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// PDFファイルを保存します
pdfDocument.Save(dataDir);
```
次のコードスニペットは、3つのオプションを持つRadioButtonFieldを追加し、それをテーブルセルに配置する手順を示しています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

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

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// PDFファイルを保存
doc.Save(dataDir);
```
### RadioButtonFieldにキャプションを追加する

次のコードスニペットは、RadioButtonFieldに関連付けられるキャプションを追加する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ソースPDFフォームを読み込む
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Yes";
        fieldoption.PartialName = "Yesname";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // TextParagraphオブジェクトを作成する
        TextParagraph par = new TextParagraph();

        // 段落の位置を設定する
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // 単語ごとに改行するモードを指定する
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // 段落に新しいTextFragmentを追加する
        par.AppendLine(updatedFragment);

        // TextBuilderを使用してTextParagraphを追加する
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### コンボボックスフィールドの追加

次のコードスニペットは、PDFドキュメントにコンボボックスフィールドを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Documentオブジェクトを作成
Document doc = new Document();

// ドキュメントオブジェクトにページを追加
doc.Pages.Add();

// ComboBox Fieldオブジェクトをインスタンス化
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// コンボボックスにオプションを追加
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// ドキュメントオブジェクトのフォームフィールドコレクションにコンボボックスオブジェクトを追加
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// PDFドキュメントを保存
doc.Save(dataDir);
```

### フォームフィールドにツールチップを追加する

Documentクラスは、PDFドキュメントのフォームフィールドを管理するFormというコレクションを提供しています。
Document クラスは、PDFドキュメントのフォームフィールドを管理する Form というコレクションを提供します。

次に示すコードスニペットは、まず C# を使用して、次に Visual Basic を使用してフォームフィールドにツールチップを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ソースPDFフォームをロード
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// テキストフィールドのツールチップを設定
(doc.Form["textbox1"] as Field).AlternateName = "テキストボックスのツールチップ";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// 更新されたドキュメントを保存
doc.Save(dataDir);
```

