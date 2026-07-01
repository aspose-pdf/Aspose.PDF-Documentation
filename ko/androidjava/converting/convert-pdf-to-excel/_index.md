---
title: PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 90
url: /ko/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java는 PDF를 Excel 형식으로 변환할 수 있게 합니다. 이 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API를 사용하면 PDF 파일을 Excel로 렌더링할 수 있습니다. [XLS](https://docs.fileformat.com/spreadsheet/xls/) 및 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 파일 형식입니다. 우리는 이미 다른 API가 있으며, 이름은 [Aspose.Cells for Java](https://products.aspose.com/cells/java), 기존 Excel 워크북을 만들고 조작할 수 있는 기능을 제공합니다. Excel 워크북을 PDF 형식으로 변환하는 기능도 제공합니다.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## PDF를 Excel XLS로 변환

PDF 파일을 XLS 형식으로 변환하려면, Aspose.PDF에는 다음과 같은 클래스가 있습니다 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). 객체는 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스는 Document.Save(..) 생성자에 두 번째 인수로 전달됩니다. 

PDF 파일을 XLSX 형식으로 변환하는 것은 Aspose.PDF for Java 18.6 버전의 라이브러리 일부입니다. PDF 파일을 XLSX 형식으로 변환하려면 setFormat() 메서드를 사용하여 형식을 XLSX로 설정해야 합니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스.

다음 코드 조각은 PDF 파일을 xls 및 .xlsx 형식으로 변환하는 방법을 보여줍니다:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Control Column을 사용하여 PDF를 XLS로 변환

PDF를 XLS 형식으로 변환할 때, 빈 열이 첫 번째 열로 출력 파일에 추가됩니다. The in [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) class InsertBlankColumnAtFirst 옵션은 이 열을 제어하는 데 사용됩니다. 기본값은 true입니다.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
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

PDF 파일을 페이지가 많은 상태로 XLS로 내보낼 때, 각 페이지가 Excel 파일의 서로 다른 시트로 내보내집니다. 이는 MinimizeTheNumberOfWorksheets 속성이 기본값으로 false로 설정되어 있기 때문입니다. 모든 페이지를 출력 Excel 파일의 하나의 시트로 내보내려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정하십시오.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
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

기본적으로 Aspose.PDF는 데이터를 저장하기 위해 XML Spreadsheet 2003을 사용합니다. PDF 파일을 XLSX 형식으로 변환하려면 Aspose.PDF에 Format이 있는 ExcelSaveOptions라는 클래스가 있습니다. 그 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스 객체는 Document.Save(..) 메서드의 두 번째 인수로 전달됩니다.

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
