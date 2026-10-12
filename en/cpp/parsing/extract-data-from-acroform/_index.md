---
title: Extract AcroForm data in C++
linktitle: Extract Data from AcroForm
type: docs
weight: 50
url: /cpp/extract-data-from-acroform/
description: Read PDF form fields and export values to XML, FDF, XFDF, or a JSON-style file using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Read PDF form fields and export values to XML, FDF, XFDF, or a JSON-style file using Aspose.PDF for C++.

## Read field names and values

Print the partial name and value of each form field.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the document form fields.
1. Iterate through the fields and read PartialName and Value.
1. Print each name and value.

Source example: `acroforms-01.cpp`.

```cpp
#include <system/console.h>

#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;

void ExtractFormFields(System::String inputFile)
{
    // Open document
    auto document = MakeObject<Document>(inputFile);

    // Get values from all fields
    for (auto& formField : document->get_Form()->get_Fields()) {
        System::Console::WriteLine(u"Field Name : {0}", formField->get_PartialName());
        System::Console::WriteLine(u"Value : {0}", formField->get_Value());
    }
}
```

## Export form data to XML

Write the form data to an XML output stream.

1. Create a [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade from the input file.
1. Open a writable output stream.
1. Call [ExportXml()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Close the output stream.

Source example: `acroforms-02.cpp`.

```cpp
#include <system/io/file.h>

#include <Aspose.PDF.Cpp/Facades/Form.h>

void ExtractFormFieldsToXML(System::String inputFile, System::String outputFile)
{

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto fdfOutputStream = System::IO::File::OpenWrite(outputFile);

    // Export data
    form->ExportXml(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
}
```

## Export form data to FDF

Write the form data to a FDF output stream.

1. Create a [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade from the input file.
1. Open a writable output stream.
1. Call [ExportFdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Close the output stream.

Source example: `acroforms-03.cpp`.

```cpp
#include <system/io/file.h>

#include <Aspose.PDF.Cpp/Facades/Form.h>

void ExtractFormExportFDF(System::String inputFile, System::String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);

    auto fdfOutputStream = System::IO::File::OpenWrite(outputFile);

    // Export data
    form->ExportFdf(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
}
```

## Export form data to XFDF

Write the form data to an XFDF output stream.

1. Create a [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade from the input file.
1. Open a writable output stream.
1. Call [ExportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Close the output stream.

Source example: `acroforms-04.cpp`.

```cpp
#include <system/io/file.h>

#include <Aspose.PDF.Cpp/Facades/Form.h>

void ExtractFormExportXFDF(System::String inputFile, System::String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);

    auto fdfOutputStream = System::IO::File::OpenWrite(outputFile);

    // Export data
    form->ExportXfdf(fdfOutputStream);

    // Close file stream
    fdfOutputStream->Close();
}
```

## Export field values to a JSON-style file

Build an object mapping field names to values and write it next to the input PDF.

The helper only escapes backslashes and quotation marks. Values containing control characters such as newlines need additional JSON escaping. The example overwrites the derived JSON output path.

1. Create a [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade from the input file.
1. Read FieldNames and retrieve each value with [GetField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Escape backslashes and quotation marks using the supplied helper.
1. Build the object text with StringBuilder.
1. Save the text to inputFile + .json.

Source example: `acroforms-05.cpp`.

```cpp
#include <system/io/file.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/Form.h>

using namespace System;
using namespace Aspose::Pdf::Facades;

static String escapeJson(String value) {
    if (value == nullptr) {
        return String::Empty;
    }
    return value
        .Replace(u"\\", u"\\\\")
        .Replace(u"\"", u"\\\"");
}

void ExtractFormFieldsToJSON(System::String inputFile)
{
    auto form = MakeObject<Form>(inputFile);

    auto json = MakeObject<System::Text::StringBuilder>();
    json->Append(u"{\n");
    auto fieldNames = form->get_FieldNames();
    for (int i = 0; i < fieldNames->get_Length(); i++) {
        String fieldName = fieldNames[i];
        json->Append(u"    \"")
            ->Append(escapeJson(fieldName))
            ->Append(u"\": \"")
            ->Append(escapeJson(form->GetField(fieldName)))
            ->Append(u"\"");
        if (i < fieldNames->get_Length() - 1) {
            json->Append(u",");
        }
        json->Append(u"\n");
    }
    json->Append(u"}\n");
    System::IO::File::WriteAllText(inputFile + u".json", json->ToString());
}
```
