---
title: PDF 문서에서 이미지 검색 및 가져오기
linktitle: 이미지 검색 및 가져오기
type: docs
weight: 60
url: ko/java/search-and-get-images-from-pdf-document/
description: 이 섹션에서는 Aspose.PDF for Java 라이브러리를 사용하여 PDF 문서에서 이미지를 검색하고 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
---

[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber)를 사용하여 PDF 문서의 모든 페이지에서 이미지를 검색할 수 있습니다.

문서 전체에서 이미지를 검색하려면:

1. [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 컬렉션의 Accept 메서드를 호출합니다. Accept 메서드는 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) 객체를 매개변수로 받습니다. 이는 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement) 객체의 컬렉션을 반환합니다.
2. ImagePlacements 객체를 순회하면서 그 속성(이미지, 치수, 해상도 등)을 가져옵니다.

다음 코드 스니펫은 문서에서 모든 이미지를 검색하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // 문서 열기
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // 이미지 배치 검색을 수행하기 위한 ImagePlacementAbsorber 객체 생성
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // 모든 페이지에 대해 흡수기를 수락
        doc.getPages().accept(abs);

        // 모든 ImagePlacements를 반복하여 이미지 및 ImagePlacement 속성 가져오기
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // ImagePlacement 객체를 사용하여 이미지 가져오기
            // XImage image = imagePlacement.getImage();

            // 모든 배치에 대한 이미지 배치 속성 표시
            System.out.println("이미지 너비:" + imagePlacement.getRectangle().getWidth());
            System.out.println("이미지 높이:" + imagePlacement.getRectangle().getHeight());
            System.out.println("이미지 LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("이미지 LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("이미지 수평 해상도:" + imagePlacement.getResolution().getX());
            System.out.println("이미지 수직 해상도:" + imagePlacement.getResolution().getY());
        }

    }
}
```

To get an image from an individual page, use the following code:

```java
doc.getPages().get_Item(1).accept(abs)
```

개별 페이지에서 이미지를 가져오려면 다음 코드를 사용하세요: