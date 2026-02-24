---
title: Python에서 PDF의 양식 삭제
linktitle: 양식 삭제
type: docs
weight: 70
url: /ko/python-net/remove-form/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 하위 유형/양식을 기반으로 텍스트를 제거합니다. PDF에서 모든 양식을 제거합니다.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET를 사용하여 PDF에서 양식 제거
Abstract: 이 문서는 Aspose.PDF for Python via .NET를 사용하여 PDF 파일에서 양식 요소를 제거하는 두 가지 Python 기반 접근 방식을 제시합니다. 첫 번째 방법은 페이지의 리소스 사전을 액세스하고 양식 컬렉션에서 clear() 메서드를 호출하여 특정 페이지의 모든 양식 객체를 지우는 방법을 보여줍니다. 두 번째 방법은 양식 주석을 반복하면서 타자기 스타일 양식을 식별하고 해당 속성에 따라 선택적으로 삭제하는 보다 목표 지향적인 솔루션을 제공합니다. 두 기술 모두 업데이트된 PDF를 지정된 출력 경로에 저장하는 것으로 마무리되며, 자동화된 워크플로에서 양식 정리 및 문서 정제에 대한 유연한 옵션을 제공합니다.
---

## PDF에서 모든 양식 제거

이 코드는 PDF 문서의 첫 페이지에서 모든 양식 요소를 제거한 다음 수정된 문서를 지정된 출력 경로에 저장합니다.

1. PDF 문서를 로드합니다.
1. 페이지 리소스에 접근합니다.
1. 양식 객체를 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## 지정된 양식 제거

다음 예제는 지정된 PDF 페이지의 양식 객체를 반복하며, 타자기 양식 주석을 식별하고 삭제한 후 Aspose.PDF for Python via .NET를 사용하여 업데이트된 PDF를 저장합니다.

1. PDF 문서를 로드합니다.
1. 페이지 양식에 접근합니다.
1. 양식을 반복합니다.
1. 타자기 양식 여부를 확인합니다.
1. 일치하는 양식을 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
