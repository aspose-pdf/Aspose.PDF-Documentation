---
title: PDF 파일에 텍스트 스탬프 추가
linktitle: PDF 파일의 텍스트 스탬프
type: docs
weight: 20
url: ko/cpp/text-stamps-in-the-pdf-file/
description: C++의 TextStamp 클래스를 사용하여 PDF 파일에 텍스트 스탬프를 추가합니다.
lastmod: "2021-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## C++로 텍스트 스탬프 추가

[TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) 클래스를 사용하여 PDF 파일에 텍스트 스탬프를 추가할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등과 같은 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 텍스트 스탬프를 추가하려면, Document 객체와 필요한 속성을 사용하여 TextStamp 객체를 생성해야 합니다. 그런 다음, PDF에 스탬프를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다. 다음 코드 스니펫은 PDF 파일에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```cpp
void AddTextStampToPDFFile() {

    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 텍스트 스탬프 생성
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // 스탬프가 배경인지 설정
    textStamp->set_Background(true);
    // 원점 설정
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // 스탬프 회전
    textStamp->set_Rotate(Rotation::on90);

    // 텍스트 속성 설정
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // 특정 페이지에 스탬프 추가
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // 출력 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## TextStamp 객체에 대한 정렬 정의

PDF 문서에 워터마크를 추가하는 것은 자주 요구되는 기능 중 하나이며 Aspose.PDF for C++는 이미지 및 텍스트 워터마크를 추가하는 기능을 완벽하게 지원합니다. 우리는 PDF 파일 위에 텍스트 스탬프를 추가하는 기능을 제공하는 [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp)라는 클래스를 가지고 있습니다. 최근에 TextStamp 객체를 사용할 때 텍스트의 정렬을 지정하는 기능을 지원해야 한다는 요구가 있었습니다. 따라서 이 요구를 충족시키기 위해 우리는 TextStamp 클래스에 TextAlignment 속성을 도입했습니다. 이 속성을 사용하여 수평 텍스트 정렬을 지정할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서를 로드하고 그 위에 TextStamp를 추가하는 방법의 예를 보여줍니다.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 샘플 문자열로 FormattedText 객체 인스턴스화
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // FormattedText에 새 텍스트 줄 추가
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // FormattedText를 사용하여 TextStamp 객체 생성
    auto stamp = MakeObject<TextStamp>(text);
    // 텍스트 스탬프의 수평 정렬을 가운데 정렬로 지정
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // 텍스트 스탬프의 수직 정렬을 가운데 정렬로 지정
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // TextStamp의 텍스트 수평 정렬을 가운데 정렬로 지정
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // 스탬프 객체의 상단 여백 설정
    stamp->set_TopMargin(20);
    // PDF 파일의 모든 페이지에 스탬프 추가
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // 출력 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## PDF 파일에서 스탬프로 채우기 및 윤곽선 텍스트

텍스트 추가 및 편집 시나리오에 대한 렌더링 모드 설정을 구현했습니다. 윤곽선 텍스트를 렌더링하려면 TextState 객체를 생성하고 RenderingMode를 TextRenderingMode.StrokeText로 설정하고 StrokingColor 속성에 대한 색상을 선택하십시오. 이후, BindTextState() 메서드를 사용하여 스탬프에 TextState를 바인딩합니다.

다음 코드 스니펫은 채우기 및 윤곽선 텍스트 추가를 보여줍니다:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 고급 속성을 전달하기 위한 TextState 객체 생성
    auto ts = MakeObject<TextState>();

    // 윤곽선 색상 설정
    ts->set_StrokingColor(Color::get_Gray());

    // 텍스트 렌더링 모드 설정
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // 입력 PDF 문서 로드
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // TextState 바인딩
    stamp->BindTextState(ts);

    // X,Y 원점 설정
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // 스탬프 추가
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```