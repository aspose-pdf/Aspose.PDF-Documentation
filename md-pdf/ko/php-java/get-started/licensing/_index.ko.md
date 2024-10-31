---
title: 라이선스 및 제한
linktitle: 라이선스 및 제한
type: docs
weight: 90
url: /php-java/licensing/
description: Aspose.PDF for PHP via Java는 고객에게 클래식 라이선스와 계량 라이선스를 제공합니다. 제품을 더 잘 탐색하기 위해 제한된 라이선스를 사용할 수도 있습니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 평가판의 제한 사항

우리는 고객이 구매 전에 우리 구성 요소를 철저히 테스트하기를 원하기 때문에 평가판에서는 일반적으로 사용하는 것처럼 사용할 수 있습니다.

- **평가용 워터마크가 있는 PDF 생성.** Aspose.PDF for PHP via Java의 평가판은 전체 제품 기능을 제공하지만, 생성된 PDF 문서의 모든 페이지에는 상단에 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"라는 워터마크가 표시됩니다.

- **처리할 수 있는 컬렉션 항목 수의 한계.**

평가판에서는 어떤 컬렉션에서도 4개의 요소만 처리할 수 있습니다(예: 페이지 4개, 양식 필드 4개 등).

당신은 [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)에서 Java용 **Aspose.PDF**의 평가판을 다운로드할 수 있습니다. 평가판은 제품의 라이선스 버전과 동일한 기능을 제공합니다. 또한, 평가판은 라이선스를 구매하고 라이선스를 적용하기 위해 몇 줄의 코드를 추가하면 간단히 라이선스 버전이 됩니다.

**Aspose.PDF**의 평가에 만족하시면 Aspose 웹사이트에서 [라이선스를 구매](https://purchase.aspose.com/)할 수 있습니다. 제공되는 다양한 구독 유형을 잘 파악하십시오. 질문이 있으시면 언제든지 Aspose 영업팀에 문의하십시오.

모든 Aspose 라이선스는 1년 동안의 무료 업그레이드 구독을 제공하며, 이 기간 동안 출시되는 모든 새 버전이나 수정사항에 대해 무료 업그레이드가 가능합니다. 기술 지원은 무료이며 무제한으로 제공되며, 라이선스 사용자와 평가 사용자 모두에게 제공됩니다.

>Java를 통한 PHP용 Aspose.PDF를 평가판의 제한 없이 테스트하고 싶다면, 30일 임시 라이선스를 요청할 수도 있습니다.
 [임시 라이선스를 얻는 방법](https://purchase.aspose.com/temporary-license)을 참조하십시오.

## 클래식 라이선스

라이선스는 파일이나 스트림 객체에서 로드할 수 있습니다. 라이선스를 설정하는 가장 쉬운 방법은 라이선스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 두고 경로 없이 파일 이름만 지정하는 것입니다. 아래 예제와 같이 수행할 수 있습니다.

라이선스는 제품 이름, 라이선스가 부여된 개발자 수, 구독 만료 날짜 등을 포함하는 일반 텍스트 XML 파일입니다. 파일은 디지털 서명되어 있으므로 파일을 수정하지 마십시오. 파일에 줄 바꿈을 추가하는 등의 부주의한 수정은 파일을 무효화합니다.

문서 작업을 수행하기 전에 라이선스를 설정해야 합니다. 애플리케이션이나 프로세스당 한 번만 라이선스를 설정하면 됩니다.

라이선스는 다음 위치에서 스트림 또는 파일로 로드할 수 있습니다:

1. 명시적 경로.
1. aspose-pdf-xx.x.jar가 포함된 폴더.

License.setLicense 메서드를 사용하여 구성 요소에 라이선스를 설정하십시오. 종종 라이선스를 설정하는 가장 쉬운 방법은 라이선스 파일을 Aspose.PDF.jar과 동일한 폴더에 넣고 경로 없이 파일 이름만 지정하는 것입니다. 다음 예제를 참조하세요:

{{% alert color="primary" %}}

Aspose.PDF for PHP via Java 4.2.0부터 라이선스를 초기화하려면 다음 코드 줄을 호출해야 합니다.

{{% /alert %}}

### 파일에서 라이선스 로드하기

이 예제에서는 **Aspose.PDF**가 애플리케이션의 JAR이 포함된 폴더에서 라이선스 파일을 찾으려고 시도합니다.

```java
// 라이선스 인스턴스 초기화
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 라이선스를 설정하기 위해 setLicense 메서드 호출
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

#### 2005/01/22 이전에 구매한 라이선스 설정하기**Aspose.PDF** for Java는 더 이상 오래된 라이선스를 지원하지 않으므로 [영업 팀](https://company.aspose.com/contact)에 문의하여 새 라이선스 파일을 받으십시오.

### 라이선스 유효성 검사

라이선스가 제대로 설정되었는지 여부를 확인할 수 있습니다. Document 클래스에는 라이선스가 제대로 설정되었을 경우 true를 반환하는 isLicensed 메서드가 있습니다.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// 라이선스가 유효한지 확인
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## 미터드 라이선스

Aspose.PDF는 개발자가 미터드 키를 적용할 수 있도록 합니다. 이는 새로운 라이선스 메커니즘입니다. 새로운 라이선스 메커니즘은 기존의 라이선스 방법과 함께 사용됩니다. API 기능의 사용량에 따라 청구되기를 원하는 고객은 미터드 라이선스를 사용할 수 있습니다. 자세한 내용은 [미터드 라이선스 FAQ](https://purchase.aspose.com/faqs/licensing/metered) 섹션을 참조하십시오.

미터드 키를 적용하기 위해 새로운 클래스 [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)가 도입되었습니다.
 다음은 계량된 공용 및 비공용 키를 설정하는 방법을 보여주는 샘플 코드입니다.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// 선택적으로, 유효한 라이선스가 적용되었을 경우 true를 반환하고;
// 컴포넌트가 평가 모드에서 실행 중인 경우 false를 반환합니다.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Aspose의 여러 제품 사용하기

응용 프로그램에서 Aspose.PDF 및 Aspose.Words와 같이 여러 Aspose 제품을 사용하는 경우, 몇 가지 유용한 팁이 있습니다.

- **각 Aspose 제품에 대해 별도로 라이선스를 설정하십시오.** 모든 구성 요소에 대한 단일 라이선스 파일이 있는 경우에도, 예를 들어 'Aspose.Total.lic', 응용 프로그램에서 사용하는 각 Aspose 제품에 대해 **License.SetLicense**를 별도로 호출해야 합니다.
- **정확한 라이선스 클래스 이름을 사용하십시오.** 각 Aspose 제품은 그 네임스페이스에 **License** 클래스를 가지고 있습니다. 예를 들어, Aspose.PDF에는 **com.aspose.pdf.License**가 있고 Aspose.Words에는 **com.aspose.words.License** 클래스가 있습니다. 완전한 클래스 이름을 사용하면 어떤 제품에 어떤 라이선스가 적용되는지에 대한 혼란을 피할 수 있습니다.

```java
// Aspose.Pdf의 License 클래스 인스턴스화
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 라이선스 설정
license.setLicense("Aspose.Total.Java.lic");

// Aspose.Words for Java에 대한 라이선스 설정

// Aspose.Words의 License 클래스 인스턴스화
com.aspose.words.License licenseaw = new com.aspose.words.License();
// 라이선스 설정
licenseaw.setLicense("Aspose.Total.Java.lic");
```