---
title: PDF/A를 PDF 형식으로 변환 
linktitle: PDF/A를 PDF 형식으로 변환
type: docs
weight: 110
url: ko/php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: 이 주제는 Aspose.PDF가 PHP 라이브러리로 PDF/A 파일을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A 문서를 PDF로 변환

PDF/A 문서를 PDF로 변환하는 것은 원본 문서에서 <abbr title="Portable Document Format Archive">PDF/A</abbr> 제한을 제거하는 것을 의미합니다. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스에는 입력/소스 파일에서 PDF 준수 정보를 제거하는 removePdfaCompliance(..) 메서드가 있습니다.

```php
// 입력 파일로 Document 클래스의 새 인스턴스를 만듭니다.
$document = new Document($inputFile);

// 문서에서 PDF/A 준수를 제거합니다.
$document->removePdfaCompliance();

// 수정된 문서를 출력 파일에 저장합니다.
$document->save($outputFile);
```

이 정보는 문서에 변경 사항을 가할 때도 제거됩니다 (예:
 페이지를 추가). 다음 예제에서 출력 문서는 페이지를 추가한 후 PDF/A 호환성을 잃습니다.

```php
// 입력 파일로 Document 클래스의 새 인스턴스를 생성합니다
$document = new Document($inputFile);

// 문서에서 PDF/A 호환성을 제거합니다
$document->getPages()->add();

// 수정된 문서를 출력 파일에 저장합니다
$document->save($outputFile);
```