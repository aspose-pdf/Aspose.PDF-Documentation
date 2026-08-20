---
title: PHP에서 Aspose.PDF 다운로드 및 구성
linktitle: PHP에서 Aspose.PDF 다운로드 및 구성
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: PHP 프로젝트 내에서 쉽게 통합하고 PDF를 조작할 수 있도록 Aspose.PDF를 PHP에서 다운로드하고 구성하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
필수 라이브러리 다운로드



아래에 언급된 필수 라이브러리를 다운로드하세요. 이는 PHP 예제용 Aspose.PDF Java를 실행하는 데 필요합니다.

- **Aspose:** [Java 구성 요소용 Aspose.PDF](https://downloads.aspose.com/pdf/java)

- 
PHP/자바 브릿지


## 
소셜 코딩 사이트에서 예제 다운로드



실행 예제의 다음 릴리스는 아래에 언급된 소셜 코딩 사이트에서 다운로드할 수 있습니다.


### 
GitHub

- **Aspose.PDF PHP용 Java 예제**

  - 
[Aspose.PDF PHP용 Java](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)


## 
Linux 플랫폼에서 소스 코드를 구성하는 방법



다음을 사용하는 동안 소스 코드를 열고 확장하려면 다음의 간단한 단계를 따르세요.


## 
1. 톰캣 서버 설치

Tomcat 서버를 설치하려면 Linux 콘솔에서 다음 명령을 실행하세요. 이렇게 하면 Tomcat 서버가 성공적으로 설치됩니다.


{{< highlight actionscript3 >}}

 
sudo apt-get tomcat8 설치


{{< /highlight >}}

## 
2. PHP/JavaBridge 다운로드 및 구성



PHP/JavaBridge 바이너리를 다운로드하려면 Linux 콘솔에서 다음 명령을 실행하세요.


{{< highlight actionscript3 >}}

  
wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Linux 콘솔에서 다음 명령을 실행하여 PHP/JavaBridge 바이너리의 압축을 풉니다.


{{< highlight actionscript3 >}}

  
압축 풀기 -d php-java-bridge_6.2.1_documentation.zip


{{< /highlight >}}


그러면 **JavaBridge.war**В 파일이 추출됩니다. Linux 콘솔에서 다음 명령을 실행하여 tomcat88В **webapps**В 폴더에 복사합니다.


{{< highlight actionscript3 >}}

  
sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war


{{< /highlight >}}


복사하면 tomcat8은 **webapps**에 자동으로 새 폴더 "**JavaBridge**"를 생성합니다. 폴더가 생성되면 tomcat8이 실행 중인지 확인한 다음 브라우저에서 http://localhost:8080/JavaBridge을 확인하면 JavaBridge의 기본 페이지가 열립니다.

오류 메시지가 나타나면 Linux 콘솔에서 다음 명령을 실행하여 **FastCGI**В를 설치하세요.


{{< highlight actionscript3 >}}

  
sudo apt-get 설치 php55-cgi


{{< /highlight >}}


php5.5 CGI를 설치한 후 tomcat8 서버를 다시 시작하고 브라우저에서 http://localhost:8080/JavaBridge을 다시 확인하세요.



**JAVA_HOME**В 오류가 표시되면 /etc/default/tomcat8 파일을 열고 JAVA_HOME을 설정하는 줄의 주석 처리를 제거하세요. http://localhost:8080/JavaBridge 브라우저에서 다시 확인하세요. PHP/JavaBridge 예제 페이지가 함께 제공되어야 합니다.


## 
3. PHP 예제용 Aspose.PDF Java 구성

webapps/JavaBridge 폴더 내에서 다음 명령을 실행하여 PHP 예제를 복제합니다.


{{< highlight actionscript3 >}}


$ 자식 초기화&nbsp;



$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]


{{< /highlight >}}

## 
Windows에서 소스 코드를 구성하는 방법



Windows 플랫폼에서 PHP/Java Bridge를 구성하려면 아래의 간단한 단계를 따르십시오.

1. PHP5를 설치하고 평소와 같이 구성하십시오.

2. 
JRE 6(Java Runtime Environment)이 아직 설치되어 있지 않은 경우 설치하십시오. C:\Program 파일 등에서 확인하실 수 있습니다. 여기에서 다운로드하실 수 있습니다. 저는 PHP Java Bridge(PJB)와 호환되는 JRE 6을 사용하고 있습니다.


3. 
아파치 톰캣 8.0을 설치합니다. 여기에서 다운로드할 수 있습니다.


4. 
JavaBridge.war을 다운로드합니다.

5. 
이 파일을 tomcat webapps 디렉토리에 복사하세요.
(예: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )


6. 
Tomcat Apache 서비스를 다시 시작합니다.


7. 
PHP가 작동하는지 확인하려면 http://localhost:8080/JavaBridge/test.php로 이동하세요. 거기에서 다른 예를 찾을 수 있습니다


8. 
[Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 파일을 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib에 복사하세요.


9. 
C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 폴더에 [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) 예제를 복제합니다.

10. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 폴더를 Aspose.PDF Java for PHP 예제 폴더에 복사합니다.


11. 
Apache Tomcat 서비스를 다시 시작하고 예제 사용을 시작합니다.
