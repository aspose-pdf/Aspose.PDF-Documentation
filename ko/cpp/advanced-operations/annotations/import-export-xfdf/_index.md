---
title: Aspose.PDF for C++를 사용하여 XFDF 형식으로 주석 가져오기 및 내보내기
linktitle: XFDF 형식으로 주석 가져오기 및 내보내기
type: docs
weight: 40
url: ko/cpp/import-export-xfdf/
description: C++ 및 Aspose.PDF for C++ 라이브러리를 사용하여 XFDF 형식으로 주석을 가져오고 내보낼 수 있습니다.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF는 PDF 리더와 호환되는 파일 형식입니다. XFDF 파일은 XML 형식을 사용하여 양식 인코딩 및 주석과 같은 데이터를 저장하며, 이를 PDF로 저장하고 가져오거나 내보내어 볼 수 있습니다.

XFDF는 훨씬 더 다양한 작업에 사용할 수 있지만, 우리의 경우 양식 데이터나 주석을 다른 컴퓨터나 서버 등으로 보내거나 받을 때 사용할 수 있으며, 양식 데이터나 주석을 보관하는 데 사용할 수도 있습니다.

{{% /alert %}}

**Aspose.PDF for C++**는 PDF 문서를 편집할 때 기능이 풍부한 구성 요소입니다. As we know XFDF is an important aspect of PDF forms manipulation, Aspose.Pdf.Facades namespace in Aspose.PDF for C++ has considered this very well, and have provided methods to import and export annotations data to XFDF files.

XFDF는 PDF 양식 조작의 중요한 측면이라는 것을 알고 있듯이, Aspose.PDF for C++의 Aspose.Pdf.Facades 네임스페이스는 이를 매우 잘 고려하여 XFDF 파일로 주석 데이터를 가져오고 내보내는 메서드를 제공합니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) class contains two methods to work with import and export of annotations to XFDF file.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) 클래스에는 XFDF 파일로 주석을 가져오고 내보내기 위한 두 가지 메서드가 포함되어 있습니다. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) 메서드는 PDF 문서에서 XFDF 파일로 주석을 내보내는 기능을 제공하며, [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) 메서드는 기존 XFDF 파일에서 주석을 가져올 수 있게 합니다. 주석을 가져오거나 내보내기 위해서는 주석 유형을 지정해야 합니다. 이러한 유형을 열거형의 형태로 지정한 다음, 이 열거형을 이들 메서드 중 하나의 인수로 전달할 수 있습니다.

다음 코드 스니펫은 XFDF 파일로 주석을 내보내는 방법을 보여줍니다:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // PdfAnnotationEditor 객체 생성
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 주석 편집기에 PDF 문서 바인딩
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // 주석 내보내기
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
다음 코드 스니펫은 XFDF 파일로 주석을 가져오는 방법을 설명합니다:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // PdfAnnotationEditor 객체 생성
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 새 PDF 문서 생성
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // 주석 가져오기
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // 출력 PDF 저장
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## 주석을 한 번에 내보내기/가져오는 또 다른 방법

아래 코드에서 ImportAnnotations 메서드는 다른 PDF 문서에서 직접 주석을 가져올 수 있게 해줍니다.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // PdfAnnotationEditor 객체 생성
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 새 PDF 문서 생성
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // 주석 편집기는 여러 PDF 문서에서 주석을 가져올 수 있지만,
    // 이 예제에서는 하나만 사용합니다.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // 출력 PDF 저장
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```