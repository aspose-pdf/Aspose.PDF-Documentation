---
title: C++를 사용하여 포함된 이미지의 해상도 및 크기 가져오기
linktitle: 해상도 및 크기 가져오기
type: docs
weight: 40
url: /ko/cpp/get-resolution-and-dimensions-of-embedded-images/
description: 이 섹션은 포함된 이미지의 해상도 및 크기를 가져오는 방법의 세부 정보를 보여줍니다.
lastmod: "2021-12-18"
---

이 주제는 이미지를 추출하지 않고 해상도 및 크기 정보를 얻을 수 있는 기능을 제공하는 Aspose.PDF 네임스페이스의 연산자 클래스를 사용하는 방법을 설명합니다.

이를 달성하는 다양한 방법이 있습니다. 이 문서는 `arraylist`와 [이미지 배치 클래스](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement)를 사용하는 방법을 설명합니다.

1. 먼저 소스 PDF 파일(이미지 포함)을 로드합니다.
1. 그런 다음 문서의 이미지 이름을 저장할 ArrayList 객체를 생성합니다.
1. Page.Resources.Images 속성을 사용하여 이미지를 가져옵니다.
1. 이미지의 그래픽 상태를 저장할 스택 객체를 생성하고 이를 사용하여 서로 다른 이미지 상태를 추적합니다.
1. 문서를 변환하는 현재 변환을 정의하는 ConcatenateMatrix 객체를 만듭니다. 또한 모든 콘텐츠를 확대, 회전 및 왜곡하는 것을 지원합니다. 새 행렬을 이전 것과 연결합니다. 변환을 처음부터 정의할 수 없으며 기존 변환만 수정할 수 있음을 유의하십시오.
1. ConcatenateMatrix로 행렬을 수정할 수 있기 때문에 원본 이미지 상태로 되돌려야 할 수도 있습니다. [GSave 연산자](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) 및 [GRestore 연산자](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/)를 사용하십시오. 이 연산자들은 쌍으로 사용되므로 함께 호출해야 합니다. 예를 들어 복잡한 변환으로 그래픽 작업을 수행하고 최종적으로 변환을 초기 상태로 되돌리는 경우 접근 방식은 다음과 같습니다:

다음 코드 스니펫은 PDF 문서에서 이미지를 추출하지 않고 이미지의 치수와 해상도를 가져오는 방법을 보여줍니다.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // 원본 PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // 이미지에 대한 기본 해상도 정의
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // 이미지 이름을 저장할 배열 리스트 객체 정의
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // 객체를 스택에 삽입
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // 문서의 첫 번째 페이지에 있는 모든 연산자 가져오기
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // GSave/GRestore 연산자를 사용하여 변환을 이전에 설정한 상태로 되돌리기
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // 현재 변환 행렬을 정의하는 ConcatenateMatrix 객체 인스턴스화
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // 리소스에서 객체를 그리는 Do 연산자 생성, 이는 Form 객체와 Image 객체를 그립니다.
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // 이전 상태를 저장하고 현재 상태를 스택의 맨 위로 푸시
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // 현재 상태를 버리고 이전 상태 복원
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // 현재 행렬을 상태 행렬과 곱함
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // 이미지 그리기 연산자인 경우
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // 첫 번째 pdf 페이지의 이미지를 저장할 XImage 객체 생성
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // 이미지 치수 가져오기
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // 이미지의 높이 및 너비 정보 가져오기
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // 위 정보를 기반으로 해상도 계산
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // 각 이미지의 치수 및 해상도 정보 표시
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```