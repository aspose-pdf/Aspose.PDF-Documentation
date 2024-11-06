---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 50
url: ko/androidjava/licensing/
description: Aspose.PDF for Android via Java invites its customers to get a Classic license and Metered License. As well as use a limited license to better explore the product.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 평가 버전의 제한

우리는 고객들이 구매 전에 구성 요소를 철저히 테스트하기를 원하기 때문에 평가 버전은 일반적으로 사용할 수 있게 해줍니다.

- **평가 워터마크가 있는 PDF 생성.** Aspose.PDF for Android via Java의 평가 버전은 전체 제품 기능을 제공하지만, 생성된 PDF 문서의 모든 페이지의 상단에는 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"라는 워터마크가 표시됩니다.

- **처리할 수 있는 컬렉션 항목 수의 제한.**

평가 버전에서는 어떤 컬렉션에서든 단 4개의 요소만 처리할 수 있습니다 (예: 4페이지, 4개의 양식 필드 등).

You can download an evaluation version of Aspose.PDF for Android via Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). The evaluation version provides absolutely the same capabilities as the licensed version of the product. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

Aspose.PDF** 평가에 만족하시면 Aspose 웹사이트에서 [라이선스를 구매](https://purchase.aspose.com/)할 수 있습니다. 제공되는 다양한 구독 유형을 숙지하십시오. 질문이 있는 경우, 주저하지 말고 Aspose 영업팀에 문의하십시오.

모든 Aspose 라이선스에는 새로운 버전이나 수정 사항이 출시될 때 받을 수 있는 1년간의 무료 업그레이드 구독이 포함되어 있습니다. 기술 지원은 무료이며, 라이선스 사용자와 평가 사용자 모두에게 무제한으로 제공됩니다.

>평가판 제한 없이 Aspose.PDF for Android via Java를 테스트하고자 한다면, 30일 임시 라이선스를 요청할 수도 있습니다.
 [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)을 참조하십시오.

## 클래식 라이센스

라이센스는 파일 또는 스트림 객체에서 로드할 수 있습니다. 라이센스를 설정하는 가장 쉬운 방법은 라이센스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 넣고 아래 예제와 같이 경로 없이 파일 이름을 지정하는 것입니다.

라이센스는 제품 이름, 라이센스가 부여된 개발자 수, 구독 만료일 등 세부 정보를 포함하는 일반 텍스트 XML 파일입니다. 파일은 디지털 서명되어 있으므로 파일을 수정하지 마십시오. 파일에 추가 줄 바꿈을 추가해도 파일이 무효화됩니다.

문서와 작업을 수행하기 전에 라이센스를 설정해야 합니다. 애플리케이션 또는 프로세스당 한 번만 라이센스를 설정하면 됩니다.

라이센스는 다음 위치의 스트림 또는 파일에서 로드할 수 있습니다:

1. 명시적 경로.
1. aspose-pdf-xx.x.jar가 포함된 폴더.

License.setLicense 메서드를 사용하여 컴포넌트에 라이센스를 설정하십시오. 라이선스를 설정하는 가장 쉬운 방법은 Aspose.PDF.jar와 동일한 폴더에 라이선스 파일을 놓고 경로 없이 파일 이름만 지정하는 것입니다. 다음 예제를 참조하십시오:

{{% alert color="primary" %}}

Aspose.PDF for Java 4.2.0부터는 라이선스를 초기화하기 위해 다음 코드 줄을 호출해야 합니다.

{{% /alert %}}

### 파일에서 라이선스 로드하기

이 예제에서는 **Aspose.PDF**가 애플리케이션의 JAR이 포함된 폴더에서 라이선스 파일을 찾으려고 시도합니다.

```java
// 라이선스 인스턴스 초기화
com.aspose.pdf.License license = new com.aspose.pdf.License();
// setLicense 메서드를 호출하여 라이선스를 설정
license.setLicense("Aspose.Pdf.Java.lic");
```

### 스트림 객체에서 라이선스 로드하기

다음 예제는 스트림에서 라이선스를 로드하는 방법을 보여줍니다.

```java
// 라이선스 인스턴스 초기화
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 스트림에서 라이선스를 설정
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### 2005/01/22 이전에 구매한 라이선스 설정하기
**Aspose.PDF** for Java는 더 이상 오래된 라이선스를 지원하지 않으므로 새로운 라이선스 파일을 받으시려면 [영업팀](https://company.aspose.com/contact)에 문의하십시오.

### 라이선스 검증

라이선스가 제대로 설정되었는지 확인할 수 있습니다. Document 클래스에는 라이선스가 제대로 설정되었을 경우 true를 반환하는 isLicensed 메서드가 있습니다.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// 라이선스가 검증되었는지 확인
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## 미터드 라이선스

Aspose.PDF는 개발자가 미터드 키를 적용할 수 있도록 합니다. 이것은 새로운 라이선스 메커니즘입니다. 새로운 라이선스 메커니즘은 기존의 라이선스 방법과 함께 사용될 것입니다. API 기능의 사용량에 따라 청구되기를 원하는 고객은 미터드 라이선스를 사용할 수 있습니다. 자세한 내용은 [미터드 라이선스 FAQ](https://purchase.aspose.com/faqs/licensing/metered) 섹션을 참조하십시오.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// 선택적으로, 유효한 라이선스가 적용되었을 경우 true를 반환하고;
// 컴포넌트가 평가 모드로 실행 중일 경우 false를 반환합니다.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```

## Aspose의 여러 제품 사용하기

애플리케이션에서 여러 Aspose 제품을 사용하는 경우, 예를 들어 Aspose.PDF와 Aspose.Words를 사용하는 경우 몇 가지 유용한 팁이 있습니다.

- **각 Aspose 제품에 대해 라이선스를 개별적으로 설정하십시오.** 모든 구성 요소에 대한 단일 라이선스 파일이 있는 경우에도 예를 들어 'Aspose.Total.lic', 애플리케이션에서 사용하는 각 Aspose 제품에 대해 **License.SetLicense**를 개별적으로 호출해야 합니다.
- **정규화된 라이선스 클래스 이름을 사용하십시오.** 각 Aspose 제품은 해당 네임스페이스에 **License** 클래스를 가지고 있습니다. 예를 들어, Aspose.PDF는 **com.aspose.pdf.License** 클래스를 가지고 있고, Aspose.Words는 **com.aspose.words.License** 클래스를 가지고 있습니다. 정규화된 클래스 이름을 사용하면 어떤 제품에 어떤 라이선스가 적용되는지에 대한 혼란을 피할 수 있습니다.

```java
// Aspose.Pdf의 License 클래스 인스턴스화
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 라이선스 설정
license.setLicense("Aspose.Total.Java.lic");

// Aspose.Words for Java의 라이선스 설정

// Aspose.Words의 License 클래스 인스턴스화
com.aspose.words.License licenseaw = new com.aspose.words.License();
// 라이선스 설정
licenseaw.setLicense("Aspose.Total.Java.lic");
```