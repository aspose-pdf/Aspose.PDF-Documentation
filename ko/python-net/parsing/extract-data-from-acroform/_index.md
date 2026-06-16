---
title: 파이썬을 사용하여 AcroForm에서 데이터 추출
linktitle: 아크로폼에서 데이터 추출
type: docs
weight: 50
url: /ko/python-net/extract-data-from-acroform/
description: Aspose.PDF 파일을 사용하면 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있습니다.AcroForms에서 데이터를 추출하여 JSON, XML 또는 FDF 형식으로 저장하는 방법을 알아보십시오.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 통해 AcroForm에서 데이터를 추출하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서 내의 양식 필드를 관리하는 방법에 대한 포괄적인 가이드를 제공합니다.PDF에서 양식 데이터를 추출, 조작 및 내보내는 다양한 방법을 자세히 설명합니다.이 글은 먼저 양식 필드 값을 추출하여 사전에 저장한 후 데이터를 JSON 형식으로 출력하는 방법을 보여 줍니다.또한 양식 데이터를 JSON 파일로 직접 내보내 데이터 직렬화 기능을 향상시키는 방법을 설명합니다.또한 이 문서에서는 양식 데이터를 XML, FDF (Forms Data Format), XFDF와 같은 다른 형식으로 내보내는 방법을 다룹니다. 이러한 형식은 데이터 교환 및 구조화된 데이터 저장에 유용합니다.각 섹션에는 이해 및 구현에 도움이 되는 Python 코드 스니펫이 포함되어 있습니다.전반적으로 이 문서는 PDF 양식 처리를 Python 응용 프로그램에 통합하려는 개발자에게 실용적인 리소스 역할을 합니다.
---

## PDF 문서에서 양식 필드 추출

[양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 에서 `aspose.pdf.facades` 네임스페이스는 전체 문서 개체 모델을 열지 않고도 AcroForm 필드 데이터를 읽을 수 있는 간단한 방법을 제공합니다.반복해 보세요. `form.field_names` 양식에 있는 모든 필드 이름을 가져오려면 다음을 호출하십시오. `form.get_field(name)` 현재 값을 검색합니다.

1. a를 구성하세요 `Form` 입력 파일 경로를 전달하여 객체를 생성합니다.
1. 이터레이션 오버 `form.field_names` 모든 필드 이름을 열거합니다.
1. 전화 `form.get_field(name)` 각 이름에 대해 결과를 사전에 저장합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## 제목별로 양식 필드 값 검색

PDF 양식에 정의된 정확한 필드 이름 (제목) 을 알고 있으면 다음을 사용하여 해당 값을 직접 검색할 수 있습니다. `form.get_field(name)` 전체 필드 컬렉션을 반복하지 않아도 됩니다.이는 특정 필드만 필요한 경우 가장 빠른 접근 방식입니다.

1. a를 구성하세요 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 입력 파일 경로를 가진 객체
1. 전화 `form.get_field("FieldName")` PDF에 표시된 것과 동일한 필드 제목을 사용합니다.
1. 애플리케이션에서 필요에 따라 반환된 문자열 값을 사용합니다.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## PDF 문서에서 JSON으로 양식 필드 추출

AcroForm 데이터를 JSON으로 내보내는 두 가지 방법이 있습니다.첫 번째 방법은 내장 기능을 사용합니다. `export_json` 메서드 온 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form)한 번의 호출로 모든 필드 데이터를 파일 스트림으로 직접 직렬화합니다.

1. a를 구성하세요 `Form` 입력 파일 경로를 가진 객체
1. 를 사용하여 출력 파일을 바이너리 스트림으로 엽니다. `FileIO`.
1. 전화 `form.export_json(stream, True)` JSON 출력을 작성하기 위해서입니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

두 번째 방법은 다음과 같은 방법으로 Python 사전을 작성합니다. `field_names` 과 `get_field`를 사용하여 직렬화합니다. `json.dumps`.데이터를 쓰기 전에 데이터를 변환하거나 필터링해야 할 때 사용하십시오.

1. 이터레이션 오버 `form.field_names` 그리고 필드 값으로 딕셔너리를 채웁니다.
1. 를 사용하여 사전을 직렬화합니다. `json.dumps(form_data, indent=4)`.
1. 결과 JSON 문자열을 출력 파일에 씁니다.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## PDF 파일에서 데이터를 XML로 추출

XML 내보내기는 구조화된 XML 피드 또는 스키마를 사용하는 시스템과 PDF 양식 데이터를 통합하는 데 유용합니다. [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 클래스는 제공합니다 `export_xml` 변환을 한 번에 처리합니다.

1. 만들기 `Form` PDF를 인스턴스화하고 바인딩합니다. `form.bind_pdf(path)`.
1. 출력 파일을 바이너리 스트림으로 엽니다.
1. 전화 `form.export_xml(stream)` 모든 필드 데이터를 XML로 작성합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## PDF 파일에서 FDF로 데이터 내보내기

FDF (양식 데이터 형식) 는 AcroForm 데이터의 표준 교환 형식이며 PDF 뷰어 및 처리 도구에서 널리 지원됩니다.사용 `export_fdf` 에 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 원본 PDF나 다른 호환 양식으로 다시 가져올 수 있는 독립 실행형 FDF 파일을 생성하기 위한 클래스입니다.

1. 만들기 `Form` 소스 PDF를 인스턴스화하고 바인딩합니다. `form.bind_pdf(path)`.
1. 출력 파일을 바이너리 스트림으로 엽니다.
1. 전화 `form.export_fdf(stream)` FDF 데이터를 기록합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## PDF 파일에서 XFDF로 데이터 내보내기

XFDF (XML 양식 데이터 형식) 는 FDF의 XML 기반 후속 버전이며 웹 서비스 및 최신 데이터 파이프라인에서 사용하기에 더 적합합니다.FDF와 마찬가지로 XFDF 파일도 호환되는 PDF 양식으로 다시 가져올 수 있습니다.사용 `export_xfdf` 에 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 출력을 생성할 클래스입니다.

1. 만들기 `Form` 소스 PDF를 인스턴스화하고 바인딩합니다. `form.bind_pdf(path)`.
1. 출력 파일을 바이너리 스트림으로 엽니다.
1. 전화 `form.export_xfdf(stream)` XFDF 데이터를 기록합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```
