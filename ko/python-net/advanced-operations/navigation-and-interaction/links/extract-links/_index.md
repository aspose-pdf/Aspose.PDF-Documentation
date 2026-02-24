---
title: Python을 사용하여 PDF 파일에서 링크 추출
linktitle: 링크 추출
type: docs
weight: 30
url: /ko/python-net/extract-links/
description: Aspose.PDF를 사용한 콘텐츠 관리 및 링크 분석을 위해 Python으로 PDF 문서에서 하이퍼링크를 추출하는 방법을 알아보세요.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 링크를 추출하는 방법
Abstract: Aspose.PDF for Python via .NET 링크 추출 가이드는 Python을 사용하여 PDF 문서에서 하이퍼링크 주석을 프로그래밍 방식으로 가져오는 방법을 설명합니다. 문서에는 실용적인 코드 예제가 포함되어 있으며, 이 기능을 링크 감사, 탐색 분석 또는 인터랙티브 문서 기능 구축과 같은 작업에 어떻게 활용할 수 있는지 강조합니다. 단일 페이지 PDF를 다루든 대량 배치를 처리하든, 이 가이드는 하이퍼링크 추출에 대한 명확하고 효율적인 접근 방식을 제공합니다.
---

## PDF 파일에서 링크 추출

이 예제는 Aspose.PDF for Python을 사용하여 PDF 첫 페이지의 모든 링크 주석을 반복하는 방법을 보여줍니다. 주석을 필터링하여 LinkAnnotation 타입을 식별하고, 안전하게 형변환한 뒤 페이지 인덱스와 페이지상의 사각형 위치를 출력합니다.

이는 PDF의 기존 링크 주석을 디버깅, 분석 또는 자동 업데이트하는 데 사용할 수 있습니다.

1. PDF 문서를 로드합니다. ap.Document(path_infile)를 사용하여 파일을 엽니다.
1. 첫 페이지의 주석에 접근합니다. document.pages[1].annotations를 사용하여 모든 주석을 가져옵니다.
1. LinkAnnotation 유형만 필터링합니다. 각 주석의 annotation_type을 확인합니다.
1. LinkAnnotation을 형변환하고 처리합니다. is_assignable()와 cast()를 사용하여 LinkAnnotation 속성에 안전하게 접근합니다.
1. 주석 상세 정보를 출력합니다. 각 링크의 페이지 인덱스와 사각형(위치)를 출력합니다.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## PDF 파일에서 하이퍼링크 추출

이 코드는 Aspose.PDF for Python을 사용하여 PDF 문서 첫 페이지에서 모든 LinkAnnotation 객체를 추출하고, GoToURIAction을 포함하는 링크를 식별하는 방법을 보여줍니다. 해당 링크마다 페이지 인덱스와 대상 URI를 출력합니다.

다음과 같은 작업에 유용합니다:

- PDF에서 외부 링크 감사
- 문서 또는 지원 URL 추출
- 깨지거나 오래된 하이퍼링크 감지

1. PDF 문서를 로드합니다. ap.Document를 사용하여 파일을 엽니다.
1. 첫 페이지에서 모든 링크 주석을 가져옵니다. AnnotationType.LINK 타입인 주석만 포함하도록 필터링합니다.
1. 타입을 확인하고 LinkAnnotation으로 형변환합니다. 각 주석이 실제로 LinkAnnotation인지 확인한 후 속성에 접근합니다.
1. 링크의 액션 타입을 확인합니다. GoToURIAction(웹 URL로 연결되는 링크)을 사용하는 링크만 필터링합니다.
1. URI와 페이지 인덱스를 추출하고 출력합니다. .uri를 사용해 외부 링크를 얻고 .page_index를 사용해 컨텍스트를 확인합니다.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
