---
title: Python을 사용한 PDF 텍스트 주석 활용
linktitle: 텍스트 주석
type: docs
weight: 10
url: /ko/python-net/text-annotation/
description: Aspose.PDF for Python을 사용하면 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: PDF에서 텍스트 주석을 조작하는 방법에 대한 가이드
Abstract: 이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 파일 내에서 텍스트 주석을 조작하는 포괄적인 가이드를 제공합니다. 여기에서는 Text, Free Text, StrikeOutAnnotations와 같은 다양한 주석 유형의 추가, 검색 및 삭제에 대해 다룹니다. 텍스트 주석은 PDF의 특정 위치에 첨부된 메모이며, 아이콘으로 표시되어 열면 팝업 창에 텍스트가 나타납니다. Free Text 주석은 페이지에 직접 텍스트를 표시하고, StrikeOutAnnotations는 텍스트에 선을 그어 제거하거나 무시함을 나타냅니다. 이 과정은 `add()` 메서드를 사용하여 페이지의 Annotations 컬렉션에 주석을 추가하는 것을 포함하며, 각 주석 유형에 대한 예제가 제공됩니다. 코드 스니펫은 제목, 주제, 색상 및 플래그와 같은 특정 속성을 가진 주석을 생성하고, PDF 페이지에서 주석을 검색 및 삭제하는 방법을 보여줍니다. 이 가이드는 Aspose.PDF를 사용하여 주석 조작을 통해 PDF 문서를 향상시키고자 하는 개발자에게 실용적인 자료가 됩니다.
---

## 기존 PDF 파일에 텍스트 주석 추가하는 방법

텍스트 주석은 PDF 문서의 특정 위치에 첨부된 주석입니다. 닫힌 상태에서는 아이콘으로 표시되며, 열면 독자가 선택한 글꼴과 크기로 메모 텍스트가 포함된 팝업 창이 표시됩니다.

주석은 특정 페이지의 [주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) 컬렉션에 포함됩니다. 이 컬렉션은 해당 페이지에만 적용되는 주석을 포함하며, 모든 페이지는 자체 주석 컬렉션을 가집니다.

특정 페이지에 주석을 추가하려면, 해당 페이지의 Annotations 컬렉션에 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods) 메서드를 사용하여 추가합니다.

1. 먼저, PDF에 추가하려는 주석을 생성합니다.
1. 그런 다음 입력 PDF를 엽니다.
1. 주석을 'page' 객체의 [주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) 컬렉션에 추가합니다.

다음 코드 스니펫은 PDF 페이지에 주석을 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## PDF 파일에서 텍스트 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## PDF 파일에서 텍스트 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## 새로운 자유 텍스트 주석 추가(또는 생성) 방법

자유 텍스트 주석은 페이지에 직접 텍스트를 표시합니다. [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) 클래스는 이러한 유형의 주석을 생성할 수 있게 합니다. 다음 스니펫에서는 문자열이 처음 등장하는 위치 위에 자유 텍스트 주석을 추가합니다.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## PDF 파일에서 자유 텍스트 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## PDF 파일에서 자유 텍스트 주석 삭제

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### StrikeOutAnnotation을 사용하여 단어에 취소선 적용

Aspose.PDF for Python을 사용하면 PDF 문서에서 주석을 추가, 삭제 및 업데이트할 수 있습니다. 이 중 하나의 클래스는 주석에 취소선을 적용할 수도 있습니다. StrikeOutAnnotation이 PDF에 적용되면 지정된 텍스트에 선이 그어져 해당 텍스트를 제거하거나 무시해야 함을 나타냅니다.

다음 코드 스니펫은 PDF에 [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) 를 추가하는 방법을 보여줍니다.

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


## PDF에서 StrikeOutAnnotation 가져오기

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

## PDF에서 StrikeOutAnnotation 삭제

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



