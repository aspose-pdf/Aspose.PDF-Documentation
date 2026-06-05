---
title: Python에서 PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Python에서 PDF를 Excel로 변환하는 방법을 배우세요. 여기에는 XLS, XLSX, CSV, ODS, 단일 워크시트 출력 및 열 처리와 같은 기능이 포함되며 Aspose.PDF를 사용합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 Excel, XLSX, CSV 및 ODS로 변환합니다.
Abstract: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 파일을 스프레드시트 형식으로 변환하는 방법을 보여줍니다. XLS, XLSX, XLSM, CSV 및 ODS 출력에 대해 다루며, 빈 열을 제어하고 생성된 워크시트 수를 줄이는 옵션도 포함합니다.
---

## Python에서 PDF를 Excel로 변환

**Aspose.PDF for Python via .NET**는 Python 코드에서 PDF 파일을 Excel 및 기타 스프레드시트 형식으로 변환하는 것을 지원합니다.

표 추출, 보고서 재사용, 정렬, 필터링 또는 하위 분석을 위해 PDF를 XLS, XLSX, CSV 또는 ODS로 변환해야 할 때 이 페이지를 사용하십시오. PDF를 Excel로 변환하는 동안 개별 PDF 페이지를 Excel 워크시트로 렌더링할 수 있습니다.

첫 번째 예제는 PDF 파일을 Spreadsheet 2003 XML 형식으로 변환합니다. 이후 섹션에서는 XLSX, XLSM, CSV, ODS 및 단일 워크시트 출력이 표시됩니다.

{{% alert color="success" %}}
**PDF를 온라인에서 Excel로 변환해 보세요**

Aspose.PDF가 온라인 애플리케이션을 제공합니다 ["PDF를 XLSX로"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![Aspose.PDF를 사용한 PDF를 Excel로 변환 앱](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

다음 코드 스니펫은 Aspose.PDF for Python via .NET을 사용하여 PDF 파일을 XLS 또는 XLSX 형식으로 변환하는 프로세스를 보여줍니다.

단계: PDF 파일을 Excel (XML Spreadsheet 2003) 형식으로 변환합니다

1. PDF 문서를 로드합니다.
1. Excel 저장 옵션을 사용하여 설정 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 변환된 파일을 저장하십시오.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Python에서 PDF를 XLSX로 변환

단계: PDF 파일을 XLSX 형식(Excel 2007+)으로 변환

1. PDF 문서를 로드합니다.
1. Excel 저장 옵션을 사용하여 설정 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 변환된 파일을 저장하십시오.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 열 제어와 함께 PDF를 XLSX로 변환

PDF를 Excel 형식으로 변환할 때, 출력 파일의 첫 번째 열에 빈 열을 추가할 수 있습니다. Use the `insert_blank_column_at_first` 옵션 `ExcelSaveOptions` 이 동작을 제어하는 클래스입니다. 기본값은 `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 단일 Excel 워크시트로 변환

Aspose.PDF for Python via .NET는 PDF를 Excel (.xlsx) 파일로 변환하는 방법을 보여주며, 'minimize_the_number_of_worksheets' 옵션을 활성화합니다.

단계: Python에서 PDF를 XLS 또는 XLSX 단일 워크시트로 변환하기

1. PDF 문서를 로드합니다.
1. Excel 저장 옵션을 사용하여 설정 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 'minimize_the_number_of_worksheets' 옵션은 PDF 페이지를 결합하여 워크시트 수를 줄임으로써 Excel 시트 수를 감소시킵니다 (예: 가능한 경우 전체 문서에 대해 하나의 워크시트).
1. 변환된 파일을 저장하십시오.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 Excel 2007 매크로 사용 가능 (XLSM)으로 변환

이 Python 예제는 PDF 파일을 XLSM 형식(Excel 매크로 사용 워크북)의 Excel 파일로 변환하는 방법을 보여줍니다.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 다른 스프레드시트 형식으로 변환

### PDF를 CSV로 변환

'convert_pdf_to_excel_2007_csv' 함수는 이전과 동일한 작업을 수행하지만, 이번에는 대상 형식이 XLSM이 아니라 CSV(Comma-Separated Values) 대신 CSV(쉼표로 구분된 값)입니다.

단계: Python에서 PDF를 CSV로 변환

1. 인스턴스를 생성합니다 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 소스 PDF 문서가 있는 객체.
1. 인스턴스를 생성합니다 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 다음과 함께 **ExcelSaveOptions.ExcelFormat.CSV**
1. 호출하여 **CSV** 형식으로 저장합니다 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* 메서드와 전달하기 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 ODS로 변환

단계: Python에서 PDF를 ODS로 변환

1. 인스턴스를 생성합니다 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 소스 PDF 문서가 있는 객체.
1. 인스턴스를 생성합니다 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 와 함께 **ExcelSaveOptions.ExcelFormat.ODS**
1. 호출하여 **ODS** 형식으로 저장합니다 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드와 이를 전달하는 것 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

ODS 형식으로의 변환은 다른 모든 형식과 동일한 방식으로 수행됩니다.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 관련 변환

- [PDF를 Word로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 편집 가능한 텍스트 흐름을 우선으로 하고 스프레드시트 구조보다 중요하게 생각한다면.
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 브라우저에 친화적인 출력이 필요할 때.
- [PDF를 다른 형식으로 변환](/pdf/ko/python-net/convert-pdf-to-other-files/) EPUB, Markdown, 텍스트, XPS 및 관련 내보내기 워크플로에 대해.
