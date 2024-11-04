---
title: 既存のJasperReportsデモをAspose.Pdf for JasperReportsを使用するように更新する方法
type: docs
weight: 20
url: /jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReportsには、レポートをPDFにエクスポートするのに役立ついくつかのデモプロジェクトが含まれています。これらのデモは、新しいエクスポーターの使用方法を示すように修正された標準のJasperReportsデモに基づいています。このチュートリアルでは、既存のJasperReportsデモをAspose.PDF for JasperReportsを使用するように更新するために必要な手順を説明します。

{{% /alert %}}
### **Aspose.PDFを使用するようにデモを更新する**

{{% alert color="primary" %}}

次の手順では、JasperReportの標準のPDFエクスポート機能を使用するのではなく、Aspose.PDF for JasperReportsエクスポート拡張機能を使用するように既存のデモを更新する方法を説明します。
{{% /alert %}}

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>からJasperReportsをダウンロードします。
   ソースコードとデモを含むアーカイブされたプロジェクト全体をダウンロードし、単一のJARだけでなく、すべてを含めるようにしてください。 このチュートリアルはJasperReports-3.5.2を使用して準備されました。  
2. アーカイブされたプロジェクトをハードディスク上の任意の場所に解凍します。たとえば、C:\。  
3. **Aspose.PDF.JasperReports.zip** の \lib フォルダから **aspose.pdf.jasperreports.jar** を ```<InstallDir>```\jasperreports\lib にコピーします。  
4. ```<InstallDir>```\jasperreports\demo\samples を開きます（```<InstallDir>``` は JasperReports を解凍した場所です）。既存のデモを更新します。たとえば、Aspose.PDF for JasperReports と一緒に使用するためにフォントデモを選択した場合、オリジナルのデモがそのまま残るようにコピーを作成します。この例の目的のために、新しいフォルダを **fonts.ap** と名付けました。  
注意: デモは ```<InstallDir>``` \jasperreports\demo\samples から実行されます。なぜなら、デモビルドスクリプトは JasperReports のフォルダ構造に依存しているからです。サンプルフォルダを変更した場合、ビルドスクリプトを修正する必要があります。  
5. src フォルダから **FontsApp.java** ファイルを開き、Aspose.PDF for JasperReports への参照を追加します:

   import com.aspose.pdf.jr3_7_0.jasperreports.*;```
(このチュートリアルはJasperReports 3.5.2で準備されたため、jr3_7_0を使用しています。)
6. 新しい文字列を追加します:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; 既存の変数と共に、Aspose.PDF for JasperReportsを通じてエクスポートオプションとして。
7. for else if (TASK_PDF.equals(taskName)) コードセグメントを見つけて、セグメント全体をコピーします。
8. 同じセグメントの下にコードスニペットを貼り付けます。

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
```
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("PDF作成時間 : " + (System.currentTimeMillis() - start));
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
9. **build.xml** ファイルを開きます。
10. 次のセグメントをコピーして、同じファイル内に配置します:

```
<target name="pdf" description="Aspose.PDF for JasperReportsを介してPDFを生成します。">
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

11. デモを実行するには:

   - ANTツールを<http://ant.apache.org/bindownload.cgi>からダウンロードします。
- ANTツールを解凍し、ツールのマニュアルに従って環境変数を設定します。
- 現在のディレクトリを<InstallDir>\demo\hsqldbに変更し、次のコマンドラインを実行します。
  ant runServer

12. 新しいコマンドプロンプトインスタンスを開き、現在のディレクトリを<InstallDir>\demo\samples\fonts.apに変更し、次のコマンドをコマンドラインで実行します。
13. ant javac – テストアプリケーションのJavaソースファイルをコンパイルします
14. ant compile – XMLレポートデザインをコンパイルして.jasperファイルを生成します
15. ant fill – コンパイルされたレポートデザインにデータを埋め込み、.jrprintファイルを生成します
16. ant aspose_pdf – Aspose.PDF for JasperReportsを使用してPDFファイルを生成します。
17. <InstallDir>\demo\samples\fonts.ap\build\reports\フォルダーから生成されたPDF(**FontsReport.pdf**)を開きます。