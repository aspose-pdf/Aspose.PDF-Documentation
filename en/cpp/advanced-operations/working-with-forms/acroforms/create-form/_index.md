---
title: Create PDF form fields in C++
linktitle: Create AcroForm
type: docs
weight: 10
url: /cpp/create-form/
description: Create text, checkbox, choice, barcode, and unsigned signature fields in PDF documents using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build Fillable PDF Fields and Configure Their Appearance in C++
Abstract: Learn how to construct AcroForm fields with Aspose.PDF for C++. The examples add text boxes, checkboxes, lists, radio buttons, a barcode, and an unsigned signature field.
---

## Add a text box

The source constructs the field using the appended page but calls Form::Add(field, 1). Review the intended page association when adapting this example.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a page and create a [TextBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/textboxfield/) using a [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/).
1. Set PartialName, Value, and [DefaultAppearance](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/defaultappearance/).
1. Configure a dashed [Border](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/border/) and border and background colors.
1. Add the field through [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) using page number 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/TextBoxField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/BorderStyle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Dash.h>
#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;

void FormExamples::AddTextBoxField(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->Add();

    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(10, 600, 110, 620, true);
    auto textBoxField = MakeObject<TextBoxField>(page, rectangle);
    textBoxField->set_PartialName(String(u"textbox1"));
    textBoxField->set_Value(String(u"Text Box"));
    textBoxField->set_DefaultAppearance(
        MakeObject<DefaultAppearance>(String(u"Arial"), 10, Color::get_DarkBlue()->ToRgb()));

    auto border = MakeObject<Border>(textBoxField);
    border->set_Width(1);
    border->set_Style(BorderStyle::Dashed);
    border->set_Dash(MakeObject<Dash>(3, 3));
    textBoxField->set_Border(border);

    textBoxField->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
    textBoxField->get_Characteristics()->set_Background(Color::get_Yellow()->ToRgb());

    document->get_Form()->Add(textBoxField, 1);
    document->Save(outputFile);
}
```

## Add a text field with multiple widgets

The inputFile parameter is unused. Make Arial, Helvetica, and Calibri available for the supplied appearance settings.

1. Create a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create three rectangles and three [DefaultAppearance](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/defaultappearance/) objects.
1. Construct a [TextBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/textboxfield/) from the rectangles and set its name and value.
1. Assign a different default appearance to each widget.
1. Set the shared border and colors, then add the field to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/TextBoxField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/BorderStyle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Dash.h>
#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Text;

void FormExamples::AddTextBoxFieldNt(String inputFile, String outputFile)
{
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();

        auto rects =
            MakeArray<SharedPtr<Rectangle>>({MakeObject<Aspose::Pdf::Rectangle>(10, 600, 110, 620, true),
                                             MakeObject<Aspose::Pdf::Rectangle>(10, 630, 110, 650, true),
                                             MakeObject<Aspose::Pdf::Rectangle>(10, 660, 110, 680, true)});

        auto defaultAppearances = MakeArray<SharedPtr<DefaultAppearance>>(
            {MakeObject<DefaultAppearance>(String(u"Arial"), 10, Color::get_DarkBlue()->ToRgb()),
             MakeObject<DefaultAppearance>(String(u"Helvetica"), 12, Color::get_DarkGreen()->ToRgb()),
             MakeObject<DefaultAppearance>(FontRepository::FindFont(String(u"Calibri")), 14,
                                           Color::get_DarkMagenta()->ToRgb())});

        auto textBoxField = MakeObject<TextBoxField>(page, rects);
        textBoxField->set_PartialName(String(u"textbox1"));
        textBoxField->set_Value(String(u"Some text"));

        int index = 0;
        for (auto& widget : textBoxField)
        {
            widget->set_DefaultAppearance(defaultAppearances[index]);
            index++;
        }

        auto border = MakeObject<Border>(textBoxField);
        border->set_Width(1);
        border->set_Style(BorderStyle::Dashed);
        border->set_Dash(MakeObject<Dash>(3, 3));
        textBoxField->set_Border(border);

        textBoxField->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
        textBoxField->get_Characteristics()->set_Background(Color::get_Yellow()->ToRgb());

        document->get_Form()->Add(textBoxField, 1);
        document->Save(outputFile);
    }
}
```

## Add a checkbox

This creates a new PDF and does not use inputFile.

1. Create a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Construct a [CheckboxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/checkboxfield/) using the supplied rectangle.
1. Set its background color and circular box style.
1. Add the field to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/BoxStyle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/CheckboxField.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Text;

void FormExamples::AddCheckboxFieldToPdf(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto checkbox =
        MakeObject<CheckboxField>(page, MakeObject<Aspose::Pdf::Rectangle>(50, 620, 100, 650, true));
    checkbox->get_Characteristics()->set_Background(Color::get_Aqua()->ToRgb());
    checkbox->set_Style(BoxStyle::Circle);

    document->get_Form()->Add(checkbox, 1);
    document->Save(outputFile);
}
```

## Add a combo box

The inputFile parameter is unused.

1. Create a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a [ComboBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/comboboxfield/) at the supplied rectangle.
1. Add Red, Yellow, Green, and Blue options.
1. Set Selected to 3 and add the field to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ComboBoxField.h>
#include <Aspose.PDF.Cpp/Document.h>

#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void FormExamples::AddComboBox(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto combo =
        MakeObject<ComboBoxField>(page, MakeObject<Aspose::Pdf::Rectangle>(100, 640, 150, 656, true));
    combo->AddOption(String(u"Red"));
    combo->AddOption(String(u"Yellow"));
    combo->AddOption(String(u"Green"));
    combo->AddOption(String(u"Blue"));
    combo->set_Selected(3);

    document->get_Form()->Add(combo, 1);
    document->Save(outputFile);
}
```

## Add a list box

The inputFile parameter is unused.

1. Create a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a [ListBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/listboxfield/) and name it list.
1. Add Red, Green, and Blue options.
1. Add the field to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ListBoxField.h>
#include <Aspose.PDF.Cpp/Document.h>

#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void FormExamples::AddListBoxFieldToPdf(String inputFile, String outputFile)
{
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();

        auto listBox =
            MakeObject<ListBoxField>(page, MakeObject<Aspose::Pdf::Rectangle>(50, 650, 100, 700, true));
        listBox->set_PartialName(String(u"list"));
        listBox->AddOption(String(u"Red"));
        listBox->AddOption(String(u"Green"));
        listBox->AddOption(String(u"Blue"));

        document->get_Form()->Add(listBox, 1);
        document->Save(outputFile);
    }
}
```

## Add radio-button options

The inputFile parameter is unused.

1. Create a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a [RadioButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/radiobuttonfield/) for the page.
1. Add two options with separate rectangles.
1. Add the field to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/RadioButtonField.h>
#include <Aspose.PDF.Cpp/Document.h>

#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;


void FormExamples::AddRadioButton(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto radio = MakeObject<RadioButtonField>(page);
    radio->AddOption(String(u"Option 1"), MakeObject<Aspose::Pdf::Rectangle>(100, 640, 120, 680, true));
    radio->AddOption(String(u"Option 2"), MakeObject<Aspose::Pdf::Rectangle>(140, 640, 160, 680, true));

    document->get_Form()->Add(radio, 1);
    document->Save(outputFile);
}
```

## Add a barcode field

The inputFile parameter is unused.

1. Create a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a [BarcodeField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/barcodefield/) and name it Barcode1.
1. Call [AddBarcode()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/barcodefield/) with the sample value 1234567890.
1. Add the field to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/BarcodeField.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void FormExamples::AddBarcodeField(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto barcode =
        MakeObject<BarcodeField>(page, MakeObject<Aspose::Pdf::Rectangle>(100, 700, 200, 740, true));
    barcode->set_PartialName(String(u"Barcode1"));
    barcode->AddBarcode(String(u"1234567890"));
    document->get_Form()->Add(barcode, 1);
    document->Save(outputFile);
}
```

## Add an unsigned signature field

This adds an unsigned field; it does not apply a cryptographic signature. As in the text-box example, the constructor uses the appended page while Form::Add specifies page 1.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a page and create a [SignatureField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) using its rectangle.
1. Set PartialName to Signature1.
1. Add the field through [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) using page number 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/SignatureField.h>
#include <Aspose.PDF.Cpp/Document.h>

#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void FormExamples::AddSignatureField(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->Add();

    auto signatureField =
        MakeObject<SignatureField>(page, MakeObject<Aspose::Pdf::Rectangle>(100, 700, 200, 800, true));
    signatureField->set_PartialName(String(u"Signature1"));
    document->get_Form()->Add(signatureField, 1);
    document->Save(outputFile);
}
```
