---
title: Créer des AcroForms en utilisant C++
linktitle: Créer des AcroForms
type: docs
weight: 10
url: /cpp/create-form/
description: Cette section explique comment créer des AcroForms à partir de zéro dans vos documents PDF avec Aspose.PDF pour C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un champ de formulaire dans un document PDF

La classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) fournit une collection nommée Form qui aide à gérer les champs de formulaire dans un document PDF.

Pour ajouter un champ de formulaire :

1. Créez le champ de formulaire que vous souhaitez ajouter.
2. Appelez la méthode add de la collection [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms).

Cet exemple montre comment ajouter un [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). Vous pouvez ajouter n'importe quel champ de formulaire en utilisant la même approche :

1. Tout d'abord, créez un objet champ et définissez ses propriétés.
2. Ensuite, ajoutez le champ à la collection Form.

### Ajouter un TextBoxField

Un champ de texte est un élément de formulaire qui permet à un destinataire de saisir du texte dans votre formulaire. Cela serait utilisé chaque fois que vous souhaitez permettre à l'utilisateur de taper ce qu'il veut.

Les extraits de code suivants montrent comment ajouter un TextBoxField à un document PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // Créer un champ
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // Ajouter le champ au document
    document->get_Form()->Add(textBoxField, 1);

    // Enregistrer le PDF modifié
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## Ajout de RadioButtonField

Un RadioButton est le plus souvent utilisé pour des questions à choix multiples, dans le scénario où une seule réponse peut être sélectionnée.

Les extraits de code suivants montrent comment ajouter [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) dans un document PDF.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto document = MakeObject<Document>();

    // Ajouter une page au fichier PDF
    document->get_Pages()->Add();

    // Instancier un objet RadioButtonField avec le numéro de page comme argument

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // Ajouter la première option de bouton radio et spécifier également son origine à l'aide d'un objet Rectangle
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // Ajouter la deuxième option de bouton radio
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Ajouter le bouton radio à l'objet form de l'objet Document
    document->get_Form()->Add(radio,1);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

Le snippet de code suivant montre les étapes pour ajouter [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) avec trois options et les placer à l'intérieur des cellules du tableau.

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

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## Ajout de légende à RadioButtonField

Le code suivant montre comment ajouter une légende qui sera associée à [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // Charger le formulaire PDF source
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
            fieldoption->set_OptionName (u"Yes");
            fieldoption->set_PartialName (u"Yesname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"test123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // Créer un objet TextParagraph
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // Définir la position du paragraphe
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // Spécifier le mode de retour à la ligne
            par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // Ajouter un nouveau TextFragment au paragraphe
            par->AppendLine(updatedFragment);

            // Ajouter le TextParagraph en utilisant TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## Ajouter un champ ComboBox

Une Combo Box est un champ de formulaire qui ajoutera un menu déroulant à votre document.

Les extraits de code suivants montrent comment ajouter un champ [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) dans un document PDF.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Créer un objet Document
    auto document = MakeObject<Document>();
    // Ajouter une page à l'objet document
    document->get_Pages()->Add();
    // Instancier l'objet Champ ComboBox
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // Ajouter une option à la ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // Ajouter l'objet combo box à la collection de champs de formulaire de l'objet document
    document->get_Form()->Add(combo);

    // Enregistrer le document PDF
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## Ajouter une info-bulle au formulaire

La classe Document fournit une collection nommée Form qui gère les champs de formulaire dans un document PDF. Pour ajouter une info-bulle à un champ de formulaire, utilisez la classe Field AlternateName. Adobe Acrobat utilise le « nom alternatif » comme info-bulle de champ.

Les extraits de code suivants montrent comment ajouter une info-bulle à un champ de formulaire avec C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Charger le formulaire PDF source
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Définir l'info-bulle pour le champ texte
    //(doc.Form["textbox1"] as Field).AlternateName = "Texte de l'info-bulle";

    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```