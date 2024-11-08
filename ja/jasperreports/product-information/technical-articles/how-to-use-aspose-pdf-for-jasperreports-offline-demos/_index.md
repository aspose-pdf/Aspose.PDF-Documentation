---
title: How to - use Aspose.Pdf for JasperReports offline demos
type: docs
weight: 10
url: /ja/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReportsには、アプリケーションからレポートをPDF形式にエクスポートする際の手助けとなるいくつかのデモプロジェクトが含まれています。これらのデモは、新しいエクスポーターの使用方法を示すように変更された標準的なJasperReportsデモです。

{{% /alert %}}
### **Aspose.PDF for JasperReportsデモの実行**
Aspose.PDF for JasperReportsデモを実行するには：

{{% alert color="primary" %}}

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>からJasperReportsをダウンロードします。ソースコードとデモを含むアーカイブされたプロジェクト全体をダウンロードし、単一のJARだけをダウンロードしないようにしてください。
2. アーカイブされたプロジェクトをハードディスク上の任意の場所に解凍します。例えばC:\。 
デモフォルダを **Aspose.PDF.JasperReports.zip** の \demo フォルダから ```<InstallDir>```\jasperreports\demo\samples にコピーします。ここで ```<InstallDir>``` は JasperReports を展開した場所です。このステップは、デモビルドスクリプトが JasperReports のフォルダ構造に依存しているため必要です。そうでない場合はビルドスクリプトを変更する必要があります。  
4. **Aspose.PDF.JasperReports.zip** の \lib フォルダから **aspose.pdf.jasperreports.jar** ファイルを ```<InstallDir>```\jasperreports\lib にコピーします。  
5. <http://ant.apache.org/bindownload.cgi> から ANT ツールをダウンロードします。  
6. ANT ツールを解凍し、ツールのマニュアルに記載されているように環境変数を設定します。  
7. 現在のディレクトリを ```<InstallDir>```\demo\hsqldb に変更し、次のコマンドラインを実行します。  
   ant runServer  
8. 新しいコマンドプロンプトインスタンスを開き、Aspose.PDF for JasperReports のデモの1つの現在のディレクトリに変更します。例えば、```<InstallDir>```\demo\samples\charts.ap。  
9. 次のコマンドをコマンドラインで実行します。  
10. ant javac – テストアプリケーションのJavaソースファイルをコンパイルします。  
11. ant compile – XMLレポートデザインをコンパイルし、.jasperファイルを生成します。  
12. ant fill – コンパイルされたレポートデザインにデータを埋め込み、.jrprintファイルを生成します。  
13. コマンドラインで次のコマンドを実行します:  
    ant pdf – デモレポートからPDFファイルを生成します。  
14. 結果として得られたドキュメントの1つを開いて表示します。例えば、```<InstallDir>```\\demo\\samples\\charts.ap\\AreaChartReport.pdfをAdobe Readerまたは別のアプリケーションで開きます。  

{{% /alert %}}