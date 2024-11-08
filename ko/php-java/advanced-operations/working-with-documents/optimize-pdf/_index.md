---
title: PHP에서 PDF 크기 최적화, 압축 또는 줄이기
linktitle: PDF 문서 최적화
type: docs
weight: 40
url: /ko/php-java/optimize-pdf/
description: PHP를 사용하여 PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 글꼴 임베드 해제, 사용되지 않는 객체 제거.
lastmod: "2024-06-05"
---

PDF 문서는 때때로 추가 데이터를 포함할 수 있습니다. PDF 파일 크기를 줄이면 네트워크 전송 및 저장을 최적화하는 데 도움이 됩니다. 이는 웹 페이지에 게시하거나, 소셜 네트워크에서 공유하거나, 이메일로 보내거나, 저장소에 보관할 때 특히 유용합니다. 우리는 PDF를 최적화하기 위해 여러 기술을 사용할 수 있습니다:

- 온라인 브라우징에 맞게 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 글꼴 임베드 해제
- 사용되지 않는 객체 제거
- 평탄화된 양식 필드 제거
- 주석 제거 또는 평탄화

## 웹용 PDF 문서 최적화

최적화 또는 선형화는 웹 브라우저를 사용한 온라인 브라우징에 적합한 PDF 파일을 만드는 과정을 의미합니다.
 Aspose.PDF는 이 프로세스를 지원합니다.

웹 디스플레이를 위해 PDF를 최적화하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체에서 입력 문서를 엽니다.
1. [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) 메서드를 사용합니다.
1. save(..) 메서드를 사용하여 최적화된 문서를 저장합니다.

다음 코드 스니펫은 웹을 위해 PDF 문서를 최적화하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 웹을 위해 최적화
    $document->optimize();

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## PDF 파일 크기 줄이기

이 주제는 PDF 파일 크기를 최적화/줄이는 단계를 설명합니다. Aspose.PDF API는 불필요한 객체를 제거하고 이미지를 포함한 PDF 파일을 압축하여 출력 PDF를 최적화할 수 있는 유연성을 제공하는 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) 클래스를 제공합니다. 이 두 가지 옵션은 다음 섹션에서 설명됩니다.

### 불필요한 객체 제거

중복되고 사용되지 않는 객체를 제거하여 PDF 문서의 크기를 최적화할 수 있습니다. 다음 코드 스니펫은 그 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // PDF 문서 최적화. 그러나 이 메서드가 문서 축소를 보장할 수 없음을 유의하십시오.
    $document->optimizeResources();

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();

```

## 모든 이미지 축소 또는 압축

원본 PDF 파일에 이미지가 포함되어 있는 경우 이미지를 압축하고 품질을 설정하는 것을 고려하십시오. 이미지 압축을 활성화하려면 setCompressImages(..) 메서드에 true를 인수로 전달하십시오. 문서의 모든 이미지는 다시 압축됩니다. 압축은 setImageQuality(..) 메서드에 의해 정의되며, 이는 품질의 백분율 값입니다. 100%는 변경되지 않은 품질과 이미지 크기입니다. 이미지 크기를 줄이려면 setImageQuality(..) 메서드에 100 미만의 인수를 전달하십시오.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();

    // CompressImages 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // ImageQuality 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

또 다른 방법은 더 낮은 해상도로 이미지를 크기 조정하는 것입니다. 이 경우, ResizeImages를 true로 설정하고 MaxResolution을 적절한 값으로 설정해야 합니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();

    // CompressImages 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // ImageQuality 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // ResizeImage 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // MaxResolution 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

또 다른 중요한 문제는 실행 시간입니다. 하지만 다시 말하지만, 이 설정도 관리할 수 있습니다. 현재 우리는 두 가지 알고리즘 - 표준과 빠른 알고리즘 - 을 사용할 수 있습니다. 실행 시간을 제어하려면 Version 속성을 설정해야 합니다. 다음 스니펫은 빠른 알고리즘을 보여줍니다:

```php
    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new optimization_OptimizationOptions();

    // CompressImages 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // ImageQuality 옵션 설정
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // 이미지 압축 버전을 빠르게 설정
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## 사용되지 않는 객체 제거

PDF 문서는 때때로 문서의 다른 어떤 객체에서도 참조되지 않는 PDF 객체를 포함할 수 있습니다. 예를 들어, 페이지가 문서 페이지 트리에서 제거되었지만 페이지 객체 자체는 제거되지 않은 경우에 발생할 수 있습니다. 이러한 객체를 제거하는 것은 문서를 무효화하지 않으며 오히려 문서의 크기를 줄입니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // 최적화 옵션 초기화
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // 최적화 옵션을 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## 사용되지 않는 스트림 제거

때때로 문서에는 사용되지 않는 리소스 스트림이 포함될 수 있습니다.
 이러한 스트림은 페이지의 리소스 사전에서 참조되기 때문에 "미사용 객체"가 아닙니다. 이는 이미지가 페이지에서 제거되었지만 페이지 리소스에서는 제거되지 않은 경우에 발생할 수 있습니다. 또한 문서에서 페이지가 추출되고 문서 페이지에 "공통" 리소스, 즉 동일한 Resources 객체가 있는 경우 이러한 상황이 자주 발생합니다. 리소스 스트림이 사용되는지 여부를 판단하기 위해 페이지 내용을 분석합니다. 사용되지 않는 스트림은 제거됩니다. 때로는 이것이 문서 크기를 줄입니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## 중복 스트림 연결

때때로 문서에는 여러 개의 동일한 리소스 스트림(예: 이미지)이 포함되어 있습니다. 이것은 예를 들어 문서가 자기 자신과 연결될 때 발생할 수 있습니다. 출력 문서에는 동일한 리소스 스트림의 두 개의 독립적인 복사본이 포함됩니다. 우리는 모든 리소스 스트림을 분석하고 비교합니다. 스트림이 중복되면 병합되어 한 개의 복사본만 남고, 참조가 적절히 변경되며 객체의 복사본이 제거됩니다. 때때로 이는 문서 크기를 줄입니다.

```php
    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

또한, AllowReusePageContent 설정을 사용할 수 있습니다. 이 속성이 true로 설정되면 동일한 페이지에 대해 문서를 최적화할 때 페이지 콘텐츠가 재사용됩니다.

```php
    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## 글꼴 비내장화

문서가 내장 글꼴을 사용한다는 것은 모든 글꼴 데이터가 문서에 포함되어 있다는 것을 의미합니다. 이점은 사용자의 컴퓨터에 글꼴이 설치되어 있지 않더라도 문서를 볼 수 있다는 것입니다. 하지만 글꼴을 내장하면 문서가 더 커집니다. 글꼴 비내장화 메소드는 모든 내장 글꼴을 제거합니다. 이는 문서 크기를 줄이지만 올바른 글꼴이 설치되어 있지 않으면 문서가 읽을 수 없게 될 수 있습니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $document->optimizeResources($optimizationOptions);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## 주석 제거 또는 평면화

주석은 불필요할 때 삭제할 수 있습니다.
 필요할 때 추가 편집이 필요하지 않으면 평탄화할 수 있습니다. 이 두 가지 기술 모두 파일 크기를 줄여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## 양식 필드 제거

PDF 문서에 AcroForms가 포함되어 있다면, 양식 필드를 평탄화하여 파일 크기를 줄일 수 있습니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // 양식 평탄화
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## RGB 색상 공간의 PDF를 그레이스케일로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다. RGB 색상 공간의 PDF를 그레이스케일로 변환해야 하는 요구 사항이 있을 수 있습니다. 이렇게 하면 이러한 PDF 파일을 인쇄할 때 더 빨라집니다. 또한 파일이 그레이스케일로 변환되면 문서의 크기도 줄어들지만 이로 인해 문서의 품질이 떨어질 수 있습니다. 현재 이 기능은 Adobe Acrobat의 프리플라이트 기능에서 지원되지만, Office 자동화에 대해 이야기할 때 Aspose.PDF는 문서 조작을 위한 이러한 이점을 제공하는 궁극적인 솔루션입니다.

이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용할 수 있습니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```


## FlateDecode 압축

Aspose.PDF for PHP via Java는 PDF 최적화 기능을 위한 FlateDecode 압축을 지원합니다. 아래의 코드 스니펫은 FlateDecode 압축으로 이미지를 저장하기 위해 최적화에서 옵션을 사용하는 방법을 보여줍니다:

```php

    // 문서 열기
    $document = new Document($inputFile);

    // OptimizationOptions 초기화
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // OptimizationOptions를 사용하여 PDF 문서 최적화
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## XImageCollection에 이미지 저장

Aspose.PDF for PHP via Java는 FlateDecode 압축을 사용하여 새 이미지를 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection)에 저장하는 기능을 제공합니다.
 이 옵션을 활성화하려면 ImageFilterType.Flate 플래그를 사용할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

```php
    // 문서 열기
    $document = new Document($inputFile);

    // 문서 초기화
    $page = $document->getPages()->get_Item(1);

    // 이미지를 스트림에 로드
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // 좌표 설정
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // ConcatenateMatrix(행렬 연결) 연산자 사용: 이미지가 배치되어야 하는 방식을 정의
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```