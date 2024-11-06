---
title: 기존 PDF에 TOC 추가하기 PHP에서
type: docs
weight: 20
url: ko/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - TOC 추가

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에 TOC를 추가하려면, 간단히 **AddToc** 클래스를 호출하세요.

PHP 코드

```php

# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

# PDF 파일의 첫 번째 페이지에 접근합니다.
$toc_page = $doc->getPages()->insert(1);

# TOC 정보를 나타내는 객체를 생성합니다.
$toc_info = new TocInfo();
$title = new TextFragment("목차");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# TOC의 제목을 설정합니다.
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# TOC 요소로 사용될 문자열 객체를 생성합니다.
$titles = array("첫 번째 페이지", "두 번째 페이지");

$i = 0;
while ($i < 2){

    # Heading 객체를 생성합니다.
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Heading 객체의 목적지 페이지를 지정합니다.
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # 목적지 페이지
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # 목적지 좌표
    $segment2->setText($titles[$i]);

    # TOC가 포함된 페이지에 헤딩을 추가합니다.
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# PDF 문서를 저장합니다.
$doc->save($dataDir . "TOC.pdf");

print "TOC가 성공적으로 추가되었습니다. 출력 파일을 확인하세요.";

```


**코드 실행 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Add TOC (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)