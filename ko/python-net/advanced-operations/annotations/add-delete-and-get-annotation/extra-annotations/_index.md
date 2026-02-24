---
title: Python을 사용한 추가 주석
linktitle: 추가 주석
type: docs
weight: 60
url: /ko/python-net/extra-annotations/
description: Aspose.PDF를 사용하여 Python에서 PDF에 하이라이트나 메모와 같은 추가 주석을 추가하는 방법을 배우고 PDF 콘텐츠를 향상시킵니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 추가 주석을 조작하는 방법 가이드
Abstract: 이 문서는 Python, 특히 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 다양한 유형의 주석을 추가, 검색 및 삭제하는 방법에 대한 포괄적인 가이드를 제공합니다. 여기서는 세 가지 주석 유형인 Caret, Link 및 Redaction을 다룹니다. 문서에서는 Caret 주석이 텍스트 편집 제안에 사용된다고 설명합니다. PDF 파일을 로드하고, 특정 매개변수(예 사각형, 제목, 주제, 플래그 및 색상)를 가진 Caret 주석을 생성한 뒤 문서에 추가하고 변경사항을 저장하는 과정을 설명합니다. Caret 주석을 추가, 검색 및 삭제하기 위한 코드 스니펫이 제공됩니다. Link 주석은 URL이나 문서의 특정 위치로 이동하는 클릭 가능한 영역을 만들 때 사용됩니다. 가이드에는 텍스트 조각(예 전화번호)을 식별하고, 동작을 설정하며, 이러한 주석을 관리하는 방법에 대한 지침과 코드가 포함되어 있습니다.
---

## Python을 사용하여 기존 PDF 파일에 Caret 주석을 추가하는 방법

Caret 주석은 텍스트 편집을 나타내는 기호입니다. Caret 주석은 마크업 주석이기도 하므로 Caret 클래스는 Markup 클래스를 상속받으며, Caret 주석의 속성을 가져오거나 설정하고 주석 외관 흐름을 재설정하는 기능을 제공합니다.
Caret 주석은 텍스트에 대한 변경, 추가 또는 수정 사항을 제안할 때 자주 사용됩니다.

Caret 주석을 만드는 단계:

1. PDF 파일 로드 - new [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새로운 [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/)을 생성하고 Caret 매개변수(새 사각형, 제목, 주제, 플래그, 색상)를 설정합니다. 이 주석은 텍스트 삽입을 나타내는 데 사용됩니다.
1. 페이지에 주석을 추가할 수 있게 되었습니다.

다음 코드 스니펫은 PDF 파일에 Caret 주석을 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### Caret 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 Caret 주석을 가져와 보세요

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Caret 주석 삭제

다음 코드 스니펫은 Python을 사용하여 PDF 파일에서 Caret 주석을 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Aspose.PDF for Python을 사용하여 Redaction 주석으로 특정 페이지 영역 가리기

Aspose.PDF for Python via .NET는 기존 PDF 파일에 주석을 추가하고 조작하는 기능을 지원합니다. PDF 문서의 Redaction 주석은 문서에서 기밀 정보를 영구적으로 제거하거나 숨기는 목적을 가집니다. 정보 편집 과정은 텍스트, 이미지 또는 그래픽과 같은 특정 콘텐츠를 가리거나 색칠하여 다른 사람이 볼 수 없고 접근할 수 없도록 하는 방식으로 이루어집니다. 이를 통해 민감한 정보가 문서 내에서 숨겨지고 보호됩니다. 이러한 요구를 충족시키기 위해 [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/)이라는 클래스가 제공되며, 이를 사용하여 특정 페이지 영역을 가리거나 기존 RedactionAnnotations를 조작하여 가릴 수 있습니다(예: 주석을 평면화하고 그 아래 텍스트를 제거).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### Redaction 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### Redaction 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



