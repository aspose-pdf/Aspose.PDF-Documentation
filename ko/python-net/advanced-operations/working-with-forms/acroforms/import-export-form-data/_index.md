---
title: 양식 데이터 가져오기 및 내보내기
linktitle: 양식 데이터 가져오기 및 내보내기
type: docs
weight: 80
url: /ko/python-net/import-export-form-data/
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 XML, FDF, XFDF 및 JSON 형식의 AcroForm 필드 데이터를 가져오고 내보낼 수 있습니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 기술을 가져오고 내보냅니다.
Abstract: 이 편집본은.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 양식 데이터를 가져오고 내보내는 포괄적인 기술 모음을 제공합니다.PDF 양식을 XML, FDF, XFDF 및 JSON과 같은 외부 데이터 형식과 통합하는 워크플로우를 다룹니다.사용자는 구조화된 데이터를 대화형 필드로 가져와서 대량 양식 채우기를 자동화하거나 분석, 백업 또는 다른 시스템과의 통합을 위해 필드 값을 추출할 수 있습니다.예제에서는 PDF 양식을 바인딩하고, 형식 간에 데이터를 전송하고, 업데이트된 문서를 저장하여 다양한 애플리케이션에서 확장 가능하고 일관된 문서 처리를 가능하게 하는 방법을 보여줍니다.
---

이 페이지에서는 .NET을 통해 Python용 Aspose.PDF 를 사용하여 AcroForm 데이터를 가져오고 내보내는 일반적인 워크플로를 보여줍니다.모든 작업에서는 다음을 사용합니다. [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관.

## XML에서 양식 필드 데이터 가져오기

이 방법을 사용하여 외부 XML 데이터에서 PDF 양식을 채울 수 있습니다.

1. 만들기 `Form` 목적.
1. 입력 PDF를 바인딩합니다.
1. XML 데이터 파일을 엽니다.
1. XML 데이터를 양식으로 가져옵니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## 양식 필드 데이터를 XML로 내보내기

이 메서드는 PDF 문서의 양식 필드 값을 XML로 내보냅니다.

1. 만들기 `Form` 목적.
1. 입력 PDF를 바인딩합니다.
1. XML 출력 파일을 엽니다.
1. 양식 데이터를 XML로 내보냅니다.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## FDF에서 양식 필드 데이터 가져오기

더 `import_data_from_fdf` 메서드는 FDF (양식 데이터 형식) 파일의 양식 필드 데이터를 PDF 양식으로 가져옵니다.

1. 만들기 `Form` 목적.
1. 입력 PDF를 바인딩합니다.
1. 를 사용하여 양식 데이터 가져오기 `import_fdf()`.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## 양식 필드 데이터를 FDF로 내보내기

이 예제에서는 PDF 문서의 양식 데이터를 FDF 파일로 내보냅니다.

1. 만들기 `Form` 목적.
1. PDF 문서를 바인딩합니다.
1. 를 사용하여 양식 데이터 내보내기 `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## XFDF에서 양식 필드 데이터 가져오기

이 방법을 사용하여 XFDF (XML 양식 데이터 형식) 파일의 양식 필드 데이터를 PDF 양식으로 가져올 수 있습니다.

1. 만들기 `Form` 목적.
1. 입력 PDF를 바인딩합니다.
1. XFDF 파일에서 양식 데이터를 가져옵니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## 양식 필드 데이터를 XFDF로 내보내기

이 코드는 PDF 문서의 양식 필드 데이터를 XFDF 파일로 내보냅니다.

1. 만들기 `Form` 목적.
1. 입력 PDF를 바인딩합니다.
1. 양식 데이터를 XFDF로 내보냅니다.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## 다른 PDF에서 데이터 가져오기

이 예제에서는 XFDF를 메모리 내 스트림으로 내보내고 대상 양식으로 가져오는 방식으로 소스 PDF에서 대상 PDF로 양식 필드 데이터를 전송합니다.

1. 소스 및 대상 생성 `Form` 사물.
1. 소스 및 대상 PDF를 바인딩합니다.
1. 소스 PDF에서 양식 데이터를 내보냅니다.
1. 양식 데이터를 대상 PDF로 가져옵니다.
1. 업데이트된 대상 PDF를 저장합니다.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## 양식 필드를 JSON으로 추출

이 메서드는 다음을 사용하여 양식 필드를 JSON 파일로 내보냅니다. `export_json()`.

1. 만들기 `Form` 목적.
1. JSON 출력 파일을 엽니다.
1. 를 사용하여 양식 필드 내보내기 `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## 양식 필드를 JSON 문서로 추출

이 예제에서는 양식 필드 이름과 값에서 사용자 지정 JSON 문서를 만듭니다.

1. 입력 파일에서 Form 객체를 만듭니다.
1. 양식 필드 데이터를 저장하기 위해 빈 사전을 초기화합니다.
1. 모든 양식 필드를 반복하고 값을 추출합니다.
1. 양식 데이터 사전을 4칸 들여쓰기를 사용하여 JSON 문자열로 직렬화합니다.
1. UTF-8 인코딩을 사용하여 JSON 문자열을 출력 파일에 씁니다.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## 관련 주제 (파사드 접근법)

- [XML 데이터 가져오기](/pdf/ko/python-net/import-xml-data/)
- [FDF 데이터 가져오기](/pdf/ko/python-net/import-fdf-data/)
- [XFDF 데이터 가져오기](/pdf/ko/python-net/import-xfdf-data/)
- [JSON 데이터 가져오기](/pdf/ko/python-net/import-json-data/)
- [XML로 내보내기](/pdf/ko/python-net/export-to-xml/)
- [FDF로 내보내기](/pdf/ko/python-net/export-to-fdf/)
- [XFDF로 내보내기](/pdf/ko/python-net/export-to-xfdf/)
- [JSON으로 내보내기](/pdf/ko/python-net/export-to-json/)
