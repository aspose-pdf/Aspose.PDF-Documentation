title: PDF에서 제목 작업하기
type: docs
weight: 70
url: ko/php-java/working-with-headings/
lastmod: "2024-06-05"
description: PHP를 사용하여 PDF 문서의 제목에 번호 매기기를 생성합니다. Aspose.PDF for PHP via Java는 다양한 번호 매기기 스타일을 제공합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 제목에 번호 매기기 스타일 적용하기

제목은 문서의 중요한 부분입니다. 작가들은 항상 제목을 독자에게 더 두드러지고 의미 있게 만들려고 합니다. 문서에 여러 개의 제목이 있을 경우, 작가는 이러한 제목을 구성하는 여러 가지 옵션을 가지고 있습니다. 제목을 구성하는 가장 일반적인 방법 중 하나는 제목을 번호 매기기 스타일로 작성하는 것입니다.

Aspose.PDF for PHP via Java는 많은 미리 정의된 번호 매기기 스타일을 제공합니다. 이 미리 정의된 번호 매기기 스타일은 NumberingStyle 열거형에 저장됩니다. NumberingStyle 열거형의 미리 정의된 값과 그 설명은 아래에 나와 있습니다:

|**제목 유형**|**설명**|
| :- | :- |

|NumeralsArabic|아랍 유형, 예를 들어, 1,1.1,...|
|NumeralsRomanUppercase|로마 대문자 유형, 예를 들어, I,I.II, ...|
|NumeralsRomanLowercase|로마 소문자 유형, 예를 들어, i,i.ii, ...|
|LettersUppercase|영어 대문자 유형, 예를 들어, A,A.B, ...|
|LettersLowercase|영어 소문자 유형, 예를 들어, a,a.b, ...|
[com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 클래스의 [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 속성은 제목의 번호 스타일을 설정하는 데 사용됩니다.

위 그림에 표시된 출력을 얻기 위한 소스 코드는 아래 예제에 제공됩니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("목록 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("목록 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("각 허용된 것에 대한 계획에 따라 분배될 자산의 계획 기준일 현재의 가치");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```