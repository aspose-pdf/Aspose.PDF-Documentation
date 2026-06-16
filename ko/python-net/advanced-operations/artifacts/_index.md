---
title: 파이썬에서 PDF 아티팩트로 작업하기
linktitle: 아티팩트 다루기
type: docs
weight: 170
url: /ko/python-net/artifacts/
description: .NET을 통해 Aspose.PDF for Python을 사용하여 Python에서 PDF 아티팩트를 사용하여 배경, 워터마크 및 베이츠 넘버링을 추가하고 아티팩트 유형을 계산하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 배경, 워터마크 및 Bates 넘버링 아티팩트 추가
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 에서 PDF 아티팩트를 사용하는 방법을 설명합니다.아티팩트가 무엇인지, 아티팩트가 접근성과 문서 레이아웃에 중요한 이유, Python을 사용하여 배경 이미지를 추가하고, 워터마크를 적용하고, Bates 넘버링을 추가하고, PDF 파일에서 아티팩트 유형을 검사하는 방법을 알아봅니다.
---

PDF의 아티팩트는 문서의 실제 내용에 포함되지 않는 그래픽스 객체 또는 기타 요소입니다.일반적으로 장식, 레이아웃 또는 배경용으로 사용됩니다.아티팩트의 예로는 페이지 머리글, 바닥글, 구분자 또는 의미를 전달하지 않는 이미지가 있습니다.

PDF에서 아티팩트의 목적은 내용 요소와 비 내용 요소를 구분할 수 있도록 하는 것입니다.화면 판독기 및 기타 보조 기술은 아티팩트를 무시하고 관련 콘텐츠에 초점을 맞출 수 있으므로 접근성 측면에서 매우 중요합니다.또한 아티팩트는 인쇄, 검색 또는 복사에서 생략될 수 있으므로 PDF 문서의 성능과 품질을 향상시킬 수 있습니다.

문서 배경, 페이지 워터마크, 베이츠 넘버링 마크와 같이 내용이 아닌 PDF 요소를 Python에서 만들거나 검사해야 할 때 이 섹션을 사용하십시오.다음 가이드는.NET을 통해 파이썬용 Aspose.PDF 에서 지원하는 주요 아티팩트 워크플로를 보여줍니다.

요소를 PDF에서 아티팩트로 만들려면 다음을 사용해야 합니다. [아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 수업.
여기에는 다음과 같은 유용한 속성이 포함되어 있습니다.

- **사용자 정의_유형** - 아티팩트 유형의 이름을 가져옵니다.아티팩트 유형이 표준이 아닌 경우 사용할 수 있습니다.
- **사용자 정의_하위 유형** - 아티팩트 하위 유형의 이름을 가져옵니다.아티팩트 하위 유형이 표준 하위 유형이 아닌 경우 사용할 수 있습니다.
- **type** - 아티팩트 유형을 가져옵니다.
- **하위 유형** - 아티팩트 하위 유형을 가져옵니다.아티팩트에 비표준 하위 유형이 있는 경우 CustomSubType을 통해 하위 유형의 이름을 읽을 수 있습니다.
- **contents** - 아티팩트 내부 연산자 컬렉션을 가져옵니다.
- **form** - 아티팩트의 XForm을 가져옵니다 (XForm을 사용하는 경우).
- **사각형** - 아티팩트의 사각형을 가져옵니다.
- **위치** - 아티팩트 위치를 가져오거나 설정합니다.이 속성을 지정하면 여백과 정렬이 무시됩니다.
- **right_margin** - 아티팩트의 오른쪽 여백. 위치 속성에서 위치를 명시적으로 지정한 경우 이 값은 무시됩니다.
- **left_margin** - 아티팩트의 왼쪽 여백. 위치 속성에서 위치를 명시적으로 지정한 경우 이 값은 무시됩니다.
- **상단_여백** - 아티팩트의 상단 여백.위치를 명시적으로 지정한 경우 (위치 속성에서) 이 값은 무시됩니다.
- **bottom_margin** - 아티팩트의 아래쪽 여백. 위치 속성에서 위치를 명시적으로 지정한 경우 이 값은 무시됩니다.
- **아티팩트_수평_정렬** - 아티팩트의 수평 정렬.위치를 명시적으로 지정한 경우 (위치 속성에서) 이 값은 무시됩니다.
- **아티팩트_수직_정렬** - 아티팩트의 수직 정렬.위치를 명시적으로 지정한 경우 (위치 속성에서) 이 값은 무시됩니다.
- **rotation** - 아티팩트 회전 각도를 가져오거나 설정합니다.
- **text** - 아티팩트의 텍스트를 가져옵니다.
- **image** - 아티팩트의 이미지를 가져옵니다 (있는 경우).
- **불투명도** - 아티팩트의 불투명도를 가져오거나 설정합니다.가능한 값의 범위는 0.0.1입니다.
- **lines** - 여러 줄 텍스트 아티팩트의 줄.
- **텍스트_상태** - 아티팩트 텍스트의 텍스트 상태입니다.
- **is_background** - 실제 아티팩트가 페이지 콘텐츠 뒤에 배치되는 경우

다음 클래스는 아티팩트 작업에도 유용할 수 있습니다.

- [아티팩트 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [배경 아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [헤더 아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [푸터 아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [워터마크 아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [베이츠 아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## 이 섹션에서 다루는 아티팩트 워크플로

이 문서의 다음 섹션을 검토하십시오.

- [배경 추가](/pdf/ko/python-net/add-backgrounds/) - Python을 사용하여 PDF 파일에 배경 이미지를 추가합니다.
- [베이츠 넘버링 추가](/pdf/ko/python-net/add-bates-numbering/) - PDF에 베이츠 넘버링 추가
- [워터마크 추가](/pdf/ko/python-net/add-watermarks/) - Python으로 PDF에 워터마크를 추가하는 방법.
- [아티팩트 계산](/pdf/ko/python-net/counting-artifacts/) - Python을 사용하여 PDF에서 아티팩트를 계산합니다.
- [PDF 머리글 및 바닥글 관리](/pdf/ko/python-net/artifacts-header-footer/) - PDF 문서의 머리말과 꼬리말을 관리합니다.

이 자습서는 기본 문서 콘텐츠 스트림을 변경하지 않고 장식적이거나 구조적인 PDF 요소를 관리해야 할 때 유용합니다.
