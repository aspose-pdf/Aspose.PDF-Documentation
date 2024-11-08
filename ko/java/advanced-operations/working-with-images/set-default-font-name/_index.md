---
title: 기본 글꼴 이름 설정
linktitle: 기본 글꼴 이름 설정
type: docs
weight: 90
url: /ko/java/set-default-font-name/
description: 이 섹션에서는 Aspose.PDF for Java 라이브러리를 사용하여 기본 글꼴 이름을 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

**Aspose.PDF for Java** API는 문서에 글꼴이 없을 때 기본 글꼴 이름을 설정할 수 있게 해줍니다. [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) 클래스의 [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) 메서드를 사용하여 기본 글꼴 이름을 설정할 수 있습니다. setDefaultFontName이 null로 설정된 경우 **Times New Roman** 글꼴이 사용됩니다.

다음 코드 스니펫은 PDF를 이미지로 저장할 때 기본 글꼴 이름을 설정하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

public class ExampleSetDefaultFontName {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SetDefaultFontName() {
        
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        FileOutputStream imageStream = null;;
        try {
            imageStream = new FileOutputStream(_dataDir + "SetDefaultFontName.png");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        RenderingOptions ro = new RenderingOptions();
        ro.setDefaultFontName ("Arial");
        pngDevice.setRenderingOptions(ro);
        pngDevice.process(pdfDocument.getPages().get_Item(1), imageStream);
    }    
}
```