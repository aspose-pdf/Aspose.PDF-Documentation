---
title: C++를 사용하여 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 50
url: /cpp/rotate-pages/
description: 이 주제는 C++를 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

이 주제는 C++를 사용하여 기존 PDF 파일의 페이지 방향을 업데이트하거나 변경하는 방법을 설명합니다.

## 페이지 방향 변경

Aspose.PDF for C++는 페이지 방향을 가로에서 세로로, 또는 그 반대로 변경할 수 있습니다. 페이지 방향을 변경하려면 다음 코드 스니펫을 사용하여 페이지의 MediaBox를 설정합니다. 또한 Rotate() 메서드를 사용하여 회전 각도를 설정하여 페이지 방향을 변경할 수 있습니다.

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // 페이지 크기 변경을 보상하기 위해 페이지를 위로 이동해야 합니다.
        // (페이지의 하단 모서리는 0,0이고 정보는 일반적으로 페이지 상단에서 시작됩니다.
        //  따라서 하단 모서리를 이전 높이와 새 높이의 차이만큼 위로 이동합니다.)

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // 때때로 원본 파일에 설정된 경우 CropBox도 설정해야 합니다.
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // 페이지의 회전 각도 설정
        page->set_Rotate(Rotation::on90);
    }

    // 출력 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

## 페이지 콘텐츠를 새 페이지 방향에 맞추기

위의 코드 스니펫을 사용할 때 페이지 높이가 감소하기 때문에 문서의 일부 내용이 잘릴 수 있습니다. 이를 피하려면 너비를 비례적으로 늘리고 높이는 그대로 두십시오. 계산 예:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // 새 높이는 동일
        double newHeight = r->get_Height();
        // 새 너비는 방향을 가로로 만들기 위해 비례적으로 확장됩니다
        // (이전 방향이 세로라고 가정합니다)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

위 접근 방식 외에도 페이지 콘텐츠에 확대를 적용할 수 있는 PdfPageEditor 퍼사드를 사용하는 것을 고려하십시오.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDF의 첫 페이지의 사각형 영역 가져오기
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // PdfPageEditor 인스턴스 생성
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // 원본 PDF 바인딩
    ppe->BindPdf(_dataDir + inputFileName);
    // 확대 계수 설정
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // 페이지 크기 업데이트
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // 출력 파일 저장
    document->Save(_dataDir + outputFileName);
}
```