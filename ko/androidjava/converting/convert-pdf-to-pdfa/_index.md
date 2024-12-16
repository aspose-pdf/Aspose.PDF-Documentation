---
title: PDF 파일을 PDF/A로 변환
linktitle: PDF 파일을 PDF/A로 변환
type: docs
weight: 180
url: /ko/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: 이 주제는 Aspose.PDF for Java가 PDF 파일을 PDF/A 준수 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF를 사용하면 PDF 파일을 PDF/A 준수 PDF 파일로 변환할 수 있습니다. 그 전에 파일을 검증해야 합니다. 이 문서는 그 방법을 설명합니다.

우리는 PDF/A 적합성을 검증하기 위해 Adobe Preflight을 따릅니다. 시장에 있는 모든 도구들은 PDF/A 적합성에 대한 그들만의 "표현"을 가지고 있습니다. 참조를 위해 [PDF/A 검증 도구](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)에 관한 이 기사를 확인하십시오. 우리는 Aspose.PDF가 PDF 파일을 어떻게 생성하는지 확인하기 위해 Adobe 제품을 선택했습니다. 왜냐하면 Adobe가 PDF와 관련된 모든 것의 중심에 있기 때문입니다.

PDF를 PDF/A 준수 파일로 변환하기 전에, validate 메서드를 사용하여 PDF를 검증하십시오.
 검증 결과는 XML 파일에 저장된 후 이 결과는 convert 메서드에도 전달됩니다. 변환할 수 없는 요소에 대한 작업을 [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) 열거형을 사용하여 지정할 수도 있습니다.

{{% alert color="primary" %}}

온라인으로 시도하세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다 [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDF에서 PDF/A_1b로의 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1b 규격의 PDF로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoPDFa1b() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 규격의 문서로 변환
        // 변환 과정에서 검증도 수행됩니다
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // 출력 문서 저장
        document.save(pdfaFileName.toString());
    }
```

문서의 유효성 검사를 수행하려면 다음 코드를 사용하십시오:

```java
public void ValidatePDF_A_1B() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 호환 문서로 유효성 검사

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("문서는 유효합니다");
        }
        else {
            resultMessage.setText("문서는 유효하지 않습니다");
        }
    }
```

## PDF에서 PDF/A_3b로 변환

```java
    public void convertPDFtoPDFa3b() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 호환 문서로 변환
        // 변환 과정에서 유효성 검사도 수행됩니다
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // 출력 문서 저장
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDF to PDF/A_3a 변환

```java
public void convertPDFtoPDFa3a() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 호환 문서로 변환
        // 변환 과정에서 유효성 검사도 수행됨
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // 출력 문서 저장
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF to PDF/A_2a 변환

```java
public void convertPDFtoPDFa2a() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 호환 문서로 변환
        // 변환 과정에서 유효성 검사도 수행됨
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // 출력 문서 저장
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## PDF를 PDF/A_3U로 변환

```java
 public void convertPDFtoPDFa3u() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 호환 문서로 변환
        // 변환 과정 중에 검증도 수행됩니다
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // 출력 문서 저장
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF/A-3 생성 및 XML 파일 첨부

Aspose.PDF for Android via Java는 PDF 파일을 PDF/A 형식으로 변환하는 기능을 제공하며, PDF 문서에 파일을 첨부하는 기능도 지원합니다.
 파일을 PDF/A 준수 형식으로 첨부해야 하는 요구 사항이 있는 경우, com.aspose.pdf.PdfFormat 열거형의 PDF_A_3A 값을 사용하는 것을 권장합니다. PDF/A_3a는 PDF/A 준수 파일에 첨부 파일로 모든 파일 형식을 첨부할 수 있는 기능을 제공하는 형식입니다. 하지만 파일이 첨부되면 메타데이터를 수정하기 위해 다시 Pdf-3a 형식으로 변환해야 합니다. 다음 코드 스니펫을 참조하십시오.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // 문서 열기
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDF/A 준수 문서로 변환
        // 변환 과정에서 검증도 수행됩니다.
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // 출력 문서 저장
        try {
            // XML 파일 로드
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "샘플 xml 파일");
            // 문서의 첨부 파일 컬렉션에 첨부 파일 추가
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```