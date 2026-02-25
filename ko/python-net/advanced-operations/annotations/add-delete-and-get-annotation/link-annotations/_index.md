---
title: PDF에서 링크 주석 사용
linktitle: 링크 주석
type: docs
weight: 70
url: /ko/python-net/link-annotations/
description: Aspose.PDF for Python via .NET는 PDF 문서에서 링크 주석을 추가, 가져오기 및 삭제할 수 있게 해줍니다.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## 기존 PDF 파일에 링크 주석 추가

[Links](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)은 클릭하면 URL을 열거나 동일 문서 또는 외부 문서의 특정 위치로 이동하는 주석입니다.

링크 주석은 페이지 어디에든 배치할 수 있는 사각형 영역입니다. 각 링크에는 해당하는 PDF 동작이 연결되어 있습니다. 사용자가 이 링크 영역을 클릭하면 해당 동작이 수행됩니다.

다음 코드 스니펫은 전화번호 예제를 사용하여 PDF 파일에 링크 주석을 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### 링크 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)을 가져와 보세요.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### 링크 주석 삭제

다음 코드 스니펫은 PDF 파일에서 링크 주석을 삭제하는 방법을 보여줍니다. 이를 위해 첫 페이지에 있는 모든 링크 주석을 찾고 제거해야 합니다. 그런 다음 제거된 주석이 포함된 문서를 저장합니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
