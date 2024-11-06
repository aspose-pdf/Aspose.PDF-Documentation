---
title: 업데이트 방법 - 기존 JasperReports 데모를 Aspose.Pdf for JasperReports로 업데이트하는 방법
type: docs
weight: 20
url: ko/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports는 보고서를 PDF로 내보내는 데 도움이 되는 여러 데모 프로젝트를 포함하고 있습니다. 이러한 데모는 새로운 내보내기 기능을 사용하는 방법을 보여주기 위해 수정된 표준 JasperReports 데모를 기반으로 합니다. 이 튜토리얼은 기존 JasperReports 데모를 Aspose.PDF for JasperReports를 사용하도록 업데이트하는 데 필요한 단계를 안내합니다.

{{% /alert %}}
### **Aspose.PDF 사용을 위한 데모 업데이트**

{{% alert color="primary" %}}

다음 단계는 JasperReport의 표준 PDF 내보내기 기능 대신 Aspose.PDF for JasperReports 내보내기 확장을 사용하도록 기존 데모를 업데이트하는 방법을 설명합니다.
{{% /alert %}}

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>에서 JasperReports를 다운로드합니다.
   단일 JAR만이 아닌 소스 코드 및 데모가 포함된 전체 아카이브 프로젝트를 다운로드했는지 확인하십시오. 이 튜토리얼은 JasperReports-3.5.2를 사용하여 준비되었습니다.  
2. 하드 디스크의 일부 위치, 예를 들어 C:\에 압축된 프로젝트를 풀어 놓으십시오.  
3. **Aspose.PDF.JasperReports.zip**의 \lib 폴더에 있는 **aspose.pdf.jasperreports.jar**를 ```<InstallDir>```\jasperreports\lib에 복사하십시오.  
4. 기존의 데모를 업데이트하려면 ```<InstallDir>```\jasperreports\demo\samples를 열어보십시오 (여기서 ```<InstallDir>```는 JasperReports를 풀어놓은 위치입니다). 예를 들어 Aspose.PDF for JasperReports와 함께 사용하기 위해 폰트 데모를 선택한 경우, 원본 데모는 그대로 유지되도록 복사본을 만드십시오. 이 예제의 목적상, 새 폴더의 이름을 **fonts.ap**로 지정하였습니다.  
참고: 데모는 JasperReports의 폴더 구조에 의존하기 때문에 ```<InstallDir>``` \jasperreports\demo\samples에서 실행됩니다. 샘플 폴더를 변경하면 빌드 스크립트를 수정해야 합니다.  
5. src 폴더에서 **FontsApp.java** 파일을 열고 Aspose.PDF for JasperReports에 대한 참조를 추가하십시오:

   import com.aspose.pdf.jr3_7_0.jasperreports.*;```
(우리는 이 튜토리얼이 JasperReports 3.5.2로 준비되었기 때문에 jr3_7_0을 사용하고 있습니다.)
6. 새로운 문자열을 추가합니다:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; 를 기존 변수와 함께 Aspose.PDF를 통한 JasperReports의 내보내기 옵션으로 추가합니다.
7. for else if (TASK_PDF.equals(taskName)) 코드 세그먼트를 찾아서 전체 세그먼트를 복사합니다.
8. 동일한 세그먼트 아래에 코드 스니펫을 붙여넣습니다.

```
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
```
```java
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("PDF 생성 시간 : " + (System.currentTimeMillis() - start));
}
```

```
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
10. 다음 세그먼트를 복사하여 같은 파일 안에 배치합니다:

```
<target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. 데모를 실행하려면:

   - ANT 도구를 <http://ant.apache.org/bindownload.cgi>에서 다운로드하십시오.
```

- ANT 도구를 풀고 도구 설명서에 설명된 대로 환경 변수를 설정합니다.
- 현재 디렉터리를 <InstallDir>\demo\hsqldb로 변경하고 다음 명령어를 실행합니다:
  ant runServer
12. 새 명령 프롬프트 인스턴스를 열고 현재 디렉터리를 <InstallDir>\demo\samples\fonts.ap로 변경한 다음 명령 프롬프트에서 다음 명령을 실행합니다:
13. ant javac – 테스트 애플리케이션의 Java 소스 파일을 컴파일합니다
14. ant compile – XML 보고서 디자인을 컴파일하고 .jasper 파일을 생성합니다
15. ant fill – 컴파일된 보고서 디자인에 데이터를 채워 .jrprint 파일을 생성합니다
16. ant aspose_ pdf – Aspose.PDF for JasperReports를 사용하여 PDF 파일을 생성합니다.
17. <InstallDir>\demo\samples\fonts.ap\build\reports\ 폴더에서 생성된 PDF (**FontsReport.pdf**)를 엽니다.
```