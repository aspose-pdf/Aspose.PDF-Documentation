---
title: PDF에서 이미지 추출 
linktitle: 이미지 추출
type: docs
weight: 20
url: /php-java/extract-images-from-the-pdf-file/
description: Aspose.PDF for PHP를 사용하여 PDF에서 이미지의 일부를 추출하는 방법
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 문서의 각 페이지는 리소스(이미지, 폼 및 폰트)를 포함하고 있습니다. 이러한 리소스에 액세스하기 위해 [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 메서드를 호출할 수 있습니다. 클래스 [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)는 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection)을 포함하고 있으며, [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) 메서드를 호출하여 이미지 목록을 얻을 수 있습니다.

따라서 페이지에서 이미지를 추출하기 위해, 페이지에 대한 참조를 얻고, 다음으로 페이지 리소스와 마지막으로 이미지 컬렉션에 대한 참조를 얻어야 합니다.
특정 이미지는 예를 들어 인덱스로 추출할 수 있습니다.

이미지의 인덱스는 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) 객체를 반환합니다.
This object provides a [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

```php

    // PDF 문서 로드
    $document = new Document($inputFile);

    // 문서의 첫 페이지 가져오기
    $page = $document->getPages()->get_Item(1);

    // 페이지의 이미지 컬렉션 가져오기
    $xImageCollection = $page->getResources()->getImages();

    // 컬렉션에서 첫 번째 이미지 가져오기
    $xImage = $xImageCollection->get_Item(1);

    // 이미지를 저장할 새로운 FileOutputStream 객체 생성
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // 이미지를 출력 파일에 저장
    $xImage->save($outputImage);

    // 출력 이미지 파일 닫기
    $outputImage->close();
```