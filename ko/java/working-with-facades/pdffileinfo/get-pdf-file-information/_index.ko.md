---
title: PDF 파일 정보 가져오기 - 파사드
type: docs
weight: 10
url: /java/get-pdf-information/
description: 이 섹션에서는 PdfFileInfo 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일 정보를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 파일에 특정한 정보를 얻기 위해서는 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 클래스의 객체를 생성해야 합니다. 그런 다음, Subject, Title, Keywords, Creator 등의 개별 속성 값을 얻을 수 있습니다.

다음 코드 조각은 PDF 파일 정보를 얻는 방법을 보여줍니다.

```java
public static void GetPdfInfo()
    {
        // 문서 열기
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // PDF 정보 얻기
        System.out.println("Subject: " + fileInfo.getSubject());
        System.out.println("Title: " + fileInfo.getTitle());
        System.out.println("Keywords: " + fileInfo.getKeywords());
        System.out.println("Creator: " + fileInfo.getCreator());
        System.out.println("Creation Date: " + fileInfo.getCreationDate());
        System.out.println("Modification Date: " + fileInfo.getModDate());
        // 유효한 PDF인지 그리고 암호화되어 있는지 확인하기
        System.out.println("Is Valid PDF: " + fileInfo.isPdfFile());
        System.out.println("Is Encrypted: " + fileInfo.isEncrypted());

        System.out.println("Page width:" +fileInfo.getPageWidth(1));
    }
```


## 메타 정보 가져오기

정보를 얻기 위해, 우리는 [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--) 메서드를 사용합니다. 'Hashtable'을 사용하여 가능한 모든 값을 가져옵니다.

```java
public static void GetMetaInfo()
    {        
        // PdffileInfo 객체의 인스턴스 생성
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // 모든 기존 사용자 정의 속성 검색
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // 키 가져오기
            String key = enumerator.nextElement();  
            // 해당 키에 해당하는 키와 값 출력
            System.out.println(key + ": " + hTable.get(key));
        }

        // 하나의 사용자 정의 속성 검색
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```