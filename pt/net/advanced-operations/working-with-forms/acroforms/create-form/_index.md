---
title: Criar AcroForm - Criar PDF Preenchível em C#
linktitle: Criar AcroForm
type: docs
weight: 10
url: /pt/net/create-form/
description: Com Aspose.PDF para .NET, você pode criar um formulário do zero em seu arquivo PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Criar AcroForm",
    "alternativeHeadline": "Como criar AcroForm em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, criar acroform",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "description": "Com Aspose.PDF para .NET, você pode criar um formulário do zero em seu arquivo PDF"
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Criar formulário do zero

### Adicionar Campo de Formulário em um Documento PDF

A classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) fornece uma coleção chamada [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) que ajuda você a gerenciar campos de formulário em um documento PDF.

Para adicionar um campo de formulário:

1. Crie o campo de formulário que deseja adicionar.
1. Chame o método Add da coleção [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### Adicionando TextBoxField

O exemplo abaixo mostra como adicionar um [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// Criar um campo
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// Adicionar campo ao documento
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// Salvar PDF modificado
pdfDocument.Save(dataDir);
```
### Adicionando RadioButtonField

Os seguintes trechos de código mostram como adicionar [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) em um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Instanciar objeto Document
Document pdfDocument = new Document();
// Adicionar uma página ao arquivo PDF
pdfDocument.Pages.Add();
// Instanciar objeto RadioButtonField com número de página como argumento
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// Adicionar primeira opção de botão de rádio e também especificar sua origem usando o objeto Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// Adicionar segunda opção de botão de rádio
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Adicionar botão de rádio ao objeto de formulário do objeto Document
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// Salvar o arquivo PDF
pdfDocument.Save(dataDir);
```
O seguinte trecho de código mostra os passos para adicionar RadioButtonField com três opções e colocá-las dentro das células de uma Tabela.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
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
// Salve o arquivo PDF
doc.Save(dataDir);
```
### Adicionando Legenda ao RadioButtonField

O trecho de código a seguir mostra como adicionar uma legenda que será associada com RadioButtonField:

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Carregar o formulário PDF de origem
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

        // Criar objeto TextParagraph
        TextParagraph par = new TextParagraph();

        // Definir posição do parágrafo
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // Especificar modo de quebra de palavras
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // Adicionar novo TextFragment ao parágrafo
        par.AppendLine(updatedFragment);

        // Adicionar o TextParagraph usando TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### Adicionando campo ComboBox

O seguinte trecho de código mostra como adicionar um campo ComboBox em um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Criar objeto Document
Document doc = new Document();

// Adicionar página ao objeto documento
doc.Pages.Add();

// Instanciar objeto Campo ComboBox
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// Adicionar opção ao ComboBox
combo.AddOption("Vermelho");
combo.AddOption("Amarelo");
combo.AddOption("Verde");
combo.AddOption("Azul");

// Adicionar objeto combo box à coleção de campos de formulário do objeto documento
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// Salvar o documento PDF
doc.Save(dataDir);
```

### Adicionar Dica de Ferramenta ao Campo de Formulário

A classe Document fornece uma coleção chamada Form que gerencia campos de formulário em um documento PDF.
A classe Document fornece uma coleção chamada Form que gerencia campos de formulário em um documento PDF.

Os trechos de código a seguir mostram como adicionar uma dica de ferramenta a um campo de formulário, primeiro usando C# e depois Visual Basic.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Carregar o formulário PDF de origem
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// Definir a dica de ferramenta para o campo de texto
(doc.Form["textbox1"] as Field).AlternateName = "Dica de ferramenta da caixa de texto";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```

