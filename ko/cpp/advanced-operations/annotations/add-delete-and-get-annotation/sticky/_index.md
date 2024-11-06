---
title: PDF 스티키 주석을 C++로 사용하기
linktitle: 스티키 주석
type: docs
weight: 50
url: ko/cpp/sticky-annotations/
description: 이 주제는 스티키 주석에 관한 것이며, 예로 텍스트에 워터마크 주석을 보여줍니다. 페이지에 그래픽을 나타내는 데 사용됩니다. 이 작업을 해결하기 위해 코드 스니펫을 확인하세요.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 워터마크 주석 추가

워터마크 주석은 인쇄된 페이지의 크기와 관계없이 페이지의 고정된 크기와 위치에 인쇄되어야 하는 그래픽을 나타내는 데 사용됩니다.

PDF 페이지의 특정 위치에 [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/)을 사용하여 워터마크 텍스트를 추가할 수 있습니다. 워터마크의 불투명도는 불투명도 속성을 사용하여 제어할 수도 있습니다.

워터마크 주석을 추가하기 위한 다음 코드 스니펫을 확인하세요.

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 주석 생성
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    // 페이지의 주석 컬렉션에 주석 추가
    page->get_Annotations()->Add(wa);

    // 폰트 설정을 위한 TextState 생성
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    // 주석 텍스트의 불투명도 수준 설정
    wa->set_Opacity(0.5);

    // 주석에 텍스트 추가
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    // 문서 저장
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## 워터마크 주석 가져오기

PDF 문서에서 워터마크 주석을 가져오려면 다음 코드 스니펫을 사용해 보세요.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // AnnotationSelector를 사용하여 주석 필터링
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // 결과 출력
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## 워터마크 주석 삭제

PDF 문서에서 워터마크 주석을 삭제하려면 다음 코드 스니펫을 사용해 보세요.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // AnnotationSelector를 사용하여 주석 필터링
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // 주석 삭제
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```