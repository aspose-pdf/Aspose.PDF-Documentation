---
title: 이미지 및 서명 정보 추출
linktitle: 이미지 및 서명 정보 추출
type: docs
weight: 30
url: /ko/java/extract-image-and-signature-information/
description: Java에서 SignatureField 클래스를 사용하여 서명 필드에서 이미지를 추출하고 서명 정보를 추출할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 서명 필드에서 이미지 추출

Aspose.PDF for Java는 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 클래스를 사용하여 PDF 파일에 디지털 서명을 추가하는 기능을 지원하며, 문서에 서명할 때 SignatureAppearance에 대한 이미지를 설정할 수도 있습니다. 이제 이 API는 서명 필드와 연관된 이미지뿐만 아니라 서명 정보를 추출할 수 있는 기능도 제공합니다.

서명 정보를 추출하기 위해 우리는 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 클래스에 [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) 메서드를 도입했습니다.
 다음은 SignatureField 객체에서 이미지를 추출하는 단계들을 보여주는 코드 스니펫입니다:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### 서명 이미지 교체

때때로 PDF 파일 안에 이미 존재하는 서명 필드의 이미지만 교체해야 하는 요구사항이 있을 수 있습니다. 이 요구사항을 충족하기 위해서는 먼저 PDF 파일 안의 양식 필드를 검색하고, 서명 필드를 식별한 다음 서명 필드의 치수(사각형 치수)를 얻은 후 동일한 치수에 이미지를 스탬프해야 합니다.

## 서명 정보 추출

Aspose.PDF for Java는 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 클래스를 사용하여 PDF 파일에 디지털 서명을 할 수 있는 기능을 지원합니다. 현재 우리는 인증서의 유효성을 확인할 수 있지만 전체 인증서를 추출할 수는 없습니다. 추출할 수 있는 정보는 공개 키, 지문, 발급자 등이 있습니다.

서명 정보를 추출하기 위해 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 클래스에 [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) 메서드를 도입했습니다.
 다음은 SignatureField 객체에서 인증서를 추출하는 단계를 보여주는 코드 조각입니다:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```