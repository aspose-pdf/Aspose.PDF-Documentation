---
title: PDF에 배경 추가
linktitle: 배경 추가
type: docs
weight: 110
url: /php-java/add-backgrounds/
descriptions: PHP를 사용하여 PDF 파일에 배경 이미지를 추가합니다. BackgroundArtifact 객체를 사용하세요.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

배경 이미지는 문서에 워터마크나 다른 미묘한 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for PHP via Java에서 각 PDF 문서는 페이지의 모음이며 각 페이지는 아티팩트의 모음으로 구성됩니다. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) 클래스는 페이지 객체에 배경 이미지를 추가하는 데 사용할 수 있습니다.

다음 코드 스니펫은 PHP를 사용하여 BackgroundArtifact 객체를 통해 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서 객체에 새로운 페이지 추가
    $page = $document->getPages()->add();

    // BackgroundArtifact 객체 생성    
    $background = new BackgroundArtifact();

    // backgroundArtifact 객체에 대한 이미지 지정
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // 페이지의 아티팩트 컬렉션에 backgroundArtifact 추가
    $page->getArtifacts()->add($background);

    // 업데이트된 PDF 파일 저장
    $document->save($outputFile);
    $document->close();
```