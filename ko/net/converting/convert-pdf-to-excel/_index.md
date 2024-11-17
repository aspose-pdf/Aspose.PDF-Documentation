---
title: .NET에서 PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Aspose.PDF for .NET 라이브러리를 사용하면 C#을 사용하여 PDF를 Excel 형식으로 변환할 수 있습니다. 이 형식에는 XLS, XLSX, XML 2003 스프레드시트, CSV, ODS가 포함됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 개요

이 문서에서는 **C#을 사용하여 PDF를 Excel 형식으로 변환하는 방법**에 대해 설명합니다. 다음 주제를 다룹니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

_형식_: **XLS**

- [C# PDF를 XLS로](#csharp-pdf-to-xls)
- [C# PDF를 XLS로 변환](#csharp-pdf-to-xls)
- [C# PDF 파일을 XLS로 변환하는 방법](#csharp-pdf-to-xls)

_형식_: **XLSX**

- [C# PDF를 XLSX로](#csharp-pdf-to-xlsx)
- [C# PDF를 XLSX로 변환](#csharp-pdf-to-xlsx)
- [C# PDF 파일을 XLSX로 변환하는 방법](#csharp-pdf-to-xlsx)
- [C# PDF 파일을 XLSX로 변환하는 방법](#csharp-pdf-to-xlsx)

_형식_: **Excel**

- [C# PDF를 Excel로 변환](#csharp-pdf-to-xlsx)
- [C# PDF를 Excel XLS로 변환](#csharp-pdf-to-xls)
- [C# PDF를 Excel XLSX로 변환](#csharp-pdf-to-xlsx)

_형식_: **단일 Excel 워크시트**

- [C# PDF를 단일 워크시트가 있는 XLS로 변환](#csharp-pdf-to-excel-single)
- [C# PDF를 단일 워크시트가 있는 XLSX로 변환](#csharp-pdf-to-excel-single)

_형식_: **XML 스프레드시트 2003 형식**

- [C# PDF를 XML Excel로 변환](#csharp-pdf-to-excel-xml-2003)
- [C# PDF를 XML Excel 스프레드시트로 변환](#csharp-pdf-to-excel-xml-2003)

_형식_: **CSV**

- [C# PDF를 CSV로 변환](#csharp-pdf-to-csv)
- [C# PDF를 CSV로 변환](#csharp-pdf-to-csv)
- [C# PDF 파일을 CSV로 변환하는 방법](#csharp-pdf-to-csv)

_형식_: **ODS**

- [C# PDF를 ODS로 변환](#csharp-pdf-to-ods)
- [C# PDF를 ODS로 변환](#csharp-pdf-to-ods)
- [C# PDF 파일을 ODS로 변환하는 방법](#csharp-pdf-to-ods)

## C# PDF를 Excel로 변환

**Aspose.PDF for .NET**은 PDF 파일을 Excel 2007, CSV 및 SpeadsheetML 형식으로 변환하는 기능을 지원합니다.
**Aspose.PDF for .NET**은 2007년 Excel, CSV 및 SpeadsheetML 형식으로 PDF 파일을 변환하는 기능을 지원합니다.

Aspose.PDF for .NET은 PDF 조작 컴포넌트로, PDF 파일을 Excel 워크북(XLSX 파일)으로 렌더링하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.

{{% alert color="success" %}}
**온라인에서 PDF를 Excel로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)을 제공합니다. 여기에서 기능성과 품질을 직접 탐구해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 Excel로 변환](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

PDF 파일을 <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> 형식으로 변환하기 위해 Aspose.PDF는 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions)라는 클래스를 가지고 있습니다.
PDF 파일을 <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> 형식으로 변환하기 위해 Aspose.PDF에는 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions)라는 클래스가 있습니다.

다음 코드 스니펫은 Aspose.PDF for .NET을 사용하여 PDF 파일을 XLS 또는 XLSX 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-xls"><strong>단계: C#에서 PDF를 XLS로 변환</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **.xls 확장자**를 지정하여 **XLS** 형식으로 저장합니다.

<a name="csharp-pdf-to-xlsx"><strong>단계: C#에서 PDF를 XLSX로 변환</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **.xlsx 확장자**를 지정하여 **XLSX** 형식으로 저장합니다.

```csharp
// PDF를 XLS로 변환하는 코드 예제
Document pdfDocument = new Document("input.pdf");
ExcelSaveOptions saveOptions = new ExcelSaveOptions();
pdfDocument.Save("output.xls", saveOptions);

// PDF를 XLSX로 변환하는 코드 예제
Document pdfDocument = new Document("input.pdf");
ExcelSaveOptions saveOptions = new ExcelSaveOptions();
pdfDocument.Save("output.xlsx", saveOptions);
```
```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// PDF 문서를 로드합니다
Document pdfDocument = new Document(dataDir + "input.pdf");

// ExcelSave 옵션 객체를 인스턴스화합니다
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// 출력을 XLS 형식으로 저장합니다
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## PDF를 XLS로 변환하면서 컨트롤 열

PDF를 XLS 형식으로 변환할 때 첫 번째 열로 빈 열이 출력 파일에 추가됩니다. ExcelSaveOptions 클래스의 InsertBlankColumnAtFirst 옵션을 사용하여 이 열을 제어할 수 있습니다. 기본값은 `false`이며, 이는 빈 열이 삽입되지 않음을 의미합니다.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
    // PDF 문서를 로드합니다
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // ExcelSave 옵션 객체를 인스턴스화합니다
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // 출력을 XLS 형식으로 저장합니다
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## PDF를 단일 Excel 워크시트로 변환

PDF 파일을 XLS로 내보낼 때 많은 페이지가 각각 Excel 파일의 다른 시트로 내보내집니다. 기본적으로 MinimizeTheNumberOfWorksheets 속성이 false로 설정되어 있기 때문입니다. 출력 Excel 파일에서 모든 페이지를 하나의 시트로 내보내려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정하세요.

<a name="csharp-pdf-to-excel-single"><strong>단계: C#에서 PDF를 XLS 또는 XLSX 단일 워크시트로 변환</strong></a>

1. 소스 PDF 문서를 사용하여 **Document** 객체의 인스턴스를 생성합니다.
2. **MinimizeTheNumberOfWorksheets = true**를 가진 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메소드를 호출하고 **ExcelSaveOptions**를 전달하여 단일 워크시트가 있는 **XLS** 또는 **XLSX** 형식으로 저장합니다.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
    // PDF 문서를 로드합니다.
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // ExcelSave Option 객체를 인스턴스화합니다.
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // 출력을 XLS 형식으로 저장합니다.
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## 다른 스프레드시트 형식으로 변환

### XML 스프레드시트 2003 형식으로 변환

버전 20.8부터 Aspose.PDF는 데이터 저장을 위해 기본적으로 Microsoft Excel Open XML 스프레드시트 2007 파일 형식을 사용합니다. PDF 파일을 XML 스프레드시트 2003 형식으로 변환하기 위해, Aspose.PDF는 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) 클래스를 [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format)와 함께 제공합니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) 클래스의 객체는 [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메소드의 두 번째 인자로 전달됩니다.

다음 코드 스니펫은 PDF 파일을 XLS Excel 2003 XML 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-excel-xml-2003"><strong>단계: C#에서 PDF를 Excel 2003 XML 형식으로 변환</strong></a>

1. 소스 PDF 문서를 가진 **Document** 객체의 인스턴스를 생성합니다.
2.
2. **XLS - Excel 2003 XML 포맷**으로 저장하려면 **Document.Save()** 메소드를 호출하고 **ExcelSaveOptions**를 전달하세요.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 방문하세요.

    // PDF 문서를 로드합니다
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // ExcelSave Option 객체 인스턴스 생성
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // 출력을 XLS 형식으로 저장합니다
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### CSV로 변환

CSV 형식으로의 변환은 위와 같은 방식으로 수행됩니다. 필요한 것은 적절한 형식을 설정하는 것입니다.

<a name="csharp-pdf-to-csv"><strong>단계: C#에서 PDF를 CSV로 변환</strong></a>

1. 원본 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2.
2.
3. **CSV** 형식으로 저장하려면 **Document.Save()** 메소드를 호출하고 **ExcelSaveOptions**를 전달하십시오.


```csharp
 // ExcelSave Option 객체를 인스턴스화합니다.
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### ODS로 변환

<a name="csharp-pdf-to-ods"><strong>단계: C#에서 PDF를 ODS로 변환</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **Format = ExcelSaveOptions.ExcelFormat.ODS**인 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메소드를 호출하고 **ExcelSaveOptions**를 전달하여 **ODS** 형식으로 저장합니다.


ODS 형식으로의 변환은 다른 모든 형식과 동일한 방식으로 수행됩니다.

```csharp
 // ExcelSave Option 객체를 인스턴스화합니다.
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## 참고 

이 문서는 위와 같은 코드를 사용하는 다음 주제들도 다룹니다.

_형식_: **Excel**
- [C# PDF to Excel 코드](#csharp-pdf-to-xlsx)
- [C# PDF to Excel API](#csharp-pdf-to-xlsx)
- [C# PDF를 Excel로 변환 API](#csharp-pdf-to-xlsx)
- [C# PDF를 Excel로 프로그래밍 방식으로 변환](#csharp-pdf-to-xlsx)
- [C# PDF를 Excel로 변환 라이브러리](#csharp-pdf-to-xlsx)
- [C# PDF를 Excel로 저장](#csharp-pdf-to-xlsx)
- [C# PDF에서 Excel 생성](#csharp-pdf-to-xlsx)
- [C# PDF에서 Excel 생성](#csharp-pdf-to-xlsx)
- [C# PDF를 Excel로 변환기](#csharp-pdf-to-xlsx)

_Format_: **XLS**
- [C# PDF를 XLS 코드로 변환](#csharp-pdf-to-xls)
- [C# PDF를 XLS API로 변환](#csharp-pdf-to-xls)
- [C# PDF를 XLS로 프로그래밍 방식으로 변환](#csharp-pdf-to-xls)
- [C# PDF를 XLS로 변환 라이브러리](#csharp-pdf-to-xls)
- [C# PDF를 XLS로 저장](#csharp-pdf-to-xls)
- [C# PDF에서 XLS 생성](#csharp-pdf-to-xls)
- [C# PDF에서 XLS 생성](#csharp-pdf-to-xls)
- [C# PDF를 XLS로 변환기](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [C# PDF를 XLSX 코드로 변환](#csharp-pdf-to-xlsx)
- [C# PDF를 XLSX API로 변환](#csharp-pdf-to-xlsx)
- [C# PDF를 XLSX로 프로그래밍 방식으로 변환](#csharp-pdf-to-xlsx)
- [C# PDF를 XLSX로 변환 라이브러리](#csharp-pdf-to-xlsx)
- [C# PDF를 XLSX로 저장](#csharp-pdf-to-xlsx)
- [C# PDF에서 XLSX 생성](#csharp-pdf-to-xlsx)
- [C#에서 PDF에서 XLSX 생성](#csharp-pdf-to-xlsx)
- [C#에서 PDF에서 XLSX 생성](#csharp-pdf-to-xlsx)
- [C# PDF에서 XLSX 변환기](#csharp-pdf-to-xlsx)

_Format_: **CSV**
- [C# PDF에서 CSV 코드](#csharp-pdf-to-csv)
- [C# PDF에서 CSV API](#csharp-pdf-to-csv)
- [C# PDF에서 CSV 프로그래밍 방식](#csharp-pdf-to-csv)
- [C# PDF에서 CSV 라이브러리](#csharp-pdf-to-csv)
- [C# PDF를 CSV로 저장](#csharp-pdf-to-csv)
- [C# PDF에서 CSV 생성](#csharp-pdf-to-csv)
- [C# PDF에서 CSV 생성](#csharp-pdf-to-csv)
- [C# PDF에서 CSV 변환기](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# PDF에서 ODS 코드](#csharp-pdf-to-ods)
- [C# PDF에서 ODS API](#csharp-pdf-to-ods)
- [C# PDF에서 ODS 프로그래밍 방식](#csharp-pdf-to-ods)
- [C# PDF에서 ODS 라이브러리](#csharp-pdf-to-ods)
- [C# PDF를 ODS로 저장](#csharp-pdf-to-ods)
- [C# PDF에서 ODS 생성](#csharp-pdf-to-ods)
- [C# PDF에서 ODS 생성](#csharp-pdf-to-ods)
- [C# PDF에서 ODS 변환기](#csharp-pdf-to-ods)

