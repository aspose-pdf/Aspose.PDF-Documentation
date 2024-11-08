---
title: PDF 문서에서 썸네일 이미지 생성
linktitle: 썸네일 이미지 생성
type: docs
weight: 100
url: /ko/java/generate-thumbnail-images-from-pdf-documents/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 썸네일 이미지를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

## Aspose.PDF for Java 접근법

Aspose.PDF for Java는 PDF 문서를 다루기 위한 광범위한 지원을 제공합니다. 또한 PDF 문서의 페이지를 다양한 이미지 형식으로 변환하는 기능도 지원합니다. 위에서 설명한 기능은 Aspose.PDF for Java를 사용하여 쉽게 구현할 수 있습니다.

Aspose.PDF는 다음과 같은 뚜렷한 장점이 있습니다:

- 시스템에 Adobe Acrobat을 설치하지 않고도 PDF 파일을 작업할 수 있습니다.
- Aspose.PDF for Java를 사용하는 것은 Acrobat Automation에 비해 간단하고 이해하기 쉽습니다.

PDF 페이지를 JPEG로 변환해야 하는 경우, [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) 네임스페이스는 PDF 페이지를 JPEG 이미지로 렌더링하기 위한 클래스인 [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice)를 제공합니다.
 다음 코드 스니펫을 살펴보세요.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // 특정 디렉토리에서 모든 PDF 파일의 이름을 가져옴
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // 디렉토리를 읽는 동안 오류 발생
        }

        // 배열의 모든 파일 항목을 반복
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // 문서 열기
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Resolution 객체 생성
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // 특정 페이지를 변환하고 이미지를 스트림에 저장
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // 스트림 닫기
                imageStream.close();
            }
        }

    }
}
```