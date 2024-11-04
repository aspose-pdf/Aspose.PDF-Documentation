---
title: PDF 문서 저장
linktitle: 저장
type: docs
weight: 30
url: /java/save-pdf-document/
description: Aspose.PDF for Java 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 파일 시스템에 PDF 문서 저장

생성되거나 조작된 PDF 문서를 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 Save 메서드를 사용하여 파일 시스템에 저장할 수 있습니다.
형식 유형(옵션)을 제공하지 않으면 문서는 Aspose.PDF v.1.7 (*.pdf) 형식으로 저장됩니다.

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // 몇 가지 조작 수행, 예를 들어 새 빈 페이지 추가
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## PDF 문서를 스트림에 저장

Save 메서드의 오버로드를 사용하여 생성되거나 조작된 PDF 문서를 스트림에 저장할 수도 있습니다.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // 일부 조작 수행, 예: 새 빈 페이지 추가
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## 웹 애플리케이션에서 PDF 문서 저장

웹 애플리케이션에서 문서를 저장하려면 위에서 제안한 방법을 사용할 수 있습니다. 또한, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스에는 오버로드된 Save 메서드가 있습니다.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // 파일을 InputStream으로 가져오기
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // 이를 response의 OutputStream으로 복사
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("파일을 출력 스트림에 쓰는 중 오류 발생. 파일 이름은 '{}'", fileName, ex);
    //         throw new RuntimeException("파일을 출력 스트림에 쓰는 IO 오류");
    //     }
    // }
```


더 자세한 설명은 [Showcase]() 섹션을 참조하십시오.

## PDF/A 또는 PDF/X 형식으로 저장

PDF/A는 전자 문서의 보관 및 장기 보존을 위해 사용되는 PDF(Portable Document Format)의 ISO 표준화된 버전입니다. PDF/A는 장기 보관에 적합하지 않은 기능(예: 글꼴 연결 대신 글꼴 포함 및 암호화)을 금지한다는 점에서 PDF와 다릅니다. PDF/A 뷰어에 대한 ISO 요구 사항에는 색상 관리 지침, 포함된 글꼴 지원 및 포함된 주석을 읽기 위한 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다. PDF/X의 목적은 그래픽 교환을 촉진하는 것이므로 일반 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항이 있습니다.

두 경우 모두 문서를 저장하는 데 Save 메서드가 사용되며, 문서는 Convert 메서드를 사용하여 준비해야 합니다.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```