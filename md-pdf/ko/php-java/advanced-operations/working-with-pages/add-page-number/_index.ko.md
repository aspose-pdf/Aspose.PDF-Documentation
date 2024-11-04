---
title: PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 100
url: /php-java/add-page-number/
description: Aspose.PDF for PHP via Java를 사용하여 PageNumber Stamp 클래스를 통해 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 다양한 부분을 쉽게 찾을 수 있도록 도와줍니다.
**Aspose.PDF for PHP via Java**는 PageNumberStamp를 사용하여 페이지 번호를 추가할 수 있습니다.

{{% alert color="primary" %}}

온라인으로 시도해보세요. 이 링크에서 Aspose.PDF 변환의 품질을 확인하고 결과를 온라인으로 볼 수 있습니다 [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 클래스를 사용하여 PDF 문서에 페이지 번호 스탬프를 추가할 수 있습니다.
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 클래스는 형식, 여백, 정렬, 시작 번호 등 페이지 번호 기반의 스탬프를 생성하는 메서드를 제공합니다. 페이지 번호 스탬프를 추가하려면, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 필요한 텍스트 속성을 가진 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 객체를 만들어야 합니다. 그 후, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 메서드를 호출하여 PDF 파일에 스탬프를 추가할 수 있습니다. 또한 페이지 번호 스탬프의 폰트 속성을 설정할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 페이지 번호 스탬프 생성
    $pageNumberStamp = new PageNumberStamp();

    // 스탬프가 배경인지 여부
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # of " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // 텍스트 속성 설정
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // 특정 페이지에 스탬프 추가
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```