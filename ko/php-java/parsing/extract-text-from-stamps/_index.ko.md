---
title: 스탬프에서 텍스트 추출
type: docs
weight: 60
url: /php-java/extract-text-from-stamps/
---

## 스탬프 주석에서 텍스트 추출

Aspose.PDF for PHP via Java는 스탬프 주석에서 텍스트를 추출할 수 있게 해줍니다. PDF에서 스탬프 주석에서 텍스트를 추출하려면 다음 단계를 사용할 수 있습니다.

1. PDF 문서를 로드합니다
1. 문서의 원하는 페이지를 가져옵니다
1. StampAnnotation 클래스의 새 인스턴스를 만듭니다
1. AnnotationSelector 클래스의 새 인스턴스를 만들고 스탬프 주석을 전달합니다
1. 페이지에서 주석 선택기를 수락합니다
1. 선택된 스탬프 주석을 가져옵니다
1. TextAbsorber 클래스의 새 인스턴스를 만듭니다
1. 첫 번째 스탬프 주석을 가져옵니다
1. 스탬프 주석의 일반적인 모양을 가져옵니다
1. 텍스트 흡수기를 사용하여 모양을 방문합니다
1. 텍스트 흡수기에서 추출한 텍스트를 가져옵니다
1. 문서를 닫습니다

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```