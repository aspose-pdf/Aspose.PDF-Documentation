---
title: Aspose.PDF for PHP via Java 설치
linktitle: 설치
type: docs
weight: 20
url: /ko/php-java/installation/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 직접 설치하는 방법과 NuGet을 사용하는 방법을 포함한 제품 설명 및 설치 지침을 보여줍니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for PHP via Java는 두 개의 별도 구성 요소로 구성되어 있습니다: 스크립트 래퍼(aspose.pdf.php)와 Aspose.PDF for Java. 이 구성 요소들은 PHP/Java Bridge를 통해 상호작용하며, 각각의 환경 및 실행 프로세스를 필요로 합니다.

## 설치

1. \java\apache-tomcat-9.0.24와 같은 위치에 Tomcat을 설치합니다.
1. JavaBridge.war를 Tomcat의 webapps 폴더에 복사합니다. 예: \java\apache-tomcat-9.0.24\webapps.
1. aspose-pdf-xx.x.jar를 lib 폴더에 복사합니다. 예: \java\apache-tomcat-9.0.24\lib.
1. \bin\startup.bat를 실행하면 JavaBridge.war가 \java\apache-tomcat-9.0.24\webapps\JavaBridge에 배포됩니다.

1. PHP가 제대로 작동하는지 확인하기 위해 http://localhost:8080/JavaBridge/test.php를 테스트합니다.
1. aspose.pdf.php와 example.php를 \java\apache-tomcat-9.0.24\webapps\JavaBridge로 복사합니다.
1. http://localhost:8080/JavaBridge/example.php를 열거나 다음과 같이 자신만의 PHP 파일을 만듭니다.
Jar 및 PHP 라이브러리는 vendor/aspose/pdf 폴더에서 찾을 수 있습니다.