---
title: 아크로폼 채우기 - 파이썬을 사용하여 PDF 양식 채우기
linktitle: 아크로폼 채우기
type: docs
weight: 20
url: /ko/python-net/fill-form/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서의 AcroForm 필드를 채웁니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF의 양식 필드를 채우는 방법
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에서 AcroForm 필드를 채우는 방법을 설명합니다.이 예제에서는 Form 파사드를 사용하고, 필드 이름을 사전의 새 값에 매핑하고, 일치하는 필드를 업데이트하고, 출력 PDF를 저장합니다.이 방법은 자동화된 문서 완성 워크플로와 대량 양식 처리에 유용합니다.
---

## PDF 문서의 양식 필드 채우기

다음 예제에서는 를 사용하여 기존 PDF 양식의 여러 필드를 채웁니다. [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관.

다음 단계를 사용하십시오.

1. 필드 이름과 값이 포함된 사전을 생성합니다.
1. 입력 PDF를 Form 객체에 바인딩합니다.
1. 사용 가능한 양식 필드를 반복해서 살펴보세요.
1. 사전에 있는 필드를 채웁니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## 관련 주제

- [아크로폼 만들기](/pdf/ko/python-net/create-form/)
- [아크로폼 추출](/pdf/ko/python-net/extract-form/)
- [양식 데이터 가져오기 및 내보내기](/pdf/ko/python-net/import-export-form-data/)