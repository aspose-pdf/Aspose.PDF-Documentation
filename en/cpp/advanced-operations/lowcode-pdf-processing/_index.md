---
title: Process PDFs with LowCode in C++
linktitle: LowCode PDF Processing
type: docs
weight: 220
url: /cpp/lowcode-pdf-processing/
description: Convert, merge, linearize, encrypt, and sign PDFs, extract text, flatten form fields, and add tables with the C++ LowCode API.
lastmod: "2026-11-26"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use the C++ LowCode API for PDF Conversion and Processing
Abstract: Learn how to configure file inputs and outputs and run PDF operations with Aspose.PDF for C++ LowCode processors. The examples cover DOCX conversion, text extraction, form flattening, linearization, encryption, signing, table generation, and merging.
---

The [Aspose::Pdf::LowCode](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/) namespace provides processors for common PDF tasks. Create a processor and its options, register input and output paths with [FileDataSource](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/filedatasource/), and call `Process()`. Text extraction returns its content through a [ResultContainer](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/resultcontainer/).

Add the relevant source code to a project configured with Aspose.PDF for C++, apply your license, and call the example function with your file paths. Use different input and output paths, and create the output directory before running an example that writes a file.

## Convert PDF to DOCX

Convert a PDF into a Word document using the DOCX output format.

1. Create a [DocConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/docconverter/) and [PdfToDocOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/pdftodocoptions/).
2. Set the save format to `SaveFormat::DocX`.
3. Add the input PDF path and the output `.docx` path, then call `Process()`.

```cpp
#include <Aspose.PDF.Cpp/LowCode/DocConverter/DocConverter.h>
#include <Aspose.PDF.Cpp/LowCode/DocConverter/PdfToDocOptions.h>
#include <Aspose.PDF.Cpp/SaveFormat.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <system/string.h>

namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void ConvertPdfToDocx(String inputFile, String outputFile)
    {
        auto processor = MakeObject<DocConverter>();
        auto options = MakeObject<PdfToDocOptions>();
        options->set_SaveFormat(SaveFormat::DocX);
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        processor->Process(options);
    }
}
```

## Extract Text from a PDF

Read text from a PDF and print each result to the console.

1. Create a [TextExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/textextractor/) and [TextExtractorOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/textextractoroptions/).
2. Add the input PDF path and call `Process()`.
3. Iterate over the result collection and print each result using `ToString()`.

```cpp
#include <Aspose.PDF.Cpp/LowCode/TextExtractor/TextExtractor.h>
#include <Aspose.PDF.Cpp/LowCode/TextExtractor/TextExtractorOptions.h>
#include <Aspose.PDF.Cpp/LowCode/ResultContainer.h>
#include <Aspose.PDF.Cpp/LowCode/IOperationResult.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <system/string.h>
#include <system/console.h>
#include <system/collections/list.h>
namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void ExtractPdfText(String inputFile)
    {
        auto processor = MakeObject<TextExtractor>();
        auto options = MakeObject<TextExtractorOptions>();
        options->AddInput(MakeObject<FileDataSource>(inputFile));

        // Text extraction returns text through the result collection.
        auto results = processor->Process(options);
        for (const auto& result : results->get_ResultCollection())
        {
            Console::WriteLine(result->ToString());
        }
    }
}
```

## Flatten All PDF Form Fields

Flatten every field in a filled PDF form so its visible appearance becomes part of the page content.

1. Create a [FormFlattener](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/formflattener/) and [FormFlattenAllFieldsOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/formflattenallfieldsoptions/).
2. Add the filled PDF form and the output PDF path.
3. Call `Process()` to save the flattened form.

```cpp
#include <Aspose.PDF.Cpp/LowCode/FormFlattener/FormFlattener.h>
#include <Aspose.PDF.Cpp/LowCode/FormFlattener/FormFlattenAllFieldsOptions.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <system/string.h>

namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void FlattenFormFields(String inputFile, String outputFile)
    {
        auto processor = MakeObject<FormFlattener>();
        // Use a PDF containing filled form fields as input.
        auto options = MakeObject<FormFlattenAllFieldsOptions>();
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        processor->Process(options);
    }
}
```

## Linearize a PDF

Prepare a PDF for progressive loading by saving a linearized copy.

1. Create an [Optimizer](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/optimizer/) and [OptimizeOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/optimizeoptions/).
2. Add the input and output PDF paths.
3. Call `Process()` to write the linearized PDF.

```cpp
#include <Aspose.PDF.Cpp/LowCode/Optimizer/Optimizer.h>
#include <Aspose.PDF.Cpp/LowCode/Optimizer/OptimizeOptions.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <system/string.h>

namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void OptimizePdf(String inputFile, String outputFile)
    {
        auto processor = MakeObject<Optimizer>();
        // OptimizeOptions requests document linearization.
        auto options = MakeObject<OptimizeOptions>();
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        processor->Process(options);
    }
}
```

## Encrypt a PDF with AES-256

Protect a PDF with owner and user passwords and restrict user permissions with the ForbidAll preset.

1. Create a [Security](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/security/) processor.
2. Create [EncryptionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/encryptionoptions/) with the owner and user passwords, the ForbidAll privilege preset, and the AES-256 algorithm.
3. Add the input and output PDF paths, then call `Process()`.
4. Read the first operation result and print the output path returned by `ToFile()`.

```cpp
#include <Aspose.PDF.Cpp/LowCode/Security/Security.h>
#include <Aspose.PDF.Cpp/LowCode/Security/EncryptionOptions.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <Aspose.PDF.Cpp/LowCode/ResultContainer.h>
#include <Aspose.PDF.Cpp/LowCode/IOperationResult.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileResult.h>
#include <system/string.h>
#include <system/console.h>
#include <system/collections/list.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>

namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void EncryptPdf(String inputFile, String outputFile, String ownerPassword, String userPassword)
    {
        auto processor = MakeObject<Aspose::Pdf::LowCode::Security>();
        auto options = MakeObject<EncryptionOptions>(ownerPassword, userPassword,
            Aspose::Pdf::Facades::DocumentPrivilege::get_ForbidAll(),
            Aspose::Pdf::CryptoAlgorithm::AESx256);
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        auto result = processor->Process(options)->get_ResultCollection()->idx_get(0);
        Console::WriteLine(u"Encrypted PDF saved to: " + result->ToFile());
    }
}
```

## Add a Visible Digital Signature to a PDF

Sign the first page of a PDF and place a visible signature in a specified rectangle. Use a PDF with at least one page and a PFX or P12 certificate that contains the private key.

1. Create a [Signature](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/signature/) processor and initialize [SignOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/signoptions/) with the certificate path and password.
2. Set the page number to 1, enable signature visibility, and specify the rectangle and signing reason.
3. Add the input and output PDF paths, then call `Process()` to save the signed PDF.

```cpp
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <Aspose.PDF.Cpp/LowCode/Signature/Signature.h>
#include <Aspose.PDF.Cpp/LowCode/Signature/SignOptions.h>
#include <Aspose.PDF.Cpp/LowCode/IDataSource.h>
#include <system/string.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void SignPdf(String inputFile, String outputFile, String certificateFile, String certificatePassword)
    {
        auto processor = MakeObject<Signature>();
        // Supply a PFX/P12 certificate containing the private key.
        auto options = MakeObject<SignOptions>(certificateFile, certificatePassword);
        options->set_PageNumber(1);
        options->set_Visible(true);
        options->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(50, 50, 250, 120));
        options->set_Reason(u"Document approval");
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        processor->Process(options);
    }
}
```

## Add a Table to a PDF

Add a two-column table with one header row and one data row to an existing PDF.

1. Create a [TableGenerator](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/tablegenerator/) and [TableOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/tableoptions/). Add the input and output PDF paths.
2. Call the AddTable method on the options, then use [TableBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/tablebuilder/) and [TableRowBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/tablerowbuilder/) to create two rows with two cells each.
3. Use [TableCellBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/tablecellbuilder/) to add a text fragment to each cell, then call the Process method to save the PDF.

```cpp
#include <Aspose.PDF.Cpp/LowCode/PdfGenerator/TableGenerator.h>
#include <Aspose.PDF.Cpp/LowCode/PdfGenerator/TableOptions.h>
#include <Aspose.PDF.Cpp/LowCode/PdfGenerator/Builder/TableRowBuilder.h>
#include <Aspose.PDF.Cpp/LowCode/PdfGenerator/Builder/TableCellBuilder.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <system/string.h>
#include <Aspose.PDF.Cpp/Generator/BaseParagraph.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <system/array.h>
namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void AddTableToPdf(String inputFile, String outputFile)
    {
        auto processor = MakeObject<TableGenerator>();
        auto options = MakeObject<TableOptions>();
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));

        auto table = options->AddTable();
        auto header = table->AddRow();
        header->AddCell()->AddParagraph(MakeArray<SharedPtr<Aspose::Pdf::BaseParagraph>>({
            MakeObject<Aspose::Pdf::Text::TextFragment>(u"Document") }));
        header->AddCell()->AddParagraph(MakeArray<SharedPtr<Aspose::Pdf::BaseParagraph>>({
            MakeObject<Aspose::Pdf::Text::TextFragment>(u"Status") }));

        auto row = table->AddRow();
        row->AddCell()->AddParagraph(MakeArray<SharedPtr<Aspose::Pdf::BaseParagraph>>({
            MakeObject<Aspose::Pdf::Text::TextFragment>(u"Annual report") }));
        row->AddCell()->AddParagraph(MakeArray<SharedPtr<Aspose::Pdf::BaseParagraph>>({
            MakeObject<Aspose::Pdf::Text::TextFragment>(u"Approved") }));
        processor->Process(options);
    }
}
```

## Merge Two PDF Documents

Combine two PDFs into one file. Pages from the first input appear before pages from the second.

1. Create a [Merger](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/merger/) and [MergeOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.lowcode/mergeoptions/).
2. Add both input PDF paths in the order their pages should appear.
3. Add the output PDF path and call `Process()` to write the merged file.

```cpp
#include <Aspose.PDF.Cpp/LowCode/Merger/Merger.h>
#include <Aspose.PDF.Cpp/LowCode/Merger/MergeOptions.h>
#include <Aspose.PDF.Cpp/LowCode/Implementations/FileDataSource.h>
#include <system/string.h>

namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void MergePdfDocuments(String firstInputFile, String secondInputFile, String outputFile)
    {
        auto processor = MakeObject<Merger>();
        auto options = MakeObject<MergeOptions>();
        // Input order determines the page order in the merged document.
        options->AddInput(MakeObject<FileDataSource>(firstInputFile));
        options->AddInput(MakeObject<FileDataSource>(secondInputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        processor->Process(options);
    }
}
```

See the [Aspose.PDF for C++ API Reference](https://reference.aspose.com/pdf/cpp/) for the full API.
