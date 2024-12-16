---
title: C++에서 PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF for C++를 사용하면 C++를 통해 PDF를 Excel 형식으로 변환할 수 있습니다. 이 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서는 **C++를 사용하여 PDF를 Excel 형식으로 변환하는 방법**에 대해 설명합니다. 다음 주제를 다룹니다.

_형식_: **XLS**
- [C++ PDF를 XLS로](#cpp-pdf-to-xls)
- [C++ PDF를 XLS로 변환](#cpp-pdf-to-xls)
- [C++ PDF 파일을 XLS로 변환하는 방법](#cpp-pdf-to-xls)

_형식_: **XLSX**
- [C++ PDF를 XLSX로](#cpp-pdf-to-xlsx)
- [C++ PDF를 XLSX로 변환](#cpp-pdf-to-xlsx)
- [C++ PDF 파일을 XLSX로 변환하는 방법](#cpp-pdf-to-xlsx)

_형식_: **Microsoft Excel XLS 형식**
- [C++ PDF를 Excel로](#cpp-pdf-to-excel-xls)
- [C++ PDF를 Excel로 변환](#cpp-pdf-to-excel-xls)
- [C++ PDF 파일을 Excel로 변환하는 방법](#cpp-pdf-to-excel-xls)

_형식_: **Microsoft Excel XLSX 형식**
- [C++ PDF를 Excel로](#cpp-pdf-to-excel-xlsx)
- [C++ PDF를 Excel로 변환](#cpp-pdf-to-excel-xlsx)
- [C++ PDF 파일을 Excel로 변환하는 방법](#cpp-pdf-to-excel-xlsx)

Other topics covered by this article
- [See Also](#see-also)

## C++ PDF를 Excel로 변환

**Aspose.PDF for C++**는 PDF 파일을 Excel 형식으로 변환하는 기능을 지원합니다.

Aspose.PDF for C++는 PDF 조작 구성 요소로, PDF 파일을 Excel 워크북(XLS 파일)으로 렌더링하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지는 Excel 워크시트로 변환됩니다.

PDF 파일을 <abbr title="Microsoft Excel Spreadsheet">XLS</abbr> 형식으로 변환하기 위해, Aspose.PDF에는 ExcelSaveOptions라는 클래스가 있습니다. ExcelSaveOptions 클래스의 객체는 Document.Save(..) 생성자에 두 번째 인수로 전달됩니다.

다음 코드 스니펫은 Aspose.PDF for C++를 사용하여 PDF 파일을 XLS 형식으로 변환하는 과정을 보여줍니다.

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>단계: C++에서 PDF를 XLS로 변환</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>단계: C++에서 PDF를 Excel XLS 형식으로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 인스턴스를 만듭니다.
2. **Document->Save()** 메서드를 호출하여 _XLS_ 형식으로 저장합니다.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // 출력물을 XLS 형식으로 저장
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 제어 열로 PDF를 XLS로 변환

PDF를 XLS 형식으로 변환할 때 출력 파일의 첫 번째 열로 빈 열이 추가됩니다. ExcelSaveOptions 클래스의 InsertBlankColumnAtFirst 옵션은 이 열을 제어하는 데 사용됩니다. 기본값은 true입니다.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Excel 저장 옵션 객체 인스턴스화
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // ExcelSaveOptions 클래스의 InsertBlankColumnAtFirst 옵션은 이 열을 제어하는 데 사용됩니다. 기본값은 true입니다.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // 출력물을 XLS 형식으로 저장
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF를 단일 Excel 워크시트로 변환

페이지가 많은 PDF 파일을 XLS로 내보낼 때 각 페이지가 Excel 파일의 다른 시트로 내보내집니다. 이것은 기본적으로 MinimizeTheNumberOfWorksheets 속성이 false로 설정되어 있기 때문입니다. 모든 페이지가 출력 Excel 파일의 하나의 시트로 내보내지도록 하려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정하십시오.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Excel 저장 옵션 객체 인스턴스화
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // XLS 형식으로 출력 저장
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## XLSX 형식으로 변환

기본적으로 Aspose.PDF는 데이터를 저장하기 위해 XML Spreadsheet 2003을 사용합니다. PDF 파일을 XLSX 형식으로 변환하기 위해, Aspose.PDF는 'Format'이라는 [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) 클래스를 가지고 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) 클래스의 객체는 [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 메서드의 두 번째 인수로 전달됩니다.

다음 코드 스니펫은 PDF 파일을 XLSX 형식으로 변환하는 과정을 보여줍니다.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>단계: C++에서 PDF를 XLSX로 변환</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>단계: C++에서 PDF를 Excel XLSX 형식으로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 인스턴스를 생성합니다.
2. 인스턴스를 만듭니다 [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. 형식을 _ExcelSaveOptions::ExcelFormat::XLSX_로 설정합니다.
4. **Document->Save()** 메서드를 호출하고 _ExcelSaveOptions_의 인스턴스를 전달하여 _XLSX_ 형식으로 저장합니다.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // ExcelSave Option 객체 인스턴스화
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // XLS 형식으로 출력 저장
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**PDF를 Excel로 온라인 변환 시도**
Aspose.PDF for C++는 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## See Also

이 문서에서는 다음 주제도 다룹니다. 코드는 위와 동일합니다.

_Format_: **Microsoft Excel XLS 형식**
- [C++ PDF to Excel XLS Code](#cpp-pdf-to-excel-xls)
- [C++ PDF to Excel XLS Programmatically](#cpp-pdf-to-excel-xls)
- [C++ PDF to Excel XLS Library](#cpp-pdf-to-excel-xls)
- [C++ Save PDF as Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Generate Excel XLS from PDF](#cpp-pdf-to-excel-xls)
- [C++ Create Excel XLS from PDF](#cpp-pdf-to-excel-xls)
- [C++ PDF to Excel XLS Converter](#cpp-pdf-to-excel-xls)

_Format_: **Microsoft Excel XLSX 형식**
- [C++ PDF to Excel XLSX Code](#cpp-pdf-to-excel-xlsx)

- [C++ PDF to Excel XLSX Programmatically](#cpp-pdf-to-excel-xlsx)
- [C++ PDF를 Excel XLSX 라이브러리로](#cpp-pdf-to-excel-xlsx)
- [C++ PDF를 Excel XLSX로 저장](#cpp-pdf-to-excel-xlsx)
- [C++ PDF에서 Excel XLSX 생성](#cpp-pdf-to-excel-xlsx)
- [C++ PDF에서 Excel XLSX 생성](#cpp-pdf-to-excel-xlsx)
- [C++ PDF를 Excel XLSX 변환기](#cpp-pdf-to-excel-xlsx)

_형식_: **XLS**
- [C++ PDF를 XLS 코드로](#cpp-pdf-to-xls)
- [C++ PDF를 XLS로 프로그래밍](#cpp-pdf-to-xls)
- [C++ PDF를 XLS 라이브러리로](#cpp-pdf-to-xls)
- [C++ PDF를 XLS로 저장](#cpp-pdf-to-xls)
- [C++ PDF에서 XLS 생성](#cpp-pdf-to-xls)
- [C++ PDF에서 XLS 생성](#cpp-pdf-to-xls)
- [C++ PDF를 XLS 변환기](#cpp-pdf-to-xls)

_형식_: **XLSX**
- [C++ PDF를 XLSX 코드로](#cpp-pdf-to-xlsx)
- [C++ PDF를 XLSX로 프로그래밍](#cpp-pdf-to-xlsx)
- [C++ PDF를 XLSX 라이브러리로](#cpp-pdf-to-xlsx)
- [C++ PDF를 XLSX로 저장](#cpp-pdf-to-xlsx)
- [C++ PDF에서 XLSX 생성](#cpp-pdf-to-xlsx)
- [C++ PDF에서 XLSX 생성](#cpp-pdf-to-xlsx)
- [C++ PDF를 XLSX 변환기](#cpp-pdf-to-xlsx)