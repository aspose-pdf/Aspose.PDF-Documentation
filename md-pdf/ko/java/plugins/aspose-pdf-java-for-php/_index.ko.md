---
title: Aspose.PDF Java for PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Aspose.PDF Java for PHP 소개

### PHP / Java 브리지

PHP/Java 브리지는 스트리밍, XML 기반 [네트워크 프로토콜](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT)의 구현으로, PHP, Scheme 또는 Python과 같은 네이티브 스크립트 엔진을 Java 가상 머신과 연결하는 데 사용할 수 있습니다. SOAP를 통한 로컬 RPC보다 최대 50배 빠르며, 웹 서버 측에서 더 적은 리소스를 필요로 합니다. Java 네이티브 인터페이스를 통한 직접 통신보다 [빠르고](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) 더 신뢰할 수 있으며, PHP에서 Java 프로시저를 호출하거나 Java에서 PHP 프로시저를 호출하기 위해 추가 구성 요소가 필요하지 않습니다.

[sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)에서 더 읽어보세요.

### Aspose.PDF for Java

Aspose.PDF for Java는 Java 애플리케이션이 Adobe Acrobat을 사용하지 않고 PDF 문서를 읽고, 쓰고, 조작할 수 있게 하는 PDF 문서 생성 구성 요소입니다.

Aspose.PDF for Java는 놀라운 기능을 제공하는 적절한 가격의 구성 요소입니다. 이 기능에는 PDF 압축 옵션, 테이블 생성 및 조작, 그래프 지원, 이미지 기능, 광범위한 하이퍼링크 기능, 확장된 보안 제어 및 사용자 정의 글꼴 처리가 포함됩니다.

Aspose.PDF for Java를 사용하면 제공된 API와 XML 템플릿을 통해 직접 PDF 파일을 생성할 수 있습니다. 또한, Aspose.PDF for Java를 사용하면 응용 프로그램에 PDF 기능을 신속하게 추가할 수 있습니다.

### Aspose.PDF Java for PHP

Project Aspose.PDF for PHP는 PHP에서 Aspose.PDF Java API를 사용하여 다양한 작업을 수행하는 방법을 보여줍니다. 이 프로젝트는 PHP/Java Bridge를 사용하여 PHP 프로젝트에서 Aspose.PDF for Java를 활용하려는 PHP 개발자를 위한 유용한 예제를 제공하는 것을 목표로 합니다.

## 시스템 요구 사항 및 지원 플랫폼

### 시스템 요구 사항

다음은 Java를 통해 Aspose.PDF for PHP를 사용하기 위한 시스템 요구 사항입니다:

- Tomcat Server 8.0 이상 설치됨.
- PHP/JavaBridge가 구성됨.
- FastCGI가 설치됨.
- Aspose.PDF 컴포넌트 다운로드 완료.

### 지원 플랫폼

다음은 지원되는 플랫폼입니다:

- PHP 5.3 이상
- Java 1.8 이상

## 다운로드 및 구성

### 필요한 라이브러리 다운로드

아래에 언급된 필요한 라이브러리를 다운로드하십시오. 이는 Aspose.PDF Java for PHP 예제를 실행하는 데 필요합니다.

- **Aspose:** [Aspose.PDF for Java Component](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### 소셜 코딩 사이트에서 예제 다운로드

소셜 코딩 사이트에서 다운로드할 수 있는 실행 예제의 릴리스는 다음과 같습니다:

### GitHub

- Aspose.PDF Java for PHP 예제
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Linux 플랫폼에서 소스 코드 구성 방법

소스 코드를 열고 확장하려면 다음의 간단한 단계를 따르십시오:

### 1. Tomcat Server 설치

Tomcat 서버를 설치하려면, 리눅스 콘솔에서 다음 명령을 입력하십시오. 이 명령은 Tomcat 서버를 성공적으로 설치할 것입니다.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. PHP/JavaBridge 다운로드 및 구성

PHP/JavaBridge 바이너리를 다운로드하려면, 리눅스 콘솔에서 다음 명령을 실행하세요.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

리눅스 콘솔에서 다음 명령을 실행하여 PHP/JavaBridge 바이너리를 압축 해제하세요.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

이 작업은 **JavaBridge.war** 파일을 추출합니다. 리눅스 콘솔에서 다음 명령을 실행하여 tomcat8의 **webapps** 폴더에 복사하세요.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

복사하면, tomcat8은 자동으로 **webapps**에 "**JavaBridge**"라는 새 폴더를 생성합니다.

오류 메시지가 나타나면 리눅스 콘솔에서 다음 명령을 실행하여 **FastCGI**를 설치하세요.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

**JAVA_HOME** 오류가 표시되면 /etc/default/tomcat8 파일을 열고 JAVA_HOME을 설정하는 줄의 주석을 제거하세요.

### 3. Aspose.PDF Java for PHP 예제 구성

webapps/JavaBridge 폴더 안에서 다음 명령을 실행하여 PHP 예제를 클론하세요.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Windows 플랫폼에서 소스 코드 구성 방법

Windows 플랫폼에서 PHP/Java Bridge를 구성하려면 아래의 간단한 단계를 따르세요.

1. PHP5를 설치하고 일반적으로 구성하듯이 구성하세요.
2. JRE 6 (Java Runtime Environment)을 설치하세요. 이미 설치되어 있지 않다면 C:\Program Files 등에서 확인할 수 있습니다. 여기에서 다운로드할 수 있습니다. PHP Java Bridge (PJB)와 호환되므로 JRE 6을 사용하고 있습니다.

3. Apache Tomcat 8.0을 설치하세요. 여기에서 다운로드할 수 있습니다.

4. [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download)을 다운로드합니다. 이 파일을 tomcat 웹앱 디렉토리에 복사합니다.  
(예: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

5. tomcat apache 서비스를 다시 시작합니다.

6. http://localhost:8080/JavaBridge/test.php로 이동하여 php가 작동하는지 확인합니다. 거기에서 다른 예제들을 찾을 수 있습니다.

7. [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 파일을 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib에 복사합니다.

8. [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) 예제를 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 폴더 내에 클론합니다.

9. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 폴더를 Aspose.PDF Java for PHP 예제 폴더로 복사합니다.

10. apache tomcat 서비스를 다시 시작하고 예제를 사용하기 시작합니다.

## 지원, 확장 및 기여

### 지원

Aspose의 초기부터, 우리는 고객에게 좋은 제품을 제공하는 것만으로는 충분하지 않다는 것을 알고 있었습니다. 우리는 또한 좋은 서비스를 제공해야 했습니다. 우리도 개발자이기 때문에 기술적 문제나 소프트웨어의 특이점이 여러분이 해야 할 일을 방해할 때 얼마나 좌절스러운지 이해합니다. 우리는 문제를 해결하기 위해 여기에 있으며, 문제를 만들지 않습니다.

이 때문에 우리는 무료 지원을 제공합니다. 우리 제품을 사용하는 사람은, 그들이 구매했든 평가판을 사용하든, 우리의 전적인 관심과 존중을 받을 자격이 있습니다.

Aspose.Cells Java for PHP와 관련된 문제나 제안을 다음 플랫폼 중 하나를 사용하여 로그할 수 있습니다:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 확장 및 기여

Aspose.PDF Java for PHP는 오픈 소스이며 그 소스 코드는 아래에 나열된 주요 소셜 코딩 웹사이트에서 이용 가능합니다.
 개발자들은 소스 코드를 다운로드하고 새로운 기능을 제안하거나 추가하거나 기존의 기능을 개선하여 다른 사람들이 이익을 얻을 수 있도록 기여하는 것이 권장됩니다.

### 소스 코드

최신 소스 코드는 다음 위치 중 하나에서 얻을 수 있습니다.

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)