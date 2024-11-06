---
title: C++로 PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 100
url: ko/cpp/add-page-number/
description: Aspose.PDF for C++를 사용하여 PageNumber Stamp 클래스를 통해 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF에 페이지 번호 추가하는 방법

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 다양한 부분을 쉽게 찾을 수 있도록 합니다. **Aspose.PDF for C++**를 사용하면 PageNumberStamp로 페이지 번호를 추가할 수 있습니다.

다음 단계와 샘플 코드는 [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) 페이지 요소를 사용하여 기존 PDF 문서에 페이지 번호 레이블을 추가하여 PDF에 자동으로 페이지 번호를 추가하는 방법을 보여줍니다.

기존 PDF 문서에 페이지 번호를 추가하는 단계:

페이지 번호 스탬프를 추가하려면 필요한 속성을 사용하여 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체와 [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) 객체를 생성해야 합니다.

그런 다음, PDF에 스탬프를 추가하기 위해 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)의 [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) 메서드를 호출할 수 있습니다.

페이지 번호 스탬프의 글꼴 속성도 설정할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 페이지 번호 스탬프 생성
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// 스탬프가 배경인지 여부
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// 텍스트 속성 설정
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // 특정 페이지에 스탬프 추가
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // 출력 문서 저장
    document->Save(_dataDir+ outputFileName);
}
```

## 라이브 예제

[PDF 페이지 번호 추가](https://products.aspose.app/pdf/page-number)는 페이지 번호 추가 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![C++를 사용하여 PDF에 페이지 번호 추가 방법](page_number.png)](https://products.aspose.app/pdf/page-number)

## Bates 번호 추가/제거

**Bates 번호**(Bates 스탬핑이라고도 함)는 법률, 의료 및 비즈니스 분야에서 이미지와 문서가 스캔되거나 처리될 때 식별 번호 및/또는 날짜/시간 표시를 부여하기 위해 사용됩니다. 예를 들어 재판 준비 과정에서 증거 발견 단계 또는 비즈니스 영수증 식별 시 사용됩니다. 이 과정은 이미지나 문서의 식별, 보호 및 자동 연속 번호 부여를 제공합니다.

Aspose.PDF는 현재 Bates 번호에 대해 제한된 지원을 제공합니다. 이 기능은 고객의 요청에 따라 업데이트될 예정입니다.

### Bates 번호 제거 방법

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // 출력 문서 저장
    document->Save(_dataDir + outputFileName);
}
```