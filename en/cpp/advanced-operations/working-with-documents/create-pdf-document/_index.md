---
title: Create PDF documents in C++
linktitle: Create PDF documents
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: Create PDF documents from text and make scanned PDFs searchable with Tesseract OCR using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create Text PDFs and Searchable Scanned Documents in C++
Abstract: Learn how to create a PDF page containing text with Aspose.PDF for C++. Use an external Tesseract hOCR callback to add searchable text to a scanned PDF, or render pages to images and combine Tesseract PDF output.
---

Create PDF documents from text and make scanned PDFs searchable with Tesseract OCR using Aspose.PDF for C++.

The examples below cover three workflows: creating a new document, adding OCR text through an hOCR callback, and rebuilding a document from rendered pages. Each function accepts an output PDF path through `outputFile`. The OCR examples also accept an existing PDF through `inputFile`.

## Create a PDF with text

The following example creates a single-page PDF containing **Hello World!**. The `outputFile` parameter specifies the destination PDF path. A new `Document` has no pages, so add a page before adding text.

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

## Create a searchable PDF with an hOCR callback

Install Tesseract and the required language data separately. The callback invokes an external OCR executable; Aspose.PDF consumes its hOCR output to add searchable text to the scanned PDF. hOCR contains recognized text and its position within the image.

Set `tesseractExecutable` to the installed executable and `language` to an installed language code, such as `eng`. The example uses the default Tesseract language-data location. If your installation stores language data elsewhere, configure `TESSDATA_PREFIX` for the process.

The `CreateSearchablePdf` function opens the scanned PDF and passes a `Document::CallBackGetHocr` callback to `Convert(callback, true)`. The callback writes each supplied image to a temporary bitmap and waits for Tesseract to finish. Its cleanup object removes the bitmap and hOCR file when the callback returns or an exception occurs.

1. Supply the Tesseract executable path and an installed OCR language code.
1. Create a `Document::CallBackGetHocr` callback that saves each image as a temporary bitmap.
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
    if (!document->Convert(callback, true)) {
        throw InvalidOperationException(u"Searchable PDF conversion failed.");
    }
    document->Save(outputFile);
}
```

## Create a searchable PDF from rendered pages

The `CreateSearchablePdf2` example uses Tesseract's PDF output instead of an hOCR callback. It renders each source page as a PNG image at 600 DPI, runs Tesseract to create a searchable PDF for that image, and merges the generated PDFs in page order. The output is rebuilt from rendered images, so existing interactive elements and document structure are not preserved by this workflow.

Install Tesseract and the required language data before running the example. Update `tesseractExecutable`, `language`, and `tessdata` for your installation. The output directory must already exist and be writable. This example reuses `page.png` and `page.pdf` in that directory; use a dedicated directory without files of those names and avoid overlapping runs. Temporary files are deleted after each successful merge, but may remain if processing fails.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a `PngDevice` with a resolution of 600 DPI.
1. Set the temporary file paths in the output directory.
1. Create an empty document for the combined result.
1. Render each page to the temporary PNG file and close the output stream.
1. Run Tesseract with the `pdf` output option and check its exit code.
1. Merge the generated page PDF into the result document.
1. Delete the temporary image and page PDF.
1. Save the combined searchable PDF to `outputFile`.

```cpp
#include <system/console.h>
#include <system/diagnostics/process.h>
#include <system/diagnostics/process_start_info.h>
#include <system/diagnostics/process_window_style.h>
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/PngDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>

using namespace System;
using namespace Aspose::Pdf;

void CreateSearchablePdf2(String inputFile, String outputFile)
{
    String tesseractExecutable(u"C:\\Program Files\\Tesseract-OCR\\tesseract.exe");
    String language(u"eng");
    String tessdata(u"C:\\Program Files\\Tesseract-OCR\\tessdata");

    auto document = MakeObject<Document>(inputFile);
    auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(
        MakeObject<Aspose::Pdf::Devices::Resolution>(600));
    String outputDirectory = System::IO::Path::GetDirectoryName(outputFile);
    String tempImage = System::IO::Path::Combine(outputDirectory, u"page.png");
    String tempDoc = System::IO::Path::Combine(outputDirectory, u"page");
    String tempPdf = System::IO::Path::Combine(outputDirectory, u"page.pdf");

    auto resultDocument = MakeObject<Document>();
    const auto arguments = String::Format(
        u"\"{0}\" \"{1}\" -l {2} --tessdata-dir \"{3}\" pdf",
        tempImage, tempDoc, language, tessdata);
    System::Console::WriteLine(u"Running Tesseract with arguments: " + arguments);
    for (const auto& page : document->get_Pages())
    {
        auto stream = System::IO::File::OpenWrite(tempImage);
        pngDevice->Process(page, stream);
        stream->Close();

        auto info = MakeObject<Diagnostics::ProcessStartInfo>(tesseractExecutable, arguments);
        info->set_UseShellExecute(false);
        info->set_CreateNoWindow(true);
        info->set_WindowStyle(Diagnostics::ProcessWindowStyle::Normal);

        auto process = Diagnostics::Process::Start(info);
        if (process == nullptr) {
            throw InvalidOperationException(u"Could not start Tesseract.");
        }
        process->WaitForExit();
        if (process->get_ExitCode() != 0) {
            throw InvalidOperationException(u"Tesseract failed to generate hOCR.");
        }

        resultDocument->Merge(MakeArray<String>({tempPdf}));

        System::IO::File::Delete(tempImage);
        System::IO::File::Delete(tempPdf);
    }

    resultDocument->Save(outputFile);
}
```
