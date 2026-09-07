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

Aspose.PDF for JasperReports 包含多个示范项目，可协助您快速上手将报表汇出为 PDF。这些演示基于标准的 JasperReports 演示，并经过修改以演示如何使用新的汇出器。本教学将逐步介绍如何将现有的 JasperReports 示范更新为使用 Aspose.PDF for JasperReports。

{{% /alert %}}

## Updating Demos to use Aspose.PDF

{{% alert color="primary" %}}

以下步骤说明如何更新现有演示以使用 Aspose.PDF 进行 JasperReports 导出扩展，而不是使用 JasperReport 的标准 PDF 导出功能。

1. 从 <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579> 下载 JasperReports
请务必下载包含源代码和示例的完整项目包，而不仅仅是单个 JAR 文件。本教程使用 JasperReports 3.5.2 版本编写。
2. Unpack the archived project to some location on your hard disk, for example C:\.
3. 将 **aspose.pdf.jasperreports.jar** 从 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹复制到“`<InstallDir>`”\jasperreports\lib。
4. 打开```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` 是您解压 JasperReports 的位置）以更新现有演示。例如，如果您选择了字体演示，以便与 JasperReports 的 Aspose.PDF 一起使用，请创建它的副本，以便原始演示保持不变。出于本示例的目的，我们将新文件夹命名为 **fonts.ap**。
注意：演示程序将从 `<安装目录>` \jasperreports\demo\samples` 运行，因为演示程序的构建脚本依赖于 JasperReports 的文件夹结构。如果您更改了示例文件夹，则必须修改构建脚本。
5. 打开 src 文件夹中的 **FontsApp.java** 文件，并添加对 Aspose.PDF for JasperReports 的引用：
import com.aspose.pdf.jr3_7_0.jasperreports.*;
（我们使用 jr3_7_0 是因为本教程是基于 JasperReports 3.5.2 编写的。）
6. 添加新字符串：
`private static final String TASK_ASPOSE_PDF = "aspose_pdf";` 作为新的导出选项，与现有变量一起使用。
7. 找到 for else if (TASK_PDF.equals(taskName)) 代码段并复制整个段。
8. 将代码片段粘贴到同一段落下。

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

