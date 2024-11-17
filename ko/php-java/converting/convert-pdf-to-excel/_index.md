---
title: PDF를 Microsoft Excel로 변환하기
linktitle: PDF를 Excel로 변환하기
type: docs
weight: 20
url: /ko/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
description: Aspose.PDF for PHP를 사용하면 PHP를 통해 PDF를 Excel 형식으로 변환할 수 있습니다. 이 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for PHP API는 PDF 파일을 Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 및 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 파일 형식으로 렌더링할 수 있게 해줍니다. 우리는 이미 기존의 Excel 워크북을 생성하고 조작할 수 있는 기능을 제공하는 [Aspose.Cells for PHP via Java](https://products.aspose.com/cells/php-java)라는 또 다른 API를 가지고 있습니다. 이 API는 또한 Excel 워크북을 PDF 형식으로 변환하는 기능도 제공합니다.

{{% alert color="primary" %}}

**온라인으로 PDF를 Excel로 변환해보세요**

Aspose.PDF for PHP는 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)라는 온라인 무료 애플리케이션을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDF를 Excel XLS로 변환

PDF 파일을 XLS 형식으로 변환하기 위해 Aspose.PDF에는 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)이라는 클래스가 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 객체는 Document.Save(..) 메소드의 두 번째 인수로 전달됩니다.

PDF 파일을 XLSX 형식으로 변환하는 것은 Aspose.PDF for PHP 18.6 버전의 라이브러리의 일부입니다. PDF 파일을 XLSX 형식으로 변환하려면 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 클래스의 setFormat() 메소드를 사용하여 형식을 XLSX로 설정해야 합니다.

다음 코드 스니펫은 PDF 파일을 XLS 및 XLSX 형식으로 변환하는 방법을 보여줍니다:

```php
// Document 클래스를 사용하여 입력 PDF 문서를 로드합니다.
$document = new Document($inputFile);

// 저장 옵션을 지정하기 위해 ExcelSaveOptions 클래스의 인스턴스를 생성합니다.
$saveOption = new ExcelSaveOptions();

// 출력 형식을 XLS로 설정합니다.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// 출력 형식을 XLSX로 설정합니다.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// 지정된 저장 옵션을 사용하여 PDF 문서를 Excel 파일로 저장합니다.
$document->save($outputFile, $saveOption);
```