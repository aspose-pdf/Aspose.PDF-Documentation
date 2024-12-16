---
title: Python에서 PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: Aspose.PDF for Python 라이브러리를 사용하여 Python으로 PDF를 Excel 형식으로 변환할 수 있습니다. 이러한 형식에는 XLS, XLSX, XML 2003 스프레드시트, CSV, ODS가 포함됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서는 **Python을 사용하여 PDF를 Excel 형식으로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **XLS**

- [Python PDF에서 XLS로](#python-pdf-to-xls)
- [Python PDF를 XLS로 변환](#python-pdf-to-xls)
- [Python PDF 파일을 XLS로 변환하는 방법](#python-pdf-to-xls)

_형식_: **XLSX**

- [Python PDF에서 XLSX로](#python-pdf-to-xlsx)
- [Python PDF를 XLSX로 변환](#python-pdf-to-xlsx)
- [Python PDF 파일을 XLSX로 변환하는 방법](#python-pdf-to-xlsx)

_형식_: **Excel**

- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF to Excel XLS](#python-pdf-to-xls)
- [Python PDF to Excel XLSX](#python-pdf-to-xlsx)

_형식_: **CSV**

- [Python PDF to CSV](#python-pdf-to-csv)
- [Python Convert PDF to CSV](#python-pdf-to-csv)
- [Python How to convert PDF file to CSV](#python-pdf-to-csv)

_형식_: **ODS**

- [Python PDF to ODS](#python-pdf-to-ods)
- [Python Convert PDF to ODS](#python-pdf-to-ods)
- [Python How to convert PDF file to ODS](#python-pdf-to-ods)

## Python을 통한 PDF에서 EXCEL로의 변환

**Aspose.PDF for Python via .NET**은 PDF 파일을 Excel 및 CSV 형식으로 변환하는 기능을 지원합니다.

Aspose.PDF for Python via .NET은 PDF 조작 구성 요소로, PDF 파일을 Excel 워크북(XLSX 파일)으로 렌더링하는 기능을 도입했습니다. 이 변환 과정에서는 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.

{{% alert color="success" %}}
**온라인으로 PDF를 Excel로 변환해보세요**

Aspose.PDF는 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)라는 온라인 무료 애플리케이션을 제공하여 기능 및 품질을 조사할 수 있습니다.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

다음 코드 스니펫은 Aspose.PDF for Python via .NET을 사용하여 PDF 파일을 XLS 또는 XLSX 형식으로 변환하는 프로세스를 보여줍니다.

<a name="python-pdf-to-xls"><strong>단계: Python에서 PDF를 XLS로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 만듭니다.
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)의 인스턴스를 만듭니다.
3. [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)를 전달하여 **.xls 확장자**를 지정하여 **XLS** 형식으로 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # 파일을 MS Excel 형식으로 저장
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>단계: Python에서 PDF를 XLSX로 변환</strong></a>

1. 원본 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 만듭니다.
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)의 인스턴스를 만듭니다.
3. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)을 전달하여 **.xlsx 확장자**를 지정하여 **XLSX** 형식으로 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # 파일을 MS Excel 형식으로 저장
    document.save(output_pdf, save_option)
```

## 열 제어로 PDF를 XLS로 변환

PDF를 XLS 형식으로 변환할 때 출력 파일의 첫 번째 열로 빈 열이 추가됩니다.
 'ExcelSaveOptions 클래스'의 InsertBlankColumnAtFirst 옵션은 이 열을 제어하는 데 사용됩니다. 기본값은 true입니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # 파일을 MS Excel 형식으로 저장
    document.save(output_pdf, save_option)
```

## PDF를 단일 Excel 워크시트로 변환

페이지가 많은 PDF 파일을 XLS로 내보낼 때 각 페이지는 Excel 파일의 다른 시트로 내보내집니다. 이는 MinimizeTheNumberOfWorksheets 속성이 기본적으로 false로 설정되어 있기 때문입니다. 모든 페이지가 출력 Excel 파일의 하나의 시트로 내보내지도록 하려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정하십시오.

<a name="python-pdf-to-excel-single"><strong>단계: PDF를 Python에서 XLS 또는 XLSX 단일 워크시트로 변환</strong></a>
1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 만듭니다.
2. **MinimizeTheNumberOfWorksheets = true**를 사용하는 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)의 인스턴스를 만듭니다.
3. 단일 워크시트를 갖는 **XLS** 또는 **XLSX** 형식으로 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)를 전달하여 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # 파일을 MS Excel 형식으로 저장
    document.save(output_pdf, save_option)

```


## 다른 스프레드시트 형식으로 변환하기

### CSV로 변환

CSV 형식으로의 변환은 위와 같은 방식으로 수행됩니다. 필요한 것은 적절한 형식을 설정하는 것입니다.

<a name="python-pdf-to-csv"><strong>단계: Python에서 PDF를 CSV로 변환하기</strong></a>

1. 원본 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. **Format = ExcelSaveOptions.ExcelFormat.CSV**로 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)의 인스턴스를 생성합니다.
3. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)을 전달하여 **CSV** 형식으로 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # 파일 저장
    document.save(output_pdf, save_option)
```


### ODS로 변환

<a name="python-pdf-to-ods"><strong>단계: Python에서 PDF를 ODS로 변환</strong></a>

1. 원본 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 만듭니다.
2. **Format = ExcelSaveOptions.ExcelFormat.ODS**로 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)의 인스턴스를 만듭니다.
3. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)를 전달하여 **ODS** 형식으로 저장합니다.

ODS 형식으로의 변환은 다른 모든 형식과 동일한 방식으로 수행됩니다.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # 파일 저장
    document.save(output_pdf, save_option)
```


## 참조

이 기사에서는 이러한 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **Excel**
- [Python PDF를 Excel로 변환 코드](#python-pdf-to-xlsx)
- [Python PDF를 Excel API로 변환](#python-pdf-to-xlsx)
- [Python PDF를 Excel로 프로그래밍 방식으로 변환](#python-pdf-to-xlsx)
- [Python PDF를 Excel 라이브러리로 변환](#python-pdf-to-xlsx)
- [Python PDF를 Excel로 저장](#python-pdf-to-xlsx)
- [Python PDF에서 Excel 생성](#python-pdf-to-xlsx)
- [Python PDF에서 Excel 만들기](#python-pdf-to-xlsx)
- [Python PDF를 Excel로 변환기](#python-pdf-to-xlsx)

_형식_: **XLS**
- [Python PDF를 XLS로 변환 코드](#python-pdf-to-xls)
- [Python PDF를 XLS API로 변환](#python-pdf-to-xls)
- [Python PDF를 XLS로 프로그래밍 방식으로 변환](#python-pdf-to-xls)
- [Python PDF를 XLS 라이브러리로 변환](#python-pdf-to-xls)
- [Python PDF를 XLS로 저장](#python-pdf-to-xls)
- [Python PDF에서 XLS 생성](#python-pdf-to-xls)
- [Python PDF에서 XLS 만들기](#python-pdf-to-xls)
- [Python PDF를 XLS로 변환기](#python-pdf-to-xls)

_형식_: **XLSX**

- [Python PDF를 XLSX로 변환 코드](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_형식_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_형식_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)

- [Python Save PDF as ODS](#python-pdf-to-ods)
- [파이썬 PDF에서 ODS 생성](#python-pdf-to-ods)
- [파이썬 PDF에서 ODS 만들기](#python-pdf-to-ods)
- [파이썬 PDF를 ODS로 변환기](#python-pdf-to-ods)