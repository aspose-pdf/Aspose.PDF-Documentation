---
title: Criar AcroForms usando C++
linktitle: Criar AcroForms
type: docs
weight: 10
url: pt/cpp/create-form/
description: Esta seção explica como criar AcroForms do zero em seus documentos PDF com Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Campo de Formulário em Documento PDF

A classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) fornece uma coleção chamada Form que ajuda a gerenciar campos de formulário em um documento PDF.

Para adicionar um campo de formulário:

1. Crie o campo de formulário que deseja adicionar.
2. Chame o método add da coleção [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms).

Este exemplo mostra como adicionar um [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). Você pode adicionar qualquer campo de formulário usando a mesma abordagem:

1. Primeiro, crie um objeto de campo e defina suas propriedades.
2. Em seguida, adicione o campo à coleção Form.

### Adicionando TextBoxField

Um campo de texto é um elemento de formulário que permite que um destinatário insira texto em seu formulário. Este seria utilizado sempre que você quiser permitir ao usuário a liberdade de digitar o que quiser.

Os seguintes trechos de código mostram como adicionar um TextBoxField a um documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // Criar um campo
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Caixa de Texto");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // Adicionar campo ao documento
    document->get_Form()->Add(textBoxField, 1);

    // Salvar PDF modificado
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## Adicionando RadioButtonField

Um RadioButton é mais comumente usado para perguntas de múltipla escolha, no cenário onde apenas uma resposta pode ser selecionada.

Os seguintes trechos de código mostram como adicionar [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) em um documento PDF.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>();

    // Adicionar uma página ao arquivo PDF
    document->get_Pages()->Add();

    // Instanciar objeto RadioButtonField com número da página como argumento

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // Adicionar primeira opção de botão de rádio e também especificar sua origem usando o objeto Rectangle
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // Adicionar segunda opção de botão de rádio
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Adicionar botão de rádio ao objeto de formulário do objeto Document
    document->get_Form()->Add(radio,1);

    // Salvar o arquivo PDF
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

O trecho de código a seguir mostra as etapas para adicionar [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) com três opções e colocá-las dentro de células da Tabela.

```cpp
void AddRadioButtonFieldInsideTableCells()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Aspose::Pdf::Table>();

    table->set_ColumnWidths(u"120 120 120");

    page->get_Paragraphs()->Add(table);

    auto r1 = table->get_Rows()->Add();
    auto c1 = r1->get_Cells()->Add();
    auto c2 = r1->get_Cells()->Add();
    auto c3 = r1->get_Cells()->Add();

    auto rf = MakeObject<RadioButtonField>(page);
    rf->set_PartialName(u"radio");
    document->get_Form()->Add(rf, 1);

    auto opt1 = MakeObject<RadioButtonOptionField>();
    auto opt2 = MakeObject<RadioButtonOptionField>();
    auto opt3 = MakeObject<RadioButtonOptionField>();

    opt1->set_OptionName(u"Item1");
    opt2->set_OptionName(u"Item2");
    opt3->set_OptionName(u"Item3");

    opt1->set_Width (15);
    opt1->set_Height(15);
    opt2->set_Width (15);
    opt2->set_Height(15);
    opt3->set_Width (15);
    opt3->set_Height(15);

    rf->Add(opt1);
    rf->Add(opt2);
    rf->Add(opt3);

    opt1->set_Border(MakeObject<Border>(opt1));
    opt1->get_Border()->set_Width(1);
    opt1->get_Border()->set_Style(BorderStyle::Solid);
    opt1->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt1->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt1->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item1"));
    opt2->set_Border(MakeObject<Border>(opt2));
    opt2->get_Border()->set_Width(1);
    opt2->get_Border()->set_Style(BorderStyle::Solid);
    opt2->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt2->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt2->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item2"));
    opt3->set_Border(MakeObject<Border>(opt3));
    opt3->get_Border()->set_Width(1);
    opt3->get_Border()->set_Style(BorderStyle::Solid);
    opt3->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt3->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt3->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item3"));
    c1->get_Paragraphs()->Add(opt1);
    c2->get_Paragraphs()->Add(opt2);
    c3->get_Paragraphs()->Add(opt3);

    // Salvar o arquivo PDF
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## Adicionando Legenda ao RadioButtonField

O snippet de código a seguir mostra como adicionar uma legenda que será associada ao [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // Carregar formulário PDF de origem
    auto form1 =
        MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"RadioButtonField.pdf");

    auto PDF_Template_PDF_HTML = MakeObject<Document>(_dataDir + u"RadioButtonField.pdf");

    for(auto item : form1->get_FieldNames())
    {
        System::Console::WriteLine(item);
        auto radioOptions = form1->GetButtonOptionValues(item);
        if (item.Contains(u"radio1"))
        {
            auto field0 = System::DynamicCast<RadioButtonField>(PDF_Template_PDF_HTML->get_Form()->idx_get(item));
            auto fieldoption = MakeObject<RadioButtonOptionField>();
            fieldoption->set_OptionName (u"Sim");
            fieldoption->set_PartialName (u"Simname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"teste123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // Criar objeto TextParagraph
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // Definir posição do parágrafo
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // Especificar modo de quebra de linha
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // Adicionar novo TextFragment ao parágrafo
            par->AppendLine(updatedFragment);

            // Adicionar o TextParagraph usando TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## Adicionando campo ComboBox

Um Combo Box é um campo de formulário que adicionará um menu suspenso ao seu documento.

Os seguintes trechos de código mostram como adicionar um campo [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) em um documento PDF.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Criar objeto Documento
    auto document = MakeObject<Document>();
    // Adicionar página ao objeto documento
    document->get_Pages()->Add();
    // Instanciar objeto Campo ComboBox
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // Adicionar opção ao ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // Adicionar objeto combo box à coleção de campos de formulário do objeto documento
    document->get_Form()->Add(combo);

    // Salvar o documento PDF
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```


## Adicionar Tooltip ao Formulário

The Document class fornece uma coleção chamada Form que gerencia campos de formulário em um documento PDF. Para adicionar uma dica de ferramenta a um campo de formulário, use a classe Field AlternateName. O Adobe Acrobat usa o 'nome alternativo' como dica de ferramenta de campo.

Os trechos de código a seguir mostram como adicionar uma dica de ferramenta a um campo de formulário com C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Carregar formulário PDF de origem
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Definir a dica de ferramenta para o campo de texto
    //(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

    // Salvar o documento atualizado
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```