---
title: 方法 - JasperReports オフライン デモに Aspose.PDF を使用する
linktitle: 方法 - JasperReports オフライン デモに Aspose.PDF を使用する
type: docs
weight: 10
url: /ja/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Aspose.PDF for JasperReports のオフライン デモをご覧ください。実践的な方法で実際の実装と機能を学びます。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports には、アプリケーションから PDF 形式へのレポートのエクスポートを開始するのに役立つ多数のデモ プロジェクトが含まれています。このデモは、新しいエクスポーターの使用方法を示すために変更された標準の JasperReports デモです。

{{% /alert %}}

## JasperReports デモ用の Aspose.PDF の実行

Aspose.PDF for JasperReports デモを実行するには:

{{% alert color="primary" %}}

1. <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. から JasperReports をダウンロードします。単一の JAR だけでなく、ソース コードとデモを含むアーカイブされたプロジェクト全体を必ずダウンロードしてください。
2. アーカイブされたプロジェクトをハードディスク上の任意の場所 (例: C:\.) に解凍します。
3. **Aspose.PDF.JasperReports.zip** の \demo フォルダーからすべてのデモ フォルダーを、JasperReports を解凍した場所である「`<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>`」にコピーします。デモのビルド スクリプトは JasperReports フォルダー構造に依存しているため、この手順が必要です。それ以外の場合は、ビルド スクリプトを変更する必要があります。
4. **aspose.pdf.jasperreports.jar** ファイルを **Aspose.PDF.JasperReports.zip** の \lib フォルダーから ```<InstallDir>```\jasperreports\lib にコピーします。
5. <http://ant.apache.org/bindownload.cgi>. から ANT ツールをダウンロードします。
6. ANT ツールを解凍し、ツールのマニュアルの説明に従って環境変数を設定します。
7. 現在のディレクトリを ```<InstallDir>```\demo\hsqldb に変更し、次のコマンド ラインを実行します。
   ant 実行サーバー
8. 新しいコマンド プロンプト インスタンスを開き、現在のディレクトリをいずれかの Aspose.PDF for JasperReports デモに変更します (例: ```<InstallDir>```\demo\samples\charts.ap)。
9. コマンドラインで次のコマンドを実行します。
10. ant javac – テスト アプリケーションの Java ソース ファイルをコンパイルします。
11. ant コンパイル - XML レポート設計をコンパイルし、.jasper ファイルを生成します。
12. ant fill – コンパイルされたレポート設計にデータを入力し、.jrprint ファイルを生成します。
13. コマンドラインで次のコマンドを実行します。
   ant pdf – デモ レポートから PDF ファイルを生成します。
14. 結果として表示されるドキュメントの 1 つ (例: ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf) を Adob​​e Reader または別のアプリケーションで開きます。

{{% /alert %}}

