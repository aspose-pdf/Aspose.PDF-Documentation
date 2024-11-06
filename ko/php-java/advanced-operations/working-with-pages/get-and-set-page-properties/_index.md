---
title: Get and Set Page Properties
type: docs
weight: 30
url: ko/php-java/get-and-set-page-properties/
description: 이 주제는 PDF 파일에서 숫자를 가져오고, 페이지 속성을 얻고 Aspose.PDF for PHP를 통해 Java를 사용하여 페이지 색상을 결정하는 방법을 설명합니다.
lastmod: "2024-06-05"
---

Aspose.PDF for PHP via Java를 사용하면 Java 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 얻고, 색상과 같은 PDF 페이지 속성에 대한 정보를 얻고 페이지 속성을 설정하는 방법을 보여줍니다.

## PDF 파일의 페이지 수 얻기

문서를 사용할 때 종종 몇 페이지로 구성되어 있는지 알고 싶습니다. Aspose.PDF를 사용하면 두 줄의 코드로 이 작업을 수행할 수 있습니다.

PDF 파일의 페이지 수를 얻으려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 파일을 엽니다.
1. 그런 다음 문서의 페이지를 가져옵니다. 가져온 페이지에서 페이지 수를 얻으려고 시도합니다.

다음 코드 스니펫은 PDF 파일의 페이지 수를 얻는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // 페이지 수 얻기
    $responseData = $responseData . "Page Count : " + $pages->size();
```

### 문서를 저장하지 않고 페이지 수 얻기

PDF 파일이 저장되고 모든 요소가 실제로 PDF 파일 내부에 배치되지 않으면 특정 문서에 대한 페이지 수를 얻을 수 없습니다 (모든 요소가 수용될 페이지 수를 확신할 수 없기 때문입니다). 그러나 Aspose.PDF for PHP via Java 릴리스부터, 파일을 저장하지 않고 PDF 문서의 페이지 수를 얻을 수 있는 기능을 제공하는 [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--)라는 메서드를 도입했습니다. 그래서 우리는 즉시 페이지 수 정보를 얻을 수 있습니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용해 보십시오.

```php

    // 문서 열기
    $document = new Document($inputFile);      

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    $page = $document->getPages()->add();
    
    // 300개의 TextFragment 인스턴스를 추가하는 루프 생성
    for ($i=0; $i < 300; $i++) { 
       // PDF의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
       $page->getParagraphs()->add(new TextFragment("Pages count test"));
    }
    
    // 페이지 수 정보를 얻기 위해 단락 처리
    $document->processParagraphs();

    $pages = $document->getPages();

    // 페이지 수 얻기
    $responseData = $responseData . "Page Count : " + $pages->size();
```


## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드 박스, 크롭 박스, 트림 박스와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

### **페이지 속성 이해하기: 아트박스, 블리드 박스, 크롭 박스, 미디어 박스, 트림 박스 및 직사각형 속성의 차이점**

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 다시 말해, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우, PDF에도 블리드 박스가 있습니다.
 Bleed는 페이지의 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양입니다. 이는 문서가 인쇄되고 크기에 맞게 잘려질 때("트림") 잉크가 페이지 가장자리까지 가도록 보장하기 위해 사용됩니다. 페이지가 잘못 잘려서 트림 마크에서 약간 벗어나 잘리더라도 페이지에 흰색 가장자리가 나타나지 않습니다.

- **Trim box**: Trim box는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **Art box**: Art box는 문서의 실제 페이지 내용 주위에 그려진 상자입니다. 이 페이지 상자는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **Crop box**: Crop box는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 crop box의 내용만 표시됩니다. 이 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.

자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하세요.

### 페이지 속성 접근

다음 코드 스니펫은 문서의 특정 페이지에 대해 ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, 페이지 번호 및 회전과 같은 속성을 가져옵니다. 그런 다음 추출된 데이터를 별도의 변수에 저장하고 이를 응답 문자열로 연결합니다.

1. $inputFile 변수를 사용하여 새 Document 객체를 만듭니다.
1. getPages() 메서드를 사용하여 문서에서 페이지 컬렉션을 가져옵니다.
1. get_Item() 메서드를 사용하여 페이지 컬렉션에서 특정 페이지를 가져옵니다.
1. 특정 페이지 객체에서 다양한 속성(ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, 페이지 번호, 회전)을 추출하고 이를 별도의 변수에 저장합니다.
1. 코드가 추출된 속성 값을 개별 응답 문자열($responseData1, $responseData2 등)로 연결합니다.
1. 다음으로, $pages 객체에서 size() 메소드를 사용하여 페이지 수를 가져오려고 시도하지만, $pages 변수가 정의되어 있지 않습니다.

다음 코드 스니펫은 페이지 속성을 가져오는 방법을 보여줍니다.

```php

   // 문서 열기
    $document = new Document($inputFile);

    // 페이지 컬렉션 가져오기
    $pageCollection = $document->getPages();

    // 특정 페이지 가져오기
    $page = $pageCollection->get_Item(1);

    // 페이지 속성 가져오기
    $responseData1 = "ArtBox : Height = " . $page->getArtBox()->getHeight()
        . ", Width = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Height = " . $page->getBleedBox()->getHeight() . ", Width = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Height = " . $page->getCropBox()->getHeight() . ", Width = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Height = " . $page->getMediaBox()->getHeight() . ", Width = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Height = " . $page->getTrimBox()->getHeight() . ", Width = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Height = " . $page->getRect()->getHeight() . ", Width = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Page Number :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotate :-" . $page->getRotate() . PHP_EOL;

    // 페이지 수 가져오기
    $responseData8 = $responseData8 . "Page Count : " . $pages->size();
```


## 페이지 색상 결정

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스는 PDF 문서의 특정 페이지와 관련된 속성을 제공하며, 페이지가 사용하는 색상 유형 - RGB, 흑백, 그레이스케일 또는 미정 - 을 포함합니다.

PDF 파일의 모든 페이지는 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 컬렉션에 포함되어 있습니다. [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 속성은 페이지 상의 요소의 색상을 지정합니다. 특정 PDF 페이지의 색상 정보를 가져오거나 결정하려면 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스 객체의 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 속성을 사용합니다.

다음 코드 스니펫은 PDF 파일의 개별 페이지를 반복하여 색상 정보를 얻는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // PDF 파일의 모든 페이지 반복
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // 특정 PDF 페이지의 색상 유형 정보 가져오기
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="페이지 # -" . $pageCount . " 은(는) 흑백입니다..";
                break;
            case 1:
                $responseData ="페이지 # -" . $pageCount . " 은(는) 그레이 스케일입니다...";
                break;
            case 0:
                $responseData ="페이지 # -" . $pageCount . " 은(는) RGB입니다..";
                break;
            case 3:
                $responseData ="페이지 # -" . $pageCount . " 색상이 미정입니다..";
                break;
        }
    }
```