---
title: Python에서 PDF를 Excel로 변환하기
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Aspose.PDF for Python via .NET를 사용하여 PDF를 Excel 스프레드시트로 손쉽게 변환합니다. 정확한 PDF에서 XLSX 변환을 위해 이 가이드를 따르세요.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 Excel로 변환하는 방법
Abstract: 이 문서는 Python을 사용하여 PDF 파일을 다양한 Excel 형식으로 변환하는 포괄적인 가이드를 제공합니다. 특히 Aspose.PDF for Python via .NET 라이브러리를 사용합니다. XLS, XLSX, CSV, ODS 형식에 대한 변환 과정을 자세히 설명합니다. 문서는 PDF를 XLS 및 XLSX로 변환하기 위한 단계들을 설명하며, Document 및 ExcelSaveOptions 인스턴스 생성, 그리고 출력 형식을 지정하기 위한 Document.Save() 메서드 사용을 강조합니다. 또한 변환 중 빈 열 삽입을 제어하고 워크시트 수를 최소화하는 기능에 대해 논의합니다. 추가로 PDF를 단일 Excel 워크시트와 CSV, ODS와 같은 다른 형식으로 변환하는 예제를 제공하여 Aspose.PDF의 유연성과 기능성을 강조합니다. PDF를 XLSX로 변환하는 온라인 도구도 언급되어 사용자가 변환 품질을 확인할 수 있습니다. 문서는 관련 주제 목록과 코드 스니펫으로 마무리되어 이러한 변환을 프로그래밍 방식으로 이해하고 구현하는 데 도움을 줍니다.
---

## Python을 통한 PDF를 Excel로 변환

**Aspose.PDF for Python via .NET** 은 PDF 파일을 Excel 및 CSV 형식으로 변환하는 기능을 지원합니다.

Aspose.PDF for Python via .NET는 PDF 조작 구성 요소이며, PDF 파일을 Excel 워크북(XLSX 파일)으로 렌더링하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 각 페이지가 Excel 워크시트로 변환됩니다.

{{% alert color="success" %}}
**온라인에서 PDF를 Excel로 변환해 보세요**

Aspose.PDF는 온라인 무료 애플리케이션 ["PDF를 XLSX로"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)를 제공하며, 여기서 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 Excel로 변환](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

다음 코드 스니펫은 Aspose.PDF for Python via .NET를 사용하여 PDF 파일을 XLS 또는 XLSX 형식으로 변환하는 과정을 보여줍니다.

단계: PDF 파일을 Excel (XML Spreadsheet 2003) 형식으로 변환

1. PDF 문서를 로드합니다.
1. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)를 사용하여 Excel 저장 옵션을 설정합니다.
1. 변환된 파일을 저장합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

단계: PDF 파일을 XLSX 형식(Excel 2007 이상)으로 변환

1. PDF 문서를 로드합니다.
1. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)를 사용하여 Excel 저장 옵션을 설정합니다.
1. 변환된 파일을 저장합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 제어 컬럼을 사용하여 PDF를 XLS로 변환

PDF를 XLS 형식으로 변환할 때, 첫 번째 열에 빈 열이 추가됩니다. 'ExcelSaveOptions 클래스'의 'insert_blank_column_at_first' 옵션을 사용하여 이 열을 제어합니다. 기본값은 true입니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 단일 Excel 워크시트로 변환

Aspose.PDF for Python via .NET는 'minimize_the_number_of_worksheets' 옵션을 활성화하여 PDF를 Excel(.xlsx) 파일로 변환하는 방법을 보여줍니다.

단계: Python에서 PDF를 XLS 또는 XLSX 단일 워크시트로 변환

1. PDF 문서를 로드합니다.
1. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)를 사용하여 Excel 저장 옵션을 설정합니다.
1. 'minimize_the_number_of_worksheets' 옵션은 PDF 페이지를 결합하여 워크시트 수를 줄임으로써 Excel 시트 수를 감소시킵니다(가능하면 전체 문서에 대해 하나의 워크시트를 사용).
1. 변환된 파일을 저장합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF 파일을 XLSM 형식의 Excel 파일로 변환

이 Python 예제는 PDF 파일을 XLSM 형식(Excel 매크로 사용 가능 통합 문서) Excel 파일로 변환하는 방법을 보여줍니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## 다른 스프레드시트 형식으로 변환

### CSV로 변환

'convert_pdf_to_excel_2007_csv' 함수는 이전과 동일한 작업을 수행하지만, 이번에는 대상 형식이 XLSM이 아닌 CSV(쉼표로 구분된 값)입니다.

단계: Python에서 PDF를 CSV로 변환

1. 원본 PDF 문서를 사용하여 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
1. **ExcelSaveOptions.ExcelFormat.CSV** 로 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)의 인스턴스를 생성합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)을 전달하여 **CSV** 형식으로 저장합니다.

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### ODS로 변환

단계: Python에서 PDF를 ODS로 변환

1. 원본 PDF 문서와 함께 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 생성합니다.
1. **ExcelSaveOptions.ExcelFormat.ODS** 로 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 인스턴스를 생성합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 를 전달하여 **ODS** 형식으로 저장합니다.

ODS 형식으로의 변환은 다른 모든 형식과 동일한 방식으로 수행됩니다.

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

