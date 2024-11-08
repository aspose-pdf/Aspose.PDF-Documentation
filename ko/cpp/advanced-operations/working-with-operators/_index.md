---
title: C++를 사용한 연산자 작업
linktitle: 연산자 작업
type: docs
weight: 170
url: /ko/cpp/operators/
description: 이 주제는 C++에서 Aspose.PDF를 사용하여 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 연산자 및 사용법 소개

연산자는 페이지에 그래픽 모양을 그리는 것과 같이 수행할 작업을 지정하는 PDF 키워드입니다. 연산자 키워드는 초기 슬래시 문자(2Fh)가 없는 점에서 명명된 객체와 구별됩니다. 연산자는 콘텐츠 스트림 내에서만 의미가 있습니다.

콘텐츠 스트림은 페이지에 그릴 그래픽 요소를 설명하는 명령으로 구성된 데이터인 PDF 스트림 객체입니다. PDF 연산자에 대한 자세한 내용은 [PDF 사양](https://opensource.adobe.com/dc-acrobat-sdk-docs/)에서 찾을 수 있습니다.

### 구현 세부사항

이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다. 선택된 예제는 개념을 설명하기 위해 PDF 파일에 이미지를 추가합니다. PDF 파일에 이미지를 추가하려면 다양한 연산자가 필요합니다. 이 예제에서는 [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do), 그리고 [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore)를 사용합니다.

- **GSave** 연산자는 PDF의 현재 그래픽 상태를 저장합니다.
- **ConcatenateMatrix** (행렬 연결) 연산자는 이미지가 PDF 페이지에 어떻게 배치되어야 하는지를 정의하는 데 사용됩니다.
- **Do** 연산자는 페이지에 이미지를 그립니다.
- **GRestore** 연산자는 그래픽 상태를 복원합니다.

PDF 파일에 이미지를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 객체를 생성하고 입력 PDF 문서를 엽니다.
1. 특정 페이지에 이미지를 추가합니다.
1. 이미지가 페이지의 리소스 컬렉션에 추가됩니다.
1. 연산자를 사용하여 페이지에 이미지를 배치합니다:
   - 먼저, GSave 연산자를 사용하여 현재 그래픽 상태를 저장합니다.
   - 그런 다음 ConcatenateMatrix 연산자를 사용하여 이미지가 배치될 위치를 지정합니다.
   - Do 연산자를 사용하여 페이지에 이미지를 그립니다.
1. 마지막으로 GRestore 연산자를 사용하여 업데이트된 그래픽 상태를 저장합니다.

다음 코드 스니펫은 PDF 연산자를 사용하는 방법을 보여줍니다.
## 페이지에 연산자를 사용하여 XForm 그리기

이 주제는 GSave/GRestore 연산자를 사용하는 방법, xForm의 위치를 지정하기 위한 ContatenateMatrix 연산자, 그리고 페이지에 xForm을 그리기 위한 Do 연산자를 사용하는 방법을 보여줍니다.

아래 코드는 PDF 파일의 기존 내용을 GSave/GRestore 연산자 쌍으로 감쌉니다. 이 접근 방식은 기존 내용의 끝에서 초기 그래픽 상태를 얻는 데 도움이 됩니다. 이 방법이 없으면 기존 연산자 체인의 끝에서 바람직하지 않은 변환이 남아 있을 수 있습니다.

```cpp
void DrawXFormOnPageUsingOperators() {
    // 문서 열기
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // 샘플은 다음을 보여줍니다.
    // GSave/GRestore 연산자 사용
    // xForm의 위치를 지정하기 위한 ContatenateMatrix 연산자 사용
    // 페이지에서 xForm을 그리기 위한 Do 연산자 사용

    // 기존 내용을 GSave/GRestore 연산자 쌍으로 감싸기
    //        이는 기존 내용의 끝에서 초기 그래픽 상태를 얻기 위함입니다
    //        그렇지 않으면 기존 연산자 체인의 끝에서 바람직하지 않은 변환이 남아 있을 수 있습니다
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 새로운 명령 후 그래픽 상태를 제대로 지우기 위한 그래픽 상태 저장 연산자 추가
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // xForm 생성

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // 이미지 너비와 높이 정의
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // 이미지를 스트림에 로드
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // XForm 자원의 Images 컬렉션에 이미지 추가
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Do 연산자 사용: 이 연산자는 이미지를 그립니다
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // x=100 y=500 좌표에 폼 배치
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Do 연산자로 폼 그리기
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // x=100 y=300 좌표에 폼 배치
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Do 연산자로 폼 그리기
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // GSave 이후에 GRestore로 그래픽 상태 복원
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## 연산자 클래스를 사용하여 그래픽 개체 제거하기

연산자 클래스는 PDF 조작을 위한 뛰어난 기능을 제공합니다. PDF 파일에 [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor) 클래스의 [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) 메서드를 사용하여 제거할 수 없는 그래픽이 포함되어 있을 때, 연산자 클래스를 사용하여 대신 제거할 수 있습니다.

다음 코드 스니펫은 그래픽을 제거하는 방법을 보여줍니다. 이 접근 방식을 사용할 때 PDF 파일에 그래픽의 텍스트 레이블이 포함되어 있다면, 그것들이 PDF 파일에 남아 있을 수 있음을 유의하십시오. 따라서 그러한 이미지를 삭제할 대체 방법을 위해 그래픽 연산자를 검색하십시오.

```cpp
void RemoveGraphicsObjects() {
    // 문서 열기
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // 사용된 경로-페인팅 연산자들
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```