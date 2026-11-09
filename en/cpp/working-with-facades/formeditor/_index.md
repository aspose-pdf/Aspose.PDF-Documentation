---
title: Create and edit PDF form fields in C++
linktitle: FormEditor Class
type: docs
weight: 20
url: /cpp/formeditor-class/
description: Create, copy, move, decorate, rename, and remove form fields and configure lists, scripts, and submission actions using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Customize PDF Form Fields in C++
Abstract: Use FormEditor to create fields and change their geometry, appearance, and behavior. Examples also copy fields, manage choice items, and configure JavaScript and XFDF submission.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) to create, copy, move, decorate, rename, and remove form fields and configure lists, scripts, and submission actions.

Most examples edit existing named fields. CopyInnerField uses page 2, so its input must contain at least two pages. JavaScript and submit actions depend on viewer support when the output is opened.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add list item

Add New Zealand as a choice in the Country field.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add choice items with [FormEditor::AddListItem()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addlistitem/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FormEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;
	using FormEditor = Aspose::Pdf::Facades::FormEditor;

	void AddListItem(String inputFile, String outputFile)
	{
		auto editor = MakeObject<FormEditor>();

		editor->BindPdf(inputFile);
		editor->AddListItem(u"Country", MakeArray<String>({ u"New Zealand", u"New Zealand" }));
		editor->SaveableFacade::Save(outputFile);
	}
} // namespace Facades::Examples::PDF_FormEditor
```

## Copy inner field

Copy First Name to First Name Copy on page 2 at the specified coordinates.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Copy the field within the document with [FormEditor::CopyInnerField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/copyinnerfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CopyInnerField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->CopyInnerField(u"First Name", u"First Name Copy", 2, 200, 600);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Copy outer field

Create a new one-page destination PDF and copy First Name from the source PDF onto it.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Copy the field from the other PDF with [FormEditor::CopyOuterField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/copyouterfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CopyOuterField(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();

    document->get_Pages()->Add();
    document->Save(outputFile);

    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(outputFile);
    editor->CopyOuterField(inputFile, u"First Name", 1, 200, 600);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Create check box field

Add checkbox1 to page 1 with its name, caption, and rectangle.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the fields with [FormEditor::AddField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FieldType.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateCheckBoxField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->AddField(FieldType::CheckBox, u"checkbox1", u"Check Box 1", 1, 240, 498, 256, 514);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Create combo box field

Create combobox1 on page 1 and add Australia and New Zealand choices.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the fields with [FormEditor::AddField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfield/).
1. Add choice items with [FormEditor::AddListItem()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addlistitem/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FieldType.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateComboBoxField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->AddField(FieldType::ComboBox, u"combobox1", u"Australia", 1, 230, 498, 350, 514);
    editor->AddListItem(u"combobox1", MakeArray<String>({u"Australia", u"Australia"}));
    editor->AddListItem(u"combobox1", MakeArray<String>({u"New Zealand", u"New Zealand"}));
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Create text box field

Add first_name and last_name text fields to page 1 with initial values Alexander and Smith.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the fields with [FormEditor::AddField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FieldType.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void CreateTextBoxField(String inputFile, String outputFile)
	{
		auto editor = MakeObject<FormEditor>();

		editor->BindPdf(inputFile);
		editor->AddField(FieldType::Text, u"first_name", u"Alexander", 1, 50, 570, 150, 590);
		editor->AddField(FieldType::Text, u"last_name", u"Smith", 1, 235, 570, 330, 590);
		editor->SaveableFacade::Save(outputFile);
	}
} // namespace Facades::Examples::PDF_FormEditor
```

## Decorate field

Apply a red background, blue text, green border, and centered alignment to First Name.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set facade through [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) using the example values.
1. Apply the configured appearance with [FormEditor::DecorateField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/decoratefield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Facades/FormFieldFacade.h>
#include <drawing/color.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using DrawingColor = System::Drawing::Color;

void DecorateField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    auto facade = MakeObject<FormFieldFacade>();
    facade->set_BackgroundColor(DrawingColor::get_Red());
    facade->set_TextColor(DrawingColor::get_Blue());
    facade->set_BorderColor(DrawingColor::get_Green());
    facade->set_Alignment(FormFieldFacade::AlignCenter);
    editor->set_Facade(facade);
    editor->DecorateField(u"First Name");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Delete list item

Remove UK from the Country choice field.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the selected choice with [FormEditor::DelListItem()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/dellistitem/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteListItem(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->DelListItem(u"Country", u"UK");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Move field

Move Country to the rectangle (200, 600, 280, 620).

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the field rectangle with [FormEditor::MoveField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/movefield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void MoveField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->MoveField(u"Country", 200, 600, 280, 620);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Remove field

Remove the Country field from the PDF.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Remove the field with [FormEditor::RemoveField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/removefield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->RemoveField(u"Country");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Rename field

Rename City to Town.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Rename the field with [FormEditor::RenameField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/renamefield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RenameField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->RenameField(u"City", u"Town");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Set field alignment

Center the text in First Name.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set field alignment with [FormEditor::SetFieldAlignment()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setfieldalignment/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Facades/FormFieldFacade.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetFieldAlignment(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->SetFieldAlignment(u"First Name", FormFieldFacade::AlignCenter);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Set field script

Add an alert script to Script_Demo_Button, then replace it with a second alert script.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add a field script with [FormEditor::AddFieldScript()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfieldscript/).
1. Replace the field script with [FormEditor::SetFieldScript()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setfieldscript/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetFieldScript(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->AddFieldScript(u"Script_Demo_Button", u"app.alert('Script 1 has been executed');");
    editor->SetFieldScript(u"Script_Demo_Button", u"app.alert('Script 2 has been executed');");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Set submit url

Configure Script_Demo_Button to submit XFDF to the sample HTTPS endpoint.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the submission endpoint with [FormEditor::SetSubmitUrl()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setsubmiturl/).
1. Set the submission format with [FormEditor::SetSubmitFlag()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setsubmitflag/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Facades/SubmitFormFlag.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetSubmitUrl(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->SetSubmitUrl(u"Script_Demo_Button", u"https://www.example.com/submit");
    editor->SetSubmitFlag(u"Script_Demo_Button", SubmitFormFlag::Xfdf);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```

## Single to multiple

Convert City from a single-line field to a multiline field.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Enable multiline input with [FormEditor::Single2Multiple()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/single2multiple/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SingleToMultiple(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->Single2Multiple(u"City");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
