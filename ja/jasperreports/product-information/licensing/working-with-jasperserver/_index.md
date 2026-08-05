---
title: JasperServer の操作
linktitle: Working with JasperServer
type: docs
weight: 20
description: Aspose.PDF を使用して JasperServer を効率的に操作する方法を検討します。レポートをプロフェッショナルな PDF に簡単にエクスポートします。
lastmod: "2021-06-05"
---

## <ins>licenseFile Exporter パラメータを applicationContext.xml に設定します

{{% alert color="primary" %}}

このメソッドは JasperServer で使用されます。

{{% /alert %}}

1. ライセンスをコンピュータにダウンロードし、「`<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` folder, where  ```<InstallDir>`」にコピーします。これは、JasperServer インストール ディレクトリを表します。
2. ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` ファイルを見つけて、次の行を追加します。

```xml
 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
注: ライセンス ファイルにアクセスするときに問題が発生するため、インストール パスにスペースを含めないでください (例: C:/Program Files/JasperServer…)。
{{% /alert %}}

## ライセンスが機能することを確認する

レポートを PDF 形式にエクスポートし、レポートに評価メッセージが含まれているかどうかを確認します。評価メッセージが表示されない場合、ライセンスは適切に機能しています。

Aspose.PDF for JasperReports は、評価モードで作業するときにウォーターマークを挿入します

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports は、評価モードで作業するときにウォーターマークを挿入します

![Integration with JasperServer_2](working-with-jasperserver_2.png)

