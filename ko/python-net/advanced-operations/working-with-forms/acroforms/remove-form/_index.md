---
title: 파이썬에서 PDF에서 양식 삭제하기
linktitle: 양식 삭제
type: docs
weight: 70
url: /ko/python-net/remove-form/
description: .NET을 통해 Python용 Aspose.PDF 를 사용하여 전체 정리 및 대상 삭제를 포함하여 PDF 페이지에서 양식 객체를 제거합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF에서 양식 제거
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 양식 요소를 제거하는 두 가지 방법을 제공합니다.첫 번째 방법은 선택한 페이지에서 모든 양식 객체를 지우는 반면, 두 번째 방법은 일치하는 Typewriter 양식 리소스만 제거합니다.이러한 예제는 양식 정리, 템플릿 준비 및 문서 정규화 워크플로에 도움이 됩니다.
---

## 페이지에서 모든 양식 제거

이 코드는 에서 지정한 페이지에서 모든 양식 객체를 제거합니다. `page_num` 업데이트된 문서를 저장합니다.

1. PDF 문서를 로드합니다.
1. 페이지 리소스에 액세스하세요.
1. 클리어 폼 오브젝트.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## 특정 양식 유형 제거

다음 예제에서는 지정된 PDF 페이지의 양식 객체를 반복하여 타자기 양식 주석을 식별하고 삭제한 다음 업데이트된 PDF를.NET을 통해 Python용 Aspose.PDF 를 사용하여 저장합니다.

1. PDF 문서를 로드합니다.
1. 페이지 양식에 액세스합니다.
1. 양식을 반복하세요.
1. 타자기 양식을 확인하세요.
1. 일치하는 양식을 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## 관련 주제

- [아크로폼 만들기](/pdf/ko/python-net/create-form/)
- [아크로폼 채우기](/pdf/ko/python-net/fill-form/)
- [아크로폼 수정](/pdf/ko/python-net/modifying-form/)
- [게시 양식](/pdf/ko/python-net/posting-form/)
