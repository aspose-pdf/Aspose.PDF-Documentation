---
title: Python을 사용한 PDF 하이라이트 주석
linktitle: 하이라이트 주석
type: docs
weight: 20
url: /ko/python-net/highlights-annotation/
description: Python에서 Aspose.PDF를 사용하여 텍스트 강조를 위해 PDF 파일에 하이라이트 주석을 추가하는 방법을 배우세요.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 하이라이트 주석을 조작하는 방법에 대한 안내
Abstract: 이 문서는 PDF 문서에서 텍스트 마크업 주석을 사용하는 방법에 대한 포괄적인 안내를 제공하며, Python용 Aspose.PDF 라이브러리가 제공하는 기능에 초점을 맞춥니다. 여기서는 하이라이트, 언더라인, 스트라이크아웃, 스퀴글리 주석 등 다양한 유형의 주석의 목적과 사용 방법을 설명하며, 각각은 텍스트를 강조하거나 다양한 방식으로 수정하도록 설계되었습니다. 문서에서는 PDF에 이러한 주석을 추가하기 위한 단계—문서 로드, 제목 및 색상과 같은 특정 매개변수로 주석 생성, 원하는 페이지에 주석을 추가—를 개략적으로 설명합니다. 또한, PDF에서 주석을 검색하는 코드 스니펫을 포함하여 사용자가 유형에 따라 주석 세부 정보를 필터링하고 출력할 수 있도록 합니다. 마지막으로, 주석 삭제 과정을 상세히 다루며, 문서에서 각 텍스트 마크업 주석 유형을 제거하는 코드 예제를 제공합니다. 이 가이드는 Python을 사용하여 프로그래밍 방식으로 PDF 파일의 텍스트 주석을 조작하려는 개발자에게 실용적인 리소스로 활용됩니다.
---

PDF의 텍스트 마크업 주석은 텍스트를 하이라이트하거나, 밑줄을 긋거나, 건너뛰거나, 메모를 추가하는 데 사용됩니다. 이러한 주석은 텍스트의 특정 부분을 강조하거나 주의를 끌기 위해 설계되었습니다. 사용자는 PDF 파일의 내용을 시각적으로 표시하거나 수정할 수 있습니다.

하이라이트 주석은 텍스트에 일반적으로 노란색 배경 색으로 표시하여 중요하거나 관련성이 있음을 나타냅니다.

밑줄 주석은 선택된 텍스트 아래에 선을 배치하여 중요성, 강조 또는 제안된 수정 사항을 나타냅니다.

스트라이크아웃 주석은 특정 텍스트를 취소선으로 표시하여 삭제되었거나, 교체되었거나, 더 이상 유효하지 않음을 나타냅니다.

스퀴글리 선은 텍스트 아래에 물결선 형태의 밑줄을 적용하여 철자 오류, 잠재적 문제, 제안된 변경 사항 등을 표시하는 데 사용됩니다.

## 텍스트 마크업 주석 추가

PDF 문서에 텍스트 마크업 주석을 추가하려면 다음 작업을 수행해야 합니다.

1. PDF 파일을 로드합니다 - 새 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체.
1. 주석을 생성합니다:
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) 및 매개변수(제목, 색상)를 설정합니다.
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) 및 매개변수(제목, 색상)를 설정합니다.
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) 및 매개변수(제목, 색상)를 설정합니다.
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) 및 매개변수(제목, 색상)를 설정합니다.
1. 그 후 모든 주석을 페이지에 추가해야 합니다.

### 하이라이트 주석 추가

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### 스트라이크아웃 주석 추가

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### 스퀴글리 주석 추가

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### 밑줄 주석 추가

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## 텍스트 마크업 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 텍스트 마크업 주석을 가져와 보세요.

### 하이라이트 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### 스트라이크아웃 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```


### 스퀴글리 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### 밑줄 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## 텍스트 마크업 주석 삭제

다음 코드 스니펫은 PDF 파일에서 텍스트 마크업 주석을 삭제하는 방법을 보여줍니다.

### 하이라이트 주석 삭제

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### 스트라이크아웃 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 스퀴글리 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 밑줄 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



