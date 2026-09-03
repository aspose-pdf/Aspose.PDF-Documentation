---
title: 如何 - 更新现有的 JasperReports 演示以使用 Aspose.PDF for JasperReports
linktitle: 如何 - 更新现有的 JasperReports 演示以使用 Aspose.PDF for JasperReports
type: docs
weight: 20
url: /zh/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: 了解如何更新现有的 JasperReports 演示以利用 Aspose.PDF for JasperReports 的功能。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports includes a number of demo projects to help you get started exporting reports to PDF. These demos are based on standard JasperReports demos that have been modified to demonstrate how to use new exporters. This tutorial, goes through the steps required to update the existing JasperReports demos to use Aspose.PDF for JasperReports.

{{% /alert %}}

## Updating Demos to use Aspose.PDF

{{% alert color="primary" %}}

以下步骤说明如何更新现有演示以使用 Aspose.PDF 进行 JasperReports 导出扩展，而不是使用 JasperReport 的标准 PDF 导出功能。

1. 从 <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. 下载 JasperReports
   Make sure to download the entire archived project with the source code and demos, not just a single JAR. This tutorial was prepared using JasperReports-3.5.2.
2. Unpack the archived project to some location on your hard disk, for example C:\.
3. 将 **aspose.pdf.jasperreports.jar** 从 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹复制到“`<InstallDir>`”\jasperreports\lib。
4. 打开```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>``` 是您解压 JasperReports 的位置）以更新现有演示。例如，如果您选择了字体演示，以便与 JasperReports 的 Aspose.PDF 一起使用，请创建它的副本，以便原始演示保持不变。出于本示例的目的，我们将新文件夹命名为 **fonts.ap**。
Note: demos will run from ```<InstallDir>``` \jasperreports\demo\samples because the demo build scripts rely on the JasperReports' folder structure. If you change the sample folder, you have to modify build scripts.
5. Open the **FontsApp.java** file from the src folder and add a reference to Aspose.PDF for JasperReports:
   import com.aspose.pdf.jr3_7_0.jasperreports.*;
   (We are using jr3_7_0 because this tutorial was prepared with JasperReports 3.5.2.)
6. 添加新字符串：
   `private static final String TASK_ASPOSE_PDF = "aspose_pdf";` 作为新的导出选项，与现有变量一起使用。
7. 找到 for else if (TASK_PDF.equals(taskName)) 代码段并复制整个段。
8. Paste the code snippet under same segment.

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

9. 打开 **build.xml** 文件。
10. 复制以下段并将其放入同一文件中：

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

11. 运行演示：
   -  从<http://ant.apache.org/bindownload.cgi>.下载ANT工具
   - 解压 ANT 工具并按照工具手册中的说明设置环境变量。
   -  将当前目录更改为<InstallDir>\demo\hsqldb并运行以下命令行：
      ant运行服务器
12. 打开一个新的命令提示符实例并将当前目录更改为 <InstallDir>\demo\samples\fonts.ap 并在命令行中运行以下命令：
13. ant javac – 编译测试应用程序的 Java 源文件
14. ant compile – to compile the XML report design and produce the .jasper file
15. ant fill – 用数据填充已编译的报告设计并生成 .jrprint 文件
16. ant aspose_ pdf – 使用 Aspose.PDF for JasperReports 生成 PDF 文件。
17. 从 <InstallDir>\demo\samples\ fonts.ap\build\reports\ 文件夹中打开生成的 PDF (**FontsReport.pdf**)。

{{% /alert %}}

