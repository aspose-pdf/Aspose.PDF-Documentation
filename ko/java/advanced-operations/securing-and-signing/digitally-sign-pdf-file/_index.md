---
title: PDF를 디지털 서명하는 방법
linktitle: PDF 디지털 서명
type: docs
weight: 10
url: ko/java/digitally-sign-pdf-file/
description: Java를 사용하여 PDF 문서를 디지털 서명합니다. Java 기반 애플리케이션과 PDF 라이브러리를 사용하여 디지털 서명된 PDF를 확인하거나 검증합니다. PKCS1-인증서로 PDF 파일을 인증할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

서명을 사용하여 PDF 문서에 서명할 때 기본적으로 해당 내용이 "있는 그대로" 유지되어야 함을 확인하게 됩니다. 결과적으로, 이후에 이루어진 모든 변경은 서명을 무효화하며, 이를 통해 문서가 변경되었는지 알 수 있습니다. 문서를 처음 인증하면 사용자가 인증을 무효화하지 않고 문서에 가할 수 있는 변경 사항을 지정할 수 있습니다.

다시 말해, 문서는 여전히 무결성을 유지한다고 간주되며 수신자는 여전히 문서를 신뢰할 수 있습니다. 자세한 내용은 PDF 인증 및 서명을 방문하십시오.

위에 명시된 요구 사항을 충족하기 위해 다음과 같은 공개 API 변경이 이루어졌습니다.

isCertified(…) 메서드가 PdfFileSignature 클래스에 추가되었습니다.

## 디지털 서명으로 PDF 서명하기

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // PKCS7/PKCS7Detached
                                                                                              // 객체 사용
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // 출력 PDF 파일 저장
        signature.save(outFile);
    }
```

## 디지털 서명에 타임스탬프 추가하기

Aspose.PDF for Java는 타임스탬프 서버 또는 웹 서비스를 통해 PDF를 디지털 서명하는 기능을 지원합니다.

이 요구 사항을 충족하기 위해 [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) 클래스가 Aspose.PDF 네임스페이스에 추가되었습니다. PDF 문서에 타임스탬프를 얻고 추가하는 다음 코드 조각을 참조하십시오:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // 사용자/비밀번호는
                                                                                                    // 생략 가능
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // 세 가지 서명 유형 중 하나를 생성합니다
        signature.sign(1, "서명 이유", "연락처", "위치", true, rect, pkcs);
        // 출력 PDF 파일 저장
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```