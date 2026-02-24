---
title: .NET을 통한 Python에서 아티팩트 작업
linktitle: 아티팩트 작업
type: docs
weight: 170
url: /ko/python-net/artifacts/
description: Aspose.PDF for Python via .NET은 PDF 페이지에 배경 이미지를 추가하고, Artifact 클래스를 사용하여 각 워터마크를 가져올 수 있습니다.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 아티팩트 추가
Abstract: 이 문서는 PDF 문서에서 아티팩트의 개념과 적용을 살펴보며, 특히 접근성 및 성능 향상에서의 역할에 초점을 맞춥니다. 아티팩트는 장식이나 레이아웃 구성 요소와 같이 문서 의미를 전달하지 않는 비콘텐츠 요소입니다. 본문에서는 Aspose.PDF for Python via .NET 라이브러리의 `Artifact` 클래스를 사용하여 이러한 요소를 관리하는 방법을 강조하며, `custom_type`, `contents`, `opacity`와 같은 속성을 제공하여 상세하게 사용자 정의할 수 있습니다. 또한 특정 아티팩트 유형을 처리하기 위한 관련 클래스들을 소개합니다. 실용적인 예제로 워터마크 가져오기, 배경 이미지 추가, 아티팩트 유형 카운팅, Bates 번호 매기기 등을 시연합니다.
---

PDF에서 아티팩트는 실제 문서 내용에 속하지 않는 그래픽 객체나 기타 요소를 말합니다. 일반적으로 장식, 레이아웃, 배경 용도로 사용됩니다. 아티팩트의 예로는 페이지 헤더, 풋터, 구분선, 의미를 전달하지 않는 이미지 등이 있습니다.

PDF에서 아티팩트의 목적은 콘텐츠와 비콘텐츠 요소를 구분하도록 하는 것입니다. 이는 접근성에 중요하며, 스크린 리더 및 기타 보조 기술이 아티팩트를 무시하고 관련 콘텐츠에 집중할 수 있게 합니다. 또한 아티팩트를 인쇄, 검색, 복사에서 제외함으로써 PDF 문서의 성능과 품질을 향상시킬 수 있습니다.

PDF에서 요소를 아티팩트로 만들려면 [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 클래스를 사용해야 합니다.
다음과 같은 유용한 속성을 포함합니다:

- **custom_type** - 아티팩트 유형의 이름을 가져옵니다. 비표준 유형인 경우 사용할 수 있습니다.
- **custom_subtype** - 아티팩트 하위 유형의 이름을 가져옵니다. 하위 유형이 표준이 아닌 경우 사용할 수 있습니다.
- **type** - 아티팩트 유형을 가져옵니다.
- **subtype** - 아티팩트 하위 유형을 가져옵니다. 아티팩트에 비표준 하위 유형이 있는 경우, 해당 이름은 CustomSubtype을 통해 읽을 수 있습니다.
- **contents** - 아티팩트 내부 연산자의 컬렉션을 가져옵니다.
- **form** - 아티팩트의 XForm을 가져옵니다 (XForm이 사용된 경우).
- **rectangle** - 아티팩트의 사각형을 가져옵니다.
- **position** - 아티팩트 위치를 가져오거나 설정합니다. 이 속성이 지정되면 여백 및 정렬이 무시됩니다.
- **right_margin** - 아티팩트의 오른쪽 여백. 위치가 명시적으로 지정된 경우 (Position 속성) 이 값은 무시됩니다.
- **left_margin** - 아티팩트의 왼쪽 여백. 위치가 명시적으로 지정된 경우 (Position 속성) 이 값은 무시됩니다.
- **top_margin** - 아티팩트의 위쪽 여백. 위치가 명시적으로 지정된 경우 (Position 속성) 이 값은 무시됩니다.
- **bottom_margin** - 아티팩트의 아래쪽 여백. 위치가 명시적으로 지정된 경우 (Position 속성) 이 값은 무시됩니다.
- **artifact_horizontal_alignment** - 아티팩트의 수평 정렬. 위치가 명시적으로 지정된 경우 (Position 속성) 이 값은 무시됩니다.
- **artifact_vertical_alignment** - 아티팩트의 수직 정렬. 위치가 명시적으로 지정된 경우 (Position 속성) 이 값은 무시됩니다.
- **rotation** - 아티팩트 회전 각도를 가져오거나 설정합니다.
- **text** - 아티팩트의 텍스트를 가져옵니다.
- **image** - 아티팩트의 이미지를 가져옵니다 (존재하는 경우).
- **opacity** - 아티팩트의 불투명도를 가져오거나 설정합니다. 가능한 값은 0..1 범위입니다.
- **lines** - 다중 행 텍스트 아티팩트의 라인들.
- **text_state** - 아티팩트 텍스트의 텍스트 상태.
- **is_background** - true인 경우 아티팩트가 페이지 콘텐츠 뒤에 배치됩니다.

다음 클래스들도 아티팩트 작업에 유용할 수 있습니다:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Bates Numbering](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

다음 섹션들을 검토해 주세요:

- [Adding backgrounds](/pdf/python-net/add-backgrounds/) - Python으로 PDF 파일에 배경 이미지를 추가합니다.
- [Adding Bates Numbering](/pdf/python-net/add-bates-numbering/) - PDF에 Bates 번호 매기기를 추가합니다.
- [Adding Watermark](/pdf/python-net/add-watermarks/) - Python으로 PDF에 워터마크를 추가하는 방법.
- [Counting Artifacts](/pdf/python-net/counting-artifacts/) - Python을 사용하여 PDF에서 아티팩트를 카운팅합니다.

