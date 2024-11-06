---
title: 기존 PDF 파일의 이미지 교체
linktitle: 이미지 교체
type: docs
weight: 70
url: ko/java/replace-image-in-existing-pdf-file/
description: 이 섹션에서는 Java 라이브러리를 사용하여 기존 PDF 파일의 이미지를 교체하는 방법에 대해 설명합니다.
lastmod: "2021-06-05"
---

[XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) 컬렉션의 [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) 메서드를 사용하면 기존 PDF 파일의 이미지를 교체할 수 있습니다.

이미지 컬렉션은 페이지의 리소스 컬렉션에 있습니다. 이미지를 교체하려면:

1. Document 객체를 사용하여 PDF 파일을 엽니다.
2. 특정 이미지를 교체하고, Document 객체의 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 교체하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // 문서 열기
        Document pdfDocument = new Document("input.pdf");
        // 특정 이미지 교체
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO 자동 생성된 catch 블록
            e.printStackTrace();
        }
        // 업데이트된 PDF 파일 저장
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```