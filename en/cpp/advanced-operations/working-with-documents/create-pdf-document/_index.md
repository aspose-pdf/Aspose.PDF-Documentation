---
title: Create PDF documents in C++
linktitle: Create PDF documents
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: Create a PDF from text or add searchable text to a scanned PDF through an external OCR callback with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Create a PDF from text or add searchable text to a scanned PDF through an external OCR callback with Aspose.PDF for C++.

## Create a PDF with text

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a page through [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Add a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) containing Hello World! to the page paragraphs.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateNewDocument(String outputFile) {
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Hello World!"));
    document->Save(outputFile);
}
```

## Create a searchable PDF with Tesseract

Install Tesseract and the required language data separately. The callback invokes an external OCR executable; Aspose.PDF consumes its hOCR output.

1. Supply the Tesseract executable path and an installed OCR language code.
1. Create a Document::CallBackGetHocr callback that saves each image as a temporary bitmap.
1. Run Tesseract to generate hOCR and check its exit code.
1. Read the hOCR output and clean up the temporary files.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) with the callback and check the returned result.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <filesystem>
#include <functional>
#include <system/diagnostics/process.h>
#include <system/diagnostics/process_start_info.h>
#include <system/diagnostics/process_window_style.h>
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/path.h>
#include <drawing/bitmap.h>
#include <drawing/imaging/image_format.h>
#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;

void CreateSearchablePdf(String inputFile, String outputFile,
                         String tesseractExecutable, String language)
{
    if (tesseractExecutable.IsEmpty() || language.IsEmpty() ||
        language.Contains(u"\"") || language.Contains(u" ") || language.Contains(u"\n")) {
        throw ArgumentException(u"Specify an OCR executable and a valid language code.");
    }
    Document::CallBackGetHocr callback(
        std::function<String(const SharedPtr<System::Drawing::Image>&)>(
        [tesseractExecutable, language](const SharedPtr<System::Drawing::Image>& image) {
            const auto tempFile = System::IO::Path::GetTempFileNameSafe();
            struct TemporaryFiles {
                String path;
                ~TemporaryFiles() {
                    std::error_code error;
                    std::filesystem::remove(std::filesystem::path(path.ToWCS()), error);
                    std::filesystem::remove(std::filesystem::path((path + u".hocr").ToWCS()), error);
                }
            } cleanup{tempFile};
            auto bitmap = MakeObject<System::Drawing::Bitmap>(image);
            bitmap->Save(tempFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
            const auto arguments = String::Format(u"\"{0}\" \"{0}\" -l \"{1}\" hocr", tempFile, language);
            auto info = MakeObject<Diagnostics::ProcessStartInfo>(tesseractExecutable, arguments);
            info->set_UseShellExecute(false);
            info->set_CreateNoWindow(true);
            info->set_WindowStyle(Diagnostics::ProcessWindowStyle::Hidden);
            auto process = Diagnostics::Process::Start(info);
            if (process == nullptr) {
                throw InvalidOperationException(u"Could not start Tesseract.");
            }
            process->WaitForExit();
            if (process->get_ExitCode() != 0) {
                throw InvalidOperationException(u"Tesseract failed to generate hOCR.");
            }
            return System::IO::File::ReadAllText(tempFile + u".hocr");
        }));
    auto document = MakeObject<Document>(inputFile);
    if (!document->Convert(callback)) {
        throw InvalidOperationException(u"Searchable PDF conversion failed.");
    }
    document->Save(outputFile);
}
```
