---
title: C++에서 아티팩트 작업하기
linktitle: 아티팩트 작업하기
type: docs
weight: 110
url: ko/cpp/artifacts/
description: 이 페이지는 Aspose.PDF for C++를 사용하여 Artifact 클래스를 작업하는 방법을 설명합니다. 코드 스니펫은 PDF 페이지에 배경 이미지를 추가하는 방법과 PDF 파일의 첫 페이지에 있는 각 워터마크를 얻는 방법을 보여줍니다.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF에서 워터마크를 얻는 방법?

**PDF에서 아티팩트란 무엇입니까?**

PDF / UA ISO 참조에 따르면, 중요하지 않거나 배경에 나타나지 않는 콘텐츠는 관련 정보를 포함하지 않으며, 보조 기술이 이를 무시할 수 있도록 아티팩트로 플래그 지정되어야 합니다.
아티팩트를 생성할 프로그램에서 식별할 수 없는 경우, Aspose.PDF for C++를 사용하여 수동으로 수행해야 합니다.

[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) 클래스는 다음과 같은 속성을 포함합니다:

- **Artifact.Type** – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거의 값을 지원하며, 이 값에는 Background, Layout, Page, Pagination 및 Undefined가 포함됩니다).
- **Artifact.Subtype** – 아티팩트 하위 유형을 가져옵니다 (값에는 Background, Footer, Header, Undefined, Watermark가 포함된 Artifact.ArtifactSubtype 열거형의 값을 지원합니다).

{{% alert color="primary" %}}

Adobe Acrobat으로 생성된 워터마크는 Pagination 유형과 Watermark 하위 유형을 가집니다.

{{% /alert %}}

- **Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
- **Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용되는 경우). 워터마크, 헤더 및 푸터 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.
- **Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 있는 경우, 그렇지 않으면 null).
- **Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.
- **Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.
- **Artifact.Rotation** – 아티팩트의 회전을 가져옵니다 (도 단위, 양수 값은 반시계 방향 회전을 나타냅니다).
- **Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다. 값의 범위는 0...1이며, 1은 완전히 불투명합니다.

PDF 파일에서 아티팩트를 다루는 예로 워터마크를 살펴보겠습니다.

Adobe Acrobat 지원을 통해 생성된 워터마크는 아티팩트로 간주됩니다 (14.8.2.2 Present Content and PDF Specification Artifacts에 설명되어 있음). 아티팩트를 다루기 위해 Aspose.PDF에는 두 개의 클래스가 포함되어 있습니다:
[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) 및 [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

특정 페이지의 모든 아티팩트를 가져오기 위해 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스에는 Artifacts 속성이 있습니다. 이 주제에서는 PDF 파일에서 워터마크 아티팩트를 다루는 방법을 보여줍니다.

다음 코드 스니펫은 C++를 사용하여 PDF 파일의 첫 번째 페이지에서 각 워터마크를 얻는 방법을 보여줍니다:
배경 이미지는 PDF 문서에 워터마크 또는 독점 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for C++는 [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) 클래스를 사용하여 페이지 객체에 배경 이미지를 추가합니다.

다음 코드 스니펫은 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto pdfDocument = MakeObject<Document>();

    // 문서 객체에 페이지 추가
    auto page = pdfDocument->get_Pages()->Add();

    // Background Artifact 객체 생성
    auto background = MakeObject<BackgroundArtifact>();

    // BackgroundArtifact 객체에 대한 이미지 지정
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // 페이지의 artifacts 컬렉션에 BackgroundArtifact 추가
    page->get_Artifacts()->Add(background);

    // 수정된 PDF 저장
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### 프로그래밍 샘플: 워터마크 가져오기

다음 코드 스니펫은 PDF 파일의 첫 번째 페이지에서 각 워터마크를 가져오는 방법을 보여줍니다.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // 아티팩트의 하위 유형, 텍스트 및 위치 반복 및 가져오기
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### 프로그래밍 샘플: 특정 유형의 아티팩트 개수 세기

특정 유형의 아티팩트 총 수를 계산하려면(예: 워터마크 총 수) 다음 코드를 사용하십시오.

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // 아티팩트 유형이 워터마크인 경우 카운터 증가
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"Page contains {0} watermarks", count);
}
```