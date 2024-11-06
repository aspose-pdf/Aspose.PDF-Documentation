---
title: Aspose.PDF를 PHP에 다운로드 및 구성
type: docs
weight: 10
url: ko/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## 필수 라이브러리 다운로드

아래 언급된 필수 라이브러리를 다운로드하세요. 이것들은 Aspose.PDF Java for PHP 예제를 실행하기 위해 필요합니다.

- **Aspose:** [Aspose.PDF for Java Component](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## 소셜 코딩 사이트에서 예제 다운로드

다음 소셜 코딩 사이트에서 실행 가능한 예제의 릴리스를 다운로드할 수 있습니다:

### GitHub

- **Aspose.PDF Java for PHP 예제**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Linux 플랫폼에서 소스 코드 구성 방법

다음 간단한 단계에 따라 소스 코드를 열고 확장하세요:

## 1. Tomcat 서버 설치

Tomcat 서버를 설치하려면 Linux 콘솔에서 다음 명령을 실행하세요. 이렇게 하면 Tomcat 서버가 성공적으로 설치됩니다.

## 2. PHP/JavaBridge 다운로드 및 구성

PHP/JavaBridge 바이너리를 다운로드하려면 Linux 콘솔에서 다음 명령어를 실행하세요.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Linux 콘솔에서 다음 명령어를 실행하여 PHP/JavaBridge 바이너리를 압축 해제하세요.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


이 작업을 통해 **JavaBridge.war** 파일이 추출됩니다. 다음 명령어를 Linux 콘솔에서 실행하여 tomcat8의 **webapps** 폴더에 복사하세요.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}


복사하면, tomcat8은 **webapps** 폴더에 자동으로 "**JavaBridge**"라는 새 폴더를 생성합니다.
 폴더가 생성되면, tomcat8이 실행 중인지 확인하고 브라우저에서 http://localhost:8080/JavaBridge 를 확인하세요, JavaBridge의 기본 페이지가 열려야 합니다.

오류 메시지가 나타나면 Linux 콘솔에서 다음 명령어를 입력하여 **FastCGI**를 설치하세요.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

php5.5 CGI를 설치한 후, tomcat8 서버를 재시작하고 브라우저에서 http://localhost:8080/JavaBridge 를 다시 확인하세요.

**JAVA_HOME** 오류가 표시되면, /etc/default/tomcat8 파일을 열고 JAVA_HOME을 설정하는 줄의 주석을 해제하세요. 브라우저에서 http://localhost:8080/JavaBridge 를 다시 확인하면 PHP/JavaBridge 예제 페이지가 나와야 합니다.

## 3. Aspose.PDF Java for PHP 예제 구성

webapps/JavaBridge 폴더 내에서 다음 명령어를 입력하여 PHP 예제를 클론하세요.

{{< highlight actionscript3 >}}

$ git init&nbsp;


$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Windows에서 소스 코드를 구성하는 방법

Windows 플랫폼에서 PHP/Java Bridge를 구성하려면 아래 간단한 단계를 따르세요.

1. PHP5를 설치하고 일반적으로 하듯이 구성하세요.
2. JRE 6 (Java Runtime Environment)을 설치하세요, 이미 설치되어 있지 않다면. C:\Program Files 등에서 확인할 수 있습니다. 여기서 다운로드할 수 있습니다. 저는 PHP Java Bridge (PJB)와 호환되기 때문에 JRE 6을 사용하고 있습니다.

3. Apache Tomcat 8.0을 설치하세요. 여기서 다운로드할 수 있습니다.

4. JavaBridge.war를 다운로드하세요.
5. 이 파일을 tomcat webapps 디렉토리에 복사하세요.
(예: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

6. tomcat apache 서비스를 다시 시작하세요.

7. http://localhost:8080/JavaBridge/test.php 로 이동하여 PHP가 작동하는지 확인하세요. 그곳에서 다른 예제를 찾을 수 있습니다.

8. [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 파일을 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib에 복사하세요.

9. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 폴더 안에 [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) 예제를 클론합니다.

10. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 폴더를 Aspose.PDF Java for PHP 예제 폴더로 복사합니다.

11. Apache Tomcat 서비스를 다시 시작하고 예제를 사용하기 시작합니다.