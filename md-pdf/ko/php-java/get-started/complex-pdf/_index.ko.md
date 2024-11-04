---  
title: 복잡한 PDF 생성  
linktitle: 복잡한 PDF 생성  
type: docs  
weight: 60  
url: /php-java/complex-pdf-example/  
description: Aspose.PDF for PHP via Java를 사용하여 하나의 문서에 이미지, 텍스트 조각 및 표를 포함하는 더 복잡한 문서를 생성할 수 있습니다.  
lastmod: "2024-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

[Hello, World](/pdf/php-java/hello-world-example/) 예제에서는 Aspose.PDF를 사용하여 PDF 문서를 생성하는 간단한 단계를 보여주었습니다. 이 기사에서는 Aspose.PDF for PHP via Java로 더 복잡한 문서를 생성하는 방법을 살펴보겠습니다. 예제로는 여객 페리 서비스를 운영하는 가상의 회사의 문서를 살펴보겠습니다.

문서를 처음부터 생성하려면 다음 단계를 따라야 합니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터는 있지만 페이지가 없는 빈 PDF 문서를 생성합니다.

1. 문서 객체에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)를 추가합니다. 이제 문서에 한 페이지가 생겼습니다.
1. [이미지](https://reference.aspose.com/pdf/java/com.aspose.pdf/image)를 추가합니다. 이는 PDF 연산자를 사용한 저수준 작업을 기반으로 한 복잡한 작업입니다.
    - 스트림에서 이미지 로드
    - 페이지 리소스의 이미지 컬렉션에 이미지 추가
    - GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다.
    - [매트릭스](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) 객체 생성
    - ConcatenateMatrix 연산자 사용: 이미지가 배치되어야 하는 방식을 정의합니다.
    - Do 연산자 사용: 이 연산자는 이미지를 그립니다.
    - GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다.
1. 헤더용 [텍스트 조각](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)을 생성합니다. 헤더에는 Arial 폰트를 사용하고 글꼴 크기는 24pt, 중앙 정렬을 사용할 것입니다.

1. 페이지에 헤더 추가 [단락](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. 설명을 위한 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 생성. 설명에는 Arial 글꼴, 글꼴 크기 24pt, 중앙 정렬을 사용할 것입니다.
1. 페이지 단락에 (설명)을 추가합니다.
1. 표를 생성하고, 표 속성을 추가합니다.
1. 페이지 [단락](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)에 (표)를 추가합니다.
1. 문서를 "Complex.pdf"로 저장합니다.

```php

    $document = new Document();
    //페이지 추가
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // 이미지 추가
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // 헤더 추가
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("2020년 가을 새로운 페리 노선");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // 설명 추가
    $descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며 티켓은 하루에 5,000장으로 제한됩니다. 페리 서비스는 절반 용량으로 운영되며 일정이 축소되었습니다. 줄을 서는 것을 예상하세요.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // 표 추가
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("출발 도시");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("출발 섬");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```