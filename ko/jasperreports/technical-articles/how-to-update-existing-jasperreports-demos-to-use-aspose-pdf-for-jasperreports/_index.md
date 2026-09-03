---
title: 방법 - Aspose.PDF for JasperReports를 사용하도록 기존 JasperReports 데모를 업데이트합니다.
linktitle: 방법 - Aspose.PDF for JasperReports를 사용하도록 기존 JasperReports 데모를 업데이트합니다.
type: docs
weight: 20
url: /ko/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Aspose.PDF for JasperReports의 기능을 활용하기 위해 기존 JasperReports 데모를 업데이트하는 방법을 알아보세요.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports에는 보고서를 PDF로 내보내기 시작하는 데 도움이 되는 다양한 데모 프로젝트가 포함되어 있습니다. 이 데모는 새로운 내보내기 도구를 사용하는 방법을 보여주기 위해 수정된 표준 JasperReports 데모를 기반으로 합니다. 이 튜토리얼에서는 Aspose.PDF for JasperReports를 사용하기 위해 기존 JasperReports 데모를 업데이트하는 데 필요한 단계를 안내합니다.

{{% /alert %}}

## Aspose.PDF를 사용하도록 데모 업데이트

{{% alert color="primary" %}}

다음 단계에서는 JasperReport의 표준 PDF 내보내기 기능을 사용하는 대신 JasperReports 내보내기 확장에 Aspose.PDF를 사용하도록 기존 데모를 업데이트하는 방법을 설명합니다.

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.에서 JasperReports 다운로드
   단일 JAR뿐만 아니라 소스 코드와 데모가 포함된 전체 보관된 프로젝트를 다운로드하세요. 이 튜토리얼은 JasperReports-3.5.2를 사용하여 준비되었습니다.
2. 보관된 프로젝트를 하드 디스크의 특정 위치(예: C:\.)에 압축을 풉니다.
3. **Aspose.PDF.JasperReports.zip**의 \lib 폴더에서 **aspose.pdf.jasperreports.jar**를 ```<InstallDir>```\jasperreports\lib로 복사합니다.
4. 기존 데모를 업데이트하려면 ```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>```(JasperReports의 압축을 푼 위치)를 엽니다. 예를 들어 Aspose.PDF for JasperReports와 함께 사용하기 위해 글꼴 데모를 선택한 경우 원본 데모가 동일하게 유지되도록 복사본을 만드세요. 이 예에서는 새 폴더 이름을 **fonts.ap**으로 지정했습니다.
참고: 데모 빌드 스크립트는 JasperReports의 폴더 구조에 의존하므로 데모는 ```<InstallDir>```\jasperreports\demo\samples에서 실행해야 합니다. 샘플 폴더를 변경하면 빌드 스크립트도 수정해야 합니다.
5. src 폴더에서 **FontsApp.java** 파일을 열고 Aspose.PDF for JasperReports에 대한 참조를 추가합니다.
   import com.aspose.pdf.jr3_7_0.jasperreports.*;
   (이 튜토리얼은 JasperReports 3.5.2를 기준으로 작성되었기 때문에 jr3_7_0을 사용하고 있습니다.)
6. 새 문자열을 추가합니다.
   `private static final String TASK_ASPOSE_PDF = "aspose_pdf";`
   이 변수는 Aspose.PDF for JasperReports를 통한 내보내기 옵션으로 사용됩니다.
7. `else if (TASK_PDF.equals(taskName))` 코드 세그먼트를 찾아 전체 세그먼트를 복사합니다.
8. 동일한 세그먼트 아래에 코드 조각을 붙여넣습니다.

```java
 else if (TASK_PDF.equals(taskName))
{
  File sourceFile = new File(fileName);
  JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
  File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");
  JRPdfExporter exporter = new JRPdfExporter();
  HashMap fontMap = new HashMap();
  FontKey key = new FontKey("DejaVu Serif", true, false);
  PdfFont font = new PdfFont("DejaVuSerif-Bold.ttf", "Cp1252", true);
  fontMap.put(key, font);
  exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);
  exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
  exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
  exporter.exportReport();
  System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```text
update
else if (TASK_PDF.equals(taskName))
as
else if (TASK_ASPOSE_PDF.equals(taskName))
replace
JRPdfExporter exporter = new JRPdfExporter();
with
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```

9. **build.xml** 파일을 엽니다.
10. 다음 세그먼트의 복사본을 만들어 동일한 파일에 넣습니다.

```xml
 <target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```diff
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. 데모를 실행하려면:
   -  <http://ant.apache.org/bindownload.cgi>에서 ANT 도구를 다운로드합니다.
   - ANT 도구의 압축을 풀고 도구 설명서에 설명된 대로 환경 변수를 설정합니다.
   -  현재 디렉터리를 <InstallDir>\demo\hsqldb로 변경하고 다음 명령줄을 실행합니다.
      `ant runServer`
12. 새 명령 프롬프트 인스턴스를 열고 현재 디렉터리를 <InstallDir>\demo\samples\fonts.ap로 변경하고 명령줄에서 다음 명령을 실행합니다.
13. ant javac – 테스트 애플리케이션의 Java 소스 파일을 컴파일합니다.
14. ant compile – XML 보고서 디자인을 컴파일하고 .jasper 파일을 생성합니다.
15. ant fill – 컴파일된 보고서 디자인을 데이터로 채우고 .jrprint 파일을 생성합니다.
16. ant aspose_pdf – Aspose.PDF for JasperReports를 사용하여 PDF 파일을 생성합니다.
17. <InstallDir>\demo\samples\fonts.ap\build\reports\ 폴더에서 결과 PDF(**FontsReport.pdf**)를 엽니다.

{{% /alert %}}

