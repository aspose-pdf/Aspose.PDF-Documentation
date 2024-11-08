---
title: C++를 사용하여 PDF에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: /ko/cpp/add-image-to-existing-pdf-file/
description: 이 섹션에서는 C++ 라이브러리를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2021-12-18"
---

## 기존 PDF 파일에 이미지 추가

모든 PDF 페이지는 리소스 및 콘텐츠 속성을 포함합니다. 리소스는 예를 들어 이미지 및 양식일 수 있으며, 콘텐츠는 PDF 연산자 세트로 표현됩니다. 각 연산자는 이름과 인수를 가지고 있습니다. 이 예제는 연산자를 사용하여 PDF 파일에 이미지를 추가합니다.

기존 PDF 파일에 이미지를 추가하려면:

- [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 객체를 생성하고 입력 PDF 문서를 엽니다.
- 이미지를 추가할 페이지를 가져옵니다.
- 페이지의 리소스 컬렉션에 이미지를 추가합니다.
- 연산자를 사용하여 페이지에 이미지를 배치합니다:
- [GSave operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/)를 사용하여 현재 그래픽 상태를 저장합니다.

- 이미지를 배치할 위치를 지정하기 위해 [ConcatenateMatrix operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96)를 사용합니다.
- 페이지에 이미지를 그리기 위해 [Do 연산자](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/)를 사용하세요.
- 마지막으로, 업데이트된 그래픽 상태를 저장하기 위해 [GRestore 연산자](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/)를 사용하세요.
- 파일을 저장하세요.
다음 코드 스니펫은 PDF 문서에 이미지를 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // 좌표 설정
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // 이미지를 추가할 페이지 가져오기
    auto page = document->get_Pages()->idx_get(1);

    // 스트림에 이미지 로드
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // 페이지 리소스의 Images 컬렉션에 이미지 추가
    page->get_Resources()->get_Images()->Add(imageStream);

    // GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Rectangle 및 Matrix 객체 생성
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // ConcatenateMatrix (행렬 연결) 연산자 사용:
    // 이미지가 배치되어야 하는 방법을 정의합니다
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Do 연산자 사용: 이 연산자는 이미지를 그립니다
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 새 PDF 저장
    document->Save(_dataDir + u"updated_document.pdf");

    // 이미지 스트림 닫기
    imageStream->Close();
}
```

## PDF 문서에서 단일 이미지를 여러 번 참조 추가

때때로 우리는 동일한 이미지를 PDF 문서에서 여러 번 사용할 필요가 있습니다. 새로운 인스턴스를 추가하면 결과 PDF 문서의 크기가 증가합니다. [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) 메서드는 원본 이미지와 동일한 PDF 객체에 대한 참조를 추가하여 PDF 문서의 크기를 최적화할 수 있습니다.

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## 페이지에 이미지 배치하고 종횡비 유지(제어)

이미지의 크기를 모르는 경우 페이지에 왜곡된 이미지가 표시될 가능성이 있습니다. 다음 예제는 이를 피하는 방법 중 하나를 보여줍니다.

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## PDF 내 이미지가 컬러인지 흑백인지 식별

이미지 크기를 줄이려면 압축해야 합니다. 이미지의 압축 유형을 결정하기 전에, 이미지가 컬러인지 흑백인지 알아야 합니다.

이미지에 적용되는 압축 유형은 원본 이미지의 색상 공간(ColorSpace)에 따라 달라집니다. 즉, 이미지가 컬러(RGB)인 경우 JPEG2000 압축을 사용하고, 흑백인 경우 JBIG2 / JBIG2000 압축을 사용합니다.

PDF 파일은 텍스트, 이미지, 그래프, 첨부 파일, 주석 등 요소를 포함할 수 있으며, 소스 PDF 파일에 이미지가 포함되어 있는 경우 이미지의 색상 공간을 결정하고 적절한 압축을 적용하여 PDF 파일 크기를 줄일 수 있습니다.

다음 코드 스니펫은 PDF 내부의 이미지가 컬러인지 흑백인지 식별하는 단계를 보여줍니다.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // PDF 파일의 모든 페이지를 반복합니다.
        for (auto page : document->get_Pages()) {
            // 이미지 배치 흡수기 인스턴스를 생성합니다.
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"Grayscale Image");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"Colored Image");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"Error reading file = {0}", document->get_FileName());
    }
}
```
## 이미지 품질 제어

PDF 파일에 추가되는 이미지의 품질을 제어할 수 있습니다. [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) 클래스의 오버로드된 [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) 메서드를 사용하세요.

다음 코드 스니펫은 모든 문서 이미지를 80% 품질로 압축하는 JPEG로 변환하는 방법을 보여줍니다.

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```