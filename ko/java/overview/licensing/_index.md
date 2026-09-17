---
title: PDF 라이센스를 Aspose
linktitle: 라이센스 및 제한 사항
type: docs
weight: 50
url: /java/licensing/
description: Python용 Aspose.PDF는 고객에게 클래식 라이선스를 받도록 초대합니다. 또한 제한된 라이센스를 사용하여 제품을 더 잘 탐색할 수도 있습니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF 라이선스
Abstract: 이 기사에서는 Python용 Aspose.PDF의 제한 사항과 라이선스 옵션에 대해 설명합니다. 평가판은 전체 기능 테스트를 허용하지만 생성된 PDF에 저작권 정보와 함께 "평가 전용"이라는 워터마크를 추가한다는 점을 강조합니다. 이러한 제한 없이 테스트하려는 사용자를 위해 30일 임시 라이센스를 사용할 수 있습니다. 이 기사에서는 파일이나 스트림에서 클래식 라이선스를 로드하여 Aspose.PDF.dll 파일과 동일한 디렉터리에 라이선스 파일을 배치하고 `Aspose.Pdf.License` 클래스를 사용하여 라이선스를 설정하는 방식으로 클래식 라이선스를 구현하는 방법을 자세히 설명합니다. 라이센스 프로세스를 설명하기 위해 코드 조각이 제공됩니다.
---
## 평가판의 제한 사항



우리는 고객이 구매하기 전에 구성 요소를 철저히 테스트하여 평가판을 통해 평소처럼 사용할 수 있기를 바랍니다.


- 
**평가 워터마크로 생성된 PDF.** Java용 Aspose.PDF의 평가판은 전체 제품 기능을 제공하지만 생성된 PDF 문서의 모든 페이지에는 상단에 "평가 전용. Aspose.PDF로 생성됨. Copyright 2002-2020 Aspose Pty Ltd"라는 워터마크가 표시되어 있습니다.


- 
**처리 가능한 수집항목 개수 제한입니다.**


모든 컬렉션의 평가판에서는 4개의 요소(예: 4페이지, 4개의 양식 필드 등)만 처리할 수 있습니다.

[Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)에서 Java용 **Aspose.PDF** 평가판을 다운로드할 수 있습니다. 평가판은 제품의 라이센스 버전과 완전히 동일한 기능을 제공합니다. 또한 평가판 버전은 라이센스를 구입하고 라이센스를 적용하기 위해 몇 줄의 코드를 추가하면 라이센스가 부여됩니다.



**Aspose.PDF** 평가에 만족하시면 Aspose 웹사이트에서 [라이센스를 구매](https://purchase.aspose.com/)하실 수 있습니다. 제공되는 다양한 구독 유형을 숙지하세요. 궁금한 점이 있으면 주저하지 말고 Aspose 영업팀에 문의하세요.



모든 Aspose 라이선스에는 이 기간 동안 나오는 새 버전이나 수정 사항에 대한 무료 업그레이드를 위한 1년 구독이 포함됩니다. 기술 지원은 무료이며 무제한이며 라이센스가 있는 사용자와 평가판 사용자 모두에게 제공됩니다.



>평가판 제한 없이 Aspose.PDF for Java를 테스트하고 싶다면 30일 임시 라이선스를 요청할 수도 있습니다. [임시면허증은 어떻게 발급받나요?](https://purchase.aspose.com/temporary-license)를 참고하세요.


## 
클래식 라이센스

라이센스는 파일 또는 스트림 개체에서 로드할 수 있습니다. 라이센스를 설정하는 가장 쉬운 방법은 라이센스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 넣고 아래 예와 같이 경로 없이 파일 이름을 지정하는 것입니다.



라이선스는 제품 이름, 라이선스가 부여된 개발자 수, 구독 만료 날짜 등과 같은 세부 정보가 포함된 일반 텍스트 XML 파일입니다. 파일은 디지털 서명되었으므로 파일을 수정하지 마십시오. 파일에 실수로 추가 줄 바꿈을 추가하더라도 파일이 무효화됩니다.



문서 작업을 수행하기 전에 라이센스를 설정해야 합니다. 라이센스는 애플리케이션 또는 프로세스당 한 번만 설정하면 됩니다.



라이센스는 다음 위치의 스트림이나 파일에서 로드할 수 있습니다.


1. 
명시적 경로.
1. aspose-pdf-xx.x.jar이 포함된 폴더입니다.



License.setLicense 메서드를 사용하여 구성 요소에 라이선스를 부여합니다. 라이센스를 설정하는 가장 쉬운 방법은 라이센스 파일을 Aspose.PDF.jar과 동일한 폴더에 넣고 다음 예와 같이 경로 없이 파일 이름만 지정하는 것입니다.


{{% alert color="primary" %}}


Java 4.2.0용 Aspose.PDF부터 라이센스를 초기화하려면 다음 코드 라인을 호출해야 합니다.


{{% /alert %}}

### 
파일에서 라이센스 로드



이 예에서 **Aspose.PDF**는 애플리케이션의 JAR이 포함된 폴더에서 라이센스 파일을 찾으려고 시도합니다.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### 스트림 객체에서 라이선스 로드



다음 예에서는 스트림에서 라이선스를 로드하는 방법을 보여줍니다.


```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### 
라이센스 검증



라이센스가 제대로 설정되었는지 여부를 확인할 수 있습니다. Document 클래스에는 라이센스가 올바르게 설정된 경우 true를 반환하는 isLicensed 메서드가 있습니다.


```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## 
계량 라이센스

Aspose.PDF를 사용하면 개발자가 계량 키를 적용할 수 있습니다. 이는 새로운 라이센스 메커니즘입니다. 새로운 라이센스 메커니즘은 기존 라이센스 방법과 함께 사용됩니다. API 기능 사용량에 따라 요금을 청구하려는 고객은 측정 라이선스를 사용할 수 있습니다.В 자세한 내용은В [측정 라이선스 FAQ](https://purchase.aspose.com/faqs/licensing/metered)В 섹션을 참조하세요.



측정 키를 적용하기 위해 새로운 클래스В [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В가 도입되었습니다. 다음은 측정된 공개 키와 개인 키를 설정하는 방법을 보여주는 샘플 코드입니다.


```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```

## 
Aspose의 여러 제품 사용



애플리케이션에서 Aspose.PDF 및 Aspose.Words와 같은 여러 Aspose 제품을 사용하는 경우 다음은 몇 가지 유용한 팁입니다.


- 
**각 Aspose 제품에 대한 라이선스를 별도로 설정하세요.** 모든 구성 요소에 대한 단일 라이선스 파일(예: 'Aspose.Total.lic')이 있더라도 애플리케이션에서 사용 중인 각 Aspose 제품에 대해 별도로 **License.SetLicense**를 호출해야 합니다.
- **정규화된 라이선스 클래스 이름을 사용하세요.** 각 Aspose 제품의 네임스페이스에는 **License** 클래스가 있습니다. 예를 들어 Aspose.PDF에는 **com.aspose.pdf.License** 클래스가 있고 Aspose.Words에는 **com.aspose.words.License** 클래스가 있습니다. 정규화된 클래스 이름을 사용하면 어떤 라이센스가 어떤 제품에 적용되는지에 대한 혼동을 피할 수 있습니다.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
