---
title: AcroForm 추출 - Python에서 PDF의 양식 데이터 추출
linktitle: AcroForm 추출
type: docs
weight: 30
url: /ko/python-net/extract-form/
description: Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서에서 양식을 추출합니다. PDF 파일의 개별 필드에서 값을 가져옵니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 양식 데이터를 가져오는 방법
Abstract: 이 문서는 Python을 사용하여 PDF 문서 내의 양식 필드에서 데이터를 추출하는 방법을 안내합니다. Aspose.PDF 라이브러리를 이용해 `Form` 컬렉션에 접근하고 `Field` 유형 및 그 `value` 속성을 활용하여 모든 필드를 탐색하는 방법을 설명합니다. 샘플 Python 코드 조각이 포함되어 있으며, PDF 문서를 열고 양식 필드를 반복하면서 각 필드의 이름과 값을 출력하는 예시를 보여줍니다. 이 방법은 PDF 파일에서 양식 데이터를 프로그래밍 방식으로 가져오는 데 유용합니다.
---

## 양식에서 데이터 추출

### PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 가져오려면 모든 양식 필드를 탐색한 다음 Value 속성을 사용하여 값을 받아야 합니다. Form 컬렉션에서 각 필드를 가져오는데, 기본 필드 유형은 [필드](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/)이며 해당 [값](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) 속성에 접근합니다.

다음 Python 코드 스니펫은 PDF 문서에서 모든 필드의 값을 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

