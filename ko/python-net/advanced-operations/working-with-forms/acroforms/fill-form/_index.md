---
title: AcroForm 채우기 - Python을 사용한 PDF 양식 채우기
linktitle: AcroForm 채우기
type: docs
weight: 20
url: /ko/python-net/fill-form/
description: Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서의 양식을 채울 수 있습니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 양식 필드를 채우는 방법
Abstract: 이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서에서 양식 필드를 채우는 방법에 대한 가이드를 제공합니다. 문서의 양식 컬렉션에서 양식 필드를 가져와 해당 필드의 value 속성을 통해 값을 설정하는 과정을 설명합니다. 예제 코드는 PDF 문서를 열고, 양식 필드를 반복하면서 부분 이름(예 \"Field 1\")으로 특정 필드를 찾아 TextBoxField의 값을 \"777\"로 수정하는 방법을 보여줍니다. 마지막으로 업데이트된 문서를 출력 파일에 저장합니다. 관련 Aspose 문서에 대한 링크가 추가 참고용으로 제공됩니다.
---

## PDF 문서에서 양식 필드 채우기

다음 예제는 Aspose.PDF for Python via .NET를 사용하여 PDF 양식 필드를 새로운 값으로 채우고 업데이트된 문서를 저장합니다. 필드 이름과 값을 사전으로 지정하여 여러 필드를 업데이트하는 것을 지원합니다.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```



