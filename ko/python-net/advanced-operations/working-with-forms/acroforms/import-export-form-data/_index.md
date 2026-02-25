---
title: 양식 데이터 가져오기 및 내보내기
type: docs
weight: 80
url: /ko/python-net/import-export-form-data/
description: 이 섹션에서는 양식 데이터를 가져오고 내보내는 방법을 설명합니다.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET를 사용한 가져오기 및 내보내기 기술.
Abstract: 이 컴파일은 Aspose.PDF for Python via .NET를 사용한 양식 데이터 가져오기 및 내보내기 기술의 포괄적인 모음을 제공합니다. 여기에는 XML, FDF, XFDF, JSON을 포함한 외부 데이터 형식과 PDF 양식을 통합하는 워크플로우가 포함됩니다. 사용자는 구조화된 데이터를 인터랙티브 필드에 가져와 대량 양식 입력을 자동화하거나, 필드 값을 추출하여 분석, 백업 또는 다른 시스템과의 통합에 활용할 수 있습니다. 예제는 PDF 양식을 바인드하고, 형식 간 데이터를 전송하며, 업데이트된 문서를 저장하는 방법을 보여주어 다양한 애플리케이션에서 확장 가능하고 일관된 문서 처리를 가능하게 합니다.
---

## XML 파일에서 양식 데이터 가져오기

다음 예제에서는 Aspose.PDF for Python을 사용해 XML 파일에서 기존 PDF 양식으로 양식 데이터를 가져오는 방법을 보여줍니다. PDF 양식을 바인드하고 XML 데이터를 로드한 뒤 업데이트된 파일을 저장하면 각 페이지를 수동으로 편집하지 않고도 인터랙티브 양식 필드를 빠르게 채울 수 있습니다. 이 방법은 대량 양식 입력을 자동화하고 대규모 데이터세트를 처리하며 여러 문서 간 데이터 일관성을 보장하는 데 이상적입니다.

다음 단계:

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. PDF 양식을 바인드합니다.
1. XML 데이터를 로드합니다.
1. XML을 PDF에 가져옵니다.
1. 업데이트된 PDF를 저장합니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## PDF 문서에서 XML 파일로 양식 필드 데이터 내보내기

Python 라이브러리는 Aspose.PDF for Python을 사용하여 PDF 문서에서 XML 파일로 양식 필드 데이터를 내보내는 방법을 보여줍니다. PDF 양식을 바인드하고 필드 값을 XML 형식으로 저장하면 다른 애플리케이션이나 워크플로우에서 양식 데이터를 쉽게 저장, 처리 또는 재사용할 수 있습니다. 이 방법은 데이터 백업, 분석 및 외부 시스템과의 통합에 이상적입니다.

다음 단계:

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. PDF 양식을 바인드합니다
1. 양식 데이터를 내보냅니다
1. 필드 값을 XML로 저장합니다

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## FDF에서 양식 필드 데이터 가져오기

'import_data_from_fdf' 메서드는 FDF(Forms Data Format) 파일에서 기존 PDF 양식으로 양식 필드 데이터를 가져와 업데이트된 문서를 저장합니다. 이 방법은 문서 구조를 변경하지 않고 프로그래밍 방식으로 PDF 양식을 사전 채우거나 업데이트하는 데 유용합니다.

다음 단계:

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. 입력 PDF를 바인드합니다.
1. import_fdf()를 사용하여 양식 데이터를 가져옵니다.
1. 가져온 데이터를 포함한 PDF를 지정된 출력 파일 경로에 저장합니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## FDF로 양식 필드 데이터 내보내기

이 예제는 Aspose.PDF for Python via .NET를 사용하여 PDF 문서에서 FDF(Forms Data Format) 파일로 양식 데이터를 내보내는 방법을 보여줍니다.

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. PDF 문서를 바인드합니다.
1. export_fdf()를 사용하여 양식 데이터를 내보냅니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## XFDF에서 양식 필드 데이터 가져오기

이 예제는 PDF 문서에서 XFDF(XML Forms Data Format) 파일로 양식 필드 데이터를 내보낸 후, Aspose.PDF for Python via .NET를 사용하여 업데이트된 PDF를 저장합니다.

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. PDF 문서를 양식에 바인드합니다.
1. 양식 데이터를 XFDF 파일로 내보냅니다.
1. 처리된 양식을 저장합니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## XFDF로 양식 필드 데이터 내보내기

이 코드는 PDF 문서에서 양식 필드 데이터를 추출하고 Aspose.PDF for Python을 사용하여 XFDF(XML Forms Data Format) 파일로 내보냅니다.

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. PDF 문서를 양식에 바인드합니다.
1. 양식 데이터를 FDF 파일로 내보냅니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## 다른 PDF에서 데이터 가져오기

이 코드 스니펫은 소스 PDF에서 대상 PDF로 양식 필드 데이터를 전송하는 방법을 보여줍니다. 양식 데이터는 소스 PDF에서 XFDF 스트림으로 내보낸 다음 Aspose.PDF for Python via .NET를 사용하여 대상 PDF에 가져옵니다.

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. PDF 문서를 양식에 바인딩합니다.
1. 소스 PDF에서 양식 데이터를 내보냅니다.
1. 대상 PDF에 양식 데이터를 가져옵니다.
1. 업데이트된 대상 PDF를 저장합니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## 양식 필드를 JSON으로 추출

이 메서드는 입력 파일에서 양식 필드를 추출하고 이를 JSON 파일로 내보냅니다.

1. Aspose.PDF를 사용하여 Form 객체를 생성합니다.
1. FileIO()를 사용해 출력 파일을 쓰기 모드로 엽니다.
1. form.export_json() 메서드를 사용해 양식 필드를 JSON 파일로 내보냅니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## 양식 필드를 JSON 문서로 추출

1. 입력 파일에서 Form 객체를 생성합니다.
1. 양식 필드 데이터를 저장할 빈 딕셔너리를 초기화합니다.
1. 모든 양식 필드를 순회하며 값을 추출합니다.
1. 양식 데이터 딕셔너리를 4칸 들여쓰기된 JSON 문자열로 직렬화합니다.
1. JSON 문자열을 UTF-8 인코딩으로 출력 파일에 씁니다.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

