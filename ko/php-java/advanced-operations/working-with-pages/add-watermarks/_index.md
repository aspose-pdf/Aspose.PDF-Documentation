---
title: PDF에 워터마크 추가  
linktitle: 워터마크 추가  
type: docs  
weight: 90  
url: /ko/php-java/add-watermarks/  
description: 이 문서는 PHP를 사용하여 PDF에서 아티팩트 작업 및 워터마크 얻기 기능을 설명합니다.  
lastmod: "2024-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

**Aspose.PDF for PHP via Java**는 아티팩트를 사용하여 PDF 문서에 워터마크를 추가할 수 있습니다. 이 문서를 확인하여 작업을 해결하세요.

Adobe Acrobat으로 생성된 워터마크는 PDF 사양의 14.8.2.2 실제 콘텐츠 및 아티팩트에서 설명된 대로 아티팩트라고 합니다. 아티팩트 작업을 위해 Aspose.PDF는 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 클래스와 [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection) 클래스를 제공합니다.

특정 페이지의 모든 아티팩트를 얻으려면, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) 클래스에 Artifacts 속성이 있습니다.
 이 주제는 PDF 파일에서 아티팩트 작업하는 방법을 설명합니다.

## 아티팩트 작업하기

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 클래스는 다음 속성을 포함합니다:

**Artifact.Type** – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거형의 값을 지원하며, 값에는 Background, Layout, Page, Pagination 및 Undefined가 포함됩니다).
**Artifact.Subtype** – 아티팩트 하위 유형을 가져옵니다 (Artifact.ArtifactSubtype 열거형의 값을 지원하며, 값에는 Background, Footer, Header, Undefined, Watermark가 포함됩니다).

{{% alert color="primary" %}}

Adobe Acrobat으로 생성된 워터마크는 Pagination 유형과 Watermark 하위 유형을 가집니다.

{{% /alert %}}

**Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
**Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용되는 경우). 워터마크, 헤더 및 푸터 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.

**Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 있는 경우, 그렇지 않으면 null).**Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.  
**Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.  
**Artifact.Rotation** – 아티팩트의 회전(도 단위, 양수는 시계 반대 방향 회전을 나타냄)을 가져옵니다.  
**Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0에서 1 사이이며, 1은 완전히 불투명합니다.

## 프로그래밍 샘플: 워터마크 가져오기

다음 코드 스니펫은 PHP로 PDF 파일의 첫 페이지에 있는 각 워터마크를 가져오는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```