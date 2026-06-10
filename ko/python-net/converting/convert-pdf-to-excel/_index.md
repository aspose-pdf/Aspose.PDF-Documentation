---
title: 파이썬에서 PDF를 엑셀로 변환
linktitle: PDF를 엑셀로 변환
type: docs
weight: 20
url: /ko/python-net/convert-pdf-to-excel/
lastmod: "2026-06-10"
description: XLS, XLSX, CSV, ODS, 단일 워크시트 출력 및 Aspose.PDF 기반 열 처리를 포함하여 Python에서 PDF를 Excel로 변환하는 방법을 알아봅니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF를 엑셀, XLSX, CSV 및 ODS로 변환
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 파일을 스프레드시트 형식으로 변환하는 방법을 보여줍니다.XLS, XLSX, XLSM, CSV 및 ODS 출력 외에도 빈 열을 제어하고 생성된 워크시트 수를 줄이기 위한 옵션을 다룹니다.
---

## 파이썬에서 PDF를 엑셀로 변환

**.NET을 통한 파이썬용 Aspose.pdf**는 PDF 파일을 파이썬 코드에서 엑셀 및 기타 스프레드시트 형식으로 변환하는 기능을 지원합니다.

테이블 추출, 보고서 재사용, 정렬, 필터링 또는 다운스트림 분석을 위해 PDF를 XLS, XLSX, CSV 또는 ODS로 변환해야 하는 경우 이 페이지를 사용하십시오.PDF를 Excel로 변환하는 동안 개별 PDF 페이지를 Excel 워크시트로 렌더링할 수 있습니다.

첫 번째 예에서는 PDF 파일을 스프레드시트 2003 XML 형식으로 변환합니다.이후 섹션에서는 XLSX, XLSM, CSV, ODS 및 단일 워크시트 출력을 보여 줍니다.

{{% alert color="success" %}}
**온라인에서 PDF를 엑셀로 변환해 보세요**

Aspose.PDF 는 온라인 신청서를 제공합니다. [“PDF를 XLSX로”](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 엑셀로 변환](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

다음 코드 스니펫은.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 파일을 XLS 또는 XLSX 형식으로 변환하는 프로세스를 보여줍니다.

단계: PDF 파일을 엑셀 (XML 스프레드시트 2003) 형식으로 변환

1. PDF 문서를 로드합니다.
1. 다음을 사용하여 Excel 저장 옵션을 설정합니다. [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 변환된 파일을 저장합니다.

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

## 파이썬에서 PDF를 XLSX로 변환

단계: PDF 파일을 XLSX 형식으로 변환 (엑셀 2007+)

1. PDF 문서를 로드합니다.
1. 다음을 사용하여 Excel 저장 옵션을 설정합니다. [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 변환된 파일을 저장합니다.

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

## 열 제어를 사용하여 PDF를 XLSX로 변환

PDF를 Excel 형식으로 변환할 때 출력 파일의 첫 번째 열로 빈 열을 추가할 수 있습니다.다음을 사용하십시오. `insert_blank_column_at_first` 의 옵션 `ExcelSaveOptions` 이 동작을 제어하는 클래스입니다.기본값은 `true`.

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

.NET을 통한 파이썬용 Aspose.PDF 파일은 'minimize_the_number_of_workshets' 옵션을 활성화한 상태에서 PDF를 엑셀 (.xlsx) 파일로 변환하는 방법을 보여줍니다.

단계: 파이썬에서 PDF를 XLS 또는 XLSX 단일 워크 시트로 변환

1. PDF 문서를 로드합니다.
1. 다음을 사용하여 Excel 저장 옵션을 설정합니다. [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 'minimize_the_number_of_workshets' 옵션은 PDF 페이지를 더 적은 수의 워크시트로 결합하여 Excel 시트 수를 줄입니다 (예: 가능한 경우 전체 문서에 대해 워크시트 하나).
1. 변환된 파일을 저장합니다.

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

## PDF를 엑셀 2007 매크로 지원 (XLSM) 으로 변환

이 파이썬 예제는 PDF 파일을 XLSM 형식의 Excel 파일 (Excel 매크로 지원 통합 문서) 로 변환하는 방법을 보여줍니다.

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

'convert_pdf_to_excel_2007_csv' 함수는 이전과 동일한 작업을 수행하지만 이번에는 대상 형식이 XLSM이 아닌 CSV (쉼표로 구분된 값) 입니다.

단계: 파이썬에서 PDF를 CSV로 변환

1. 의 인스턴스 생성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 원본 PDF 문서가 있는 개체입니다.
1. 의 인스턴스 생성 [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) **엑셀 저장 옵션 포함. 엑셀 포맷.csv**
1. 전화하여**CSV** 형식으로 저장 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* 메서드 및 전달 [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

단계: 파이썬에서 PDF를 ODS로 변환

1. 의 인스턴스 생성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 원본 PDF 문서가 있는 개체입니다.
1. 의 인스턴스 생성 [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) **엑셀 저장 옵션 포함. 엑셀 포맷.ods**
1. 전화하여**ODS** 형식으로 저장 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드 및 전달 [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

## 관련 전환

- [PDF를 워드로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 우선 순위가 스프레드시트 구조가 아닌 편집 가능한 텍스트 흐름인 경우
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 브라우저 친화적인 출력이 필요할 때
- [PDF를 다른 형식으로 변환](/pdf/ko/python-net/convert-pdf-to-other-files/) EPUB, 마크다운, 텍스트, XPS 및 관련 내보내기 워크플로우에 적합합니다.
