---
title: PDF를 Excel로 변환 
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
keywords: Java를 사용하여 PDF를 Excel로 변환, Java를 사용하여 PDF를 XLS로 변환, Java를 사용하여 PDF를 XLSX로 변환, Java에서 PDF의 테이블을 Excel로 내보내기
description: Aspose.PDF for Java를 사용하면 PDF를 Excel 형식으로 변환할 수 있습니다. 이 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Java API를 사용하면 PDF 파일을 Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 및 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 파일 형식으로 렌더링할 수 있습니다. 우리는 이미 Excel 워크북을 생성하고 조작할 수 있는 기능을 제공하는 [Aspose.Cells for Java](https://products.aspose.com/cells/java) 라는 또 다른 API를 가지고 있습니다. 또한 Excel 워크북을 PDF 형식으로 변환할 수 있는 기능도 제공합니다.

{{% alert color="primary" %}}

**온라인에서 PDF를 Excel로 변환해보세요**

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)를 제공합니다. 이곳에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDF를 Excel XLS로 변환

PDF 파일을 XLS 형식으로 변환하려면, Aspose.PDF에는 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)라는 클래스가 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 객체는 Document.Save(..) 메서드의 두 번째 인수로 전달됩니다.

PDF 파일을 XLSX 형식으로 변환하는 것은 Aspose.PDF for Java 18.6 버전의 라이브러리의 일부입니다. PDF 파일을 XLSX 형식으로 변환하려면, [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 setFormat() 메소드를 사용하여 형식을 XLSX로 설정해야 합니다.

다음 코드 스니펫은 PDF 파일을 xls 및 .xlsx 형식으로 변환하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // 문서 디렉토리 경로.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // PDF 문서 로드
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Excel 저장 옵션 객체 인스턴스화
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // XLS 형식으로 출력 저장
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## PDF를 XLS로 변환하여 열 제어

PDF를 XLS 형식으로 변환할 때, 출력 파일의 첫 번째 열로 빈 열이 추가됩니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 InsertBlankColumnAtFirst 옵션은 이 열을 제어하는 데 사용됩니다. 기본값은 true입니다.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // PDF 문서 불러오기
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // ExcelSave Option 객체 인스턴스화
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // XLS 형식으로 출력 저장
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## PDF를 단일 Excel 워크시트로 변환

페이지가 많은 PDF 파일을 XLS로 내보낼 때, 각 페이지는 Excel 파일의 다른 시트로 내보내집니다.
 기본적으로 MinimizeTheNumberOfWorksheets 속성은 false로 설정되어 있습니다. 모든 페이지가 출력 Excel 파일의 단일 시트에 내보내지도록 하려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정하세요.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // PDF 문서 로드
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // ExcelSave Option 객체 인스턴스화
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // 출력물을 XLS 형식으로 저장
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## XLSX 형식으로 변환

기본적으로 Aspose.PDF는 데이터를 저장하기 위해 XML Spreadsheet 2003을 사용합니다. PDF 파일을 XLSX 형식으로 변환하기 위해 Aspose.PDF에는 Format이 있는 ExcelSaveOptions라는 클래스가 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 객체가 Document.Save(..) 메서드의 두 번째 인수로 전달됩니다.

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // PDF 문서 로드
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // ExcelSave 옵션 객체 인스턴스화
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // XLS 형식으로 출력 저장
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```