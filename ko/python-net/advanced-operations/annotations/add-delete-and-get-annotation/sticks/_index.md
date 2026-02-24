---
title: Python을 사용한 PDF 스티키 주석
linktitle: 스티키 주석
type: docs
weight: 50
url: /ko/python-net/sticky-annotations/
description: Aspose.PDF를 사용하여 .NET을 통해 Python에서 PDF 문서에 스티키 주석을 추가하는 방법을 알아보고, 댓글 및 피드백을 제공하는 방법을 발견하십시오.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 스티키 주석을 조작하는 방법에 관한 가이드
Abstract: 이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서에서 워터마크 주석을 관리하는 방법에 대한 상세한 가이드를 제공합니다. 문서의 진위성과 브랜딩을 보장하기 위해 워터마크 주석을 추가, 검색 및 삭제하는 과정을 설명합니다. 워터마크 주석은 로고와 같은 그래픽을 페이지의 고정된 크기와 위치에 삽입하는 데 사용할 수 있습니다. 이 가이드에는 조절 가능한 불투명도로 특정 위치에 워터마크 주석을 추가하는 방법과 기존 워터마크 주석을 검색 및 삭제하는 방법을 보여주는 코드 스니펫이 포함되어 있습니다. 코드 예제는 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 프로그래밍 방식으로 조작하는 방법을 보여 주며, 개발자가 애플리케이션에 워터마크 기능을 통합할 수 있는 실용적인 접근 방식을 제공합니다.
---

## 워터마크 주석 추가

가장 눈에 띄고 시각화 및 전송이 쉬운 것은 워터마크 주석입니다. 이는 PDF 문서에 로고나 원본임을 확인시켜 주는 기타 표시를 배치하는 가장 좋은 방법입니다.

워터마크 주석은 인쇄된 페이지의 크기에 관계없이 페이지에 고정된 크기와 위치로 그래픽을 표시하기 위해 사용됩니다.

PDF 페이지의 특정 위치에 워터마크 텍스트를 추가하려면 [워터마크 주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/)을 사용할 수 있습니다. 워터마크의 투명도는 [불투명도](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties) 속성을 사용하여 제어할 수도 있습니다.

다음 코드 스니펫을 확인하여 워터마크 주석을 추가하십시오.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## 워터마크 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## 워터마크 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


