---
title: PDF 파일에서 서명 작업
type: docs
weight: 40
url: ko/java/working-with-signature-in-a-pdf-file/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 PDF 파일에서 서명 작업을 수행하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 서명 정보 추출 방법

Aspose.PDF for Java는 PdfFileSignature 클래스를 사용하여 PDF 파일에 디지털 서명을 지원합니다. 현재, 인증서의 유효성을 확인하는 것은 가능하지만 전체 인증서를 추출할 수는 없습니다. 추출 가능한 정보는 공개 키, 지문, 발급자 등이 있습니다.

서명 정보를 추출하기 위해, 우리는 PdfFileSignature 클래스에 extractCertificate(..) 메서드를 도입했습니다. 다음 코드 스니펫은 PdfFileSignature 객체에서 인증서를 추출하는 단계를 보여줍니다:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## 서명 필드에서 이미지 추출(PdfFileSignature)

Aspose.PDF for Java는 PdfFileSignature 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원하며, 문서에 서명할 때 SignatureAppearance에 대한 이미지를 설정할 수 있습니다. 이제 이 API는 서명 필드와 관련된 이미지뿐만 아니라 서명 정보를 추출할 수 있는 기능도 제공합니다.

서명 정보를 추출하기 위해 우리는 PdfFileSignature 클래스에 [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) 메서드를 도입했습니다. PdfFileSignature 객체에서 이미지를 추출하는 단계를 보여주는 다음 코드 조각을 참조하십시오:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## 위치 및 사유 억제

Aspose.PDF 기능은 디지털 서명 인스턴스에 대한 유연한 구성을 허용합니다. [PdfFileSignature ](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 클래스는 PDF 파일에 서명할 수 있는 기능을 제공합니다. 서명 메서드 구현은 PDF에 서명하고 특정 서명 객체를 이 클래스에 전달할 수 있게 합니다. 서명 메서드는 출력 디지털 서명의 사용자 정의를 위한 속성 세트를 포함합니다. 결과 서명에서 일부 텍스트 속성을 억제해야 하는 경우, 해당 속성을 비워둘 수 있습니다. 다음 코드 스니펫은 서명 블록에서 위치와 사유 두 행을 억제하는 방법을 보여줍니다:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 서명 위치에 대한 사각형 생성
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // 서명 외관 설정
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // 세 가지 서명 유형 중 하나 생성
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // 출력 PDF 파일 저장
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## 디지털 서명의 사용자 정의 기능

Aspose.PDF for Java는 디지털 서명을 위한 사용자 정의 기능을 제공합니다. SignatureCustomAppearance 클래스의 Sign 메서드는 사용자의 편의를 위해 6가지 오버로드로 구현됩니다. 예를 들어, SignatureCustomAppearance 클래스 인스턴스와 그 속성 값만으로 결과 서명을 구성할 수 있습니다. 다음 코드 스니펫은 PDF의 출력 디지털 서명에서 "디지털 서명됨" 캡션을 숨기는 방법을 보여줍니다.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 서명 위치를 위한 사각형 생성
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // 세 가지 서명 유형 중 하나 생성
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("SIGNED BY:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // 출력 PDF 파일 저장
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## 디지털 서명 텍스트의 언어 변경

Aspose.PDF for Java API를 사용하면 다음 세 가지 유형의 서명을 사용하여 PDF 파일에 서명할 수 있습니다:

- PKCS#1
- PKCS#7
- PKCS#7

제공된 서명 각각에는 편의를 위해 구현된 설정 속성 집합이 포함되어 있습니다(지역화, 날짜 시간 형식, 글꼴 패밀리 등). 클래스 SignatureCustomAppearance는 해당 기능을 제공합니다. 다음 코드 스니펫은 디지털 서명 텍스트의 언어를 변경하는 방법을 보여줍니다:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // 서명 위치를 위한 사각형 생성
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // 세 가지 서명 유형 중 하나 생성
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // PDF 파일에 서명
        pdfSign.sign(1, true, rect, pkcs);
        // 출력 PDF 파일 저장
        pdfSign.save(outFile);
    }
```