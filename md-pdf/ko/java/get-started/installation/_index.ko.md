---
title: Aspose.PDF for Java 설치
linktitle: 설치
type: docs
weight: 20
url: /java/installation/
description: 이 섹션은 Aspose.PDF for Java를 직접 설치하는 방법과 NuGet을 사용하는 방법에 대한 제품 설명과 지침을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF for Java 컴포넌트

{{% alert color="primary" %}}

**Aspose.PDF는 Java** 컴포넌트로, 개발자가 간단하거나 복잡한 PDF 문서를 즉석에서 프로그래밍 방식으로 생성할 수 있도록 설계되었습니다. Aspose.PDF for Java는 개발자가 테이블, 그래프, 이미지, 하이퍼링크, 사용자 지정 글꼴 등을 PDF 문서에 삽입할 수 있도록 합니다. 또한, PDF 문서를 압축하는 것도 가능합니다. Aspose.PDF for Java는 안전한 PDF 문서를 개발하기 위한 뛰어난 보안 기능을 제공합니다. Aspose.PDF for Java의 가장 두드러진 특징은 API와 XML 템플릿을 통해 PDF 문서를 생성할 수 있다는 점입니다.

{{% /alert %}}

## 제품 설명


**Aspose.PDF for Java**는 Java를 사용하여 구현되었으며 JDK 1.8 이상에서 작동합니다. Aspose.PDF for Java는 JSP/JSF 웹 애플리케이션이나 Windows 애플리케이션과 같은 모든 애플리케이션에 통합될 수 있습니다.

**Aspose.PDF for Java**는 빠르고 가볍습니다. PDF 문서를 효율적으로 생성하며 애플리케이션의 성능을 향상시키는 데 도움을 줍니다. Aspose.PDF for Java는 가격, 뛰어난 성능 및 훌륭한 지원으로 인해 PDF 문서를 생성할 때 고객의 첫 번째 선택입니다. 이 라이브러리를 사용하여 Adobe Acrobat을 설치하지 않고도 처음부터 PDF 파일을 생성하거나 기존 PDF 문서를 완전히 처리할 수 있는 다양한 기능을 구현할 수 있습니다.

# 설치

## Aspose.PDF for Java 평가

{{% alert color="primary" %}}

평가를 위해 [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/)를 다운로드할 수 있습니다.
 평가용 다운로드는 구매한 다운로드와 동일합니다. 라이선스를 [적용하기](/pdf/java/licensing/) 위해 몇 줄의 코드를 추가하면 평가 버전이 단순히 라이선스가 됩니다.

{{% /alert %}}

Aspose.PDF의 평가 버전은 전체 제품 기능을 제공하지만 두 가지 제한이 있습니다:

- 평가 워터마크를 삽입합니다.
- 컬렉션의 어떠한 요소도 네 개 이상 볼 수 있거나 편집할 수 없습니다.
- **평가 워터마크가 표시된 문서**

![Aspose.PDF 평가](evaluate-aspose-pdf_1.png)

{{% alert color="primary" %}}

Aspose.PDF for Java를 평가 버전의 제한 없이 테스트하고 싶다면 30일 임시 라이선스를 요청할 수도 있습니다. [임시 라이선스를 얻는 방법?](https://purchase.aspose.com/temporary-license)을 참조하십시오.

{{% /alert %}}

## Aspose Repository에서 Aspose.PDF for Java 설치

Aspose는 모든 Java API를 [Aspose Repository](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/)에 호스팅합니다. Aspose.PDF for Java API를 간단한 설정으로 Maven 프로젝트에서 쉽게 사용할 수 있습니다.

### Aspose 저장소 구성 지정

먼저 Maven pom.xml에 Aspose 저장소 구성 / 위치를 다음과 같이 지정해야 합니다:

```xml
<repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Aspose.PDF for Java API 종속성 정의

그런 다음 pom.xml에 Aspose.PDF for Java API 종속성을 다음과 같이 정의합니다:

```xml
<dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

위의 단계를 수행한 후, 최종적으로 Maven 프로젝트에 Aspose.PDF for Java 종속성이 정의됩니다.

### JDK 11 호환성 및 사용 지침

이 API는 Java 11 환경에 최적화되어 있으며 모든 테스트 및 기능이 잘 작동합니다. 그러나 일부 클래스의 경우 외부 종속성을 추가하여 클래스의 클래스패스를 추가해야 합니다: javax.xml.bind.annotation.adapters.HexBinaryAdapter, 이는 JRE에서 삭제되었습니다.

예를 들어:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```