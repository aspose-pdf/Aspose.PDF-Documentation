---
title: Create AcroForms using using C++
linktitle: Create AcroForms
type: docs
weight: 10
url: /es/cpp/create-form/
description: Esta sección explica cómo crear AcroForms desde cero en sus documentos PDF con Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir un campo de formulario en el documento PDF

La clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) proporciona una colección llamada Form que ayuda a gestionar los campos de formulario en un documento PDF.

Para añadir un campo de formulario:

1. Cree el campo de formulario que desea añadir.
2. Llame al método add de la colección [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms).

Este ejemplo muestra cómo añadir un [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). Puede añadir cualquier campo de formulario utilizando el mismo enfoque:

1. Primero, cree un objeto de campo y establezca sus propiedades.
2. Luego, añada el campo a la colección Form.

### Añadiendo TextBoxField

Un campo de texto es un elemento de formulario que permite a un destinatario ingresar texto en su formulario. Esto se utilizaría cada vez que quieras permitir al usuario la libertad de escribir lo que quiera.

Los siguientes fragmentos de código muestran cómo agregar un TextBoxField a un documento PDF.

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

    // Crear un campo
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // Agregar campo al documento
    document->get_Form()->Add(textBoxField, 1);

    // Guardar PDF modificado
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## Adding RadioButtonField

Un RadioButton se utiliza más comúnmente para preguntas de opción múltiple, en el escenario donde solo se puede seleccionar una respuesta.

Los siguientes fragmentos de código muestran cómo agregar [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) en un documento PDF.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>();

    // Agregar una página al archivo PDF
    document->get_Pages()->Add();

    // Instanciar objeto RadioButtonField con número de página como argumento

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // Agregar la primera opción de botón de radio y también especificar su origen usando el objeto Rectangle
    radio->AddOption(u"Opción 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // Agregar la segunda opción de botón de radio
    radio->AddOption(u"Opción 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Agregar botón de radio al objeto formulario del objeto Document
    document->get_Form()->Add(radio,1);

    // Guardar el archivo PDF
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

El siguiente fragmento de código muestra los pasos para agregar un [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) con tres opciones y colocarlos dentro de las celdas de una tabla.

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

    // Guardar el archivo PDF
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## Agregar un subtítulo a RadioButtonField

El siguiente fragmento de código muestra cómo agregar un subtítulo que estará asociado con [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // Cargar formulario PDF fuente
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

            // Crear objeto TextParagraph
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // Establecer posición del párrafo
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // Especificar modo de ajuste de palabras
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // Agregar nuevo TextFragment al párrafo
            par->AppendLine(updatedFragment);

            // Agregar el TextParagraph usando TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## Adding ComboBox field

Un Combo Box es un campo de formulario que añadirá un menú desplegable a su documento.

Los siguientes fragmentos de código muestran cómo agregar un campo [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) en un documento PDF.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Crear objeto Document
    auto document = MakeObject<Document>();
    // Agregar página al objeto del documento
    document->get_Pages()->Add();
    // Instanciar objeto de campo ComboBox
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // Añadir opción al ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // Añadir objeto combo box a la colección de campos de formulario del objeto documento
    document->get_Form()->Add(combo);

    // Guardar el documento PDF
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## Add Tooltip to Form

The Document class proporciona una colección llamada Form que gestiona los campos de formulario en un documento PDF. Para añadir un tooltip a un campo de formulario, utiliza la clase Field AlternateName. Adobe Acrobat usa el 'nombre alternativo' como un tooltip de campo.

Los fragmentos de código que siguen muestran cómo añadir un tooltip a un campo de formulario con C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Cargar el formulario PDF de origen
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Establecer el tooltip para el campo de texto
    //(doc.Form["textbox1"] as Field).AlternateName = "Texto de ayuda para el cuadro de texto";

    // Guardar el documento actualizado
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```