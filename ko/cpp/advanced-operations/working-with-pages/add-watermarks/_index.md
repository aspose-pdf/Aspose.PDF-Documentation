---
title: PDF에 워터마크 추가하기 C++ 사용
linktitle: 워터마크 추가
type: docs
weight: 90
url: ko/cpp/add-watermarks/
description: 이 문서에서는 C++를 사용하여 프로그래밍적으로 PDF에서 아티팩트를 작업하고 워터마크를 얻는 기능을 설명합니다.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

워터마크는 일반적으로 문서나 이미지를 만든 사람을 식별하기 위해 로고나 인장을 포함하는 반투명 이미지입니다.

**Aspose.PDF for C++**는 Artifact 클래스를 사용하여 PDF 문서에 워터마크를 추가할 수 있습니다. 작업을 해결하기 위해 이 기사를 확인하십시오.

Adobe Acrobat으로 생성된 워터마크는 아티팩트(14.8.2.2 PDF 사양의 실제 콘텐츠와 아티팩트에 설명됨)라고 합니다. 아티팩트와 작업하기 위해 Aspose.PDF는 [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact)와 [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection)의 두 가지 클래스를 제공합니다.

특정 페이지의 모든 아티팩트를 얻기 위해 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스는 Artifacts 속성을 가지고 있습니다. 이 주제는 PDF 파일에서 아티팩트를 다루는 방법을 설명합니다.

## 아티팩트 작업하기

[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) 클래스는 다음과 같은 속성을 포함합니다:

**Artifact.Type** – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거형의 값으로 Background, Layout, Page, Pagination 및 Undefined를 포함합니다).
**Artifact.Subtype** – 아티팩트 서브타입을 가져옵니다 (Artifact.ArtifactSubtype 열거형의 값으로 Background, Footer, Header, Undefined, Watermark를 포함합니다).

{{% alert color="primary" %}}

Adobe Acrobat으로 생성된 워터마크는 Pagination 유형과 Watermark 서브타입을 가집니다.

{{% /alert %}}

**Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
**Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용되는 경우). 워터마크, 헤더 및 푸터 아티팩트에는 모든 아티팩트 내용을 보여주는 XForm이 포함되어 있습니다.

**Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 존재하지 않으면 null).**Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.  
**Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.  
**Artifact.Rotation** – 아티팩트의 회전(도 단위, 양수 값은 반시계 방향 회전을 나타냄)을 가져옵니다.  
**Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0…1 범위에 있으며, 1은 완전히 불투명함을 나타냅니다.

## 프로그래밍 샘플: PDF 파일에 워터마크 추가하는 방법

다음 코드 스니펫은 C++를 사용하여 PDF 파일의 첫 페이지에 각 워터마크를 가져오는 방법을 보여줍니다.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```