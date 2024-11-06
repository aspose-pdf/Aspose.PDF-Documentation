---
title: PDF 파일 메타데이터 작업하기 
linktitle: PDF 파일 메타데이터
type: docs
weight: 140
url: ko/java/pdf-file-metadata/
description: 이 섹션은 PDF 파일 정보를 얻는 방법, PDF 파일에서 XMP 메타데이터를 얻는 방법, PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일 정보 얻기

PDF 파일에 대한 파일별 정보를 얻으려면 먼저 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--) 메서드를 사용하여 [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) 객체를 가져옵니다. [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) 객체를 가져온 후에는 개별 속성의 값을 얻을 수 있습니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // 새 PDF 문서 생성
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // 문서 정보 가져오기
        DocumentInfo docInfo = pdfDocument.getInfo();
        // 문서 정보 표시
        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
```


## PDF 파일 정보 설정

Aspose.PDF for Java를 사용하여 PDF의 파일별 정보를 설정할 수 있습니다. 정보에는 작성자, 생성 날짜, 주제 및 제목이 포함됩니다.

이 정보를 설정하려면:

1. [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) 객체를 생성합니다.
1. 속성의 값을 설정합니다.
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) 메서드를 사용하여 업데이트된 문서를 저장합니다.

{{% alert color="primary" %}}

**Producer** 및 **Creator** 필드에 값을 설정할 수 없음을 유의하십시오. Aspose.PDF for Java x.x.x가 이러한 필드에 표시될 것입니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```java
 public static void SetPDFFileInformation() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 문서 정보 지정
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("PDF 정보");
        docInfo.setTitle("PDF 문서 정보 설정");

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## PDF 파일에서 XMP 메타데이터 가져오기

Aspose.PDF for Java를 사용하면 PDF 파일의 XMP 메타데이터에 접근할 수 있습니다.

PDF 파일의 메타데이터를 가져오려면,

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성하고 입력 PDF 파일을 엽니다.
1. 메타데이터를 가져오기 위해 [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) 속성을 사용합니다.

다음 코드 스니펫은 PDF 파일에서 메타데이터를 가져오는 방법을 보여줍니다.

```java
   public static void GetXMPMetadata() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## PDF 파일에 XMP 메타데이터 설정

Aspose.PDF for Java를 사용하면 PDF 파일에 메타데이터를 설정할 수 있습니다.
 메타데이터를 설정하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성합니다.
1. [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) 속성을 사용하여 메타데이터 값을 설정합니다.
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) 메서드를 사용하여 업데이트된 문서를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 메타데이터를 설정하는 방법을 보여줍니다.

```java
    public static void SetXMPMetadata() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 속성 설정
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // 문서 저장
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## 접두사가 있는 메타데이터 삽입

일부 개발자는 접두사가 있는 새 메타데이터 네임스페이스를 만들어야 합니다. 다음 코드 스니펫은 접두사가 있는 메타데이터를 삽입하는 방법을 보여줍니다.

```java
    public static void InsertMetadataWithPrefix() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // 문서 저장
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```