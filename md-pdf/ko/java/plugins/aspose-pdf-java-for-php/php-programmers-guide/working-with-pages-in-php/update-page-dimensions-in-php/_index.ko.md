---
title: PHP에서 페이지 크기 업데이트
type: docs
weight: 90
url: /java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 크기 업데이트

**Aspose.PDF Java for PHP**를 사용하여 페이지 크기를 업데이트하려면, **UpdatePageDimensions** 클래스를 호출하세요.

PHP 코드

```php

# 대상 문서 열기
$pdf = new Document($dataDir . 'input1.pdf');

# 페이지 컬렉션 가져오기
$page_collection = $pdf->getPages();

# 특정 페이지 가져오기
$pdf_page = $page_collection->get_Item(1);

# 페이지 크기를 A4 (11.7 x 8.3 인치)로 설정하기, Aspose.PDF에서는 1 인치 = 72 포인트
# 따라서 A4 크기는 포인트로 (842.4, 597.6)입니다
$pdf_page->setPageSize(597.6,842.4);

# 새로 생성된 PDF 파일 저장
$pdf->save($dataDir . "output.pdf");

print "크기가 성공적으로 업데이트되었습니다!" . PHP_EOL;

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **페이지 크기 업데이트 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)