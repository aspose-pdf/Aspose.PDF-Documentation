---
title: Python을 사용하여 PDF의 링크 업데이트
linktitle: 링크 업데이트
type: docs
weight: 20
url: /ko/python-net/update-links/
description: PDF의 링크를 프로그래밍 방식으로 업데이트합니다. 이 가이드는 Python 언어로 PDF의 링크를 업데이트하는 방법에 대해 설명합니다.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 링크 업데이트하는 방법
Abstract: Aspose.PDF for Python via .NET의 링크 업데이트 가이드는 개발자가 Python을 사용하여 PDF 문서 내 하이퍼링크 동작을 수정하는 과정을 단계별로 안내합니다. 이 가이드는 링크 목적지를 특정 페이지, 외부 웹사이트, 또는 다른 PDF 파일로 지정하는 방법을 설명합니다. 또한 텍스트 색상 등 링크 주석의 외관을 조정하는 방법을 다루며 각 시나리오에 대한 실용적인 코드 예제를 제공합니다. 오래된 URL을 수정하거나 탐색성을 향상시키려는 경우에도, 이 자료는 프로그래밍 방식으로 링크를 관리하는 명확하고 효율적인 접근 방식을 제시합니다.
---

## LinkAnnotation 텍스트 색상 업데이트

이 예제는 Aspose.PDF for Python을 사용하여 PDF 첫 페이지에 있는 모든 링크 주석을 감지한 다음, 각 링크 근처의 텍스트 색상을 빨간색으로 변경하여 강조하는 방법을 보여줍니다. 이는 각 링크 사각형 주위에 약간 확장된 영역을 지정하여 텍스트를 찾고 수정하기 위해 TextFragmentAbsorber를 활용합니다.

다음과 같이 사용할 수 있습니다:

- 문서 내의 링크를 시각적으로 표시
- 연결된 콘텐츠를 강조하여 접근성 향상
- 검토 또는 내보내기 전에 PDF 파일을 사전 처리

각 링크 주석에 대해 스크립트는 해당 사각형 경계를 가져와 주변 텍스트를 포함하도록 약간 확장합니다. 이렇게 확장된 영역에 TextFragmentAbsorber를 적용하여 해당 영역 내의 텍스트 조각을 추출하고, 추출된 조각의 폰트 색상을 빨간색으로 변경합니다. 이를 통해 주변 텍스트가 강조 표시되어 검토 시 시각적으로 식별하기 쉬워집니다. 모든 업데이트가 적용된 후 수정된 문서는 출력 경로에 저장되어 강조된 주석과 관련 텍스트가 보존됩니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## 테두리 업데이트

스크립트는 문서의 첫 페이지에 집중하고 모든 주석을 필터링한 뒤 LINK 유형인 주석만 선택합니다—이들은 일반적으로 하이퍼링크나 내비게이션 트리거와 같은 인터랙티브 요소를 나타냅니다. 각 링크 주석에 대해 코드는 이를 LinkAnnotation 유형으로 캐스팅하고 색상 속성을 빨간색으로 업데이트하여 다른 콘텐츠와 구분되도록 시각적으로 강조합니다. 모든 링크 주석이 수정된 후 업데이트된 문서는 정의된 출력 위치에 저장되어 새로운 스타일링이 유지됩니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## 웹 목적지 업데이트

경로가 설정되면 Aspose.PDF 라이브러리를 사용하여 원본 문서를 로드하고 내용에 접근할 수 있게 됩니다. 스크립트는 문서의 첫 페이지에 집중해 모든 주석을 필터링하고, 링크 유형인 주석만 선택합니다—이는 클릭 가능한 영역이나 하이퍼링크를 나타냅니다. 타입 오류를 방지하고 안전하게 처리하기 위해 각 주석은 is_assignable로 검사된 뒤 적절한 LinkAnnotation 유형으로 캐스팅됩니다. 해당 링크가 GoToURIAction과 연결되어 웹 주소를 가리키는 경우, 스크립트는 해당 URI를 "https://www.google.com"으로 업데이트하여 사용자를 리디렉션합니다. 마지막으로 모든 원하는 변경이 적용된 후 수정된 문서는 지정된 출력 경로에 저장됩니다.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
