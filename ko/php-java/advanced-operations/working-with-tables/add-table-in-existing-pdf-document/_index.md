---
title: PDF에 테이블 생성 또는 추가
linktitle: 테이블 생성 또는 추가
type: docs
weight: 10
url: /ko/php-java/add-table-in-existing-pdf-document/
description: PDF 문서에 테이블을 생성하거나 추가하는 방법, 셀 스타일 적용, 페이지에서 테이블 나누기 및 행과 열 사용자 정의 등을 배우세요.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 문서에 테이블 추가하기

Aspose.PDF for PHP를 사용하여 기존 PDF 파일에 테이블을 추가하려면 다음 단계를 따르세요:

1. 소스 파일을 로드합니다.
1. 테이블을 초기화합니다.
1. 테이블 테두리 색상을 LightGray로 설정합니다.
1. 테이블 셀의 테두리를 설정합니다.
1. 10개의 행을 추가하기 위한 루프를 생성합니다.
1. 입력 문서의 첫 번째 페이지에 테이블 객체를 추가합니다.
1. 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);        
    // 테이블의 새 인스턴스를 초기화합니다.
    $table = new Table();
    $colors= new Color();
    // 테이블 테두리 색상을 LightGray로 설정합니다.
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // 테이블 셀의 테두리를 설정합니다.
    $table->setDefaultCellBorder($borderInfo);
    // 10개의 행을 추가하기 위한 루프를 생성합니다.
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // 테이블에 행을 추가합니다.
        $row = $table->getRows()->add();
        // 테이블 셀을 추가합니다.
        $row->getCells()->add("Column (" . $row_count . ", 1)");
        $row->getCells()->add("Column (" . $row_count . ", 2)");
        $row->getCells()->add("Column (" . $row_count . ", 3)");
    }
    // 입력 문서의 첫 번째 페이지에 테이블 객체를 추가합니다.
    $document->getPages()->add()->getParagraphs()->add($table);

    // 결과 PDF 문서를 저장합니다.
    $document->save($outputFile);
    $document->close();
```