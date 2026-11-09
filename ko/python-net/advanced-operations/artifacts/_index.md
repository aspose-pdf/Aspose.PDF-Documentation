---
title: Python에서 PDF 아티팩트 작업하기
linktitle: 아티팩트 작업하기
type: docs
weight: 170
url: /ko/python-net/artifacts/
description: 배경, 워터마크, 머리글, 바닥글 및 베이츠 번호 매기기를 포함한 PDF 아티팩트를 Python에서 추가, 검사 및 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 페이지 아티팩트를 관리하기
Abstract: Aspose.PDF for Python via .NET을 사용하여 PDF 아티팩트를 추가 및 제거하고, 워터마크 세부 정보를 검사하며, 하위 유형별 페이지네이션 아티팩트를 계산하는 가이드를 찾으세요.
---

PDF 아티팩트는 장식용 배경, 연속 머리글 및 바닥글, 워터마크와 같은 페이지 요소를 표시합니다. 태그가 지정된 PDF에서는 보조 기술이 아티팩트를 건너뛰고 문서의 의미 있는 콘텐츠에 집중할 수 있습니다.

## 가이드 선택

### 아티팩트 추가

- [배경 추가](/pdf/ko/python-net/add-backgrounds/)
- [워터마크 추가](/pdf/ko/python-net/add-watermarks/)
- [베이츠 번호 매기기 추가](/pdf/ko/python-net/add-bates-numbering/)
- [헤더 및 푸터 추가](/pdf/ko/python-net/artifacts-header-footer/)

### 아티팩트 검사

- [하위 유형별 페이지 매김 아티팩트 수 세기](/pdf/ko/python-net/counting-artifacts/)
- [워터마크 세부 정보 추출](/pdf/ko/python-net/extract-watermarks/)

### 아티팩트 제거

- [배경 제거](/pdf/ko/python-net/remove-backgrounds/)
- [워터마크 제거](/pdf/ko/python-net/remove-watermarks/)
- [베이츠 번호 매기기 제거](/pdf/ko/python-net/remove-bates-numbering/)
- [머리글 및 바닥글 제거](/pdf/ko/python-net/remove-headers-footers/)

## 아티팩트 API

`artifacts` 속성은 페이지의 [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) 컬렉션을 반환합니다. [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 클래스는 [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/), [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 등에서 공통으로 쓰는 속성을 제공합니다.

| 작업 | 속성 |
| --- | --- |
| 아티팩트를 식별합니다 | 사용 `type` 그리고 `subtype` 표준 분류를 위해 및 `custom_type` 그리고 `custom_subtype` 맞춤 이름에 대해. |
| 내용을 검사합니다 | 사용 `text`, `image`, 그리고 `lines` 텍스트 및 이미지에 대해, 또는 `contents` 그리고 `form` PDF 연산자와 연관된 XForm에 대해. |
| 페이지에 위치시킵니다 | 사용 `rectangle` 경계를 검사하려면. 설정 `position` 명시적인 배치 또는 사용을 위해 `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, 그리고 `artifact_vertical_alignment`. 명시적인 위치는 여백과 정렬을 무시합니다. |
| 모양을 제어합니다 | 사용 `rotation`, `opacity` (0에서 1까지), 그리고 `text_state`. 설정 `is_background` 아티팩트를 페이지 콘텐츠 뒤에 배치하기 위해. |
