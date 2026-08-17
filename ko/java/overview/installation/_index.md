---
title: Java용 Aspose.PDF를 설치하는 방법
linktitle: 설치
type: docs
weight: 40
url: /java/installation/
description: PDF 문서 작업을 시작하려면 Python 및 .NET용 Aspose.PDF를 설치하는 단계별 지침을 찾아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF 설치
Abstract: .NET을 통한 Python용 Aspose.PDF는 32비트 및 64비트 시스템 모두와 호환되는 Python 애플리케이션 내에 PDF 처리 기능을 통합하도록 설계된 포괄적인 라이브러리입니다. 이 라이브러리는 텍스트 및 페이지 조작, 양식 처리, 메타데이터 처리, 주석, 책갈피, 워터마크 및 사용자 정의 글꼴 관리를 포함한 광범위한 문서 처리 작업을 지원합니다. Python 3.5 이상이 설치된 다양한 운영 체제에서 사용하기에 적합합니다. 라이브러리는 적절한 코드 추가를 통해 라이센스 상태로 전환되는 평가판을 다운로드하여 평가할 수 있습니다. 평가판은 모든 기능을 유지하지만 평가 워터마크를 포함하고 수집 요소 상호 작용을 4개로 제한합니다. 사용자는 이러한 제한을 우회하기 위해 30일 임시 라이센스를 요청할 수 있습니다. .NET을 통한 Python용 Aspose.PDF는 pip를 통해 설치할 수 있으므로 최신 버전에 쉽게 액세스할 수 있습니다.
---
## 
Java 구성 요소용 Aspose.PDF


{{% alert color="primary" %}}


**Aspose.PDF는 개발자가 간단하든 복잡하든 PDF 문서를 프로그래밍 방식으로 즉석에서 만들 수 있도록 만들어진 Java** 구성 요소입니다. Java용 Aspose.PDF를 사용하면 개발자는 테이블, 그래프, 이미지, 하이퍼링크, 사용자 정의 글꼴 등을 PDF 문서에 삽입할 수 있습니다. 또한 PDF 문서를 압축하는 것도 가능합니다. Aspose.PDF for Java는 안전한 PDF 문서를 개발하기 위한 뛰어난 보안 기능을 제공합니다. Aspose.PDF for Java의 가장 뚜렷한 특징은 API와 XML 템플릿을 모두 통해 PDF 문서 생성을 지원한다는 것입니다.


{{% /alert %}}

## 
제품 설명



**Java용 Aspose.PDF**는 Java를 사용하여 구현되며 JDK 1.8 이상에서 작동합니다. Aspose.PDF for Java는 JSP/JSF 웹 애플리케이션이나 Windows 애플리케이션과 같은 모든 애플리케이션과 통합될 수 있습니다.



**Java용 Aspose.PDF**는 빠르고 가볍습니다. PDF 문서를 효율적으로 생성하고 응용 프로그램의 성능을 향상시키는 데 도움이 됩니다. Aspose.PDF for Java는 가격, 뛰어난 성능 및 훌륭한 지원으로 인해 PDF 문서를 작성할 때 고객이 가장 먼저 선택하는 제품입니다.


이 라이브러리를 사용하면 처음부터 PDF 파일을 생성하는 풍부한 기능을 구현하거나 Adobe Acrobat을 설치하지 않고도 기존 PDF 문서를 완전히 처리할 수 있습니다.


## 
설치


## 
Java용 Aspose.PDF 평가


{{% alert color="primary" %}}


평가를 위해 [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/)를 다운로드할 수 있습니다. 평가판 다운로드는 구매한 다운로드와 동일합니다. 평가판은 [라이센스 적용](/pdf/java/licensing/)에 몇 줄의 코드를 추가하면 간단히 라이센스가 부여됩니다.


{{% /alert %}}


Aspose.PDF 평가판은 전체 제품 기능을 제공하지만 두 가지 제한 사항이 있습니다.


- 
평가 워터마크를 삽입합니다.

- 
컬렉션의 최대 4개 요소만 보거나 편집할 수 있습니다.

- 
**평가 워터마크가 표시된 문서**


{{% alert color="primary" %}}


평가판 제한 없이 Aspose.PDF for Java를 테스트하려면 30일 임시 라이센스를 요청할 수도 있습니다. [임시면허증은 어떻게 발급받나요?](https://purchase.aspose.com/temporary-license)를 참고해주세요.


{{% /alert %}}

## 
Aspose 저장소에서 Java용 Aspose.PDF 설치



Aspose는 [Aspose Repository](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/)에서 모든 Java API를 호스팅합니다. 간단한 구성을 통해 Maven 프로젝트에서 직접 Java API용 Aspose.PDF를 쉽게 사용할 수 있습니다.


### 
Aspose 저장소 구성 지정



먼저 Maven pom.xml에서 Aspose Repository 구성/위치를 다음과 같이 지정해야 합니다.


```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### 
Java API 종속성을 위한 Aspose.PDF 정의



그런 다음 pom.xml에서 Java API 종속성을 위한 Aspose.PDF를 다음과 같이 정의합니다.


```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```


위 단계를 수행한 후에는 최종적으로 Maven 프로젝트에 Java 종속성을 위한 Aspose.PDF가 정의됩니다.


### 
JDK 11 호환성 및 사용 지침



API는 Java 11 환경에 최적화되어 있으며 모든 테스트와 기능이 제대로 작동합니다. 그러나 일부 클래스의 경우 JRE에서 삭제된 javax.xml.bind.annotation.adapters.HexBinaryAdapter 클래스의 클래스 경로를 추가하려면 외부 종속성을 추가해야 합니다.



예를 들면:

```xml
 <dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```
