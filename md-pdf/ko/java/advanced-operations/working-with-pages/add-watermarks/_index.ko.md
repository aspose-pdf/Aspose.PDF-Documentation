---
title: PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 90
url: /java/add-watermarks/
description: 이 기사는 Java를 사용하여 프로그램적으로 PDF에서 아티팩트 작업 및 워터마크 얻기의 기능을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java**는 아티팩트를 사용하여 PDF 문서에 워터마크를 추가할 수 있습니다. 이 기사를 확인하여 작업을 해결하십시오.

Adobe Acrobat으로 생성된 워터마크는 아티팩트라고 하며 (PDF 사양의 14.8.2.2 실제 콘텐츠 및 아티팩트에 설명된 대로) Aspose.PDF는 아티팩트와 작업하기 위해 두 가지 클래스가 있습니다: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 및 [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

특정 페이지의 모든 아티팩트를 얻기 위해, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) 클래스는 Artifacts 속성을 가지고 있습니다.
 이 주제는 PDF 파일에서 아티팩트를 다루는 방법을 설명합니다.

## 아티팩트 작업하기

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 클래스는 다음 속성을 포함합니다:

**Artifact.Type** – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거형의 값을 지원하며, 값에는 Background, Layout, Page, Pagination, Undefined가 포함됩니다).
**Artifact.Subtype** – 아티팩트 하위 유형을 가져옵니다 (Artifact.ArtifactSubtype 열거형의 값을 지원하며, 값에는 Background, Footer, Header, Undefined, Watermark가 포함됩니다).

{{% alert color="primary" %}}

Adobe Acrobat으로 생성된 워터마크는 유형이 Pagination이고 하위 유형이 Watermark임을 참고하세요.

{{% /alert %}}

**Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
**Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용된 경우). 워터마크, 헤더 및 푸터 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.

**Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 있는 경우, 그렇지 않으면 null).**Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.  
**Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.  
**Artifact.Rotation** – 아티팩트의 회전(도 단위, 양수 값은 반시계 방향 회전을 나타냄)을 가져옵니다.  
**Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0에서 1 사이이며, 1은 완전히 불투명합니다.

## 프로그래밍 예제: 워터마크 가져오기

다음 코드 조각은 Java를 사용하여 PDF 파일의 첫 번째 페이지에서 각 워터마크를 가져오는 방법을 보여줍니다.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // 문서 디렉토리 경로.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // 문서 열기
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```