---
title: C++를 사용하여 PDF 문서 형식화
linktitle: PDF 문서 형식화
type: docs
weight: 20
url: ko/cpp/formatting-pdf-document/
description: Aspose.PDF for C++를 사용하여 PDF 문서를 생성 및 형식화합니다. 다음 코드 스니펫을 사용하여 작업을 해결하십시오.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서 형식화

### 문서 창 및 페이지 표시 속성 가져오기

이 주제는 문서 창, 뷰어 애플리케이션의 속성을 가져오는 방법과 페이지가 표시되는 방법을 이해하는 데 도움이 됩니다. 이러한 속성을 설정하려면 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF 파일을 엽니다. 이제 Document 객체의 속성을 설정할 수 있습니다. 예를 들어:

- CenterWindow – 문서 창을 화면 중앙에 위치시킵니다. 기본값: false.
- Direction – 읽기 순서. 페이지가 나란히 표시될 때 레이아웃이 결정됩니다. 기본값: 왼쪽에서 오른쪽.
- DisplayDocTitle – 문서 창 제목 표시줄에 문서 제목을 표시합니다.  기본값: false (제목이 표시됨).
- HideMenuBar – 문서 창의 메뉴 모음을 숨기거나 표시합니다. 기본값: false (메뉴 모음이 표시됨).
- HideToolBar – 문서 창의 도구 모음을 숨기거나 표시합니다. 기본값: false (도구 모음이 표시됨).
- HideWindowUI – 스크롤 바와 같은 문서 창 요소를 숨기거나 표시합니다. 기본값: false (UI 요소가 표시됨).
- NonFullScreenPageMode – 전체 페이지 모드로 표시되지 않을 때 문서의 표시 방식입니다.
- PageLayout – 페이지 레이아웃입니다.
- PageMode – 문서를 처음 열 때 표시되는 방식입니다. 옵션은 미리보기, 전체 화면, 첨부 파일 패널 표시입니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 다양한 문서 속성 가져오기
    // 문서 창의 위치 - 기본값: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // 주요 읽기 순서; 페이지 위치를 결정합니다
    // 나란히 표시될 때 - 기본값: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // 창의 제목 표시줄에 문서 제목을 표시할지 여부
    // false이면 제목 표시줄에 PDF 파일 이름이 표시됨 - 기본값: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // 문서 창의 크기를
    // 첫 번째 표시된 페이지의 크기에 맞춰 조정할지 여부 - 기본값: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // 뷰어 애플리케이션의 메뉴 모음을 숨길지 여부 - 기본값: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // 뷰어 애플리케이션의 도구 모음을 숨길지 여부 - 기본값: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // 스크롤 바와 같은 UI 요소를 숨길지 여부
    // 그리고 페이지 내용만 표시할지 여부 - 기본값: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서 표시 방법.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // 페이지 레이아웃 예: 단일 페이지, 한 열
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // 문서를 열 때 표시되는 방식
    // 예: 미리보기, 전체 화면, 첨부 파일 패널 표시
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### 문서 창 및 페이지 표시 속성 설정하기

이 주제에서는 문서 창, 뷰어 애플리케이션 및 페이지 표시 속성을 설정하는 방법을 설명합니다. 이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF 파일을 엽니다.
1. 다양한 문서 속성을 설정합니다:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. Save 메서드를 사용하여 업데이트된 PDF 파일을 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa)합니다.

사용 가능한 속성은 다음과 같습니다:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

각 속성은 아래 코드에서 사용 및 설명됩니다. 다음 - 코드 스니펫은 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 속성을 설정하는 방법을 보여줍니다.

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 다양한 문서 속성 설정
    // 문서 창의 위치를 지정 - 기본값: false
    document->set_CenterWindow(true);

    // 주된 읽기 순서; 페이지의 위치를 결정
    // 나란히 표시될 때 - 기본값: L2R
    document->set_Direction(Direction::R2L);

    // 창의 제목 표시줄에 문서 제목을 표시할지 여부를 지정
    // false인 경우 제목 표시줄에 PDF 파일 이름이 표시됨 - 기본값: false
    document->set_DisplayDocTitle(true);

    // 문서 창의 크기를 첫 번째 표시된 페이지 크기에 맞추도록 크기를 조정할지 여부를 지정 - 기본값: false
    document->set_FitWindow(true);

    // 뷰어 응용 프로그램의 메뉴 표시줄을 숨길지 여부를 지정 - 기본값: false
    document->set_HideMenubar(true);

    // 뷰어 응용 프로그램의 도구 모음을 숨길지 여부를 지정 - 기본값: false
    document->set_HideToolBar(true);

    // 스크롤 바와 같은 UI 요소를 숨길지 여부를 지정
    // 페이지 내용만 표시되도록 설정 - 기본값: false
    document->set_HideWindowUI(true);

    // 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서가 어떻게 표시될지 지정.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // 페이지 레이아웃 지정, 즉 단일 페이지, 한 열
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // 문서를 열 때 어떻게 표시할지 지정
    // 예: 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
    document->set_PageMode(PageMode::UseThumbs);

    // 업데이트된 PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}
```
### 기존 PDF 파일에 폰트 임베딩

PDF 리더는 문서가 표시되는 플랫폼에 상관없이 문서를 동일한 방식으로 표시할 수 있도록 [14개의 핵심 폰트](https://en.wikipedia.org/wiki/PDF#Text)를 지원합니다. PDF에 14개의 핵심 폰트 중 하나가 아닌 폰트가 포함되어 있을 때, 폰트 대체를 피하기 위해 PDF 파일에 폰트를 임베딩하세요.

Aspose.PDF for C++는 기존 PDF 파일에서 폰트 임베딩을 지원합니다. 전체 폰트나 폰트의 서브셋을 임베딩할 수 있습니다. 폰트를 임베딩하려면 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF 파일을 엽니다. 그런 다음 [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) 클래스를 사용하여 PDF 파일에 폰트를 임베딩합니다. 전체 폰트를 임베딩하려면 Font 클래스의 IsEmbeded 속성을 사용하고, 폰트의 서브셋을 사용하려면 IsSubset 속성을 사용하세요.

{{% alert color="primary" %}}

폰트 서브셋은 사용된 문자만 임베딩하며, 예를 들어 로고에 기업 폰트를 사용하지만 본문 텍스트에는 사용하지 않는 경우처럼 폰트가 짧은 문장이나 슬로건에 사용될 때 유용합니다. 출력 PDF의 파일 크기를 줄이려면 일부 집합을 사용하십시오. 그러나 본문 텍스트에 사용자 정의 글꼴이 사용되는 경우 전체적으로 포함하십시오.

{{% /alert %}}

다음 코드 스니펫은 PDF 파일에 글꼴을 포함하는 방법을 보여줍니다.

### 표준 Type 1 글꼴 포함

특수 집합에서 글꼴을 사용하는 PDF 문서가 있으며, 이는 "표준 Type 1 글꼴"이라고 합니다. 이 집합에는 14개의 글꼴이 포함되어 있으며, 이 유형의 글꼴을 포함하려면 [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6)와 같은 특수 플래그를 사용해야 합니다.

다음은 표준 Type 1 글꼴을 포함하여 모든 글꼴이 포함된 문서를 얻기 위해 사용할 수 있는 코드 스니펫입니다:

```cpp
void EmbeddingStandardType1Fonts()
{

    // 경로 이름에 대한 문자열입니다.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열입니다.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 문서의 EmbedStandardFonts 속성을 설정합니다.
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // 글꼴이 이미 포함되어 있는지 확인합니다.
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### PDF 생성 시 글꼴 포함

Adobe Reader에서 지원하는 14개의 기본 글꼴 외에 다른 글꼴을 사용해야 하는 경우, Pdf 파일을 생성할 때 글꼴 설명을 포함해야 합니다. 글꼴 정보가 포함되지 않은 경우, Adobe Reader는 시스템에 설치되어 있으면 운영 체제에서 가져오거나, Pdf의 글꼴 설명에 따라 대체 글꼴을 구성합니다.

>포함된 글꼴은 호스트 머신에 설치되어 있어야 합니다. 즉, 다음 코드의 경우 'Univers Condensed' 글꼴이 시스템에 설치되어 있습니다.

Font 클래스의 IsEmbedded 속성을 사용하여 Pdf 파일에 글꼴 정보를 포함합니다. 이 속성의 값을 ‘True’로 설정하면 글꼴 파일 전체가 Pdf에 포함되며, 이는 Pdf 파일 크기를 증가시킬 것입니다. 다음은 Pdf에 글꼴 정보를 포함하는 데 사용할 수 있는 코드 스니펫입니다.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Pdf 객체에 섹션 생성
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // PDF 문서 저장
    document->Save(_dataDir);
}
```

### PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체와 장치에 사용할 수 없는 글꼴이 포함되어 있으면, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능할 때(장치에 설치되어 있거나 문서에 포함되어 있을 때), 출력 PDF는 동일한 글꼴을 가져야 합니다(기본 글꼴로 대체되지 않아야 합니다). 기본 글꼴의 값은 글꼴 파일의 경로가 아닌 글꼴 이름을 포함해야 합니다. Apose.PDF for C++는 문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음 코드 스니펫은 기본 글꼴을 설정하는 데 사용할 수 있습니다:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름을 위한 문자열.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // 기본 글꼴 이름 지정
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오려면, [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스에서 제공하는 [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() 메서드를 사용할 수 있습니다.

기존 PDF 문서에서 모든 글꼴을 가져오기 위한 다음 코드 스니펫을 확인하세요:

```cpp
void GetAllFontsFromPDFdocument()
{
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### 글꼴 대체 경고 가져오기

Aspose.PDF for C++는 글꼴 대체 사례를 처리하기 위한 글꼴 대체에 대한 알림을 받기 위한 메서드를 제공합니다. 아래의 코드 스니펫은 해당 기능을 사용하는 방법을 보여줍니다.

```cpp
void GetWarningsForFontSubstitution()
{
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

[OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) 메소드는 아래와 같이 나열되어 있습니다.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Warning: Font " << font.get_FontName() 
            << " was substituted with another font -> " 
            << newFont.get_FontName() << std::endl;
}
```

### FontSubsetStrategy를 사용하여 글꼴 포함 개선

하위 집합으로 글꼴을 포함시키는 기능은 IsSubset 속성을 사용하여 달성할 수 있지만, 때때로 문서에서 사용되는 하위 집합만으로 완전히 포함된 글꼴 세트를 줄이기를 원할 수 있습니다. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)에는 [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) 속성이 있으며, 여기에는 SubsetFonts(FontSubsetStrategy subsetStrategy) 메서드를 포함하고 있습니다. SubsetFonts() 메서드에서 매개변수 subsetStrategy는 서브셋 전략을 조정하는 데 도움을 줍니다. FontSubsetStrategy는 폰트 서브셋팅의 두 가지 변형을 지원합니다.

- SubsetAllFonts - 문서에서 사용된 모든 폰트를 서브셋합니다.
- SubsetEmbeddedFontsOnly - 문서에 완전히 포함된 폰트만 서브셋합니다.

다음 코드는 FontSubsetStrategy를 설정하는 방법을 보여줍니다:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // 경로 이름을 위한 문자열입니다.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열입니다.
    String inputFileName("sample.pdf");
    // 파일 이름을 위한 문자열입니다.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // SubsetAllFonts의 경우 모든 폰트가 문서에 서브셋으로 포함됩니다.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // 폰트 서브셋은 완전히 포함된 폰트에 대해 포함되지만 문서에 포함되지 않은 폰트는 영향을 받지 않습니다.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### PDF 파일의 줌 팩터 설정 및 가져오기

때때로 PDF 문서의 줌 팩터를 설정하고 싶을 때가 있습니다. Aspose.PDF for C++를 사용하면 Document 클래스의 [set_OpenAction(…) 메서드](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21)로 줌 팩터 값을 설정할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) 클래스의 Destination 속성을 통해 PDF 파일과 연관된 줌 값을 가져올 수 있습니다. 이와 유사하게 파일의 줌 팩터를 설정하는 데 사용할 수 있습니다.

#### 줌 팩터 설정

다음 코드 스니펫은 PDF 파일의 줌 팩터를 설정하는 방법을 보여줍니다.

```cpp
void SetZoomFactor() {
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("sample.pdf");
    // 파일 이름을 위한 문자열.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

#### 줌 팩터 가져오기

Aspose.PDF for C++를 사용하여 PDF 파일의 줌 팩터를 가져옵니다.

다음 코드 스니펫은 PDF 파일의 줌 팩터를 가져오는 방법을 보여줍니다:

```cpp
void GetZoomFactor() 
{
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // GoToAction 객체 생성
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // PDF 파일의 줌 팩터 가져오기
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // 문서 줌 값;
}
```

### 인쇄 대화 상자 프리셋 속성 설정

Aspoose.PDF for C++는 PDF 문서의 인쇄 대화 상자 프리셋 속성을 설정할 수 있습니다. 기본적으로 단면으로 설정된 PDF 문서의 DuplexMode 속성을 변경할 수 있습니다. 이는 아래에 표시된 두 가지 방법론을 사용하여 달성할 수 있습니다.

```cpp
void SettingPrintDialogPresetProperties()
{
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");
    // 파일 이름을 위한 문자열.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### PDF 콘텐츠 편집기를 사용하여 인쇄 대화 상자 프리셋 속성 설정

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "The file has duplex flip short edge" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```