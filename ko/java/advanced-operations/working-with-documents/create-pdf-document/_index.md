---
title: 문서 생성
type: docs
weight: 10
url: ko/java/create-pdf-document/
description: Aspose.PDF for Java는 몇 가지 쉬운 단계로 PDF 문서와 검색 가능한 PDF 파일을 생성하는 데 도움을 줍니다.
lastmod: "2021-06-05"
---

이 문서에서는 Aspose.PDF for Java API를 사용하여 Java 애플리케이션에서 PDF 파일을 쉽게 생성하고 읽는 방법을 보여줍니다.

Aspose.PDF for Java API는 Java 애플리케이션 개발자가 애플리케이션에 PDF 문서 처리 기능을 포함하도록 합니다. 기본 머신에 다른 소프트웨어가 설치되지 않아도 PDF 파일을 생성하고 읽는 데 사용할 수 있습니다. Aspose.PDF for Java는 데스크톱, JSP, JSF 애플리케이션과 같은 다양한 Java 애플리케이션 유형에서 사용할 수 있습니다.

## Java를 사용하여 PDF 파일 생성하는 방법

Java를 사용하여 PDF 파일을 생성하기 위해 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 클래스의 객체를 생성합니다.

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) 객체를 Document 객체의 Pages 컬렉션에 추가합니다.
1. 페이지의 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        // 페이지 추가
        Page page = document.getPages().add();
         
        // 새 페이지에 텍스트 추가
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // 업데이트된 PDF 저장
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


이 경우, 우리는 A4 페이지 크기, 세로 방향의 PDF 한 페이지 문서를 만듭니다. 우리의 페이지는 페이지의 왼쪽 상단 부분에 "Hello, World"를 포함할 것입니다.

또한, Aspose.PDF for Java는 검색 가능한 PDF를 만드는 방법을 제공합니다. 다음 코드 스니펫을 배워봅시다:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // 콜백 생성 - PDF 이미지의 텍스트를 인식하는 로직. 외부 OCR이 HOCR 표준(http://en.wikipedia.org/wiki/HOCR)을 지원합니다.
        // 우리는 무료 구글 테서랙트 OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)을 사용했습니다.
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // out.html을 문자열로 읽기
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // 임시 파일 삭제
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // 콜백 종료
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```