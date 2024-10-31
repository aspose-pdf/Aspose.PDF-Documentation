---
title: PDF에서 테이블 데이터 추출 
linktitle: 테이블 데이터 추출
type: docs
weight: 40
url: /php-java/extract-data-from-table-in-pdf/
description: Aspose.PDF for PHP를 사용하여 PDF에서 표 형식을 추출하는 방법을 배우세요
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF에서 프로그래밍 방식으로 테이블 추출하기

PDF에서 테이블을 추출하는 것은 쉬운 작업이 아닙니다. 테이블은 다양한 방식으로 생성될 수 있기 때문입니다.

Aspose.PDF for PHP via Java는 테이블을 쉽게 검색할 수 있는 도구를 제공합니다. 테이블 데이터를 추출하려면 다음 단계를 수행해야 합니다:

1. PDF 문서를 열기 - [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document) 객체를 인스턴스화합니다;
1. 문서에서 테이블을 추출하기 위해 TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) 객체를 생성합니다.
1. 문서의 각 페이지를 반복합니다.

1. 분석할 페이지를 결정하고 원하는 페이지에 [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)을 적용합니다. 표 데이터가 스캔되고 결과는 [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable)의 목록에 저장됩니다. 이 목록은 [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) 메서드를 통해 얻을 수 있습니다.

1. 데이터를 얻기 위해 `TableList`를 반복하고 [absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) 목록과 흡수된 셀 목록을 처리합니다. 첫 번째 목록은 [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) 메서드를 호출하여 접근할 수 있으며, 두 번째 목록은 [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--) 메서드를 호출하여 접근할 수 있습니다.

1. 각 [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell)은 [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection)을 포함합니다. 이를 귀하의 목적에 맞게 처리할 수 있습니다.

다음 예제는 모든 페이지에서 표 추출을 보여줍니다:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // 행의 각 셀을 반복합니다.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // 셀의 각 텍스트 조각을 반복합니다.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // 텍스트 조각의 각 세그먼트를 반복합니다.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// 표 데이터를 출력 파일에 저장합니다.
file_put_contents($outputFile, $responseData);

// PDF 문서를 닫습니다.
$document->close();
```


## PDF에서 테이블 데이터 추출하여 CSV 파일에 저장

다음 예제는 테이블을 추출하여 CSV 파일로 저장하는 방법을 보여줍니다.
PDF를 Excel 스프레드시트로 변환하는 방법은 [PDF를 Excel로 변환](/pdf/php-java/convert-pdf-to-excel/) 기사를 참조하십시오.

```php

    // Document 클래스를 사용하여 입력 PDF 문서를 로드합니다.
    $document = new Document($inputFile);

    // 저장 옵션을 지정하기 위해 ExcelSaveOptions 클래스의 인스턴스를 생성합니다.
    $saveOption = new ExcelSaveOptions();

    // 출력 형식을 CSV로 설정합니다.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // 지정된 저장 옵션을 사용하여 PDF 문서를 Excel 파일로 저장합니다.
    $document->save($outputFile, $saveOption);
```