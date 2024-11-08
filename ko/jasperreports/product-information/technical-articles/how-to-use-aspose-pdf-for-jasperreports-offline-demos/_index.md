---
title: 사용 방법 - Aspose.Pdf for JasperReports 오프라인 데모 사용
type: docs
weight: 10
url: /ko/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports에는 애플리케이션에서 보고서를 PDF 형식으로 내보내는 방법을 시작하는 데 도움이 되는 여러 데모 프로젝트가 포함되어 있습니다. 데모는 새로운 내보내기 도구를 사용하는 방법을 보여주도록 수정된 표준 JasperReports 데모입니다.

{{% /alert %}}
### **Aspose.PDF for JasperReports 데모 실행**
Aspose.PDF for JasperReports 데모를 실행하려면:

{{% alert color="primary" %}}

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>에서 JasperReports를 다운로드합니다. 소스 코드와 데모가 포함된 전체 아카이브 프로젝트를 다운로드했는지 확인하고, 단일 JAR만 다운로드하지 마십시오.
2. 하드 디스크의 일부 위치에 아카이브 프로젝트를 압축 해제합니다. 예를 들어 C:\.
3. 문서의 텍스트는 아래와 같습니다:

모든 데모 폴더를 \demo 폴더에서 **Aspose.PDF.JasperReports.zip**의 ```<InstallDir>```\jasperreports\demo\samples로 복사합니다. 여기서 ```<InstallDir>```은 JasperReports를 압축 해제한 위치입니다. 이 단계는 데모 빌드 스크립트가 JasperReports 폴더 구조에 의존하기 때문에 필요하며, 그렇지 않으면 빌드 스크립트를 수정해야 합니다.  
4. \lib 폴더의 **aspose.pdf.jasperreports.jar** 파일을 **Aspose.PDF.JasperReports.zip**에서 ```<InstallDir>```\jasperreports\lib로 복사합니다.  
5. <http://ant.apache.org/bindownload.cgi>에서 ANT 도구를 다운로드합니다.  
6. ANT 도구를 압축 해제하고 도구 설명서에 설명된 대로 환경 변수를 설정합니다.  
7. 현재 디렉토리를 ```<InstallDir>```\demo\hsqldb로 변경하고 다음 명령줄을 실행합니다:  
   ant runServer  
8. 새 명령 프롬프트 인스턴스를 열고 현재 디렉토리를 Aspose.PDF for JasperReports 데모 중 하나로 변경합니다. 예를 들어 ```<InstallDir>```\demo\samples\charts.ap.  
9. 다음 명령을 명령줄에서 실행합니다:  
10. ant javac – 테스트 애플리케이션의 Java 소스 파일을 컴파일합니다.  
11. ant compile – XML 보고서 디자인을 컴파일하고 .jasper 파일을 생성합니다.  
12. ant fill – 컴파일된 보고서 디자인에 데이터를 채워 .jrprint 파일을 생성합니다.  
13. 명령 줄에서 다음 명령을 실행합니다:  
   ant pdf – 데모 보고서에서 PDF 파일을 생성합니다.  
14. 결과 문서 중 하나를 열어 보십시오, 예를 들어 ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf를 Adobe Reader 또는 다른 애플리케이션에서 봅니다.  

{{% /alert %}}