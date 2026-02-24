---
title: Python에서 PDF를 PDF/x 포맷으로 변환하기
linktitle: PDF를 PDF/x 포맷으로 변환하기
type: docs
weight: 120
url: /ko/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: 이 주제에서는 Aspose.PDF for Python via .NET를 사용하여 PDF를 PDF/x 포맷으로 변환하는 방법을 보여줍니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF를 PDF/x 포맷으로 변환하는 방법
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF를 PDF/A, PDF/E 및 PDF/X 포맷으로 변환하는 포괄적인 가이드를 제공합니다.
---

**PDF to PDF/x 포맷은 PDF를 추가 포맷인 PDF/A, PDF/E 및 PDF/X로 변환할 수 있는 기능을 의미합니다.**

## PDF를 PDF/A로 변환하기

**Aspose.PDF for Python**은 PDF 파일을 <abbr title="Portable Document Format / A">PDF/A</abbr> 규격을 준수하는 PDF 파일로 변환할 수 있게 해줍니다. 그 전에 파일을 검증해야 합니다. 이 주제에서는 방법을 설명합니다.

{{% alert color="primary" %}}

Adobe Preflight를 사용하여 PDF/A 적합성을 검증한다는 점에 유의하십시오. 시장에 있는 모든 도구는 PDF/A 적합성에 대한 자체 “표현”을 가지고 있습니다. 참고용으로 PDF/A 검증 도구에 관한 이 문서를 확인하십시오. 우리는 Adobe가 PDF와 관련된 모든 것의 중심에 있기 때문에 Aspose.PDF가 PDF 파일을 생성하는 방식을 확인하기 위해 Adobe 제품을 선택했습니다.

{{% /alert %}}

Document 클래스의 Convert 메서드를 사용하여 파일을 변환합니다. PDF를 PDF/A 규격에 맞는 파일로 변환하기 전에 Validate 메서드를 사용하여 PDF를 검증합니다. 검증 결과는 XML 파일에 저장되며 이 결과는 Convert 메서드에도 전달됩니다. 또한 ConvertErrorAction 열거형을 사용하여 변환할 수 없는 요소에 대한 동작을 지정할 수 있습니다.

{{% alert color="success" %}}
**온라인에서 PDF를 PDF/A로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)을 제공하며, 기능과 품질을 살펴볼 수 있습니다.

[![Aspose.PDF 변환 PDF to PDF/A 무료 앱](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

'document.validate()' 메서드는 PDF 파일이 PDF/A-1B 표준(장기 보존을 위해 설계된 ISO 표준 PDF 버전)에 부합하는지 검증합니다. 검증 결과는 로그 파일에 저장됩니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 대상 준수 수준(ap.PdfFormat.PDF_A_1B)으로 validate 메서드를 호출합니다.
1. 검증 결과가 지정된 로그 파일에 기록됩니다.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### PDF를 PDF/A-1B로 변환하기

다음 코드 스니펫은 PDF 파일을 PDF/A-1B 포맷으로 변환하는 방법을 보여줍니다:

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 다음 매개변수를 사용하여 convert 메서드를 호출합니다:
- 로그 파일 경로 - 변환 과정 및 준수 검사 세부 정보를 저장합니다.
- 대상 포맷 - 'ap.PdfFormat.PDF_A_1B' (보관 표준).
- 오류 처리 - 'ap.ConvertErrorAction.DELETE' — 자동으로 준수를 방해하는 요소를 제거합니다.
1. 변환된 PDF/A 준수 파일을 출력 경로에 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### PDF를 PDF 2.0 및 PDF/A-4로 변환하기

이 예제는 PDF 문서를 최신 표준 포맷인 PDF 2.0 및 PDF/A-4로 변환하는 방법을 보여줍니다.
두 변환 모두 최신 사양 및 보관 요구 사항을 충족하도록 돕습니다.

1. ap.Document를 사용하여 입력 문서를 로드합니다.
1. document.convert를 호출하여 PDF 2.0으로 첫 번째 변환을 수행합니다:
- 변환 세부 정보를 위한 로그 파일 경로.
- 대상 포맷 - 'ap.PdfFormat.V_2_0'.
- 오류 처리 - 'ap.ConvertErrorAction.DELETE'를 사용하여 비준수 요소를 제거합니다.
1. 같은 방법으로 PDF/A-4로 두 번째 변환을 수행하여 파일이 보관 표준에도 부합하도록 합니다.
1. 결과 문서를 지정된 출력 경로에 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### PDF를 PDF/A-3A(첨부 파일 포함)로 변환하기

다음 코드 스니펫은 외부 파일을 PDF에 포함시키고, 이후 PDF를 첨부 파일을 지원하고 임베디드 콘텐츠와 함께 장기 보관에 적합한 PDF/A-3A 포맷으로 변환하는 방법을 보여줍니다.

1. 'ap.Document'를 사용하여 입력 PDF를 로드합니다.
1. 파일을 포함하기 위해 파일을 가리키는 'FileSpecification' 객체를 생성하고(예: "aspose-logo.jpg"), 설명을 지정합니다.
1. 파일 사양을 PDF의 'embedded_files' 컬렉션에 추가합니다.
1. 'document.convert'를 사용하여 문서를 PDF/A-3A로 변환하고, 다음을 지정합니다:
- 로그 파일 경로.
- 대상 형식 - 'ap.PdfFormat.PDF_A_3A'.
- 오류 동작 - 'ap.ConvertErrorAction.DELETE' (규격에 맞지 않는 요소를 제거).
1. 변환된 PDF를 출력 경로에 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### 폰트 대체를 사용한 PDF를 PDF/A-1B로 변환

이 함수는 누락된 폰트를 사용 가능한 폰트로 대체하면서 PDF를 PDF/A-1B 형식으로 변환합니다. 이를 통해 변환된 PDF가 시각적으로 일관성을 유지하고 보존 표준을 준수하도록 합니다.

1. 'ap.Document'를 사용하여 PDF를 로드합니다.
1. 'document.convert'를 사용하여 PDF를 PDF/A-1B로 변환하고, 다음을 지정합니다:
- 로그 파일 경로.
- 대상 형식 - 'ap.PdfFormat.PDF_A_1B'.
- 오류 동작 - 'ap.ConvertErrorAction.DELETE' (규격에 맞지 않는 요소를 제거).
1. 변환된 PDF를 출력 경로에 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### 자동 태깅을 사용한 PDF를 PDF/A-1B로 변환

이 함수는 PDF 문서를 PDF/A-1B 형식으로 변환하면서 접근성과 구조적 일관성을 위해 콘텐츠에 자동으로 태그를 지정합니다. 자동 태깅은 스크린 리더의 문서 사용성을 향상시키고 적절한 의미 구조를 보장합니다.

1. 'ap.Document'를 사용하여 PDF를 로드합니다.
1. 'PdfFormatConversionOptions'를 생성하고 다음을 지정합니다:
- 로그 파일 경로.
- 대상 형식 - 'ap.PdfFormat.PDF_A_1B'.
- 오류 동작 - 'ap.ConvertErrorAction.DELETE' (규격에 맞지 않는 요소를 제거).
1. 'AutoTaggingSettings'를 구성합니다:
- 'enable_auto_tagging = True'를 활성화합니다.
- 'heading_recognition_strategy = AUTO'를 설정하여 헤딩을 자동으로 감지합니다.
1. 자동 태깅 설정을 변환 옵션에 할당합니다.
1. 'document.convert(options)'를 사용하여 PDF를 변환합니다.
1. 변환된 PDF를 출력 경로에 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## PDF를 PDF/E로 변환

이 스니펫은 PDF 문서가 엔지니어링 및 기술 문서를 위해 맞춤화된 ISO 표준인 PDF/E-1을 준수하는지 검증합니다. 검증 결과는 로그 파일에 저장됩니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. validate 메서드를 호출하고 다음을 지정합니다:
- 검증 결과를 저장할 로그 파일 경로.
- 대상 형식 - 'ap.PdfFormat.PDF_E_1'.
1. 검증 결과가 로그 파일에 저장되어 검토할 수 있습니다.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

다음 예제는 엔지니어링 및 기술 문서를 위해 맞춤화된 ISO 표준인 PDF/E-1 형식으로 PDF를 변환하는 방법을 보여줍니다. 이 형식은 엔지니어링 워크플로에 필요한 정확한 레이아웃, 그래픽 및 메타데이터를 보존합니다.

1. 'ap.Document'를 사용하여 원본 PDF를 로드합니다.
1. 'PdfFormatConversionOptions'를 생성하고 다음을 지정합니다:
- 변환 문제를 추적하기 위한 로그 파일 경로.
- 대상 형식 - 'ap.PdfFormat.PDF_E_1'.
- 오류 동작 - 'ap.ConvertErrorAction.DELETE' (규격에 맞지 않는 요소를 제거).
1. 'document.convert(options)'를 사용하여 PDF를 변환합니다.
1. 변환된 PDF를 지정된 출력 경로에 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## PDF를 PDF/X로 변환

다음 코드 스니펫은 인쇄 및 출판 업계에서 일반적으로 사용되는 ISO 표준인 PDF/X-4 형식으로 PDF 문서를 변환합니다. PDF/X-4는 색 정확성을 보장하고 투명성을 유지하며, 장치 간 일관된 출출을 위해 ICC 프로파일을 포함합니다.

1. 'ap.Document'를 사용하여 원본 PDF를 로드합니다.
1. 'PdfFormatConversionOptions'를 생성하고 지정합니다:
- 로그 파일 경로.
- 대상 형식 - 'ap.PdfFormat.PDF_X_4'.
- 오류 동작 - 'ap.ConvertErrorAction.DELETE'를 사용하여 비준수 요소를 제거합니다.
1. 'icc_profile_file_name'을 통해 색 관리용 **ICC 프로파일 파일**을 제공합니다.
1. 인쇄 요구 사항을 위해 조건 식별자(예: "FOGRA39")가 포함된 **OutputIntent**를 지정합니다.
1. 'document.convert()'를 사용하여 PDF를 변환합니다.
1. 변환된 PDF를 지정된 출력 경로에 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
