---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 90
url: /java/licensing/
description: Aspose. PDF for Java는 고객들에게 Classic 라이선스와 Metered License를 제공하여 제품을 보다 잘 탐색할 수 있도록 제한된 라이선스를 사용합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 평가판 버전의 제한

우리는 고객들이 구매 전에 우리 구성 요소를 철저히 테스트하기를 원하기 때문에 평가판 버전은 일반적으로 사용하는 것처럼 사용할 수 있도록 허용합니다.

- **평가 워터마크가 있는 PDF 생성.** Aspose.PDF for Java의 평가판 버전은 전체 제품 기능을 제공하지만, 생성된 PDF 문서의 모든 페이지 상단에는 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"라는 워터마크가 표시됩니다.

- **처리할 수 있는 컬렉션 항목 수의 제한.**

평가판 버전에서는 어떤 컬렉션에서도 네 개의 요소만 처리할 수 있습니다 (예: 4페이지, 4개의 양식 필드 등).

You can download an evaluation version of **Aspose.PDF** for Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). 평가판은 제품의 라이센스 버전과 동일한 기능을 제공합니다. 또한, 라이센스를 구매하고 라이센스를 적용하기 위한 몇 줄의 코드를 추가하면 평가판은 단순히 라이센스가 부여됩니다.

**Aspose.PDF** 평가에 만족하신 후에는 Aspose 웹사이트에서 [라이센스를 구매](https://purchase.aspose.com/)할 수 있습니다. 제공되는 다양한 구독 유형을 숙지하십시오. 질문이 있는 경우, 주저하지 말고 Aspose 영업팀에 문의하십시오.

모든 Aspose 라이센스는 1년간의 무료 구독을 포함하여 이 기간 동안 출시되는 모든 새 버전 또는 수정 사항에 대한 업그레이드를 제공합니다. 기술 지원은 무료이며 무제한이며, 라이센스 사용자와 평가 사용자 모두에게 제공됩니다.

>**Java용 Aspose.PDF**를 평가판 제한 없이 테스트하고 싶다면, 30일 임시 라이센스를 요청할 수도 있습니다.
 [임시 라이선스를 얻는 방법](https://purchase.aspose.com/temporary-license)을 참조하십시오.

## 클래식 라이선스

라이선스는 파일이나 스트림 객체에서 로드할 수 있습니다. 라이선스를 설정하는 가장 쉬운 방법은 Aspose.PDF.dll 파일과 동일한 폴더에 라이선스 파일을 넣고 경로 없이 파일 이름을 지정하는 것입니다. 아래 예제를 참조하십시오.

라이선스는 제품명, 라이선스가 부여된 개발자 수, 구독 만료일 등과 같은 세부 정보를 포함하는 일반 텍스트 XML 파일입니다. 파일은 디지털 서명되어 있으므로 파일을 수정하지 마십시오. 파일에 추가적인 줄 바꿈을 무심코 추가하더라도 파일이 무효화됩니다.

문서와 함께 작업을 수행하기 전에 라이선스를 설정해야 합니다. 애플리케이션이나 프로세스당 한 번만 라이선스를 설정하면 됩니다.

라이선스는 다음 위치에서 스트림 또는 파일로 로드할 수 있습니다:

1. 명시적 경로.
1. aspose-pdf-xx.x.jar를 포함하는 폴더.

License.setLicense 메소드를 사용하여 구성 요소에 라이선스를 설정하십시오. 라이선스를 설정하는 가장 쉬운 방법은 Aspose.PDF.jar와 같은 폴더에 라이선스 파일을 놓고, 다음 예제에서 보여주는 것처럼 경로 없이 파일 이름만 지정하는 것입니다:

{{% alert color="primary" %}}

Aspose.PDF for Java 4.2.0부터 라이선스를 초기화하기 위해 다음 코드 라인을 호출해야 합니다.

{{% /alert %}}

### 파일에서 라이선스 로드하기

이 예제에서는 **Aspose.PDF**가 애플리케이션의 JAR 파일이 포함된 폴더에서 라이선스 파일을 찾으려고 시도할 것입니다.

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

#### 2005/01/22 이전에 구매한 라이선스 설정하기**Aspose.PDF** for Java는 더 이상 구 버전을 지원하지 않으므로 새 라이센스 파일을 받으려면 [영업팀](https://company.aspose.com/contact)에 문의하십시오.

### 라이센스 검증

라이센스가 제대로 설정되었는지 여부를 검증할 수 있습니다. Document 클래스에는 라이센스가 제대로 설정되었을 경우 true를 반환하는 isLicensed 메서드가 있습니다.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// 라이센스가 검증되었는지 확인
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## 측정 라이센스

Aspose.PDF는 개발자가 측정 키를 적용할 수 있도록 허용합니다. 이는 새로운 라이센스 메커니즘입니다. 새로운 라이센스 메커니즘은 기존의 라이센스 방법과 함께 사용됩니다. API 기능 사용량에 따라 청구되기를 원하는 고객은 측정 라이센스를 사용할 수 있습니다. 자세한 내용은 [측정 라이센스 FAQ](https://purchase.aspose.com/faqs/licensing/metered) 섹션을 참조하십시오.

새로운 클래스 [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)가 측정 키를 적용하기 위해 도입되었습니다.
 다음은 계량된 공공 및 개인 키를 설정하는 방법을 보여주는 샘플 코드입니다.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// 선택적으로, 유효한 라이센스가 적용되었으면 true를 반환하고;
// 컴포넌트가 평가 모드로 실행 중이면 false를 반환하는 두 줄이 있습니다.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Aspose의 여러 제품 사용

응용 프로그램에서 여러 Aspose 제품을 사용하는 경우, 예를 들어 Aspose.PDF 및 Aspose.Words, 다음은 몇 가지 유용한 팁입니다.

- **각 Aspose 제품에 대해 별도로 라이센스를 설정하십시오.** 모든 구성 요소에 대한 단일 라이센스 파일, 예를 들어 'Aspose.Total.lic'가 있더라도, 응용 프로그램에서 사용하는 각 Aspose 제품에 대해 **License.SetLicense**를 별도로 호출해야 합니다.
- **완전한 자격 이름으로 라이센스 클래스 사용.** 각 Aspose 제품은 네임스페이스에 **License** 클래스를 가지고 있습니다. 예를 들어, Aspose.PDF에는 **com.aspose.pdf.License** 클래스가 있고 Aspose.Words에는 **com.aspose.words.License** 클래스가 있습니다. 완전한 클래스 이름을 사용하면 어떤 제품에 어떤 라이선스가 적용되는지에 대한 혼동을 피할 수 있습니다.

```java
// Aspose.Pdf의 License 클래스를 인스턴스화합니다.
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 라이선스를 설정합니다.
license.setLicense("Aspose.Total.Java.lic");

// Aspose.Words for Java의 라이선스 설정

// Aspose.Words의 License 클래스를 인스턴스화합니다.
com.aspose.words.License licenseaw = new com.aspose.words.License();
// 라이선스를 설정합니다.
licenseaw.setLicense("Aspose.Total.Java.lic");
```