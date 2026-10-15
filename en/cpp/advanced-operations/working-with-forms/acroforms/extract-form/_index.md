---
title: Extract PDF form data in C++
linktitle: Extract AcroForm
type: docs
weight: 30
url: /cpp/extract-form/
description: Read PDF form field values and export a name-to-value JSON object using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read AcroForm Values and Export Field Data to JSON in C++
Abstract: Learn how to enumerate field names and retrieve values through the Form facade in Aspose.PDF for C++. The JSON example escapes strings, while a second entry point delegates to that same implementation.
---

Read PDF form field values and export a name-to-value JSON object using Aspose.PDF for C++.

## Print field names and values

The outputFile parameter is unused; results are printed to the console.

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Iterate through FieldNames.
1. Call [GetField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for each name and print the value.
1. Print the field count and close the facade.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::GetValuesFromAllFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    for (const auto &name : form->get_FieldNames())
        std::cout << name << ": " << form->GetField(name) << std::endl;

    std::cout << "Fields: " << form->get_FieldNames()->get_Length() << std::endl;
    form->Close();
}
```

## Export field values as JSON

This exports names and values, not complete field definitions, widget geometry, or appearance settings.

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Define the helper that escapes quotation marks, backslashes, and control characters.
1. Iterate through FieldNames and retrieve each value with [GetField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Build a JSON object whose properties map field names to string values.
1. Write the JSON text to outputFile and close the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ExtractFormFieldsToJson(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto escape = [](const String &value) {
        String result;
        for (int i = 0; i < value.get_Length(); ++i)
        {
            char16_t c = value[i];
            if (c == u'"' || c == u'\\')
            {
                result += u'\\';
                result += c;
            }
            else if (c < 0x20)
                result += String::Format(u"\\u{0:x4}", static_cast<int>(c));
            else
                result += c;
        }
        return result;
    };
    String json = u"{\n";
    auto names = form->get_FieldNames();
    for (int i = 0; i < names->get_Length(); ++i)
    {
        auto name = names->idx_get(i);
        json += u"    \"" + escape(name) + u"\": \"" + escape(form->GetField(name)) + u"\"";
        if (i + 1 < names->get_Length())
            json += u",";
        json += u"\n";
    }
    json += u"}\n";
    System::IO::File::WriteAllText(outputFile, json);
    form->Close();
}
```

## Use the delegating JSON entry point

Despite the Doc suffix, this wrapper does not use a separate Document-based JSON serialization API.

1. Keep the declaration and implementation of ExtractFormFieldsToJson() available.
1. Call ExtractFormFieldsToJsonDoc() with the input PDF and output JSON paths.
1. Let it delegate to the preceding JSON exporter.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ExtractFormFieldsToJsonDoc(String inputFile, String outputFile)
{
    ExtractFormFieldsToJson(inputFile, outputFile);
}
```
