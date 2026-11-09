---
title: Fill and inspect PDF forms in C++
linktitle: Form Class
type: docs
weight: 10
url: /cpp/form-class/
description: Fill fields, exchange FDF, XFDF, and XML data, add button images, inspect values, rename fields, and flatten forms using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage AcroForm Data and Field Values in C++
Abstract: Use the Form facade to fill existing PDF fields and import or export form data. The examples also inspect values, rename fields, flatten forms, and set an image appearance.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) to fill fields, exchange FDF, XFDF, and XML data, add button images, inspect values, rename fields, and flatten forms.

The samples use named fields from the supplied form fixtures. Use a PDF with matching field names and appropriate field types; importing data also requires a compatible FDF, XFDF, or XML file.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add image appearance to button field

Fill the Image1_af_image button image field from an image stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the field image appearance with [Form::FillImageField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillimagefield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;
	using Form = Aspose::Pdf::Facades::Form;

	void AddImageAppearanceToButtonField(String inputFile, String imageFile, String outputFile)
	{
		auto form = MakeObject<Form>();
		auto imageStream = System::IO::File::OpenRead(imageFile);

		form->Facade::BindPdf(inputFile);
		form->FillImageField(u"Image1_af_image", imageStream);
		form->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_Form
```

## Export FDF

Export the bound form data to an FDF output stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Write FDF data with [Form::ExportFdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/exportfdf/).
1. Use the output stream as the exported data file.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ExportFdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto outputStream = System::IO::File::Create(outputFile);

    form->Facade::BindPdf(inputFile);
    form->ExportFdf(outputStream);
}
} // namespace Facades::Examples::PDF_Form
```

## Export XFDF

Export the bound form data to an XFDF output stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Write XFDF data with [Form::ExportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/exportxfdf/).
1. Use the output stream as the exported data file.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ExportXfdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto outputStream = System::IO::File::Create(outputFile);

    form->Facade::BindPdf(inputFile);
    form->ExportXfdf(outputStream);
}
} // namespace Facades::Examples::PDF_Form
```

## Export XML

Export the bound form data to an XML output stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Write XML data with [Form::ExportXml()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/exportxml/).
1. Use the output stream as the exported data file.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ExportXml(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto outputStream = System::IO::File::Create(outputFile);

    form->Facade::BindPdf(inputFile);
    form->ExportXml(outputStream);
}
} // namespace Facades::Examples::PDF_Form
```

## Fill barcode fields

Set product_barcode to 123456789012.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the barcode field value with [Form::FillBarcodeField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillbarcodefield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FillBarcodeFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillBarcodeField(u"product_barcode", u"123456789012");
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Fill check box fields

Set subscribe_newsletter and accept_terms to the export value Yes.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Fill the named fields with [Form::FillField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillfield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FillCheckBoxFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"subscribe_newsletter", String(u"Yes"));
    form->FillField(u"accept_terms", String(u"Yes"));
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Fill list box fields

Set favorite_colors to Red.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Fill the named fields with [Form::FillField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillfield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FillListBoxFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"favorite_colors", String(u"Red"));
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Fill radio button fields

Select option index 0 in the gender field.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Fill the named fields with [Form::FillField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillfield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FillRadioButtonFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"gender", 0);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Fill text fields

Fill name, address, and email with the sample contact details.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Fill the named fields with [Form::FillField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillfield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FillTextFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"name", String(u"John Doe"));
    form->FillField(u"address", String(u"123 Main St, Anytown, USA"));
    form->FillField(u"email", String(u"john.doe@example.com"));
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Flatten all fields

Flatten all form fields into page content before saving the PDF.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Flatten the fields with [Form::FlattenAllFields()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/flattenallfields/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FlattenAllFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FlattenAllFields();
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Import FDF

Read FDF data from dataFile and import it into the bound form.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import FDF data with [Form::ImportFdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/importfdf/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ImportFdf(String inputFile, String dataFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto inputStream = System::IO::File::OpenRead(dataFile);

    form->Facade::BindPdf(inputFile);
    form->ImportFdf(inputStream);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Import XFDF

Read XFDF data from dataFile and import it into the bound form.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import XFDF data with [Form::ImportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/importxfdf/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ImportXfdf(String inputFile, String dataFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto inputStream = System::IO::File::OpenRead(dataFile);

    form->Facade::BindPdf(inputFile);
    form->ImportXfdf(inputStream);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Import XML

Read XML data from dataFile and import it into the bound form.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import XML data with [Form::ImportXml()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/importxml/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ImportXml(String inputFile, String dataFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto inputStream = System::IO::File::OpenRead(dataFile);

    form->Facade::BindPdf(inputFile);
    form->ImportXml(inputStream);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```

## Inspect form fields

Enumerate field names and print each field's current value.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read field names through [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Read each field value with [Form::GetField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/getfield/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void InspectFormFields(String inputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);

    for (auto fieldName : form->get_FieldNames())
    {
        std::cout << fieldName << " = " << form->GetField(fieldName) << std::endl;
    }
}
} // namespace Facades::Examples::PDF_Form
```

## Rename form fields

Rename First Name and Last Name to NewFirstName and NewLastName.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Rename the field with [Form::RenameField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/renamefield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void RenameFormFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->RenameField(u"First Name", u"NewFirstName");
    form->RenameField(u"Last Name", u"NewLastName");
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
