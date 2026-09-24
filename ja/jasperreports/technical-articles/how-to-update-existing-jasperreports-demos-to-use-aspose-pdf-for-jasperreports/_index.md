---
title: 方法 - JasperReports に Aspose.PDF を使用するように既存の JasperReports デモを更新する
linktitle: 方法 - JasperReports に Aspose.PDF を使用するように既存の JasperReports デモを更新する
type: docs
weight: 20
url: /ja/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: 既存の JasperReports デモを更新して、Aspose.PDF for JasperReports の機能を活用する方法を学びます。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports には、レポートを PDF にエクスポートするのに役立つ多数のデモ プロジェクトが含まれています。これらのデモは、新しいエクスポーターの使用方法を示すために変更された標準の JasperReports デモに基づいています。このチュートリアルでは、JasperReports に Aspose.PDF を使用するように既存の JasperReports デモを更新するために必要な手順を説明します。

{{% /alert %}}

## Aspose.PDF を使用するようにデモを更新する

{{% alert color="primary" %}}

次の手順では、JasperReport の標準 PDF エクスポート機能ではなく、JasperReports エクスポート拡張機能の Aspose.PDF を使用するように既存のデモを更新する方法について説明します。

1. JasperReports を <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. からダウンロードします
   単一の JAR だけでなく、ソース コードとデモを含むアーカイブされたプロジェクト全体を必ずダウンロードしてください。このチュートリアルは、JasperReports-3.5.2 を使用して作成されました。
2. アーカイブされたプロジェクトをハードディスク上の任意の場所 (例: C:\.) に解凍します。
3. **Aspose.PDF.JasperReports.zip** の \lib フォルダーから **aspose.pdf.jasperreports.jar** を ```<InstallDir>```\jasperreports\lib にコピーします。
4. 「`<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>`` は JasperReports を解凍した場所です) を開き、既存のデモを更新します。たとえば、JasperReports の Aspose.PDF で使用するためにフォント デモを選択した場合は、元のデモが同じになるようにそのコピーを作成します。この例では、新しいフォルダーに **fonts.ap** という名前を付けました。
注: デモのビルド スクリプトは JasperReports のフォルダー構造に依存しているため、デモは ```<InstallDir>``` \jasperreports\demo\samples から実行されます。サンプル フォルダーを変更した場合は、ビルド スクリプトを変更する必要があります。
5. src フォルダーから **FontsApp.java** ファイルを開き、JasperReports の Aspose.PDF への参照を追加します。
   com.aspose.pdf.jr3_7_0.jasperreports.* をインポートします。
   (このチュートリアルは JasperReports 3.5.2 で準備されているため、jr3_7_0 を使用しています。)
6. 新しい文字列を追加します。
6. 新しい文字列を追加します。`private static final String TASK_ASPOSE_PDF = "aspose_pdf";` を追加して、Aspose.PDF for JasperReports を介したエクスポート オプションとして既存の変数と併用できます。
7. for else if (TASK_PDF.equals(taskName)) コード セグメントを見つけて、セグメント全体をコピーします。
8. コード スニペットを同じセグメントの下に貼り付けます。

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

9. **build.xml** ファイルを開きます。
10. 次のセグメントのコピーを作成し、同じファイル内に配置します。

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

11. デモを実行するには:
   -  <http://ant.apache.org/bindownload.cgi>. から ANT ツールをダウンロードします。
   - ANT ツールを解凍し、ツールのマニュアルの説明に従って環境変数を設定します。
   -  現在のディレクトリを <InstallDir>\demo\hsqldb に変更し、次のコマンド ラインを実行します。
      ant 実行サーバー
12. 新しいコマンド プロンプト インスタンスを開き、現在のディレクトリを <InstallDir>\demo\samples\fonts.ap に変更し、コマンド ラインで次のコマンドを実行します。
13. ant javac – テスト アプリケーションの Java ソース ファイルをコンパイルします。
14. ant コンパイル - XML レポート設計をコンパイルし、.jasper ファイルを生成します。
15. ant fill – コンパイルされたレポート設計にデータを入力し、.jrprint ファイルを生成します。
16. ant aspose_ pdf – Aspose.PDF for JasperReports を使用して PDF ファイルを生成します。
17. <InstallDir>\demo\samples\ fonts.ap\build\reports\ フォルダーから結果の PDF (**FontsReport.pdf**) を開きます。

{{% /alert %}}

