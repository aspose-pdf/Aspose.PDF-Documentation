---
title: 아크로폼 추출 - Python에서 PDF에서 양식 데이터 추출
linktitle: 아크로폼 추출
type: docs
weight: 30
url: /ko/python-net/extract-form/
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서의 AcroForm 필드에서 값을 추출합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 양식 데이터를 가져오는 방법
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 AcroForm 필드에서 데이터를 추출하는 방법을 보여줍니다.이 예제에서는 양식 필드 이름을 반복하고, Form 파사드를 사용하여 값을 읽고, 다운스트림 처리를 위한 사전을 반환합니다.이 워크플로는 보고, 검증 및 외부 시스템과의 통합에 유용합니다.
---

## 양식에서 데이터 추출

### PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 읽으려면 양식 필드 이름을 반복하고 에서 각 값을 검색하십시오. [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관.

다음 단계를 사용하십시오.

1. 입력 PDF를 a에 바인딩합니다. `Form` 목적.
1. 반복 실행 `field_names`.
1. 각 값을 다음과 같이 읽습니다. `get_field()`.
1. 값을 딕셔너리에 저장합니다.
1. 추출된 값을 반환하거나 처리합니다.

다음 Python 코드 스니펫은 이 접근 방식을 보여줍니다.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## 관련 주제

- [아크로폼 만들기](/pdf/ko/python-net/create-form/)
- [아크로폼 채우기](/pdf/ko/python-net/fill-form/)
- [양식 데이터 가져오기 및 내보내기](/pdf/ko/python-net/import-export-form-data/)
- [아크로폼 수정](/pdf/ko/python-net/modifying-form/)