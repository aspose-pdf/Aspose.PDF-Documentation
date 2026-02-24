---
title: Python을 사용하여 AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: /ko/python-net/extract-data-from-acroform/
description: Aspose.PDF를 사용하면 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있습니다. AcroForm에서 데이터를 추출하고 이를 JSON, XML 또는 FDF 형식으로 저장하는 방법을 알아보세요.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 AcroForm에서 데이터 추출하는 방법
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF 문서 내의 양식 필드를 관리하는 포괄적인 가이드를 제공합니다. PDF에서 양식 데이터를 추출, 조작 및 내보내는 다양한 방법을 상세히 설명합니다. 본문은 양식 필드 값을 추출하여 사전(dictionary)에 저장하고, 이를 JSON 형식으로 출력하는 방법을 보여줍니다. 또한 양식 데이터를 직접 JSON 파일로 내보내는 방법을 설명하여 데이터 직렬화 기능을 강화합니다. 추가로 XML, FDF(Forms Data Format), XFDF와 같은 다른 형식으로 양식 데이터를 내보내는 방법을 다루며, 이는 데이터 교환 및 구조화된 데이터 저장에 유용합니다. 각 섹션에는 이해와 구현을 돕는 Python 코드 스니펫이 포함되어 있습니다. 전반적으로 이 문서는 PDF 양식 처리를 Python 애플리케이션에 통합하려는 개발자에게 실용적인 자료가 됩니다.
---

## PDF 문서에서 양식 필드 추출

양식 필드를 생성하고 채우는 기능을 제공할 뿐만 아니라, Aspose.PDF for Python은 PDF 파일에서 양식 필드 데이터 또는 양식 필드 정보를 손쉽게 추출할 수 있게 합니다.

이 코드 스니펫은 PDF 양식의 모든 필드 값을 저장할 사전을 생성합니다. 양식의 필드 이름을 순회하며 값을 가져와 사전에 채웁니다. 마지막으로 수집된 양식 값을 출력합니다.

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

## 제목으로 양식 필드 값 가져오기

## PDF 문서에서 양식 필드를 JSON으로 추출

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

제공된 Python 코드 스니펫은 필드 값을 추출하고 이를 JSON 형식으로 직렬화합니다. 필요한 모듈을 임포트하고, 입력 및 출력 파일 경로를 구성한 뒤, PDF 양식에서 필드 이름과 값을 가져와 직렬화된 JSON 문자열을 지정된 출력 파일에 기록합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## PDF 파일에서 XML로 데이터 추출

다음 Python 코드 스니펫은 폼 객체를 생성하고 PDF 문서를 해당 객체에 연결한 뒤, 폼 데이터를 XML 파일로 내보냅니다. 이 코드는 PDF 양식에서 데이터를 자동으로 추출하여 구조화된 XML 형식으로 저장합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

다음 코드 스니펫은 폼 객체를 생성하고 PDF 문서를 해당 폼에 연결한 뒤, 폼 데이터를 FDF(Forms Data Format) 파일로 내보냅니다. FDF 파일은 PDF 문서에서 폼 데이터를 저장하는 형식으로, 데이터 교환을 용이하게 해줍니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

