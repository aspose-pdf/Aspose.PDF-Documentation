---
title: 방법 - JasperReports 오프라인 데모를 위해 Aspose.PDF 사용
linktitle: 방법 - JasperReports 오프라인 데모를 위해 Aspose.PDF 사용
type: docs
weight: 10
url: /ko/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Aspose.PDF for JasperReports의 오프라인 데모를 살펴보세요. 실습 방식으로 실제 구현 및 기능을 알아보세요.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports에는 애플리케이션에서 보고서를 PDF 형식으로 내보내는 데 도움이 되는 다양한 데모 프로젝트가 포함되어 있습니다. 데모는 새로운 내보내기 도구를 사용하는 방법을 보여주기 위해 수정된 표준 JasperReports 데모입니다.

{{% /alert %}}

## JasperReports 데모를 위해 Aspose.PDF 실행

JasperReports 데모를 위해 Aspose.PDF를 실행하려면:

{{% alert color="primary" %}}

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.에서 JasperReports를 다운로드하세요. 단일 JAR뿐만 아니라 소스 코드와 데모가 포함된 전체 아카이브 프로젝트를 다운로드하세요.
2. 보관된 프로젝트를 하드 디스크의 특정 위치(예: C:\.)에 압축을 풉니다.
3. **Aspose.PDF.JasperReports.zip**의 \demo 폴더에서 ```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>```로 모든 데모 폴더를 복사하세요. 이 위치가 JasperReports의 압축을 푼 위치입니다. 데모 빌드 스크립트는 JasperReports 폴더 구조에 의존하기 때문에 이 단계가 필요합니다. 그렇지 않으면 빌드 스크립트를 수정해야 합니다.
4. **Aspose.PDF.JasperReports.zip**의 \lib 폴더에 있는 **aspose.pdf.jasperreports.jar** 파일을 ```<InstallDir>```\jasperreports\lib로 복사합니다.
5. <http://ant.apache.org/bindownload.cgi>.에서 ANT 도구를 다운로드하세요.
6. ANT 도구의 압축을 풀고 도구 설명서에 설명된 대로 환경 변수를 설정합니다.
7. 현재 디렉터리를 ```<InstallDir>```\demo\hsqldb로 변경하고 다음 명령줄을 실행합니다:
   `ant runServer`
8. 새 명령 프롬프트 인스턴스를 열고 현재 디렉터리를 JasperReports 데모용 Aspose.PDF 중 하나로 변경합니다(예: ```<InstallDir>```\demo\samples\charts.ap).
9. 명령줄에서 다음 명령을 실행합니다.
10. ant javac – 테스트 애플리케이션의 Java 소스 파일을 컴파일합니다.
11. ant compile – XML 보고서 디자인을 컴파일하고 .jasper 파일을 생성합니다.
12. ant fill – 컴파일된 보고서 디자인을 데이터로 채우고 .jrprint 파일을 생성합니다.
13. 명령줄에서 다음 명령을 실행합니다.
   ant pdf – 데모 보고서에서 PDF 파일을 생성합니다.
14. Adobe Reader 또는 다른 응용 프로그램에서 결과 문서 중 하나(예: ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf)를 엽니다.

{{% /alert %}}

