---
title: PDF에 배경 추가
linktitle: 배경 추가
type: docs
weight: 110
url: /java/add-backgrounds/
descriptions: Java로 PDF 파일에 배경 이미지를 추가하세요. BackgroundArtifact 객체를 사용합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

배경 이미지는 문서에 워터마크 또는 다른 미묘한 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for Java에서는 각 PDF 문서가 페이지의 컬렉션이고 각 페이지는 아티팩트의 컬렉션을 포함합니다. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) 클래스는 페이지 객체에 배경 이미지를 추가하는 데 사용할 수 있습니다.

다음 코드 스니펫은 Java로 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-Java를 참조하세요.
        String myDir = "";
        // 새 Document 객체 생성
        Document doc = new Document();
        // 문서 객체에 새 페이지 추가
        Page page = doc.getPages().add();
        // BackgroundArtifact 객체 생성
        BackgroundArtifact background = new BackgroundArtifact();
        // backgroundartifact 객체에 대한 이미지 지정
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // 페이지의 아티팩트 컬렉션에 backgroundartifact 추가
        page.getArtifacts().add(background);
        // 문서 저장
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```