---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: PDF 파일을 최적화하고, 모든 이미지를 축소하며, PDF 크기를 줄이고, 글꼴을 임베드 해제하고, 페이지 콘텐츠 재사용을 활성화하고, 주석을 제거하거나 평면화합니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

무엇보다도, PDF 최적화는 사용자에게 유익합니다. PDF에서 사용자 최적화는 주로 PDF의 크기를 줄여 로딩 속도를 높이는 것입니다. 이것이 가장 일반적인 작업입니다.
PDF를 최적화하기 위해 여러 가지 기술을 사용할 수 있지만, 가장 중요한 것은 다음과 같습니다:

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 글꼴 임베드 해제
- 사용하지 않는 객체 제거
- 양식 필드 평면화 제거
- 주석 제거 또는 평면화

## 웹을 위한 PDF 문서 최적화

PDF 문서의 콘텐츠를 검색 엔진에서 더 나은 순위를 얻도록 최적화해야 할 때, Aspose.PDF for C++는 솔루션을 제공합니다.

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체에서 입력 문서를 엽니다.
1. [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda) 메서드를 사용합니다.
1. Save 메서드를 사용하여 최적화된 문서를 저장합니다.

다음 코드 스니펫은 웹을 위한 PDF 문서를 최적화하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimize PDF Document for the Web
void OptimizeForWeb() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outfilename("OptimizeDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Make some operations (add pages, images, etc) 
    // ...

    // Optimize for web
    document->Optimize();

    // Save output document
    document->Save(_dataDir + outfilename);
}
```

## PDF 크기 줄이기

[OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) 메서드는 불필요한 정보를 제거하여 문서 크기를 줄일 수 있게 해줍니다. 기본적으로, 이 메소드는 다음과 같이 작동합니다:

- 문서 페이지에서 사용되지 않는 리소스가 제거됩니다
- 동일한 리소스가 하나의 객체로 결합됩니다
- 사용되지 않는 객체가 삭제됩니다

아래 코드는 예제입니다. 하지만, 이 메소드는 문서 축소를 보장할 수 없다는 점에 유의하세요.

```cpp
void ReduceSizePDF() {

    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String outfilename("ShrinkDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>();
    // 몇 가지 작업 수행 (페이지 추가, 이미지 등)
    // ...

    // PDF 문서 최적화. 하지만, 이 메소드는 문서 축소를 보장할 수 없다는 점에 유의하세요
    document->OptimizeResources();

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
}
```

## 최적화 전략 관리

최적화 전략을 사용자 정의할 수도 있습니다. 현재 [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) 메서드는 5가지 기술을 사용합니다. 이러한 기술은 [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/) 매개변수를 사용하여 OptimizeResources() 메서드로 적용할 수 있습니다.

### 모든 이미지 축소 또는 압축

PDF 문서의 이미지를 최적화하기 위해 [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization)을 사용합니다. 이미지 최적화 문제를 해결하기 위해 우리는 다음과 같은 옵션을 가지고 있습니다: 이미지 품질을 낮추거나 해상도를 변경합니다. 어쨌든, [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/)를 적용해야 합니다. 다음 예제에서는 [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e)를 50으로 줄여 이미지를 축소합니다.

```cpp
void CompressImage() {
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptions 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // CompressImages 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // ImageQuality 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions); 
    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename);
}
```
이미지를 낮은 해상도로 설정하려면 [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6)를 true로 설정하고 [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e)를 해당 값으로 설정하십시오.

```cpp
void ResizeImagesWithLowerResolution() {
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptions 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // CompressImages 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // ImageQuality 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // ResizeImage 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // MaxResolution 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions);
    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF for C++는 또한 런타임 설정에 대한 제어를 제공합니다. 오늘날 우리는 두 가지 알고리즘 - Standard와 Fast를 사용할 수 있습니다. 실행 시간을 제어하려면 [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4) 속성을 설정해야 합니다.

다음 스니펫은 Fast 알고리즘을 보여줍니다:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptions 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // CompressImages 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // ImageQuality 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // ResizeImage 옵션 설정
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // 이미지 압축 버전을 fast로 설정
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions);
    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### 사용되지 않는 객체 제거

때때로 페이지에서 참조되지 않는 PDF 문서의 일부 사용되지 않는 객체를 제거해야 할 수 있습니다. 예를 들어, 문서 페이지 트리에서 페이지가 제거되지만 페이지 객체 자체는 제거되지 않는 경우가 발생할 수 있습니다. 이러한 객체를 제거해도 문서가 유효하지 않게 되는 것은 아니지만, 오히려 문서 크기가 줄어듭니다. 다음 코드 스니펫을 확인하세요:

```cpp
void RemovingUnusedObject() { 
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 최적화 옵션 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 사용되지 않는 객체 제거 옵션 설정
    optimizationOptions->set_RemoveUnusedObjects(true);

    // 최적화 옵션을 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions);

    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename); 
}
```

### 사용하지 않는 스트림 제거하기

때때로 문서에는 사용하지 않는 리소스 스트림이 포함되어 있습니다. 이러한 스트림은 페이지 리소스 사전에서 참조되기 때문에 "사용하지 않는 객체"가 아닙니다. 따라서 "사용하지 않는 객체 제거" 메서드로 제거되지 않습니다. 하지만 이 스트림은 페이지 내용에서 사용되지 않습니다. 이는 이미지가 페이지에서 제거되었지만 페이지 리소스에서는 제거되지 않았을 때 발생할 수 있습니다. 또한 문서에서 페이지가 추출되고 문서 페이지에 "공통" 리소스, 즉 동일한 Resources 객체가 있을 때 이 상황이 자주 발생합니다. 리소스 스트림이 사용되는지 여부를 확인하기 위해 페이지 내용을 분석합니다. 사용되지 않는 스트림은 제거됩니다. 이는 때때로 문서 크기를 줄일 수 있습니다. 이 기술의 사용은 이전 단계와 유사합니다:

```cpp
void RemovingUnusedStreams() { 
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>();

    // OptimizationOptions 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // RemoveUnusedStreams 옵션 설정
    optimizationOptions->set_RemoveUnusedStreams(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions);

    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename); 
}
```

### 중복 스트림 연결

일부 문서는 여러 중복 리소스 스트림(예: 이미지)을 포함할 수 있습니다. 이는 예를 들어 문서가 자기 자신과 연결되었을 때 발생할 수 있습니다. 출력 문서는 동일한 리소스 스트림의 두 독립적인 복사본을 포함합니다. 우리는 모든 리소스 스트림을 분석하고 비교합니다. 스트림이 중복되면 병합되며, 즉, 한 개의 복사본만 남습니다. 참조는 적절히 변경되고, 객체의 복사본은 제거됩니다. 일부 경우에는 문서의 크기를 줄이는 데 도움이 됩니다.

```cpp
void LinkingDuplicateStreams() { 
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptions 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // LinkDuplicateStreams 옵션 설정
    optimizationOptions->set_LinkDuplcateStreams(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions);

    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename); 
}
```

또한, 우리는 [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8) 설정을 사용할 수 있습니다. 이 속성이 true로 설정되면, 문서를 동일한 페이지로 최적화할 때 페이지 콘텐츠가 재사용됩니다.

```cpp
void AllowReusePageContent() { 
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // OptimizationOptions 초기화
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // AllowReusePageContent 옵션 설정
    optimizationOptions->set_AllowReusePageContent(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    document->OptimizeResources(optimizationOptions);

    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename); 
}
```

### 폰트 임베딩 해제

개인 디자인 파일의 PDF 버전을 만들 때, 필요한 모든 폰트의 복사본이 PDF 파일 자체에 추가됩니다. 이것이 임베딩입니다. 이 PDF가 어디에서 열리든, 당신의 컴퓨터, 친구의 컴퓨터, 혹은 인쇄 제공자의 컴퓨터에서든지, 모든 올바른 폰트가 존재하고 제대로 렌더링됩니다.

그러나 문서가 임베디드 폰트를 사용한다는 것은 모든 폰트 데이터가 문서에 저장된다는 것을 의미합니다. 장점은 사용자의 기기에 폰트가 설치되어 있지 않더라도 문서를 볼 수 있다는 것입니다. 하지만 폰트를 임베딩하면 문서가 커집니다. 폰트 임베딩 해제 방법은 모든 임베디드 폰트를 제거합니다. 따라서 문서 크기는 줄어들지만, 올바른 폰트가 설치되어 있지 않으면 문서 자체가 읽을 수 없게 될 수 있습니다.

```cpp
void UnembedFonts() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set AllowReusePageContent option
    optimizationOptions->set_UnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

최적화 리소스는 이러한 방법을 문서에 적용합니다. 이러한 방법 중 하나라도 적용되면 문서 크기가 줄어들 가능성이 높습니다. 이러한 방법이 전혀 적용되지 않으면 문서 크기는 변하지 않습니다.

## PDF 문서 크기를 줄이는 추가 방법

### 주석 제거 또는 평탄화

PDF 문서에 주석이 있으면 자연스럽게 크기가 증가합니다. 주석이 필요하지 않은 경우 삭제할 수 있습니다. 필요하지만 추가 편집이 필요하지 않은 경우 평탄화할 수 있습니다. 이 두 가지 기술 모두 파일 크기를 줄일 수 있습니다.

```cpp
void FlatteningAnnotation() {
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("OptimizeDocument.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("OptimizeDocument_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 주석 평탄화
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename);
}
```

### 양식 필드 제거

PDF에서 양식을 제거하면 문서를 최적화할 수 있습니다. PDF 문서에 AcroForms가 포함된 경우 양식 필드를 평면화하여 파일 크기를 줄일 수 있습니다.

```cpp
void FlatteningFormFields() {
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("OptimizeFormField.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("OptimizeFormField_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 양식 필드 평면화
    // 양식 평면화
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename);
}
```

### RGB 색상 공간의 PDF를 그레이스케일로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다. You may come across a requirement to convert a PDF from RGB colorspace to grayscale so that it would be faster while printing those PDF files. Also, when the file is converted to grayscale, the document size is reduced too, but it can just as well cause a decrease in the document quality. This feature is currently supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulations. In order to accomplish this requirement, the following code snippet can be used.

PDF 파일을 인쇄할 때 속도를 높이기 위해 RGB 색상 공간을 회색조로 변환해야 할 수도 있습니다. 또한 파일이 회색조로 변환되면 문서 크기도 감소하지만 문서 품질이 저하될 수도 있습니다. 이 기능은 현재 Adobe Acrobat의 사전 비행 기능에서 지원되지만, Office 자동화에 대해 논할 때 Aspose.PDF는 문서 조작을 위한 궁극적인 솔루션입니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용할 수 있습니다.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeDocument.pdf");
    // String for output file name
    String outfilename("Test-gray_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Get instance of particular page inside PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Convert the RGB colorspace image to GrayScale colorspace
        strategy->Convert(page);
    }
    // Save resultant file
    document->Save(_dataDir + outfilename); 
}
```
### FlateDecode 압축

Aspose.PDF for C++는 PDF 최적화 기능을 위한 FlateDecode 압축 지원을 제공합니다. FlateDecode 압축을 사용하여 이미지를 최적화하려면 최적화 옵션을 Flate로 설정합니다. 아래의 코드 스니펫은 **FlateDecode** 압축으로 이미지를 저장하기 위해 최적화 옵션을 사용하는 방법을 보여줍니다:

```cpp
void FlatDecodeCompression() {
 // 경로 이름을 위한 문자열
 String _dataDir("C:\\Samples\\");

 // 입력 파일 이름을 위한 문자열
 String infilename("FlateDecodeCompression.pdf");
 // 출력 파일 이름을 위한 문자열
 String outfilename("FlateDecodeCompression_out.pdf");

 // 문서 열기
 auto document = MakeObject<Document>(_dataDir + infilename);

 // 최적화 옵션 초기화
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // FlateDecode 압축을 사용하여 이미지를 최적화하려면 최적화 옵션을 Flate로 설정
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // 최적화 옵션을 사용하여 PDF 문서 최적화
 document->OptimizeResources(optimizationOptions);

 // 업데이트된 문서 저장
 document->Save(_dataDir + outfilename);
}
```

### **XImageCollection에 이미지 저장하기**

Aspose.PDF for C++는 FlateDecode 압축을 사용하여 새로운 이미지를 [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection)에 저장할 수 있는 기능을 제공합니다. 이 옵션을 활성화하려면 **ImageFilterType.Flate** 플래그를 사용할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

```cpp
void StoreImageInXImageCollection() {

 // 경로 이름에 대한 문자열
 String _dataDir("C:\\Samples\\");

 // 출력 파일 이름에 대한 문자열
 String outfilename("FlateDecodeCompression_out.pdf");

 // 문서 열기
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // 좌표 설정
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // ConcatenateMatrix (행렬 연결) 연산자 사용: 이미지가 어떻게 배치되어야 하는지 정의함
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```