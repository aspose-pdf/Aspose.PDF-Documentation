---
title: 파이썬에서 PDF를 PDF/A, PDF/E 및 PDF/X로 변환
linktitle: PDF를 PDF/A, PDF/E 및 PDF/X로 변환
type: docs
weight: 120
url: /ko/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬에서 PDF 파일을 PDF/A, PDF/E 및 PDF/X로 변환하는 방법을 알아보세요. 보관, 접근성 및 인쇄 워크플로우를 위해 파이썬용 Aspose.PDF
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF를 PDF/x 형식으로 변환하는 방법
Abstract: 이 문서에서는 파이썬용 Aspose.PDF 를 사용하여 PDF를 PDF/A, PDF/E 및 PDF/X 형식으로 변환하는 방법에 대한 포괄적인 가이드를 제공합니다.
---

**PDF를 PDF/x 형식으로 변환한다는 것은 PDF를 추가 형식, 즉 PDF/A, PDF/E 및 PDF/X로 변환할 수 있음을 의미합니다.**

## PDF를 PDF/A로 변환

**파이썬용 Aspose.pdf**를 사용하면 PDF 파일을 파일로 변환할 수 있습니다 <abbr title="Portable Document Format / A">PDF/A</abbr> 규정을 준수하는 PDF 파일입니다.그러기 전에 파일의 유효성을 검사해야 합니다.이 항목에서는 방법을 설명합니다.

{{% alert color="primary" %}}

참고로 우리는 PDF/A 적합성을 검증하기 위해 Adobe 프리플라이트를 따릅니다.시중에 나와 있는 모든 도구에는 PDF/A 적합성에 대한 고유한 “표현”이 있습니다.PDF/A 검증 도구에 대한 이 문서를 참조하시기 바랍니다.PDF와 관련된 모든 것의 중심에 Adobe가 있기 때문에 PDF 파일을 생성하는 방법을 검증하기 위해 Adobe 제품을 선택했습니다. Aspose.PDF

{{% /alert %}}

문서 클래스 Convert 메서드를 사용하여 파일을 변환합니다.PDF를 PDF/A 호환 파일로 변환하기 전에 검증 방법을 사용하여 PDF의 유효성을 검사하십시오.검증 결과는 XML 파일에 저장되고 이 결과도 Convert 메서드로 전달됩니다.ConvertErrorAction 열거를 사용하여 변환할 수 없는 요소에 대한 작업을 지정할 수도 있습니다.

{{% alert color="success" %}}
**PDF를 온라인에서 PDF/A로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 PDF/A-1A로”](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 PDF/A로 변환](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

'document.validate () '메서드는 PDF 파일이 PDF/A-1B 표준 (장기 보관을 위해 설계된 PDF의 ISO 표준 버전) 을 준수하는지 여부를 검증합니다.검증 결과는 로그 파일에 저장됩니다.

### PDF를 PDF/A-1B로 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1B 형식으로 변환하는 방법을 보여줍니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 다음 파라미터를 사용하여 convert 메서드를 호출합니다.
    - 로그 파일 경로 - 변환 프로세스 및 규정 준수 검사의 세부 정보를 저장합니다.
    - 대상 형식 - 'ap.pdfFormat.pdf_a_1b' (아카이브 표준)
    - 오류 조치 - 'ap.ConvertErrorAction.Delete' — 규정 준수를 방해하는 요소를 자동으로 제거합니다.
1. 변환된 PDF/A 호환 파일을 출력 경로에 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### PDF를 PDF 2.0 및 PDF/A-4로 변환

이 예제는 PDF 문서를 새로운 표준 형식 (PDF 2.0 및 PDF/A-4) 으로 변환하는 방법을 보여줍니다.
두 변환 모두 최신 사양 및 아카이브 요구 사항을 준수하는 데 도움이 됩니다.

1. AP.Document를 사용하여 입력 문서를 로드합니다.
1. 다음과 같이 document.convert를 호출하여 PDF 2.0으로 첫 번째 변환을 수행합니다.
    - 변환 세부 정보를 위한 로그 파일 경로
    - 대상 형식 - 'AP.PDFFormat.v_2_0'
    - 오류 조치 - 'ap.ConvertErrorAction.Delete'를 사용하여 규정을 준수하지 않는 요소를 제거합니다.
1. 동일한 방법으로 PDF/A-4로 다시 변환하여 파일이 아카이브 표준을 준수하는지 확인합니다.
1. 결과 문서를 지정된 출력 경로에 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### 포함된 파일을 사용하여 PDF를 PDF/A-3A로 변환

다음 코드 스니펫은 외부 파일을 PDF에 포함한 다음 PDF를 PDF/A-3A 형식으로 변환하는 방법을 보여줍니다. 이 형식은 첨부 파일을 지원하며 콘텐츠가 포함된 장기 보관에 적합합니다.

1. 'AP.Document'를 사용하여 입력 PDF를 로드합니다.
1. 포함할 파일 (예: "aspose-logo.jpg “) 을 가리키는 'FileSpification' 객체를 생성하여 설명과 함께 생성합니다.
1. PDF의 '임베디드_파일' 컬렉션에 파일 사양을 추가합니다.
1. 'document.convert'를 사용하여 문서를 PDF/A-3A로 변환하고 다음을 지정합니다.
    - 로그 파일 경로
    - 대상 형식 - 'ap.pdfFormat.pdf_a_3a'
    - 오류 조치 - 'ap.ConvertErrorAction.Delete'를 사용하여 규정을 준수하지 않는 요소를 제거합니다.
1. 변환된 PDF를 출력 경로에 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### 글꼴 대체를 사용하여 PDF를 PDF/A-1B로 변환

이 함수는 PDF를 PDF/A-1B 형식으로 변환하는 동시에 누락된 글꼴을 사용 가능한 글꼴로 대체하여 처리합니다.이렇게 하면 변환된 PDF가 시각적으로 일관되고 보관 표준을 준수할 수 있습니다.

1. 'AP.Document'를 사용하여 PDF를 로드합니다.
1. 다음을 지정하여 '문서.변환'을 사용하여 PDF를 PDF/A-1B로 변환합니다.
    - 로그 파일 경로
    - 대상 형식 - 'ap.pdfFormat.pdf_a_1b'
    - 오류 조치 - 'ap.ConvertErrorAction.Delete'를 사용하여 규정을 준수하지 않는 요소를 제거합니다.
1. 변환된 PDF를 출력 경로에 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### 자동 태깅을 사용하여 PDF를 PDF/A-1B로 변환

이 기능은 접근성과 구조적 일관성을 위해 내용에 자동으로 태그를 지정하는 동시에 PDF 문서를 PDF/A-1B 형식으로 변환합니다.자동 태깅은 화면 판독기의 문서 유용성을 향상시키고 적절한 의미 구조를 보장합니다.

1. 'AP.Document'를 사용하여 PDF를 로드합니다.
1. 다음을 지정하여 'PDF 형식 변환 옵션'을 생성합니다.
    - 로그 파일 경로
    - 대상 형식 - 'ap.pdfFormat.pdf_a_1b'
    - 오류 조치 - 'ap.ConvertErrorAction.Delete'를 사용하여 규정을 준수하지 않는 요소를 제거합니다.
1. '자동 태깅 설정' 구성:
    - '자동 태깅 활성화 = 참'을 활성화합니다.
    - 표제를 자동으로 감지하도록 '표제_인식_전략 = 자동'을 설정합니다.
1. 자동 태깅 설정을 변환 옵션에 할당합니다.
1. '문서.convert (옵션) '를 사용하여 PDF를 변환합니다.
1. 변환된 PDF를 출력 경로에 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PDF를 PDF/E로 변환

이 코드 스니펫은 PDF 문서를 엔지니어링 및 기술 문서에 맞게 조정된 ISO 표준인 PDF/E-1 형식으로 변환하는 방법을 보여줍니다.이 형식은 엔지니어링 워크플로에 필요한 정확한 레이아웃, 그래픽 및 메타데이터를 보존합니다.

1. 'AP.Document'를 사용하여 소스 PDF를 로드합니다.
1. 다음을 지정하여 'PDF 형식 변환 옵션'을 생성합니다.
    - 전환 문제를 추적하기 위한 로그 파일 경로.
    - 대상 형식 - 'ap.pdfFormat.pdf_e_1'
    - 오류 조치 - 'ap.ConvertErrorAction.Delete'를 사용하여 규정을 준수하지 않는 요소를 제거합니다.
1. '문서.convert (옵션) '를 사용하여 PDF를 변환합니다.
1. 변환된 PDF를 지정된 출력 경로에 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PDF를 PDF/X로 변환

다음 코드 스니펫은 PDF 문서를 인쇄 및 출판 업계에서 일반적으로 사용되는 ISO 표준인 PDF/X-4 형식으로 변환합니다.PDF/X-4는 색상 정확도를 보장하고 투명도를 유지하며 ICC 프로파일을 내장하여 장치 간에 일관된 출력을 제공합니다.

1. 'AP.Document'를 사용하여 소스 PDF를 로드합니다.
1. 다음을 지정하여 'PDF 형식 변환 옵션'을 생성합니다.
    - 로그 파일 경로
    - 대상 형식 - 'ap.pdfFormat.pdf_x_4'
    - 오류 조치 - 'ap.ConvertErrorAction.Delete'를 사용하여 규정을 준수하지 않는 요소를 제거합니다.
1. 'icc_profile_file_name'을 통해 색상 관리를 위한 **ICC 프로필 파일**을 제공합니다.
1. 인쇄 요구 사항으로 조건 식별자 (예: “FOGRA39") 와 함께 **출력 인텐트**를 지정합니다.
1. '문서.convert () '를 사용하여 PDF를 변환합니다.
1. 변환된 PDF를 지정된 출력 경로에 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 관련 전환

- [PDF를 워드로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 표준 검증 후 편집 가능한 콘텐츠 워크플로우용.
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 대상 출력이 표준 기반 PDF가 아닌 웹에서 바로 사용할 수 있는 경우
