---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /cpp/whatsnew/
description: Review selected Aspose.PDF for C++ release highlights, including new conversion formats, image handling, forms, and runtime improvements.
lastmod: "2026-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: false
AlternativeHeadline: Aspose.PDF for C++ Release Highlights
Abstract: Explore selected C++ release updates from 21.4 through 26.10, including Markdown and RTF conversion, accessibility, document security, annotations, and PDF comparison. The release notes provide the complete change history.
---

This page highlights selected new features in Aspose.PDF for C++. Releases from 25.3 through 26.10 have been reviewed for new functionality; releases containing only fixes, performance improvements, or codebase updates are omitted from these highlights. For the complete change history, see the [Aspose.PDF for C++ release notes](https://releases.aspose.com/pdf/cpp/release-notes/).

## What's new in Aspose.PDF 26.10

Preserve Literal Special Symbols During PDF Generation

Control placeholder processing with `Page::ProcessSpecialSymbols`. Disable it to keep sequences such as `$p` and `$P` as literal text.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <system/string.h>

namespace LiteralSpecialSymbolsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void PreserveLiteralSpecialSymbols(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();

        // Disable placeholder processing before adding generated content.
        page->set_ProcessSpecialSymbols(false);
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(
            u"Literal placeholders: $p and $P"));
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(
            u"Page $p of $P"));

        // Both sequences remain literal text in the saved PDF.
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <system/string.h>

namespace LiteralSpecialSymbolsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void ProcessSpecialSymbolPlaceholders(String outputFile)
    {
        auto document = MakeObject<Document>();
        for (int i = 1; i <= 2; ++i)
        {
            auto page = document->get_Pages()->Add();
            // Processing is enabled by default; set it explicitly for comparison.
            page->set_ProcessSpecialSymbols(true);
            page->get_Paragraphs()->Add(MakeObject<TextFragment>(
                u"Page $p of $P"));
        }

        // Expected text: "Page 1 of 2" and "Page 2 of 2".
        document->Save(outputFile);
    }
}
```

## What's new in Aspose.PDF 26.9

Preserve Underline and Strikeout Formatting in PDF to PPTX Conversion

Recognize underline and strikeout formatting with `PptxSaveOptions::RecognizeUnderlineAndStrikeout`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PptxSaveOptions.h>
#include <system/string.h>

namespace PdfToPptxTextDecorationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ConvertPdfToPptxRecognizeTextDecoration(String inputFile, String outputFile)
    {
        // Use a PDF containing underlined and struck-out text as input.
        auto document = MakeObject<Document>(inputFile);
        auto options = MakeObject<PptxSaveOptions>();

        // Export slide content as editable elements rather than page images.
        options->set_SlidesAsImages(false);
        // Recognize underline and strikeout lines as text formatting.
        options->set_RecognizeUnderlineAndStrikeout(true);

        document->Save(outputFile, options);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PptxSaveOptions.h>
#include <system/string.h>

namespace PdfToPptxTextDecorationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ConvertPdfToPptxWithoutTextDecorationRecognition(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto options = MakeObject<PptxSaveOptions>();
        options->set_SlidesAsImages(false);

        // Disable interpretation of underline and strikeout lines as text styles.
        // This does not request removal of those lines from the exported slide.
        options->set_RecognizeUnderlineAndStrikeout(false);

        // Use the same input and a different .pptx output to compare both settings.
        document->Save(outputFile, options);
    }
}
```

Resolve Names of Embedded Files

Resolve embedded file names with `FileSpecification::GetFileName()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/EmbeddedFileCollection.h>
#include <Aspose.PDF.Cpp/FileSpecification.h>
#include <system/console.h>
#include <system/string.h>

namespace ResolveEmbeddedFileNamesExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ListResolvedEmbeddedFileNames(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto embeddedFiles = document->get_EmbeddedFiles();
        if (embeddedFiles->get_Count() == 0)
        {
            Console::WriteLine(u"The PDF contains no document-level embedded files.");
            return;
        }

        for (const auto& file : embeddedFiles)
        {
            // Resolve UnicodeName, Name, or the embedded-file collection key.
            // With no fallback and empty names disabled, a name is generated
            // when no usable name is available.
            String resolvedName = file->GetFileName(String::Empty, false);
            Console::WriteLine(u"Resolved embedded file name: {0}", resolvedName);
        }
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/EmbeddedFileCollection.h>
#include <Aspose.PDF.Cpp/FileSpecification.h>
#include <system/console.h>
#include <system/string.h>

namespace ResolveEmbeddedFileNamesExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ResolveEmbeddedFileNamesWithOptions(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto embeddedFiles = document->get_EmbeddedFiles();
        if (embeddedFiles->get_Count() == 0)
        {
            Console::WriteLine(u"The PDF contains no document-level embedded files.");
            return;
        }

        int index = 0;
        for (const auto& file : embeddedFiles)
        {
            ++index;
            // A fallback is used only when no stored name can be resolved.
            String fallback = String::Format(u"attachment-{0}.bin", index);
            String resolvedName = file->GetFileName(fallback, false);
            Console::WriteLine(u"Name with fallback: {0}", resolvedName);

            // Allow an empty result when a name source explicitly contains
            // an empty string and no non-empty name is available.
            String emptyAllowedName = file->GetFileName(String::Empty, true);
            if (String::IsNullOrEmpty(emptyAllowedName))
            {
                Console::WriteLine(u"The resolved name is empty when empty names are allowed.");
            }
            else
            {
                Console::WriteLine(u"Name with empty names allowed: {0}", emptyAllowedName);
            }
        }
    }
}
```

## What's new in Aspose.PDF 26.8

JPEG EXIF Orientation Support

Respect EXIF orientation when loading JPEG images.

## What's new in Aspose.PDF 26.7

Side-by-Side PDF Comparison Results

Retrieve document and page comparison results from `SideBySidePdfComparer::Compare()`, including change detection and detailed differences.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySideComparisonOptions.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySidePdfComparer.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySideDocsComparisonResult.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySidePagesComparisonResult.h>
#include <Aspose.PDF.Cpp/Comparison/TextComparison/DiffOperation.h>
#include <system/collections/list.h>
#include <system/console.h>

namespace SideBySideComparisonResultsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Comparison;

    void CompareDocumentsAndReadResults(String firstInputFile, String secondInputFile, String outputFile)
    {
        auto first = MakeObject<Document>(firstInputFile);
        auto second = MakeObject<Document>(secondInputFile);
        auto options = MakeObject<SideBySideComparisonOptions>();
        options->set_AdditionalChangeMarks(true);
        auto result = SideBySidePdfComparer::Compare(first, second, outputFile, options);
        Console::WriteLine(u"Documents have changes: {0}", result->get_HasChanges());

        // The outer list is indexed by compared page pair, starting at zero.
        auto pageDifferences = result->get_FullChanges();
        for (int index = 0; index < pageDifferences->get_Count(); ++index)
        {
            Console::WriteLine(u"Compared page pair: {0}", index + 1);
            auto differences = pageDifferences->idx_get(index);
            if (differences == nullptr)
            {
                continue;
            }
            for (const auto& difference : differences)
            {
                Console::WriteLine(difference->ToString());
            }
        }

        // Per-document lists expose the changes associated with each side.
        auto firstChanges = result->get_FirstDocChanges();
        auto secondChanges = result->get_SecondDocChanges();
        Console::WriteLine(u"First document page-result entries: {0}", firstChanges->get_Count());
        Console::WriteLine(u"Second document page-result entries: {0}", secondChanges->get_Count());
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySideComparisonOptions.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySidePdfComparer.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySideDocsComparisonResult.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySidePagesComparisonResult.h>
#include <Aspose.PDF.Cpp/Comparison/TextComparison/DiffOperation.h>
#include <system/collections/list.h>
#include <system/console.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/exceptions.h>

namespace SideBySideComparisonResultsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Comparison;

    void ComparePagesAndReadResults(String firstInputFile, int firstPageNumber, String secondInputFile, int secondPageNumber, String outputFile)
    {
        auto first = MakeObject<Document>(firstInputFile);
        auto second = MakeObject<Document>(secondInputFile);
        auto options = MakeObject<SideBySideComparisonOptions>();
        options->set_AdditionalChangeMarks(true);
        // PageCollection indexes are one-based.
        if (firstPageNumber < 1 || firstPageNumber > first->get_Pages()->get_Count()
            || secondPageNumber < 1 || secondPageNumber > second->get_Pages()->get_Count())
        {
            throw ArgumentOutOfRangeException(u"pageNumber");
        }

        auto result = SideBySidePdfComparer::Compare(
            first->get_Pages()->idx_get(firstPageNumber),
            second->get_Pages()->idx_get(secondPageNumber), outputFile, options);
        Console::WriteLine(u"Pages have changes: {0}", result->get_HasChanges());
        Console::WriteLine(u"First page changes: {0}", result->get_FirstPageChanges()->get_Count());
        Console::WriteLine(u"Second page changes: {0}", result->get_SecondPageChanges()->get_Count());

        for (const auto& difference : result->get_FullChanges())
        {
            Console::WriteLine(u"Operation: {0}; text: {1}",
                static_cast<int>(difference->get_Operation()), difference->get_Text());
        }
    }
}
```

## What's new in Aspose.PDF 26.3

Page Collection Update Methods

Use the new `PageCollection::BeginUpdate()` and `EndUpdate()` methods.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <system/string.h>

namespace PageCollectionUpdateMethodsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void BatchAddPages(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto pages = document->get_Pages();

        // Suspend page-cache recalculation during the group of additions.
        pages->BeginUpdate();
        try
        {
            for (int i = 1; i <= 10; ++i)
            {
                auto page = pages->Add();
                page->get_Paragraphs()->Add(MakeObject<TextFragment>(
                    String::Format(u"Batch-created page {0}", i)));
            }
        }
        catch (...)
        {
            pages->EndUpdate();
            throw;
        }

        // Restore normal cache recalculation before saving.
        pages->EndUpdate();
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/exceptions.h>
#include <system/string.h>

namespace PageCollectionUpdateMethodsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void BatchDeleteEvenPages(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto pages = document->get_Pages();
        int originalCount = pages->get_Count();
        if (originalCount < 2)
        {
            throw ArgumentException(u"The input PDF must contain at least two pages.");
        }

        pages->BeginUpdate();
        try
        {
            // Page numbers are one-based. Delete backwards to preserve the
            // original indexes of the pages that have not yet been processed.
            int lastEvenPage = originalCount - originalCount % 2;
            for (int pageNumber = lastEvenPage; pageNumber >= 2; pageNumber -= 2)
            {
                pages->Delete(pageNumber);
            }
        }
        catch (...)
        {
            pages->EndUpdate();
            throw;
        }

        pages->EndUpdate();
        // Use a separate output path to preserve the original PDF.
        document->Save(outputFile);
    }
}
```

## What's new in Aspose.PDF 26.2

RTF to PDF Conversion

Convert RTF documents directly to PDF using `RtfLoadOptions`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/RtfLoadOptions.h>
#include <system/string.h>

namespace RtfToPdfConversionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ConvertRtfFileToPdf(String inputFile, String outputFile)
    {
        // Specify RTF loading explicitly; no intermediate format is required.
        auto options = MakeObject<RtfLoadOptions>();
        auto document = MakeObject<Document>(inputFile, options);

        // Use a .pdf output path different from the source .rtf path.
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/RtfLoadOptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace RtfToPdfConversionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ConvertRtfStreamToPdf(String inputFile, String outputFile)
    {
        auto input = System::IO::File::OpenRead(inputFile);
        try
        {
            // The stream overload also accepts RtfLoadOptions directly.
            auto options = MakeObject<RtfLoadOptions>();
            auto document = MakeObject<Document>(input, options);
            document->Save(outputFile);
        }
        catch (...)
        {
            input->Close();
            throw;
        }

        // Keep the source stream open until conversion and saving finish.
        input->Close();
    }
}
```

Complete Deletion of Invisible Text Objects

Detect and remove invisible text with `TextFragmentAbsorber`, including text hidden by its invisibility flag, rendering mode, or fully transparent foreground color.

The examples inspect every page. The shared helper detects invisible rendering, the invisibility flag, and fully transparent fill-only text; it preserves text with a visible stroked outline.

Shared helper: `invisible-text-object-deletion/invisible-text-check.h`. Save this file beside the examples that include it.

```cpp
#pragma once

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/Text/TextRenderingMode.h>

namespace InvisibleTextObjectDeletionExamples
{
    inline bool IsInvisibleText(const System::SharedPtr<Aspose::Pdf::Text::TextFragment>& fragment)
    {
        using Aspose::Pdf::Text::TextRenderingMode;
        auto state = fragment->get_TextState();
        if (state->get_Invisible() || state->get_RenderingMode() == TextRenderingMode::Invisible)
        {
            return true;
        }

        // A transparent fill does not hide a visible stroked outline.
        auto mode = state->get_RenderingMode();
        auto foreground = state->get_ForegroundColor();
        return mode == TextRenderingMode::FillText
            && foreground != nullptr && foreground->get_A() == 0;
    }
}
```

```cpp
#include "invisible-text-check.h"
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <system/console.h>

namespace InvisibleTextObjectDeletionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void DetectInvisibleText(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        int total = 0;
        for (int pageNumber = 1; pageNumber <= document->get_Pages()->get_Count(); ++pageNumber)
        {
            auto absorber = MakeObject<TextFragmentAbsorber>();
            document->get_Pages()->idx_get(pageNumber)->Accept(absorber);
            int count = 0;
            for (const auto& fragment : absorber->get_TextFragments())
            {
                if (IsInvisibleText(fragment))
                {
                    ++count;
                }
            }
            // Report counts without exposing potentially sensitive text.
            Console::WriteLine(u"Page {0}: {1} invisible text fragments", pageNumber, count);
            total += count;
        }
        Console::WriteLine(u"Total invisible text fragments: {0}", total);
    }
}
```

```cpp
#include "invisible-text-check.h"
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <system/console.h>
#include <vector>

namespace InvisibleTextObjectDeletionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void RemoveInvisibleTextObjects(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        int removed = 0;
        for (int pageNumber = 1; pageNumber <= document->get_Pages()->get_Count(); ++pageNumber)
        {
            auto absorber = MakeObject<TextFragmentAbsorber>();
            document->get_Pages()->idx_get(pageNumber)->Accept(absorber);
            auto fragments = absorber->get_TextFragments();

            // Collect first so removal does not invalidate enumeration.
            std::vector<SharedPtr<TextFragment>> invisibleFragments;
            for (const auto& fragment : fragments)
            {
                if (IsInvisibleText(fragment))
                {
                    invisibleFragments.push_back(fragment);
                }
            }

            for (const auto& fragment : invisibleFragments)
            {
                // Remove the fragment from both the collection and the document.
                fragments->Remove(fragment);
                ++removed;
            }
        }

        // Save a new PDF; use an output path different from the input path.
        document->Save(outputFile);
        Console::WriteLine(u"Removed invisible text fragments: {0}", removed);
    }
}
```

## What's new in Aspose.PDF 26.1

RTF Loading and Conversion APIs

The `RtfLoadOptions` and `RtfConverter` APIs were added ahead of the RTF conversion feature announcement in 26.2.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/RtfConverter.h>
#include <Aspose.PDF.Cpp/RtfLoadOptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace RtfLoadingAndConversionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ConvertRtfStreamToPdf(String inputFile, String outputFile)
    {
        auto input = System::IO::File::OpenRead(inputFile);
        auto options = MakeObject<RtfLoadOptions>();
        auto document = MakeObject<Document>();

        try
        {
            // Populate the destination document from the RTF input stream.
            RtfConverter::ToPdf(document, input, options);
            document->Save(outputFile);
        }
        catch (...)
        {
            input->Close();
            throw;
        }

        input->Close();
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/RtfLoadOptions.h>
#include <system/string.h>

namespace RtfLoadingAndConversionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void LoadRtfAndSaveAsPdf(String inputFile, String outputFile)
    {
        // Pass an RTF file as input and a different .pdf path as output.
        auto options = MakeObject<RtfLoadOptions>();
        auto document = MakeObject<Document>(inputFile, options);

        document->Save(outputFile);
    }
}
```

## What's new in Aspose.PDF 25.12

Detect Unsigned Content in Signed PDFs

Inspect signature coverage and retrieve unsigned pages, form widgets, XForms, and annotations with `UnsignedContentAbsorber`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Security/UnsignedContentAbsorber.h>
#include <system/console.h>
#include <system/string.h>
#include <system/collections/list.h>
#include <system/collections/dictionary.h>

namespace DetectUnsignedContentExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Facades;
    using namespace Aspose::Pdf::Security;

    void InspectSignatureCoverage(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto signatures = MakeObject<PdfFileSignature>(document);
        if (!signatures->ContainsSignature())
        {
            Console::WriteLine(u"The PDF contains no digital signatures.");
            return;
        }

        auto absorber = MakeObject<UnsignedContentAbsorber>(signatures);
        auto result = absorber->TryGetContent();
        if (result == nullptr)
        {
            Console::WriteLine(u"No analysis result was returned.");
            return;
        }

        Console::WriteLine(u"Analysis succeeded: {0}", result->get_Success());
        Console::WriteLine(u"Message: {0}", result->get_Message());
        Console::WriteLine(u"Signature coverage: {0}", static_cast<int>(result->get_Coverage()));
        if (!result->get_Success())
        {
            // A failed analysis must not be treated as an absence of unsigned content.
            return;
        }
        // Coverage describes signed-content coverage; this example does not
        // perform certificate-chain or revocation validation.
        auto content = result->get_UnsignedContent();
        if (content == nullptr)
        {
            Console::WriteLine(u"No unsigned-content collection was returned.");
            return;
        }

        auto pages = content->get_Pages();
        auto forms = content->get_Forms();
        auto xforms = content->get_XForms();
        auto annotations = content->get_Annotations();
        Console::WriteLine(u"Unsigned/modified pages: {0}", pages ? pages->get_Count() : 0);
        Console::WriteLine(u"Unsigned/modified form widgets: {0}", forms ? forms->get_Count() : 0);
        Console::WriteLine(u"Unsigned/modified XForms: {0}", xforms ? xforms->get_Count() : 0);
        Console::WriteLine(u"Unsigned/modified annotations: {0}", annotations ? annotations->get_Count() : 0);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Security/UnsignedContentAbsorber.h>
#include <system/console.h>
#include <system/string.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/XForm.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <system/collections/list.h>
#include <system/collections/dictionary.h>

namespace DetectUnsignedContentExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Facades;
    using namespace Aspose::Pdf::Security;

    void RetrieveUnsignedContent(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto signatures = MakeObject<PdfFileSignature>(document);
        if (!signatures->ContainsSignature())
        {
            Console::WriteLine(u"The PDF contains no digital signatures.");
            return;
        }

        auto absorber = MakeObject<UnsignedContentAbsorber>(signatures);
        auto result = absorber->TryGetContent();
        if (result == nullptr)
        {
            Console::WriteLine(u"No analysis result was returned.");
            return;
        }

        Console::WriteLine(u"Analysis succeeded: {0}", result->get_Success());
        Console::WriteLine(u"Message: {0}", result->get_Message());
        Console::WriteLine(u"Signature coverage: {0}", static_cast<int>(result->get_Coverage()));
        if (!result->get_Success())
        {
            // A failed analysis must not be treated as an absence of unsigned content.
            return;
        }
        auto content = result->get_UnsignedContent();
        if (content == nullptr)
        {
            Console::WriteLine(u"No unsigned-content collection was returned.");
            return;
        }

        auto pages = content->get_Pages();
        if (pages != nullptr)
        {
            for (const auto& page : pages)
            {
                Console::WriteLine(u"Unsigned/modified page: {0}", page->get_Number());
            }
        }

        auto widgets = content->get_Forms();
        if (widgets != nullptr)
        {
            for (const auto& widget : widgets)
            {
                Console::WriteLine(u"Unsigned/modified widget rectangle: {0}",
                    widget->get_Rect()->ToString());
            }
        }

        // XForms can be reported when the containing page itself is not in Pages.
        auto xforms = content->get_XForms();
        if (xforms != nullptr)
        {
            for (const auto& entry : xforms)
            {
                auto xform = entry.get_Value();
                Console::WriteLine(u"Unsigned/modified XForm object: {0}, name: {1}",
                    entry.get_Key(), xform->get_Name());
            }
        }

        auto annotations = content->get_Annotations();
        if (annotations != nullptr)
        {
            for (const auto& entry : annotations)
            {
                auto annotation = entry.get_Value();
                Console::WriteLine(u"Unsigned/modified annotation object: {0}, rectangle: {1}",
                    entry.get_Key(), annotation->get_Rect()->ToString());
            }
        }

        // Inspect only: do not save or alter the signed input document.
    }
}
```

## What's new in Aspose.PDF 25.11

Hidden Data Sanitization

Remove hidden or sensitive document data with `HiddenDataSanitizer` and configurable sanitization options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/HiddenDataSanitization/HiddenDataSanitizer.h>
#include <Aspose.PDF.Cpp/Security/HiddenDataSanitization/HiddenDataSanitizationOptions.h>
#include <system/string.h>

namespace HiddenDataSanitizationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Security::HiddenDataSanitization;

    void SanitizeHiddenDataAllOptions(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);

        // The preset removes annotations, scripts/actions, metadata, attachments,
        // search indexes and private information, and flattens forms and layers.
        auto options = HiddenDataSanitizationOptions::All();
        // All() does not enable page rasterization.
        options->set_ConvertPagesToImages(false);

        auto sanitizer = MakeObject<HiddenDataSanitizer>(options);
        sanitizer->Sanitize(document);

        // Use a different output path to retain the original document.
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/HiddenDataSanitization/HiddenDataSanitizer.h>
#include <Aspose.PDF.Cpp/Security/HiddenDataSanitization/HiddenDataSanitizationOptions.h>
#include <system/string.h>

namespace HiddenDataSanitizationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Security::HiddenDataSanitization;

    void SanitizeHiddenDataAndRasterize(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);

        auto options = HiddenDataSanitizationOptions::All();
        // Clean up first, then replace page contents with rendered images.
        // Text becomes image content and is no longer searchable or selectable.
        options->set_ConvertPagesToImages(true);
        options->set_ImageDpi(200);

        auto sanitizer = MakeObject<HiddenDataSanitizer>(options);
        sanitizer->Sanitize(document);

        // Use a different output path to retain the original document.
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/HiddenDataSanitization/HiddenDataSanitizer.h>
#include <Aspose.PDF.Cpp/Security/HiddenDataSanitization/HiddenDataSanitizationOptions.h>
#include <system/string.h>

namespace HiddenDataSanitizationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Security::HiddenDataSanitization;

    void SanitizeHiddenDataSelectedOptions(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);

        auto options = MakeObject<HiddenDataSanitizationOptions>();
        options->set_RemoveMetadata(true);
        options->set_RemoveAttachments(true);
        options->set_RemoveJavaScriptsAndActions(true);
        options->set_RemoveSearchIndexAndPrivateInfo(true);

        // Keep annotations, editable forms, and separate layers in this example.
        options->set_RemoveAnnotations(false);
        options->set_FlattenForms(false);
        options->set_FlattenLayers(false);
        options->set_ConvertPagesToImages(false);

        auto sanitizer = MakeObject<HiddenDataSanitizer>(options);
        sanitizer->Sanitize(document);

        // Use a different output path to retain the original document.
        document->Save(outputFile);
    }
}
```

Duplicate Graphics Intersecting a Region

Duplicate intersecting graphics with a specified offset using `PageExtensions::DuplicateIntersectingGraphics()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/PageExtensions.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

namespace DuplicateIntersectingGraphicsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Operators;

    void CreateAndDuplicateIntersectingShapes(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        page->SetPageSize(600, 800);
        auto contents = page->get_Contents();

        contents->Add(MakeObject<GSave>());
        // Rectangle from (80, 120) to (160, 160): partly intersects the region.
        contents->Add(MakeObject<Re>(80, 120, 80, 40));
        contents->Add(MakeObject<Stroke>());
        // A separate rectangle outside the region is not selected.
        contents->Add(MakeObject<Re>(400, 600, 80, 40));
        contents->Add(MakeObject<Stroke>());
        contents->Add(MakeObject<GRestore>());

        auto region = MakeObject<Rectangle>(100, 100, 200, 200);
        PageExtensions::DuplicateIntersectingGraphics(page, region, 200, 100);

        // Expected: both originals plus a copy of the first rectangle at
        // (280, 220)-(360, 260). The copy is not clipped to the selection region.
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/PageExtensions.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <system/exceptions.h>

namespace DuplicateIntersectingGraphicsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void DuplicateGraphicsInRegion(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        if (document->get_Pages()->get_Count() == 0)
        {
            throw ArgumentException(u"The input PDF contains no pages.");
        }

        auto page = document->get_Pages()->idx_get(1);
        // Choose a region containing vector graphics in the input PDF.
        auto region = MakeObject<Rectangle>(100, 100, 250, 250);

        // Copy whole intersecting vector elements with an offset of 200, 100.
        // Adjust the region and offsets to keep copies within the visible page.
        PageExtensions::DuplicateIntersectingGraphics(page, region, 200, 100);

        document->Save(outputFile);
    }
}
```

## What's new in Aspose.PDF 25.10

Simplified macOS Deployment

External fontconfig and freetype dependencies are no longer required on macOS. Included dynamic libraries are signed with an Apple Developer ID.

## What's new in Aspose.PDF 25.9

LowCode PDF Processing APIs

The `Aspose::Pdf::LowCode` namespace provides APIs for conversion, extraction, forms, optimization, security, signatures, tables, and document assembly. The `Aspose::Pdf::Plugins` namespace was removed.

Configure the project with an SDK exposing the LowCode APIs and apply a license before processing. Use separate input and output paths and create output directories first. The signing example requires a PDF with at least one page and a PFX/P12 certificate containing its private key.

```cpp
#include <Aspose.PDF.Cpp/LowCode/TableGenerator.h>
#include <Aspose.PDF.Cpp/LowCode/TableOptions.h>
#include <Aspose.PDF.Cpp/LowCode/TableBuilder.h>
#include <Aspose.PDF.Cpp/LowCode/TableRowBuilder.h>
#include <Aspose.PDF.Cpp/LowCode/TableCellBuilder.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

```cpp
#include <Aspose.PDF.Cpp/LowCode/DocConverter.h>
#include <Aspose.PDF.Cpp/LowCode/PdfToDocOptions.h>
#include <Aspose.PDF.Cpp/LowCode/SaveFormat.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

```cpp
#include <Aspose.PDF.Cpp/LowCode/Security.h>
#include <Aspose.PDF.Cpp/LowCode/EncryptionOptions.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
#include <system/string.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>
namespace LowCodePdfProcessingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::LowCode;

    void EncryptPdf(String inputFile, String outputFile, String ownerPassword, String userPassword)
    {
        auto processor = MakeObject<Security>();
        auto options = MakeObject<EncryptionOptions>(ownerPassword, userPassword,
            Aspose::Pdf::Facades::DocumentPrivilege::get_ForbidAll(),
            Aspose::Pdf::CryptoAlgorithm::AESx256);
        options->AddInput(MakeObject<FileDataSource>(inputFile));
        options->AddOutput(MakeObject<FileDataSource>(outputFile));
        processor->Process(options);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/LowCode/TextExtractor.h>
#include <Aspose.PDF.Cpp/LowCode/TextExtractorOptions.h>
#include <Aspose.PDF.Cpp/LowCode/ResultContainer.h>
#include <Aspose.PDF.Cpp/LowCode/IOperationResult.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

```cpp
#include <Aspose.PDF.Cpp/LowCode/FormFlattener.h>
#include <Aspose.PDF.Cpp/LowCode/FormFlattenAllFieldsOptions.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

```cpp
#include <Aspose.PDF.Cpp/LowCode/Merger.h>
#include <Aspose.PDF.Cpp/LowCode/MergeOptions.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

```cpp
#include <Aspose.PDF.Cpp/LowCode/Optimizer.h>
#include <Aspose.PDF.Cpp/LowCode/OptimizeOptions.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

```cpp
#include <Aspose.PDF.Cpp/LowCode/Signature.h>
#include <Aspose.PDF.Cpp/LowCode/SignOptions.h>
#include <Aspose.PDF.Cpp/LowCode/FileDataSource.h>
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

## What's new in Aspose.PDF 25.8

Add Text Fragments to Table Cells

Create table cells directly from `TextFragment` objects with `Cells::Add()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

namespace TextFragmentsInTableCellsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void AddStyledTextFragmentsToCells(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto table = MakeObject<Table>();
        table->set_ColumnWidths(u"180 180");
        table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.5f));
        table->set_DefaultCellPadding(MakeObject<MarginInfo>(8, 8, 8, 8));

        auto row = table->get_Rows()->Add();
        auto label = MakeObject<TextFragment>(u"Approved amount");
        label->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        label->get_TextState()->set_FontSize(12);
        label->get_TextState()->set_FontStyle(FontStyles::Bold);
        row->get_Cells()->Add(label);

        auto amount = MakeObject<TextFragment>(u"1,250.00 USD");
        amount->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        amount->get_TextState()->set_FontSize(14);
        amount->get_TextState()->set_ForegroundColor(Color::get_Green());

        // The returned Cell can be configured after adding its text fragment.
        auto amountCell = row->get_Cells()->Add(amount);
        amountCell->set_IsOverrideByFragment(true);
        amountCell->set_BackgroundColor(Color::get_LightGray());

        page->get_Paragraphs()->Add(table);
        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

namespace TextFragmentsInTableCellsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void AddTextFragmentsToCells(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto table = MakeObject<Table>();
        table->set_ColumnWidths(u"180 180");
        table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.5f));

        auto header = table->get_Rows()->Add();
        header->get_Cells()->Add(MakeObject<TextFragment>(u"Document"));
        header->get_Cells()->Add(MakeObject<TextFragment>(u"Status"));

        auto row = table->get_Rows()->Add();
        auto documentName = MakeObject<TextFragment>(u"Annual report");
        auto status = MakeObject<TextFragment>(u"Ready for review");

        // Create each cell directly from a TextFragment.
        row->get_Cells()->Add(documentName);
        row->get_Cells()->Add(status);

        page->get_Paragraphs()->Add(table);
        document->Save(outputFile);
    }
}
```

Control MediaBox Changes During Content Resizing

Control page MediaBox changes with `PdfFileEditor::ContentsResizeParameters::ChangeMediaBox`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>
#include <stdexcept>

namespace ControlMediaBoxDuringContentResizingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::Facades;

    void ResizeContentsFitMediaBox(String inputFile, String outputFile)
    {
        auto editor = MakeObject<PdfFileEditor>();

        // Use the same resize dimensions as the preserve-MediaBox example.
        auto parameters = PdfFileEditor::ContentsResizeParameters::PageResize(500, 700);

        // Allow resizing to fit the page's MediaBox to its CropBox.
        parameters->set_ChangeMediaBox(true);

        if (!editor->ResizeContents(inputFile, outputFile, MakeArray<int32_t>({1}), parameters))
        {
            throw std::runtime_error("Failed to resize PDF page contents.");
        }
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>
#include <stdexcept>

namespace ControlMediaBoxDuringContentResizingExamples
{
    using namespace System;
    using namespace Aspose::Pdf::Facades;

    void ResizeContentsPreserveMediaBox(String inputFile, String outputFile)
    {
        auto editor = MakeObject<PdfFileEditor>();

        // Resize the first page to 500 x 700 PDF units.
        auto parameters = PdfFileEditor::ContentsResizeParameters::PageResize(500, 700);

        // Preserve the original MediaBox while resizing the page contents.
        // False is the default; set it explicitly to demonstrate the option.
        parameters->set_ChangeMediaBox(false);

        if (!editor->ResizeContents(inputFile, outputFile, MakeArray<int32_t>({1}), parameters))
        {
            throw std::runtime_error("Failed to resize PDF page contents.");
        }
    }
}
```

Tagged Table of Contents Links

Set tagged heading text and connect table of contents entries, list items, and page titles to structure elements.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/TOCInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void CreatePdfWithTocPageAdvanced(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto content = document->get_TaggedContent();
    auto rootElement = content->get_RootElement();
    content->SetLanguage(u"en-US");

    auto tocPage = document->get_Pages()->Add();
    tocPage->set_TocInfo(MakeObject<TocInfo>());
    tocPage->get_TocInfo()->set_Title(MakeObject<TextFragment>(u"Table of Contents"));

    auto tocElement = content->CreateTOCElement();
    auto headerForTocPageTitle = content->CreateHeaderElement(1);
    tocElement->LinkTocPageTitleToHeaderElement(tocPage, headerForTocPageTitle);

    rootElement->AppendChild(headerForTocPageTitle, true);
    rootElement->AppendChild(tocElement, true);

    document->get_Pages()->Add();

    auto header = content->CreateHeaderElement(1);
    header->SetText(u"1. Header");
    rootElement->AppendChild(header, true);

    auto toci = content->CreateTOCIElement();
    tocElement->AppendChild(toci, true);
    header->AddEntryToTocPage(tocPage, toci);
    toci->AddRef(header);

    auto listElement = content->CreateListElement();
    for (int i = 1; i < 4; i++) {
        auto li = content->CreateListLIElement();
        listElement->AppendChild(li, true);

        auto subHeader = content->CreateHeaderElement(2);
        subHeader->get_StructureTextState()->set_FontSize(14.0f);
        subHeader->set_Language(u"en-US");
        subHeader->SetText(String::Format(u"1.{0} subheader ", i));
        subHeader->AddEntryToTocPage(tocPage, li);
        li->AddRef(subHeader);

        auto p = content->CreateParagraphElement();
        p->SetText(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit.");
        p->set_Language(u"en-US");

        rootElement->AppendChild(subHeader, true);
        rootElement->AppendChild(p, true);
    }
    toci->AppendChild(listElement, true);

    auto header2 = content->CreateHeaderElement(1);
    header2->SetText(u"2. Header");
    rootElement->AppendChild(header2, true);

    auto toci2 = content->CreateTOCIElement();
    tocElement->AppendChild(toci2, true);
    header2->AddEntryToTocPage(tocPage, toci2);
    toci2->AddRef(header2);

    document->Save(outputFile);
}
```

## What's new in Aspose.PDF 25.7


Adjust Replacement Text to a Rectangle

Set a replacement rectangle and choose font size adjustment with `TextReplaceOptions`.

These examples replace the first text fragment on page 1 and adjust its font size to the rectangle.

```cpp
#include <stdexcept>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextAndFitTextIntoRectangle(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);
    String text = fragment->get_Text();
    fragment->get_ReplaceOptions()->set_Rectangle(fragment->get_Rectangle());
    fragment->get_ReplaceOptions()->set_FontSizeAdjustmentAction(
        TextReplaceOptions::FontSizeAdjustment::ShrinkToFit);
    fragment->get_ReplaceOptions()->set_ReplaceAdjustmentAction(
        TextReplaceOptions::ReplaceAdjustment::AdjustSpaceWidth);
    fragment->set_Text(text + String(u" ") + text);

    document->Save(outputFile);
}
```

```cpp
#include <stdexcept>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextAndResizeAndExpandFont(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);
    String text = fragment->get_Text();
    fragment->get_ReplaceOptions()->set_Rectangle(
        MakeObject<Aspose::Pdf::Rectangle>(100, 300, 512, 692, true));
    fragment->get_ReplaceOptions()->set_ReplaceAdjustmentAction(
        TextReplaceOptions::ReplaceAdjustment::AdjustSpaceWidth);
    fragment->get_ReplaceOptions()->set_FontSizeAdjustmentAction(
        TextReplaceOptions::FontSizeAdjustment::ScaleToFill);
    fragment->set_Text(text + String(u" ") + text);

    document->Save(outputFile);
}
```

Render a Page to a Bitmap

Retrieve a page bitmap with `ImageDevice::GetBitmap()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/ImageDevice.h>
#include <Aspose.PDF.Cpp/Devices/PngDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <drawing/bitmap.h>
#include <system/exceptions.h>

namespace RenderPageToBitmapExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Devices;

    SharedPtr<System::Drawing::Bitmap> GetPageBitmap(String inputFile, int pageNumber)
    {
        auto document = MakeObject<Document>(inputFile);
        auto pages = document->get_Pages();
        // PDF page numbers are one-based.
        if (pageNumber < 1 || pageNumber > pages->get_Count())
        {
            throw ArgumentOutOfRangeException(u"pageNumber");
        }

        // ImageDevice is abstract; use a concrete device to retrieve the bitmap.
        SharedPtr<ImageDevice> device = MakeObject<PngDevice>(MakeObject<Resolution>(150));
        auto bitmap = device->GetBitmap(pages->idx_get(pageNumber));

        // Return the rendered bitmap for further image processing in memory.
        return bitmap;
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/PngDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <drawing/bitmap.h>
#include <drawing/imaging/image_format.h>
#include <system/console.h>
#include <system/exceptions.h>

namespace RenderPageToBitmapExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Devices;

    void SavePageBitmapAsPng(String inputFile, String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        if (document->get_Pages()->get_Count() == 0)
        {
            throw ArgumentException(u"The input PDF contains no pages.");
        }

        auto device = MakeObject<PngDevice>(MakeObject<Resolution>(300));
        // GetBitmap renders the page into a Bitmap without an intermediate file.
        auto bitmap = device->GetBitmap(document->get_Pages()->idx_get(1));
        Console::WriteLine(u"Bitmap dimensions: {0} x {1} pixels",
            bitmap->get_Width(), bitmap->get_Height());

        // Save the bitmap explicitly as PNG; pass a .png output filename.
        bitmap->Save(outputFile, System::Drawing::Imaging::ImageFormat::get_Png());
    }
}
```

Annotation Appearance Controls

Additional annotation APIs expose default font settings and `CreateExtGStateWithOpacity()`.

## What's new in Aspose.PDF 25.6

Rich Text Styling for Free Text Annotations

Apply font settings and bold, italic, or underline styles with `FreeTextAnnotation::SetTextStyle()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/FreeTextAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/RichTextFontStyles.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <system/drawing/color.h>

namespace FreeTextAnnotationRichTextStylingExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Annotations;

    void StyleEntireFreeTextAnnotation(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto appearance = MakeObject<DefaultAppearance>(u"Arial", 12,
            System::Drawing::Color::get_Black());
        auto annotation = MakeObject<FreeTextAnnotation>(page,
            MakeObject<Rectangle>(50, 600, 500, 700), appearance);
        annotation->set_Contents(u"Review complete: the document is ready for publication.");
        page->get_Annotations()->Add(annotation);

        // Apply rich-text formatting, font, size, and color to all annotation text.
        annotation->SetTextStyle(RichTextFontStyles::Bold | RichTextFontStyles::Italic,
            u"Arial", 18, System::Drawing::Color::get_Blue());

        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/FreeTextAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/RichTextFontStyles.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <system/drawing/color.h>

namespace FreeTextAnnotationRichTextStylingExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Annotations;

    void StyleFreeTextAnnotationRanges(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto appearance = MakeObject<DefaultAppearance>(u"Arial", 16,
            System::Drawing::Color::get_Black());
        auto annotation = MakeObject<FreeTextAnnotation>(page,
            MakeObject<Rectangle>(50, 600, 500, 700), appearance);
        annotation->set_Contents(u"Bold italic underline.");
        page->get_Annotations()->Add(annotation);

        // Ranges are zero-based; the end index is exclusive.
        annotation->SetTextStyle(0, 4, RichTextFontStyles::Bold);
        annotation->SetTextStyle(5, 11, RichTextFontStyles::Italic);
        annotation->SetTextStyle(12, 21,
            RichTextFontStyles::Bold | RichTextFontStyles::Underline);

        // Replace the last word's combined style with underline alone.
        annotation->SetTextStyle(12, 21,
            RichTextFontStyles::ClearExisting | RichTextFontStyles::Underline);

        document->Save(outputFile);
    }
}
```

Read License Information

Access license details and expiry dates through `License::LicenseInfo`.

```cpp
#include <Aspose.PDF.Cpp/License.h>
#include <Aspose.PDF.Cpp/LicenseInfo.h>
#include <system/collections/list.h>
#include <system/console.h>

namespace ReadLicenseInformationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ReadLicenseDetails(String licenseFile)
    {
        auto license = MakeObject<License>();
        license->SetLicense(licenseFile);

        auto info = license->get_LicenseInfo();
        if (info == nullptr)
        {
            Console::WriteLine(u"License information is unavailable.");
            return;
        }

        Console::WriteLine(u"Licensed to: {0}", info->get_LicensedTo());
        Console::WriteLine(u"License type: {0}", info->get_LicenseType());
        Console::WriteLine(u"Edition type: {0}", info->get_EditionType());
        Console::WriteLine(u"License note: {0}", info->get_LicenseNote());

        auto products = info->get_Products();
        if (products != nullptr)
        {
            for (const auto& product : products)
            {
                Console::WriteLine(u"Licensed product: {0}", product);
            }
        }
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/License.h>
#include <Aspose.PDF.Cpp/LicenseInfo.h>
#include <system/console.h>
#include <system/date_time.h>

namespace ReadLicenseInformationExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void ReadLicenseExpiryDates(String licenseFile)
    {
        auto license = MakeObject<License>();
        license->SetLicense(licenseFile);

        auto info = license->get_LicenseInfo();
        if (info == nullptr)
        {
            Console::WriteLine(u"License information is unavailable.");
            return;
        }

        auto licenseExpiry = info->get_LicenseExpiry();
        auto subscriptionExpiry = info->get_SubscriptionExpiry();

        Console::WriteLine(u"License expiry: {0}", licenseExpiry.ToString(u"yyyy-MM-dd"));
        Console::WriteLine(u"Subscription expiry: {0}", subscriptionExpiry.ToString(u"yyyy-MM-dd"));

        // Subscription expiry is the release-date cutoff for eligible library
        // updates. It is separate from the license expiry date.
    }
}
```

## What's new in Aspose.PDF 25.5

Signature Verification and Certificate Extraction

Verify signatures with certificate validation options and extract a certificate object from a signature field.

These repository examples use the `PdfFileSignature` facade to validate signatures and retrieve certificate objects.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <system/security/cryptography/x509_certificates/x509_certificate_2.h>
#include <system/console.h>

namespace SignatureVerificationAndCertificateExtractionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Facades;
    using namespace System::Security::Cryptography::X509Certificates;

    void ExtractSignatureCertificateObject(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto signatures = MakeObject<PdfFileSignature>(document);
        auto names = signatures->GetSignatureNames(true);
        if (names->get_Count() == 0)
        {
            Console::WriteLine(u"The PDF contains no signed signature fields.");
            return;
        }

        for (const auto& name : names)
        {
            // The typed output selects the certificate-object overload,
            // rather than the overload that returns a certificate stream.
            SharedPtr<X509Certificate2> certificate;
            Console::WriteLine(u"Signature: {0}", name->ToString());
            if (!signatures->TryExtractCertificate(name, certificate) || certificate == nullptr)
            {
                Console::WriteLine(u"A certificate could not be extracted from this signature.");
                continue;
            }

            // Extraction alone does not verify the signature or establish trust.
            Console::WriteLine(u"Subject: {0}", certificate->get_Subject());
            Console::WriteLine(u"Issuer: {0}", certificate->get_Issuer());
            Console::WriteLine(u"Serial number: {0}", certificate->get_SerialNumber());
            Console::WriteLine(u"Thumbprint: {0}", certificate->get_Thumbprint());
        }
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationMethod.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationMode.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationOptions.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationResult.h>
#include <system/console.h>

namespace SignatureVerificationAndCertificateExtractionExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Facades;
    using namespace Aspose::Pdf::Security;

    void VerifySignaturesWithValidationOptions(String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto signatures = MakeObject<PdfFileSignature>(document);
        auto names = signatures->GetSignatureNames(true);
        if (names->get_Count() == 0)
        {
            Console::WriteLine(u"The PDF contains no signed signature fields.");
            return;
        }

        auto options = MakeObject<ValidationOptions>();
        options->set_ValidationMode(ValidationMode::Strict);
        options->set_ValidationMethod(ValidationMethod::Auto);
        options->set_CheckCertificateChain(true);
        // Certificate revocation checks can access OCSP or CRL servers.
        options->set_RequestTimeout(20000);

        for (const auto& name : names)
        {
            SharedPtr<ValidationResult> validationResult;
            bool verified = signatures->VerifySignature(name, options, validationResult);
            Console::WriteLine(u"Signature: {0}", name->ToString());
            Console::WriteLine(u"Verified: {0}", verified);
            if (validationResult != nullptr)
            {
                Console::WriteLine(u"Certificate validation status: {0}",
                    static_cast<int>(validationResult->get_Status()));
            }
            else
            {
                Console::WriteLine(u"No certificate validation result was returned.");
            }
        }
    }
}
```

Inspect XFA Form State

Check XFA presence and rendering requirements with `Form::HasXfa` and `NeedsRendering`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/FormType.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

void ConvertXfaFormWithIgnoreNeedsRendering(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto form = document->get_Form();

    if (form != nullptr)
    {
        if (form->get_HasXfa() && form->get_NeedsRendering())
        {
            form->set_IgnoreNeedsRendering(true);
        }
        form->set_Type(FormType::Standard);
    }

    document->Save(outputFile);
}
```

Create Tagged List Elements

Create list items, labels, and bodies through `ITaggedContent`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>

namespace TaggedListElementsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Tagged;

    void CreateTaggedNestedList(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto content = document->get_TaggedContent();
        content->SetTitle(u"Tagged Nested List");
        content->SetLanguage(u"en-US");

        auto list = content->CreateListElement();
        content->get_RootElement()->AppendChild(list, true);

        auto item = content->CreateListLIElement();
        auto label = content->CreateListLblElement();
        auto body = content->CreateListLBodyElement();
        auto labelText = content->CreateSpanElement();
        labelText->SetText(u"1. ");
        label->AppendChild(labelText, true);

        auto bodyText = content->CreateSpanElement();
        bodyText->SetText(u"Review the document:");
        auto inlinePosition = MakeObject<PositionSettings>();
        inlinePosition->set_IsInLineParagraph(true);
        bodyText->AdjustPosition(inlinePosition);
        body->AppendChild(bodyText, true);
        item->AppendChild(label, true);
        item->AppendChild(body, true);
        list->AppendChild(item, true);

        // A nested L belongs inside the parent item's LBody.
        auto nestedList = content->CreateListElement();
        body->AppendChild(nestedList, true);

        const String checks[] = { u"Check the title.", u"Check the reading order." };
        for (int i = 0; i < 2; ++i)
        {
            auto nestedItem = content->CreateListLIElement();
            auto nestedLabel = content->CreateListLblElement();
            auto nestedBody = content->CreateListLBodyElement();
            auto nestedLabelText = content->CreateSpanElement();
            nestedLabelText->SetText(String::Format(u"1.{0}. ", i + 1));
            auto position = MakeObject<PositionSettings>();
            position->set_IsInLineParagraph(false);
            position->set_Margin(MakeObject<MarginInfo>(30, 0, 0, 0));
            nestedLabelText->AdjustPosition(position);

            auto nestedBodyText = content->CreateSpanElement();
            nestedBodyText->SetText(checks[i]);
            nestedBodyText->AdjustPosition(inlinePosition);
            nestedLabel->AppendChild(nestedLabelText, true);
            nestedBody->AppendChild(nestedBodyText, true);
            nestedItem->AppendChild(nestedLabel, true);
            nestedItem->AppendChild(nestedBody, true);
            nestedList->AppendChild(nestedItem, true);
        }

        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>

namespace TaggedListElementsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Tagged;

    void CreateTaggedNumberedList(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto content = document->get_TaggedContent();
        content->SetTitle(u"Tagged Numbered List");
        content->SetLanguage(u"en-US");

        auto list = content->CreateListElement();
        content->get_RootElement()->AppendChild(list, true);

        const String descriptions[] = {
            u"Prepare the input documents.",
            u"Process the documents.",
            u"Save the results."
        };

        for (int i = 0; i < 3; ++i)
        {
            auto item = content->CreateListLIElement();
            auto label = content->CreateListLblElement();
            auto body = content->CreateListLBodyElement();

            auto labelText = content->CreateSpanElement();
            labelText->SetText(String::Format(u"{0}. ", i + 1));
            auto labelPosition = MakeObject<PositionSettings>();
            labelPosition->set_IsInLineParagraph(false);
            labelText->AdjustPosition(labelPosition);

            auto bodyText = content->CreateSpanElement();
            bodyText->SetText(descriptions[i]);
            auto bodyPosition = MakeObject<PositionSettings>();
            bodyPosition->set_IsInLineParagraph(true);
            bodyText->AdjustPosition(bodyPosition);

            // L -> LI -> Lbl + LBody; each label and body contains text.
            label->AppendChild(labelText, true);
            body->AppendChild(bodyText, true);
            item->AppendChild(label, true);
            item->AppendChild(body, true);
            list->AppendChild(item, true);
        }

        document->Save(outputFile);
    }
}
```

XPS Export Font Options

Configure the default font and embedded TrueType font usage with `XpsSaveOptions`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/XpsSaveOptions.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXps(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto options = MakeObject<XpsSaveOptions>();
	options->set_UseEmbeddedTrueTypeFonts(true);
	document->Save(outputFile, options);
}
}
```

## What's new in Aspose.PDF 25.4

Automatic Tagging Settings

Configure automatic tagging and heading recognition during PDF format conversion with `AutoTaggingSettings`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/AutoTaggingSettings.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/PdfFormatConversionOptions.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/HeadingRecognitionStrategy.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void ConvertToPdfUaWithAutomaticTagging(System::String inputFile, System::String outputFile, System::String logFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<PdfFormatConversionOptions>(
    logFile, PdfFormat::PDF_UA_1, ConvertErrorAction::Delete);

    auto autoTaggingSettings = MakeObject<AutoTaggingSettings>();
    autoTaggingSettings->set_EnableAutoTagging(true);
    autoTaggingSettings->set_HeadingRecognitionStrategy(HeadingRecognitionStrategy::Auto);
    options->set_AutoTaggingSettings(autoTaggingSettings);

    document->Convert(options);
    document->Save(outputFile);
}
```

Custom Security Handler Interface

Implement custom encryption and decryption through `ICustomSecurityHandler` and `EncryptionParameters`.

The shared handler demonstrates the API lifecycle with XOR and reversible password encoding; it provides no meaningful security and is not suitable for production protection.

Shared helper: `custom-security-handler/demo-security-handler.h`. Save this file beside the examples that include it.

```cpp
#pragma once

#include <Aspose.PDF.Cpp/Security/ICustomSecurityHandler.h>
#include <Aspose.PDF.Cpp/Security/EncryptionParameters.h>
#include <system/array.h>
#include <system/exceptions.h>
#include <system/text/encoding.h>
#include <cstdint>

namespace CustomSecurityHandlerExamples
{
    // Demonstrates the API lifecycle only. XOR and exposed key material provide
    // no meaningful security. Replace this scheme for production use.
    class DemoSecurityHandler final : public Aspose::Pdf::Security::ICustomSecurityHandler
    {
    public:
        System::String get_Filter() override { return u"ExampleSecurityHandler"; }
        System::String get_SubFilter() override { return u"ExampleXor"; }
        int32_t get_Version() override { return 1; }
        int32_t get_Revision() override { return 2; }
        int32_t get_KeyLength() override { return 8; }

        void Initialize(const System::SharedPtr<Aspose::Pdf::Security::EncryptionParameters>& parameters) override
        {
            // On opening, these parameters contain the persisted encryption dictionary.
            // UserKey and OwnerKey can be null during initial encryption setup.
            parameters_ = parameters;
        }

        System::ArrayPtr<uint8_t> GetUserKey(const System::String& password) override
        {
            return EncodePassword(password);
        }

        System::ArrayPtr<uint8_t> GetOwnerKey(const System::String& userPassword,
            const System::String& ownerPassword) override
        {
            return EncodePassword(ownerPassword);
        }

        bool IsUserPassword(const System::String& password) override
        {
            return parameters_ && Equal(EncodePassword(password), parameters_->get_UserKey());
        }

        bool IsOwnerPassword(const System::String& password) override
        {
            return parameters_ && Equal(EncodePassword(password), parameters_->get_OwnerKey());
        }

        System::ArrayPtr<uint8_t> CalculateEncryptionKey(const System::String& password) override
        {
            if (!IsUserPassword(password) && !IsOwnerPassword(password))
            {
                throw System::ArgumentException(u"The supplied password does not match this document.");
            }

            // Use persisted data so either accepted password yields the same demo key.
            auto key = System::MakeArray<uint8_t>(1);
            uint8_t value = 0x5a;
            for (auto byte : parameters_->get_UserKey())
            {
                value ^= byte;
            }
            key[0] = value;
            return key;
        }

        System::ArrayPtr<uint8_t> Encrypt(const System::ArrayPtr<uint8_t>& data,
            int32_t objectNumber, int32_t generation, const System::ArrayPtr<uint8_t>& key) override
        {
            auto result = System::MakeArray<uint8_t>(data->get_Length());
            for (int32_t i = 0; i < data->get_Length(); ++i)
            {
                result[i] = data[i] ^ key[0] ^ static_cast<uint8_t>(objectNumber)
                    ^ static_cast<uint8_t>(generation);
            }
            return result;
        }

        System::ArrayPtr<uint8_t> Decrypt(const System::ArrayPtr<uint8_t>& data,
            int32_t objectNumber, int32_t generation, const System::ArrayPtr<uint8_t>& key) override
        {
            // The demonstration transform is symmetric.
            return Encrypt(data, objectNumber, generation, key);
        }

        System::ArrayPtr<uint8_t> EncryptPermissions(int32_t permissions) override
        {
            auto result = System::MakeArray<uint8_t>(16);
            auto bits = static_cast<uint32_t>(permissions);
            for (int32_t i = 0; i < 4; ++i)
            {
                result[i] = static_cast<uint8_t>(bits >> (8 * i)) ^ 0x5a;
            }
            return result;
        }

    private:
        System::SharedPtr<Aspose::Pdf::Security::EncryptionParameters> parameters_;

        static System::ArrayPtr<uint8_t> EncodePassword(const System::String& password)
        {
            // Deliberately reversible encoding, not secure password storage.
            return System::Text::Encoding::get_UTF8()->GetBytes(System::String(u"demo:") + password);
        }

        static bool Equal(const System::ArrayPtr<uint8_t>& left, const System::ArrayPtr<uint8_t>& right)
        {
            if (!left || !right || left->get_Length() != right->get_Length())
            {
                return false;
            }
            for (int32_t i = 0; i < left->get_Length(); ++i)
            {
                if (left[i] != right[i])
                {
                    return false;
                }
            }
            return true;
        }
    };
}
```

```cpp
#include "demo-security-handler.h"
#include <Aspose.PDF.Cpp/Document.h>

namespace CustomSecurityHandlerExamples
{
    void DecryptWithCustomSecurityHandler(System::String inputFile, System::String outputFile)
    {
        // Use the output of EncryptWithCustomSecurityHandler as input.
        // A fresh handler receives the saved dictionary through Initialize().
        auto handler = System::MakeObject<DemoSecurityHandler>();
        auto document = System::MakeObject<Aspose::Pdf::Document>(
            inputFile, u"owner_password", handler);

        document->Decrypt();
        document->Save(outputFile);
    }
}
```

```cpp
#include "demo-security-handler.h"
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Permissions.h>

namespace CustomSecurityHandlerExamples
{
    void EncryptWithCustomSecurityHandler(System::String inputFile, System::String outputFile)
    {
        auto document = System::MakeObject<Aspose::Pdf::Document>(inputFile);
        auto handler = System::MakeObject<DemoSecurityHandler>();

        document->Encrypt(u"user_password", u"owner_password",
            Aspose::Pdf::Permissions::ExtractContent, handler);
        document->Save(outputFile);
    }
}
```

Markdown Heading Style Selection

Choose exported heading style with `MarkdownSaveOptions::HeadingStyle`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/MarkdownSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToMarkdownAtxHeadings(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<MarkdownSaveOptions>();
		options->set_HeadingStyle(HeadingStyle::Atx);
		options->set_ResourcesDirectoryName(u"images");
		options->set_UseImageHtmlTag(true);
		document->Save(outputFile, options);
	}
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/MarkdownSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToMarkdownSetextHeadings(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<MarkdownSaveOptions>();
		options->set_HeadingStyle(HeadingStyle::Setext);
		options->set_ResourcesDirectoryName(u"images");
		options->set_UseImageHtmlTag(true);
		document->Save(outputFile, options);
	}
}
```

Inspect Explicit Text State Settings

Use the new `TextState::Is...Set` properties to inspect configured text attributes.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <system/console.h>

namespace ExplicitTextStateSettingsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void ApplyUnsetTextStateDefaults()
    {
        auto textState = MakeObject<TextState>();
        textState->set_FontSize(16);
        textState->set_Underline(false);
        textState->set_WordSpacing(0);

        // Apply defaults only when the corresponding attribute is unset.
        if (!textState->get_IsFontSizeSet())
        {
            textState->set_FontSize(12);
        }
        if (!textState->get_IsForegroundColorSet())
        {
            textState->set_ForegroundColor(Color::get_Black());
        }
        if (!textState->get_IsUnderlineSet())
        {
            textState->set_Underline(true);
        }
        if (!textState->get_IsWordSpacingSet())
        {
            textState->set_WordSpacing(2);
        }

        // Preserve the explicitly configured size, false, and zero values.
        Console::WriteLine(u"Font size: {0}", textState->get_FontSize());
        Console::WriteLine(u"Underline: {0}", textState->get_Underline());
        Console::WriteLine(u"Word spacing: {0}", textState->get_WordSpacing());
        Console::WriteLine(u"Foreground color set: {0}", textState->get_IsForegroundColorSet());
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <system/console.h>

namespace ExplicitTextStateSettingsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;

    void InspectExplicitTextStateSettings()
    {
        auto textState = MakeObject<TextState>();

        Console::WriteLine(u"Before configuration:");
        Console::WriteLine(u"Font set: {0}", textState->get_IsFontSet());
        Console::WriteLine(u"Font size set: {0}", textState->get_IsFontSizeSet());
        Console::WriteLine(u"Foreground color set: {0}", textState->get_IsForegroundColorSet());

        textState->set_Font(FontRepository::FindFont(u"Arial"));
        textState->set_FontSize(14);
        textState->set_FontStyle(FontStyles::Bold);
        textState->set_ForegroundColor(Color::get_Blue());
        textState->set_CharacterSpacing(1.5f);
        textState->set_Underline(false);

        Console::WriteLine(u"After configuration:");
        Console::WriteLine(u"Font set: {0}", textState->get_IsFontSet());
        Console::WriteLine(u"Font size set: {0}", textState->get_IsFontSizeSet());
        Console::WriteLine(u"Font style set: {0}", textState->get_IsFontStyleSet());
        Console::WriteLine(u"Foreground color set: {0}", textState->get_IsForegroundColorSet());
        Console::WriteLine(u"Character spacing set: {0}", textState->get_IsCharacterSpacingSet());

        // An explicit false value still counts as a configured attribute.
        Console::WriteLine(u"Underline set: {0}", textState->get_IsUnderlineSet());
        Console::WriteLine(u"Underline value: {0}", textState->get_Underline());

        // These attributes were not configured above.
        Console::WriteLine(u"Background color set: {0}", textState->get_IsBackgroundColorSet());
        Console::WriteLine(u"Word spacing set: {0}", textState->get_IsWordSpacingSet());
    }
}
```

Clear an Applied License

Clear the current license with `License::ClearLicense()`.

```cpp
#include <Aspose.PDF.Cpp/License.h>

namespace LicensingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ClearAppliedLicense(String licenseFile)
	{
		auto license = MakeObject<License>();
		license->SetLicense(licenseFile);

		// Clear the applied license before performing further PDF operations.
		license->ClearLicense();
	}
}
```

Tagged Content Save Methods

The `ITaggedContent::PreSave()` and `Save()` methods were added.
```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

namespace TaggedContentSaveMethodsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void PreSaveTaggedContent(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto taggedContent = document->get_TaggedContent();
        taggedContent->SetTitle(u"Prepare Tagged Content for Saving");
        taggedContent->SetLanguage(u"en-US");

        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(u"This paragraph is part of the document's logical structure.");
        taggedContent->get_RootElement()->AppendChild(paragraph, true);

        // Prepare the structure tree and tagged elements for saving.
        taggedContent->PreSave();

        document->Save(outputFile);
    }
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

namespace TaggedContentSaveMethodsExamples
{
    using namespace System;
    using namespace Aspose::Pdf;

    void SaveTaggedContent(String outputFile)
    {
        auto document = MakeObject<Document>();
        auto taggedContent = document->get_TaggedContent();
        taggedContent->SetTitle(u"Save Tagged Content");
        taggedContent->SetLanguage(u"en-US");

        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(u"This tagged paragraph will be saved to the associated PDF document.");
        taggedContent->get_RootElement()->AppendChild(paragraph, true);

        taggedContent->PreSave();

        // Save the tagged content state to the associated document.
        taggedContent->Save();

        // Write the PDF document to a file.
        document->Save(outputFile);
    }
}
```

## What's new in Aspose.PDF 25.3

The source's 25.3 section announces Markdown export, available since 25.2. Use [SaveFormat::Markdown](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/MarkdownSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToMarkdown(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<MarkdownSaveOptions>();
		options->set_ResourcesDirectoryName(u"images");
		options->set_UseImageHtmlTag(true);
		document->Save(outputFile, options);
	}
}
```

Bates Numbering and Pagination

Add, update, and delete Bates numbering with `BatesNArtifact`, `PaginationArtifact`, and `PageCollectionExtensions`.

Both examples append two pages and apply numbering to all pages. Save the shared helper as `bates-artifact.h` beside the example.

```cpp
#include <Aspose.PDF.Cpp/Artifacts/BatesNArtifact.h>
#include <Aspose.PDF.Cpp/Artifacts/Pagination/Subset.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

inline System::SharedPtr<Aspose::Pdf::BatesNArtifact> CreateBatesArtifact()
{
    using namespace Aspose::Pdf;
    auto artifact = System::MakeObject<BatesNArtifact>();
    artifact->set_StartPage(1);
    artifact->set_EndPage(0);
    artifact->set_Subset(Subset::All);
    artifact->set_NumberOfDigits(6);
    artifact->set_StartNumber(1);
    artifact->set_Prefix(u"");
    artifact->set_Suffix(u"");
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Bottom);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Right);
    artifact->set_RightMargin(72);
    artifact->set_LeftMargin(72);
    artifact->set_TopMargin(36);
    artifact->set_BottomMargin(36);
    return artifact;
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include "bates-artifact.h"
#include <Aspose.PDF.Cpp/Artifacts/Pagination/PageCollectionExtensions.h>

void AddBatesNArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int i = 0; i < 2; ++i) {
        document->get_Pages()->Add();
    }
    auto artifact = CreateBatesArtifact();
    PageCollectionExtensions::AddBatesNumbering(document->get_Pages(), artifact);
    document->Save(outputFile);
}
```

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include "bates-artifact.h"
#include <Aspose.PDF.Cpp/Artifacts/Pagination/PageCollectionExtensions.h>
#include <Aspose.PDF.Cpp/Artifacts/PaginationArtifact.h>
#include <system/collections/list.h>

void AddBatesNArtifactPagination(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int i = 0; i < 2; ++i) {
        document->get_Pages()->Add();
    }
    auto artifact = CreateBatesArtifact();
    auto artifacts = MakeObject<System::Collections::Generic::List<SharedPtr<PaginationArtifact>>>();
    artifacts->Add(artifact);
    PageCollectionExtensions::AddPagination(document->get_Pages(), artifacts);
    document->Save(outputFile);
}
```

Position Tagged Structure Elements

Adjust tagged element placement with `AdjustPosition()` and `Tagged::PositionSettings`.


```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void AdjustPosition(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();

    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto paragraph = taggedContent->CreateParagraphElement();
    taggedContent->get_RootElement()->AppendChild(paragraph, true);
    paragraph->SetText(u"Text.");

    auto positionSettings = MakeObject<PositionSettings>();
    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Left(300);
    marginInfo->set_Top(20);
    marginInfo->set_Right(0);
    marginInfo->set_Bottom(0);
    positionSettings->set_Margin(marginInfo);
    positionSettings->set_HorizontalAlignment(HorizontalAlignment::None);
    positionSettings->set_VerticalAlignment(VerticalAlignment::None);
    positionSettings->set_IsFirstParagraphInColumn(false);
    positionSettings->set_IsKeptWithNext(false);
    positionSettings->set_IsInNewPage(false);
    positionSettings->set_IsInLineParagraph(false);
    paragraph->AdjustPosition(positionSettings);

    document->Save(outputFile);
}
```

## What's new in Aspose.PDF 24.11

DJVU input became available through [DjvuLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/djvuloadoptions/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DjvuLoadOptions.h>

void ImportDjvu(System::String input, System::String output)
{
    auto settings = System::MakeObject<Aspose::Pdf::DjvuLoadOptions>();
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input, settings);
    pdf->Save(output);
}
```

## What's new in Aspose.PDF 24.10

CDR input became available through [CdrLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/cdrloadoptions/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/CdrLoadOptions.h>

void ImportCdr(System::String input, System::String output)
{
    auto settings = System::MakeObject<Aspose::Pdf::CdrLoadOptions>();
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input, settings);
    pdf->Save(output);
}
```

## What's new in Aspose.PDF 24.8

SVG placement through [Page::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addimage/) was added.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

void PlaceSvg(System::String image, System::String output)
{
    auto pdf = System::MakeObject<Aspose::Pdf::Document>();
    auto sheet = pdf->get_Pages()->Add();
    sheet->AddImage(image, System::MakeObject<Aspose::Pdf::Rectangle>(100, 100, 400, 400));
    pdf->Save(output);
}
```

## What's new in Aspose.PDF 24.4

SVG loading was corrected. See [SVG conversion examples](/pdf/cpp/convert-images-format-to-pdf/#convert-svg-to-pdf).

## What's new in Aspose.PDF 24.3

PDF-to-TIFF conversion was introduced. The source configures [TiffDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/tiffdevice/) to skip blank pages and use 8-bit color.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/TiffDevice.h>
#include <Aspose.PDF.Cpp/Devices/TiffSettings.h>
#include <Aspose.PDF.Cpp/Devices/ColorDepth.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>

void ExportTiff(System::String input, System::String output)
{
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input);
    auto renderer = System::MakeObject<Aspose::Pdf::Devices::TiffDevice>();
    renderer->get_Settings()->set_SkipBlankPages(true);
    renderer->get_Settings()->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format8bpp);
    auto stream = System::IO::File::Create(output);
    renderer->Process(pdf, 1, pdf->get_Pages()->get_Count(), stream);
    stream->Close();
}
```

## What's new in Aspose.PDF 24.2

JPX decoding performance and recovery of malformed document structures were improved.

## What's new in Aspose.PDF 23.7

EPUB export and PCL loading were added. EPUB uses [SaveFormat::Epub](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/); PCL uses [PclLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pclloadoptions/).

## What's new in Aspose.PDF 23.1

DICOM image support was added. See the [DICOM example](/pdf/cpp/convert-images-format-to-pdf/#convert-dicom-to-pdf).

## What's new in Aspose.PDF 22.11

The first public macOS edition was released.

## What's new in Aspose.PDF 22.5

XFA form support was introduced. See [XFA Forms](/pdf/cpp/xfa-forms/).

## What's new in Aspose.PDF 22.4

The codebase incorporated Aspose.PDF for .NET and Aspose.Imaging 22.4, with thumbnail, region-constructor, and monochrome-image updates.

## What's new in Aspose.PDF 22.3

Additional overloads accepted ArrayView parameters.

## What's new in Aspose.PDF 22.1

Updates included a CoreFX-based System::Xml implementation, double-conversion 3.1.7, and signed DLLs.

## What's new in Aspose.PDF 21.10

SVG-to-PDF conversion became available. See [basic and advanced SVG conversion](/pdf/cpp/convert-images-format-to-pdf/#convert-svg-to-pdf).

## What's new in Aspose.PDF 21.4

HTML export became available through [SaveFormat::Html](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/).
