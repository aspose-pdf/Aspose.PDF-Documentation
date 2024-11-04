---
title: PDF에 이미지 스탬프 프로그래밍 방식으로 추가하기
linktitle: PDF 파일에 이미지 스탬프
type: docs
weight: 10
url: /php-java/image-stamps-in-pdf-page/
description: Aspose.PDF for PHP via Java 라이브러리를 사용하여 ImageStamp 클래스로 PDF 문서에 이미지 스탬프를 추가하세요.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 이미지 스탬프 추가하기

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스를 사용하여 PDF 문서에 이미지를 스탬프로 추가할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스는 높이, 너비, 불투명도 등을 지정하는 메서드를 제공합니다.

이미지 스탬프를 추가하려면:

1. 필요한 속성을 사용하여 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 ImageStamp 객체를 생성합니다.

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 메서드를 호출하여 PDF에 스탬프를 추가합니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // 이미지 스탬프 생성
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // 특정 페이지에 스탬프 추가
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close()
```

## 스탬프 추가 시 이미지 품질 제어

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스는 PDF 문서에 스탬프로 이미지를 추가할 수 있습니다.
 이미지를 PDF 파일의 워터마크로 추가할 때 이미지 품질을 제어할 수 있습니다. 이를 위해 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스에 setQuality(...)라는 메서드가 추가되었습니다. 유사한 메서드는 com.aspose.pdf.facades 패키지의 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) 클래스에서도 찾을 수 있습니다.

다음 코드 스니펫은 PDF 파일에 스탬프로 추가할 때 이미지 품질을 제어하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // 이미지 스탬프 생성
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();        
```

## 부동 상자에서 배경으로 이미지 스탬프

Aspose.PDF API를 사용하면 부동 상자에서 배경으로 이미지 스탬프를 추가할 수 있습니다. FloatingBox 클래스의 BackgroundImage 속성은 다음 코드 샘플과 같이 플로팅 박스에 배경 이미지 스탬프를 설정하는 데 사용할 수 있습니다.

이 코드 스니펫은 PDF 문서를 생성하고 여기에 FloatingBox를 추가하는 과정을 보여줍니다. FloatingBox는 텍스트 조각, 테두리, 배경 이미지 및 배경 색상을 포함합니다. 생성된 문서는 출력 파일로 저장됩니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // PDF 문서에 페이지 추가
    $page = $pages->add();

    // FloatingBox 객체 생성
    $aBox = new FloatingBox(200, 100);

    // FloatingBox의 왼쪽 위치 설정
    $aBox->setLeft(40);

    // FloatingBox의 상단 위치 설정
    $aBox->setTop(80);

    // FloatingBox의 수평 정렬 설정
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // FloatingBox의 단락 컬렉션에 텍스트 조각 추가
    $aBox->getParagraphs()->add(new TextFragment("main text"));

    // FloatingBox에 테두리 설정
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // 배경 이미지 추가
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // FloatingBox의 배경 색상 설정
    $aBox->setBackgroundColor($colors->getYellow());

    // 페이지 객체의 단락 컬렉션에 FloatingBox 추가
    $page->getParagraphs()->add($aBox);
    
    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```