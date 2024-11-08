---
title: PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 90
url: /ko/androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java를 사용하면 PDF를 Excel 형식으로 변환할 수 있습니다. 이 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API를 사용하면 PDF 파일을 Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 및 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 파일 형식으로 렌더링할 수 있습니다. 우리는 이미 [Aspose.Cells for Java](https://products.aspose.com/cells/java)라는 또 다른 API를 가지고 있으며, 이를 통해 기존 Excel 워크북을 생성하고 조작할 수 있는 기능을 제공합니다. 또한 Excel 워크북을 PDF 형식으로 변환할 수 있는 기능도 제공합니다.

{{% alert color="primary" %}}

온라인으로 시도하십시오.
 Aspose.PDF 변환 품질을 확인하고 이 링크에서 온라인으로 결과를 볼 수 있습니다 [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

{{% /alert %}}

## PDF를 Excel XLS로 변환

PDF 파일을 XLS 형식으로 변환하기 위해, Aspose.PDF에는 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)라는 클래스가 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 객체는 Document.Save(..) 생성자에 두 번째 인수로 전달됩니다.

PDF 파일을 XLSX 형식으로 변환하는 것은 Java 18.6 버전의 Aspose.PDF 라이브러리의 일부입니다. PDF 파일을 XLSX 형식으로 변환하려면 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 setFormat() 메서드를 사용하여 형식을 XLSX로 설정해야 합니다.

다음 코드 스니펫은 PDF 파일을 xls 및 .xlsx 형식으로 변환하는 방법을 보여줍니다:

```java
public void convertPDFtoExcelSimple() {
        // 소스 PDF 문서를 엽니다
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Option 객체를 인스턴스화합니다
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // 파일을 MS 문서 형식으로 저장합니다
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF를 XLS로 변환하면서 열 제어하기

PDF를 XLS 형식으로 변환할 때, 출력 파일의 첫 번째 열로 빈 열이 추가됩니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 InsertBlankColumnAtFirst 옵션은 이 열을 제어하는 데 사용됩니다. 기본값은 true입니다.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // 소스 PDF 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Option 객체 인스턴스화
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // 파일을 MS 문서 형식으로 저장
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDF를 단일 Excel 워크시트로 변환

페이지가 많은 PDF 파일을 XLS로 내보낼 때, 각 페이지는 Excel 파일의 다른 시트로 내보내집니다. 이는 MinimizeTheNumberOfWorksheets 속성이 기본적으로 false로 설정되어 있기 때문입니다. 모든 페이지를 결과 Excel 파일의 하나의 시트로 내보내려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정하십시오.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // 소스 PDF 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Option 객체 인스턴스화
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // XLSX로 출력 저장
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // 파일을 MS Excel 형식으로 저장
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## XLSX 형식으로 변환

기본적으로 Aspose.PDF는 데이터를 저장하기 위해 XML Spreadsheet 2003을 사용합니다. PDF 파일을 XLSX 형식으로 변환하기 위해 Aspose.PDF에는 Format을 가지는 ExcelSaveOptions라는 클래스가 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 객체는 Document.Save(..) 메서드의 두 번째 인수로 전달됩니다.

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // PDF 문서 로드
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Option 객체 인스턴스화
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // CSV로 출력 저장
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // 파일을 CSV 형식으로 저장
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```