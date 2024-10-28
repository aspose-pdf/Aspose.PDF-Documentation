---
title: PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
weight: 30
url: /cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: 이 섹션에서는 PDF A 표준에 대한 PDF 문서 검증, TOC 작업 방법, PDF 만료 날짜 설정 방법 및 PDF 파일 생성 진행 상태를 결정하는 방법에 대해 설명합니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF A 표준에 대한 PDF 문서 검증 (A 1A 및 A 1B)

PDF/A-1a 또는 PDF/A-1b 호환성을 위해 PDF 문서를 검증하려면 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) 메서드를 사용하세요. 이 메서드를 통해 결과가 저장될 파일 이름과 필요한 검증 유형 [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) 열거형 : PDF_A_1A 또는 PDF_A_1B를 지정할 수 있습니다.

{{% alert color="primary" %}}

The output XML format is custom Aspose format. The XML contains a collection of tags with the name Problem; each tag contains the details of a particular problem. The Problem tag's ObjectID attribute represents the ID of the particular object this problem is related to. The Clause attribute represents a corresponding rule in the PDF specification.

{{% /alert %}}

The following code snippet shows you how to validate PDF document for PDF/A-1A.

```cpp
void ExampleValidate01() {
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // PDF/A-1a에 대한 PDF 검증
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

The following code snippet shows you how to validate PDF document for PDF/A-1B.

```cpp
void ExampleValidate02() {
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // PDF/A-1a에 대한 PDF 검증
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## TOC 작업

### 기존 PDF에 TOC 추가

Aspose.PDF API를 사용하면 PDF를 생성할 때 또는 기존 파일에 목차를 추가할 수 있습니다.

기존 PDF 파일에 TOC를 추가하려면 Aspose.Pdf 네임스페이스의 [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) 클래스를 사용하세요. Aspose.Pdf 네임스페이스를 사용하면 새로운 PDF 파일을 생성하고 기존 PDF 파일을 조작할 수 있습니다. 기존 PDF에 TOC를 추가하려면 Aspose.Pdf 네임스페이스를 사용하십시오.

다음 코드 스니펫은 기존 PDF 파일 내에 목차를 생성하는 방법을 보여줍니다.

```cpp
void ExampleToc01() {
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDF 파일의 첫 번째 페이지에 접근
    auto tocPage = document->get_Pages()->Insert(1);

    // TOC 정보를 나타내는 객체 생성
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("목차");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TOC에 제목 설정
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // TOC 요소로 사용할 문자열 객체 생성
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"첫 번째 페이지", 0);
    titles->SetValue(u"두 번째 페이지", 1);
    titles->SetValue(u"세 번째 페이지", 2);
    titles->SetValue(u"네 번째 페이지", 3);

    for (int i = 0; i < 2; i++)
    {
        // Heading 객체 생성
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Heading 객체의 대상 페이지 지정

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // 대상 페이지
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // 대상 좌표
        segment2->set_Text(titles[i]);

        // TOC를 포함하는 페이지에 제목 추가
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

### 서로 다른 TOC 레벨에 대해 다른 TabLeaderType 설정하기

Aspose.PDF for C++는 서로 다른 TOC 레벨에 대해 다른 TabLeaderType을 설정할 수 있습니다. FormatArray의 LineDash 속성을 적절한 TabLeaderType 값으로 설정해야 합니다. 그런 다음, Pdf 문서의 섹션 컬렉션에 리스트 섹션을 추가할 수 있습니다. 이후, Pdf 문서에 섹션을 생성하고 PDF 파일을 저장합니다.

```cpp
void ExampleToc02() {
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    // LeaderType 설정
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // TOC 정보를 나타내기 위한 객체 생성
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TOC의 제목 설정
    tocInfo->set_Title(title);

    // Pdf 문서의 섹션 컬렉션에 리스트 섹션 추가
    tocPage->set_TocInfo(tocInfo);

    // 왼쪽 여백을 설정하여 네 레벨 목록의 형식 정의
    // 및 각 레벨의 텍스트 형식 설정

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Pdf 문서에 섹션 생성
    auto page = document->get_Pages()->Add();

    // 섹션에 네 개의 헤딩 추가
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Sample Heading" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    // 목차에 헤딩 추가
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // Pdf 저장
    document->Save(_dataDir + outputFileName);
}
```

### TOC에서 페이지 번호 숨기기

목차에서 제목과 함께 페이지 번호를 숨기려면, [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) 클래스의 [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) 속성을 false로 설정할 수 있습니다.

다음 코드 스니펫을 확인하여 목차에서 페이지 번호를 숨기는 방법을 확인하세요:

```cpp
void ExampleToc03() {
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름에 대한 문자열.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // TOC 정보를 나타내는 객체 생성
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("목차");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TOC의 제목 설정
    tocInfo->set_Title(title);

    // Pdf 문서의 섹션 컬렉션에 목록 섹션 추가
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    // 네 개의 수준 목록 형식을 왼쪽 여백과 각 수준의 텍스트 형식 설정으로 정의

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    // 섹션에 네 개의 헤딩 추가
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"이것은 레벨 " + Level + "의 헤딩입니다.");
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // Pdf 저장
    document->Save(_dataDir + outputFileName);
}
```

## PDF 만료일 설정 방법

우리는 특정 사용자 그룹이 PDF 문서의 특정 기능/객체에 접근할 수 있도록 PDF 파일에 접근 권한을 적용합니다. PDF 파일 접근을 제한하기 위해 보통 암호화를 적용하고 PDF 파일 만료를 설정해야 할 수도 있습니다. 이렇게 하면 문서를 접근/열람하는 사용자가 PDF 파일 만료에 대한 유효한 알림을 받게 됩니다.

위에서 언급한 요구 사항을 달성하기 위해, 우리는 [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/) 객체를 사용할 수 있습니다. 다음 코드 스니펫을 확인해보세요.

```cpp
void SetPDFexpiryDate() {

    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String outputFileName("SetExpiryDate_out.pdf");

    // Document 객체 인스턴스화
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    document->get_Pages()->Add();

    // 페이지 객체의 문단 컬렉션에 텍스트 프래그먼트 추가
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // PDF 만료일을 설정하기 위한 JavaScript 객체 생성
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // JavaScript를 PDF 열기 액션으로 설정
    document->set_OpenAction(javaScript);

    // PDF 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## PDF 파일 생성 진행 상황 결정

고객이 개발자가 PDF 파일 생성 진행 상황을 결정할 수 있는 기능을 추가해 달라고 요청했습니다. 여기에 대한 응답입니다.

[DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) 클래스의 [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) 필드는 PDF 생성이 어떻게 진행되고 있는지를 결정할 수 있게 해줍니다.

아래 코드 스니펫은 [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb)를 사용하는 방법을 보여줍니다.

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름에 대한 문자열.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // 문서 열기
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## C++에서 작성 가능한 PDF 평면화

PDF 문서는 종종 라디오 버튼, 체크박스, 텍스트 상자, 목록 등과 같은 대화형 작성 가능한 위젯을 포함합니다. 다양한 애플리케이션 목적을 위해 편집이 불가능하게 만들기 위해 PDF 파일을 평면화해야 합니다. Aspose.PDF for C++는 C++에서 몇 줄의 코드만으로 PDF를 평면화할 수 있는 기능을 제공합니다:

```cpp
void FlattenFillablePDF() {
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 작성 가능한 PDF 평면화
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```