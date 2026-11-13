---
title: Manage PDF annotations in C++
linktitle: PdfAnnotationEditor Class
type: docs
weight: 40
url: /cpp/pdfannotationeditor-class/
description: Delete, extract, flatten, modify, and transfer annotations and exchange annotation data through XFDF using Aspose.PDF for C++.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Edit and Exchange PDF Annotation Data in C++
Abstract: Use PdfAnnotationEditor to filter, modify, and remove annotations or transfer them to another PDF. The examples include XFDF round trips, text extraction, author replacement, and flattening settings.
---

Use [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/) to delete, extract, flatten, modify, and transfer annotations and exchange annotation data through XFDF.

Annotation import examples create blank target pages before importing annotations; they do not copy the original page content. The flattening example enables ApplyRedactions.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## PdfAnnotationEditor workflows

- [Delete all annotations by type](#delete-all-annotations-by-type)
- [Delete all annotations](#delete-all-annotations)
- [Delete annotation by name](#delete-annotation-by-name)
- [Extract annotations](#extract-annotations)
- [Flatten annotations](#flatten-annotations)
- [Import annotations](#import-annotations)
- [Import export all annotations XFDF](#import-export-all-annotations-xfdf)
- [Import export selected annotations XFDF](#import-export-selected-annotations-xfdf)
- [Modify annotations author](#modify-annotations-author)
- [Modify annotations](#modify-annotations)

## Delete all annotations by type

Delete Text and FreeText annotations from the bound PDF.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the selected annotations with [PdfAnnotationEditor::DeleteAnnotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/deleteannotations/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void DeleteAllAnnotationsByType(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);

    editor->DeleteAnnotations(u"Text");
    editor->DeleteAnnotations(u"FreeText");

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Delete all annotations

Delete all annotations from the bound PDF.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the selected annotations with [PdfAnnotationEditor::DeleteAnnotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/deleteannotations/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteAllAnnotations(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);
    editor->DeleteAnnotations();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Delete annotation by name

Delete the annotation named sample-note-1.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the named annotation with [PdfAnnotationEditor::DeleteAnnotation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/deleteannotation/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void DeleteAnnotationByName(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);
    editor->DeleteAnnotation(u"sample-note-1");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Extract annotations

Extract Text and FreeText annotation contents across all pages and write them to a text file.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Extract the selected annotation types and page range with [PdfAnnotationEditor::ExtractAnnotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/extractannotations/).
1. Write the collected values to the output text file.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void ExtractAnnotations(String inputFile, String outputFile)
{
    auto types = MakeArray<Annotations::AnnotationType>(
        {Annotations::AnnotationType::FreeText, Annotations::AnnotationType::Text});

    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);
    String contents;
    for (auto annotation : editor->ExtractAnnotations(1, editor->get_Document()->get_Pages()->get_Count(), types))
        contents += annotation->get_Contents() + u"\n";
    System::IO::File::WriteAllText(outputFile, contents);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Flatten annotations

Flatten annotations with redaction application enabled, events disabled, buttons hidden, and appearances updated.

1. Configure [Form::FlattenSettings](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/flattensettings/) for redaction, events, buttons, and appearance handling.
1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the flattening settings with [PdfAnnotationEditor::FlatteningAnnotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/flatteningannotations/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void FlattenAnnotations(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);

    auto settings = MakeObject<Forms::Form::FlattenSettings>();
    settings->set_ApplyRedactions(true);
    settings->set_CallEvents(false);
    settings->set_HideButtons(true);
    settings->set_UpdateAppearances(true);
    editor->FlatteningAnnotations(settings);

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Import annotations

Create a blank destination with the same page count as the source and import its annotations.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import annotations into the target PDF with [PdfAnnotationEditor::ImportAnnotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/importannotations/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void ImportAnnotations(String inputFile, String outputFile)
{
    auto source = MakeObject<Document>(inputFile);
    auto target = MakeObject<Document>();
    for (int i = 0; i < source->get_Pages()->get_Count(); ++i)
        target->get_Pages()->Add();
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(target);
    editor->ImportAnnotations(MakeArray<String>({inputFile}));
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Import export all annotations XFDF

Export annotations to outputFile.xfdf, then import that file into a blank document with matching page count.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Export all annotations with [PdfAnnotationEditor::ExportAnnotationsToXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/exportannotationstoxfdf/).
1. Import the XFDF annotations with [PdfAnnotationEditor::ImportAnnotationsFromXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/importannotationsfromxfdf/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void ImportExportAllAnnotationsXfdf(String inputFile, String outputFile)
{
    String xfdfFile = outputFile + u".xfdf";
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);
    int count = editor->get_Document()->get_Pages()->get_Count();
    auto stream = System::IO::File::Create(xfdfFile);
    editor->ExportAnnotationsToXfdf(stream);
    stream->Close();
    auto target = MakeObject<Document>();
    for (int page = 0; page < count; ++page)
    {
        target->get_Pages()->Add();
    }
    auto importer = MakeObject<PdfAnnotationEditor>();
    importer->BindPdf(target);
    importer->ImportAnnotationsFromXfdf(xfdfFile);
    importer->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Import export selected annotations XFDF

Export only Text and FreeText annotations across the source page range, then import the XFDF into blank target pages.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Export the selected annotation types with [PdfAnnotationEditor::ExportAnnotationsXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/exportannotationsxfdf/).
1. Import the XFDF annotations with [PdfAnnotationEditor::ImportAnnotationsFromXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/importannotationsfromxfdf/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void ImportExportSelectedAnnotationsXfdf(String inputFile, String outputFile)
{
    String xfdfFile = outputFile + u".xfdf";
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);
    int count = editor->get_Document()->get_Pages()->get_Count();
    auto stream = System::IO::File::Create(xfdfFile);
    auto types = MakeArray<Annotations::AnnotationType>(
        {Annotations::AnnotationType::FreeText, Annotations::AnnotationType::Text});
    editor->ExportAnnotationsXfdf(stream, 1, count, types);
    stream->Close();
    auto target = MakeObject<Document>();
    for (int page = 0; page < count; ++page)
    {
        target->get_Pages()->Add();
    }
    auto importer = MakeObject<PdfAnnotationEditor>();
    importer->BindPdf(target);
    importer->ImportAnnotationsFromXfdf(xfdfFile);
    importer->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Modify annotations author

Replace the author Aspose User with Aspose.PDF user across the document page range.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace matching annotation authors with [PdfAnnotationEditor::ModifyAnnotationsAuthor()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/modifyannotationsauthor/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void ModifyAnnotationsAuthor(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);

    editor->ModifyAnnotationsAuthor(1, editor->get_Document()->get_Pages()->get_Count(), u"Aspose User",
                                    u"Aspose.PDF user");

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```

## Modify annotations

Use a TextAnnotation template to update annotation title, subject, and contents on page 1.

1. Create [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the annotation template with [PdfAnnotationEditor::ModifyAnnotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/modifyannotations/).
1. Save the resulting PDF with [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfannotationeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfAnnotationEditor.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/TextAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_AnnotationEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfAnnotationEditor;

void ModifyAnnotations(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfAnnotationEditor>();
    editor->BindPdf(inputFile);

    auto annotation = MakeObject<Annotations::TextAnnotation>(editor->get_Document()->get_Pages()->idx_get(1),
                                                              MakeObject<Rectangle>(200, 400, 400, 600));
    annotation->set_Title(u"Updated title");
    annotation->set_Subject(u"Updated subject");
    annotation->set_Contents(u"Updated sample contents for the annotation");
    editor->ModifyAnnotations(1, 1, annotation);

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_AnnotationEditor
```
