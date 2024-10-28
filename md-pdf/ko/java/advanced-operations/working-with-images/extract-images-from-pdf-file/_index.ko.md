---
title: PDF 파일에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: 이 섹션에서는 Java 라이브러리를 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.
lastmod: "2021-06-05"
---

각 페이지는 [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 컬렉션을 보유하고 있으며, 이는 다시 페이지의 모든 이미지가 저장되는 Images 컬렉션을 보유합니다. [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) 객체는 Images 컬렉션에서 주어진 이미지를 가져옵니다.

페이지에서 이미지를 추출하려면:

이미지 인덱스를 사용하여 Images 컬렉션에서 이미지를 가져옵니다.
추출한 이미지를 저장하기 위해 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) 객체의 save(..) 메소드를 사용합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // 특정 이미지 추출
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // 출력 이미지 저장
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // 업데이트된 PDF 파일 저장
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```