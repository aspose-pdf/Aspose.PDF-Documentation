---

title: 如何 - 更新现有的 JasperReports 演示以使用 Aspose.Pdf for JasperReports

type: docs

weight: 20

url: zh/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports 包含多个演示项目，帮助您开始将报告导出为 PDF。这些演示基于标准的 JasperReports 演示，已被修改以演示如何使用新的导出器。本教程将介绍更新现有 JasperReports 演示以使用 Aspose.PDF for JasperReports 所需的步骤。

{{% /alert %}}

### **更新演示以使用 Aspose.PDF**

{{% alert color="primary" %}}

以下步骤说明了如何更新现有演示以使用 Aspose.PDF for JasperReports 导出扩展，而不是使用 JasperReport 的标准 PDF 导出功能。
{{% /alert %}}

1. 从 <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579> 下载 JasperReports。
   确保下载整个存档项目，包括源代码和演示，而不仅仅是一个 JAR。 本教程使用 JasperReports-3.5.2 准备。  
2. 将归档项目解压到硬盘上的某个位置，例如 C:\。  
3. 从 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹复制 **aspose.pdf.jasperreports.jar** 到 ```<InstallDir>```\jasperreports\lib。  
4. 打开 ```<InstallDir>```\jasperreports\demo\samples，（其中 ```<InstallDir>``` 是您解压 JasperReports 的位置）以更新现有的演示。如果您选择了字体演示，例如，用于与 Aspose.PDF for JasperReports 一起使用，请创建它的副本，以便原始演示保持不变。在此示例中，我们将新文件夹命名为 **fonts.ap**。  
注意：演示将从 ```<InstallDir>``` \jasperreports\demo\samples 运行，因为演示构建脚本依赖于 JasperReports 的文件夹结构。如果您更改示例文件夹，则必须修改构建脚本。  
5. 从 src 文件夹打开 **FontsApp.java** 文件，并添加对 Aspose.PDF for JasperReports 的引用：

   import com.aspose.pdf.jr3_7_0.jasperreports.*;（我们使用 jr3_7_0 是因为本教程是用 JasperReports 3.5.2 准备的。）

6. 添加一个新的字符串：
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; 作为通过 Aspose.PDF for JasperReports 的导出选项以及现有变量。

7. 找到 for else if (TASK_PDF.equals(taskName)) 代码段并复制整个段。

8. 将代码段粘贴在同一段下。

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
System.err.println("PDF 创建时间 : " + (System.currentTimeMillis() - start));
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
9. 打开 **build.xml** 文件。
10. 复制以下段落并将其放置在同一文件中：

```
<target name="pdf" description="通过 Aspose.PDF 为 JasperReports 生成 PDF。">
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

11. 要运行演示：

   - 从 <http://ant.apache.org/bindownload.cgi> 下载 ANT 工具。
```
- 解压 ANT 工具并按照工具手册中的说明设置环境变量。
- 将当前目录更改为 <InstallDir>\demo\hsqldb 并运行以下命令行：
  ant runServer
12. 打开一个新的命令提示符实例，将当前目录更改为 <InstallDir>\demo\samples\fonts.ap 并在命令行中运行以下命令：
13. ant javac – 编译测试应用程序的 Java 源文件
14. ant compile – 编译 XML 报告设计并生成 .jasper 文件
15. ant fill – 用数据填充已编译的报告设计并生成 .jrprint 文件
16. ant aspose_pdf – 使用 Aspose.PDF for JasperReports 生成 PDF 文件。
17. 从 <InstallDir>\demo\samples\fonts.ap\build\reports\ 文件夹中打开生成的 PDF (**FontsReport.pdf**)。